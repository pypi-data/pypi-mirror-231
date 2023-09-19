import _tkinter
import os
import traceback
from cm.modules import *
import threading
import pickle
from ar_qdk.main import ARQDK
from time import sleep
from cm.wlistener import WListener
from cm.configs import config as s
from cm.styles import fonts
from cm.gcore_interaction import db_functions as db_funcs
from orup_errors.main import OrupErrorsManager
from cm.styles import color_solutions
from cm.video_worker import start_video_stream
from cm import functions
import sys
from qpi.main import QPI
from PIL import Image, ImageTk
import io


class Operator:
    """ Основной оператор взaимодействия между окнами, его экземляр
    распределяется между всеми модулями и используются
    для их взаимной обработки """

    def __init__(self, root, settings, scale, can, deffaultScreenSize,
                 loadingcan, ar_qdk, scale_server_ip=None,
                 scale_server_port=2297, fgsm=False, cm_cams_info=None):
        # Словарь, где будут хранится номера считанных авто, время считывания,
        # Сколько раз была отмена и т.д
        self.orup_black_list = {}
        self.root = root
        self.fgsm = fgsm
        self.currentPage = None
        self.cm_cams_info = cm_cams_info
        self.status_ready = False
        self.if_show_weight = True
        self.current = 'main'
        self.unfinished_records = []
        self.trash_cat_type_map = []
        self.tko_carriers = []
        self.region_operators = []
        self.loadingcan = loadingcan
        self.loading_repcentage = 0
        self.deffaultScreenSize = deffaultScreenSize
        self.current = 'main'
        self.settings = settings
        self.ar_qdk = ar_qdk
        self.cameras_info = {}
        # self.set_cam_info(
        #   self.ar_qdk.execute_method('get_cams', get_response=True)['info'])
        self.general_tables_dict = {}
        self.get_wdb_tables_info()
        self.ar_qdk.execute_method('get_cams')
        self.ar_qdk.execute_method('get_cat_type_map')
        self.terminal = Terminal(root, settings, self, can)
        if self.settings.mirrored:
            self.auto_exit_x, self.auto_exit_y = 1615, 852
            self.gross_x, self.gross_y = 417, 852
        else:
            self.auto_exit_x, self.auto_exit_y = 417, 852
            self.gross_x, self.gross_y = 1615, 852
        self.auto_cams_width, self.auto_cams_height = 420, 360
        self.terminal.launchingOperations()
        self.main_btns_drawn = False
        self.exitFlag = False
        self.road_anim_info = {
            self.settings.exit_gate: {'pos': 0, 'img': ...,
                                      'busy': False},
            self.settings.entry_gate: {'pos': 0, 'img': ...,
                                       'busy': False},
            'active': False}

        self.scale = scale
        if not scale_server_ip:
            scale_server_ip = ar_qdk.ip
        self.wr = WListener(ip=s.wrip, port=s.wrport, ar_ip=scale_server_ip,
                            scale_port=scale_server_port)
        self.aborted = False
        self.userRole = 'moder'
        ###################### PAGES ###################################
        self.authWin = AuthWin(root, settings, self, can)
        self.mainPage = MainPage(root, settings, self, can)
        self.statPage = Statistic(root, settings, self, can)
        self.sysNot = SysNot(root, settings, self, can)
        self.manual_gate_control = ManualGateControl(root, settings, self, can)
        #########################LAUNCHING##############################
        self.authWin.openWin()
        threading.Thread(target=self.wr.scale_reciever,
                         args=(scale_server_ip,), daemon=True).start()
        # threading.Thread(target=self.scaleRecieving,
        #                 args=(),
        #                 daemon=True).start()  # Запуск демона для обработки показания весов
        threading.Thread(target=self.ar_reciever_thread, args=(),
                         daemon=True).start()
        # Данные для рисования грузовика на весовой платформе
        self.orup_error_manager = OrupErrorsManager(
            canvas=self.terminal.can,
            types_list=self.get_trash_types_reprs(),
            cats_list=self.get_trash_cats_reprs(),
            text_color=cs.orup_error_txt_color,
            debtors_list=[],
            carriers_list=self.get_clients_reprs(),
            objects_list=self.get_table_reprs('pol_objects'),
            platforms_list=self.get_table_reprs('duo_pol_owners'))
        self.ar_qdk.execute_method("get_debtors")
        self.gcore_status = True
        self.create_qpi()
        root.protocol("WM_DELETE_WINDOW", self.closeApp)
        self.ar_qdk.execute_method('get_round_status')

    def turn_cams(self, on=True, cam_type=None):
        for cam in self.cameras_info:
            if not cam['enable'] or not self.get_cam_cm_enable(cam):
                continue
            if cam_type:
                if cam['type'] == cam_type:
                    cam["video_worker_inst"].can_show = on
            else:
                cam["video_worker_inst"].can_show = on

    def get_cam_ip(self, ar_cam_info):
        """ Чекнуть, не задан ли IP камеры в СМ, если нет - взять с АР"""
        cam_ip = self.cm_cams_info[ar_cam_info['type']]['ip']
        if not cam_ip:
            cam_ip = ar_cam_info['ip']
        return cam_ip

    def get_cam_port(self, ar_cam_info):
        """ Чекнуть, не задан ли IP камеры в СМ, если нет - взять с АР"""
        cam_ip = self.cm_cams_info[ar_cam_info['type']]['port']
        if not cam_ip:
            cam_ip = ar_cam_info['rtsp_port']
        return cam_ip

    def get_cam_cm_enable(self, ar_cam_info):
        """ Чекнуть, не задан ли IP камеры в СМ, если нет - взять с АР"""
        return self.cm_cams_info[ar_cam_info['type']]['enable']

    def create_video_streams(self):
        for cam in self.cameras_info:
            if cam['type'] == 'main' and cam[
                'enable'] and self.get_cam_cm_enable(cam):
                cam_ip = self.get_cam_ip(cam)
                port = self.get_cam_port(cam)
                inst = start_video_stream(self.root, self.terminal.can,
                                          xpos=417, ypos=280,
                                          v_width=420,
                                          v_height=400,
                                          cam_login=cam['login'],
                                          cam_pass=cam['pw'],
                                          cam_ip=cam_ip,
                                          cam_port=port,
                                          zoom_callback_func=self.terminal.cam_zoom_callback,
                                          hide_callback_func=self.terminal.cam_hide_callback,
                                          zoomed_y=self.terminal.h / 2,
                                          zoomed_x=self.terminal.w / 2,
                                          cam_type=cam['type'],
                                          zoomed_video_height=600,
                                          zoomed_video_width=1500)
                cam['video_worker_inst'] = inst
            if cam['type'] == 'cad_gross' and cam[
                'enable'] and self.get_cam_cm_enable(cam):
                cam_ip = self.get_cam_ip(cam)
                port = self.get_cam_port(cam)
                inst = start_video_stream(self.root, self.terminal.can,
                                          xpos=self.gross_x, ypos=self.gross_y,
                                          v_width=self.auto_cams_width,
                                          cam_port=port,
                                          v_height=self.auto_cams_height,
                                          cam_login=cam['login'],
                                          cam_pass=cam['pw'],
                                          cam_ip=cam_ip,
                                          zoom_callback_func=self.terminal.cam_zoom_callback,
                                          hide_callback_func=self.terminal.cam_hide_callback,
                                          zoomed_y=self.terminal.h / 2,
                                          zoomed_x=self.terminal.w / 2,
                                          cam_type=cam['type'],
                                          zoomed_video_height=600,
                                          zoomed_video_width=1500)
                cam['video_worker_inst'] = inst
            if cam['type'] == 'auto_exit' and cam[
                'enable'] and self.get_cam_cm_enable(cam):
                cam_ip = self.get_cam_ip(cam)
                port = self.get_cam_port(cam)
                inst = start_video_stream(self.root, self.terminal.can,
                                          xpos=self.auto_exit_x,
                                          ypos=self.auto_exit_y,
                                          v_width=self.auto_cams_width,
                                          cam_port=port,
                                          v_height=self.auto_cams_height,
                                          cam_login=cam['login'],
                                          cam_pass=cam['pw'],
                                          cam_ip=cam_ip,
                                          zoom_callback_func=self.terminal.cam_zoom_callback,
                                          hide_callback_func=self.terminal.cam_hide_callback,
                                          zoomed_y=self.terminal.h / 2,
                                          zoomed_x=self.terminal.w / 2,
                                          cam_type=cam['type'],
                                          zoomed_video_height=600,
                                          zoomed_video_width=1500)
                cam['video_worker_inst'] = inst

    def create_qpi(self):
        self.qpi = QPI('0.0.0.0', 50505, without_auth=True,
                       mark_disconnect=False,
                       core=self, auto_start=False)
        qpi_thread = threading.Thread(target=self.qpi.launch_mainloop,
                                      daemon=True)
        qpi_thread.start()

    def get_api_support_methods(self):
        methods = {'zoom_app': {'method': self.terminal.set_window_normal},
                   'close_app': {'method': self.closeApp},
                   'reboot': {'method': self.reboot}}
        return methods

    def recieve_ar_responses(self):
        response = self.ar_qdk.get_data()
        if not response:
            print("ERROR NO CONNECTION WITH AR")
            return response
        # if 'info' in response.keys():
        #    response = response['info'][0]
        try:
            core_method = response['core_method']
            method_result = response['info']
            return core_method, method_result
        except KeyError:
            print(f"ERROR {response}")
            pass

    def recieve_ar_responses_two(self, ar_qdk):
        response = ar_qdk.get_data()
        if not response:
            return response
        try:
            core_method = response['core_method']
            method_result = response['info']
            return core_method, method_result
        except KeyError:
            print(f"ERROR RESPONSE {response}")

            pass

    def null_weight(self):
        self.ar_qdk.execute_method('set_null_weight')

    def closeApp(self):
        threading.Thread(target=self.close_app_thread(), daemon=True).start()

    def escape_button_operator(self):
        if self.currentPage.blockImgDrawn:
            return
        if self.current != 'MainPage':
            self.root.bind('<Escape>',
                           lambda event: self.mainPage.openWin())

    def close_app_thread(self):
        """ Функция выполняющая завершающие операции, при закрытии программы """
        self.ar_qdk.capture_cm_terminated()
        self.ar_qdk.restart_unit()
        self.root.destroy()
        sys.exit(0)

    def ar_reciever_thread(self):
        while True:
            response = self.recieve_ar_responses()
            if not response:
                self.closeApp()
            else:
                core_method, method_result = response
                self.operate_ar_response(core_method, method_result)

    def operate_ar_response(self, core_method, method_result):
        # print(core_method, method_result)
        #print("T", locals())
        if core_method == 'get_unfinished_records':
            if method_result['status'] == 'success':
                self.operate_get_unfinished_records(method_result['info'])
            else:
                self.mainPage.tar.clearTree()
        elif core_method == "get_cat_type_map":
            self.operate_get_cat_type_map(method_result)
        if core_method == 'update_round_status':
            self.update_status_operate(method_result)
        elif core_method == 'cad_callback':
            self.cad_work(method_result)
        elif core_method == "get_gates_states":
            self.set_gates_states(method_result['internal_gate'],
                                  method_result['external_gate'])
        elif core_method == 'trailer_mode':
            self.operate_trailer_mode(method_result['stage'],
                                      method_result['previous_weights'])
        elif core_method == 'create_danger_text':
            self.terminal.create_danger_text(method_result['text'])
        elif core_method == 'tara_too_little':
            self.tara_too_little_react(
                too_little=method_result['too_little'],
                percentage=method_result['percentage'],
                avg_tara=method_result['avg_tare'])
        elif core_method == 'gross_too_little':
            self.gross_too_little_react(
                too_little=method_result['too_little'],
                avg_tare=method_result['avg_tare'],
                percentage=method_result['percentage'])
        elif core_method == 'get_cams':
            self.set_cam_info(method_result)
        elif core_method == 'get_last_event' and method_result[
            'status'] == 'success':
            self.operate_last_event(**method_result['info'][0])
        elif core_method == 'faultDetected':
            self.terminal.errors += [{'level1': method_result['info']}]
        elif core_method == 'try_auth_user':
            if method_result['status'] == 'success':
                self.try_login(method_result['info'][0]['auth_status'],
                               method_result['info'][0]['id'])
            else:
                self.authWin.incorrect_login_act()
        elif core_method == 'get_history':
            self.operate_get_history(method_result['records'],
                                     method_result['tonnage'],
                                     method_result['amount'])
        elif core_method == 'get_table_info':
            self.operate_table_info(s.tables_info, self.general_tables_dict,
                                    method_result['tablename'],
                                    method_result['info'])
        elif core_method == 'update_table':
            self.operate_table_info(s.tables_info, self.general_tables_dict,
                                    method_result['tablename'],
                                    method_result['info'],
                                    loading=False)
        elif core_method == 'get_debtors':
            self.operate_get_debtors(debtors_list=method_result)
        elif core_method == 'update_gate_status':
            self.operate_gate_changes_command(**method_result)
        elif core_method == 'update_cm':
            self.update_cm(**method_result)
        elif core_method == 'close_cm':
            self.closeApp()
        elif core_method == 'draw_auto_exit_with_pic' and self.ifORUPcanAppear(
                None):
            self.draw_auto_exit_with_pic(
                picture=method_result['picture'],
                course=method_result['course'],
                similar_numbers=method_result['similar_numbers'])
            # self.draw_auto_exit_pic(method_result['picture'])
        elif core_method == 'get_client_seal_pic':
            self.contragent_seal_pic(
                seal_pic_obj=method_result['seal_obj'],
                contragent_type=method_result['contragent_type'])
        elif core_method == 'car_detected' and self.ifORUPcanAppear(
                method_result['carnum']):
            self.car_detected_operate(
                auto_id=method_result['auto_id'],
                client_id=method_result['client_id'],
                carrier_id=method_result['last_carrier'],
                trash_cat_id=method_result[
                    'last_trash_cat'],
                trash_type_id=method_result[
                    'last_trash_type'],
                course=method_result['course'],
                have_gross=method_result['have_gross'],
                car_protocol=method_result[
                    'car_protocol'],
                polygon=method_result['last_polygon'],
                car_number=method_result['carnum'],
                pol_object=method_result['pol_object'],
                last_tare=method_result['last_tare'],
                car_read_client_id=method_result[
                    'car_read_client_id'],
                photo=method_result['photo'],
                source=method_result["source"])
        elif core_method == 'get_health_monitor':
            self.operate_get_health_monitor(method_result)
        elif core_method == 'get_status':
            self.operate_get_status(method_result)

    def operate_get_cat_type_map(self, method_result):
        self.trash_cat_type_map = method_result

    def set_gates_states(self, internal_gate, external_gate):
        if self.currentPage.blockImgDrawn:
            return
        external_gate_info = self.road_anim_info[self.settings.entry_gate]
        internal_gate_info = self.road_anim_info[self.settings.exit_gate]
        if internal_gate == 'unlock' and not internal_gate_info['busy']:
            self.road_anim_info[self.settings.exit_gate]['pos'] = 80
        if internal_gate == 'lock' and not internal_gate_info['busy']:
            self.road_anim_info[self.settings.exit_gate]['pos'] = 0
        if external_gate == 'unlock' and not external_gate_info['busy']:
            self.road_anim_info[self.settings.entry_gate]['pos'] = 80
        if external_gate == 'lock' and not external_gate_info['busy']:
            self.road_anim_info[self.settings.entry_gate]['pos'] = 0
        self.currentPage.draw_gate_arrows()

    def tara_too_little_react(self, too_little, percentage=None,
                              avg_tara=None):
        if too_little and not self.currentPage.blockImgDrawn:
            self.currentPage.initBlockImg('weight_too_little_win',
                                          'tare_too_little_btns')
            self.terminal.can.create_text(
                self.terminal.w / 2 + 20,
                self.terminal.h / 2 - 200,
                text="Слишком маленький вес!",
                fill=color_solutions.orup_fg_color,
                font=fonts.weight_too_little_header_font,
                tags=('danger_text', 'tempBtn'))
            self.terminal.can.create_text(
                self.terminal.w / 2 - 200,
                self.terminal.h / 2 - 170,
                text=f"Вес тары: \n\nЭто меньше чем {percentage}% средней тары\n"
                     f"этой машины ({int(avg_tara)} кг)\n"
                     f"Проверьте правильно ли машина стоит на весах,\n"
                     f"когда вес будет достаточный, это окно исчезнет\n"
                     f"и взвешивание продолжится как обычно.\n\n"
                     f"Однако вы можете сохранить текущий вес,\nесли все в порядке.",
                fill=color_solutions.orup_fg_color,
                font=fonts.weight_too_little_font,
                tags=('danger_text', 'tempBtn'),
                anchor='nw')
            self.currentPage.weight_too_little = True
            self.turn_cams(True, 'main')
        if not too_little:
            if self.terminal.blockImgDrawn:
                self.currentPage.destroyBlockImg('total')
            self.currentPage.weight_too_little = False

    def take_trailer_weight(self):
        self.currentPage.destroyBlockImg('total')
        self.ar_qdk.execute_method('take_trailer_weight')
        self.currentPage.trail_win_drawn = False

    def operate_trailer_mode(self, stage, previous_weights):
        self.currentPage.trail_win_drawn = True
        if stage == 0:
            self.currentPage.initBlockImg('trailer_stage0_win',
                                          'trailer_win_btns')
        elif stage == 1:
            self.currentPage.initBlockImg('trailer_stage1_win',
                                          'trailer_win_btns')
        if previous_weights:
            self.currentPage.can.create_text(self.terminal.w / 2 + 90,
                                             self.terminal.h / 2 + 60,
                                             font=fonts.weight_trail_font,
                                             text=f"+{previous_weights[0]} кг",
                                             fill='#BABABA',
                                             tag='tempBtn')
            self.currentPage.can.create_text(self.terminal.w / 2 + 165,
                                             self.terminal.h / 2 - 145,
                                             font='"Montserrat Regular" 11',
                                             text=f"({previous_weights[0]} кг)",
                                             fill='#BABABA',
                                             tag='tempBtn', anchor='w')
        self.turn_cams(True, 'main')

    def gross_too_little_react(self, too_little, percentage=None,
                               avg_tare=None):
        print("TT22", locals())
        if too_little and not self.currentPage.blockImgDrawn:
            self.currentPage.initBlockImg('weight_too_little_win',
                                          'tare_too_little_btns')
            self.terminal.can.create_text(
                self.terminal.w / 2 + 20,
                self.terminal.h / 2 - 200,
                text="Слишком маленький вес!",
                fill=color_solutions.orup_fg_color,
                font=fonts.weight_too_little_header_font,
                tags=('danger_text', 'tempBtn'))
            self.terminal.can.create_text(
                self.terminal.w / 2 - 200,
                self.terminal.h / 2 - 170,
                text=f"Вес груза: \n\nЭто меньше чем {percentage}% средней тары\n"
                     f"этой машины ({int(avg_tare)} кг)\n"
                     f"Проверьте правильно ли машина стоит на весах,\n"
                     f"когда вес будет достаточный, это окно исчезнет\n"
                     f"и взвешивание продолжится как обычно.\n\n"
                     f"Однако вы можете сохранить текущий вес,\nесли все в порядке.",
                fill=color_solutions.orup_fg_color,
                font=fonts.weight_too_little_font,
                tags=('danger_text', 'tempBtn'),
                anchor='nw')
            self.turn_cams(True, 'main')
            self.currentPage.weight_too_little = True
        if not too_little:
            if self.currentPage.blockImgDrawn:
                self.currentPage.destroyBlockImg('total')
            self.currentPage.weight_too_little = False

    def ttl_abort_round(self):
        self.ar_qdk.execute_method('abort_round')
        self.currentPage.destroyBlockImg('total')
        self.currentPage.trail_win_drawn = False
        self.currentPage.weight_too_little = False

    def ttl_save_current_weight(self):
        self.ar_qdk.execute_method('set_take_tare')
        self.currentPage.destroyBlockImg('total')

    def cad_work(self, info):
        self.cad_activate_time = datetime.datetime.now()
        if ((
                self.current != 'MainPage' and self.current != 'ManualGateControl')
                or (
                        self.currentPage.blockImgDrawn and not self.currentPage.orupState) or self.terminal.cam_zoom):
            return
        text = 'ДВИЖЕНИЕ'
        if info['cam_type'] == 'cad_gross':
            x = self.gross_x - self.auto_cams_width / 2
            y = self.gross_y - self.auto_cams_height / 2 + 60
            self.terminal.can.create_text(x + 350, y - 16, text=text,
                                          tag='cad_color',
                                          fill="#F5B85E",
                                          font=fonts.cad_work_font)
        else:
            x = self.auto_exit_x - self.auto_cams_width / 2
            y = self.auto_exit_y - self.auto_cams_height / 2 + 60
            self.terminal.can.create_text(x + 65, y - 16, text=text,
                                          tag='cad_color',
                                          fill="#F5B85E",
                                          font=fonts.cad_work_font)
        threading.Thread(target=self.cad_color_remover).start()

    def cad_color_remover(self):
        while True:
            if datetime.datetime.now() - self.cad_activate_time > datetime.timedelta(
                    seconds=5):
                self.terminal.can.delete('cad_color')
                break
            sleep(1)

    def draw_auto_exit_with_pic(self, course, picture, similar_numbers=None):
        # if course == "NONE":
        #    if similar_numbers:
        #        threading.Thread(target=self.draw_auto_entrance_pic,
        #                         args=(picture, self.terminal.w / 6.4,
        #                               self.terminal.h / 2)).start()
        #        self.currentPage.orupAct(call_method='unknown_number',
        #                                 course=course)
        #    else:
        #        self.currentPage.orupActExit(carnum='deff', call_method="auto",
        #                                     course=course, with_pic=picture)
        # else:
        crop_tuple = self.settings.external_cam_frame
        if course == "OUT":
            crop_tuple = self.settings.internal_cam_frame
        threading.Thread(target=self.draw_auto_entrance_pic,
                         args=(picture, self.terminal.w / 6.4,
                               self.terminal.h / 2, crop_tuple)).start()
        self.currentPage.orupAct(call_method='unknown_number',
                                 course=course)

    def draw_auto_exit_pic(self, picture):
        img = Image.open(io.BytesIO(picture))
        im_r = img.crop((int(1920 / 2 - 700), int(1080 / 2 - 200),
                         int(1920 / 2 + 500), int(1080 / 2 + 400)))
        img_byte_arr = io.BytesIO()
        im_r.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        self.photoimg = ImageTk.PhotoImage(
            Image.open(io.BytesIO(img_byte_arr)))
        self.currentPage.can.create_image(self.terminal.w / 2,
                                          self.terminal.h / 3,
                                          image=self.photoimg,
                                          tags=('orupentry',))
        self.currentPage.can.create_text(self.terminal.w / 2,
                                         self.terminal.h / 10,
                                         text='система не распознала гос.номер авто',
                                         font=fonts.date_font, fill='white',
                                         tags=('orupentry',))

    def contragent_seal_pic(self, seal_pic_obj, contragent_type: str):
        if contragent_type == 'client':
            self.currentPage.can.delete('orup_client_seal')
            if seal_pic_obj:
                self.draw_auto_entrance_pic(seal_pic_obj,
                                            self.terminal.w / 2 + 700,
                                            self.terminal.h / 2 - 127,
                                            crop=(0, 0, 500, 500),
                                            img_tag='orup_client_seal',
                                            corners=10)
        elif contragent_type == 'carrier':
            self.currentPage.can.delete('orup_carrier_seal')
            if seal_pic_obj:
                self.draw_auto_entrance_pic(seal_pic_obj,
                                            self.terminal.w / 2 + 700,
                                            self.terminal.h / 2 + 170,
                                            crop=(0, 0, 500, 500),
                                            img_tag='orup_carrier_seal',
                                            corners=10)

    def draw_auto_entrance_pic(self, picture, x, y,
                               crop: tuple = (700, 380, 1300, 1080),
                               img_tag=None, corners=None):
        tags = ['orupentry']
        if img_tag:
            tags.append(img_tag)
        img = Image.open(io.BytesIO(picture))
        if corners:
            img = functions.add_corners(img, corners)
        im_r = img.crop(crop)
        img_byte_arr = io.BytesIO()
        im_r.save(img_byte_arr, format='PNG')
        self.img_byte_arr = img_byte_arr.getvalue()
        orup_img = ImageTk.PhotoImage(
            Image.open(io.BytesIO(self.img_byte_arr)))
        self.terminal.orup_imgs.append(orup_img)
        self.currentPage.can.create_image(x, y, image=orup_img,
                                          tags=tags)

    def operate_get_status(self, status, *args, **kwargs):
        """ Получить статус GCore"""
        self.gcore_status = status
        if status == 'locked':
            self.terminal.block_gravity()

    def operate_get_health_monitor(self, health_monitor: dict, *args,
                                   **kwargs):
        """ От GCore пришел словарь, содержащий информацию типа health_monitor"""
        self.terminal.check_gcore_health(health_monitor)
        self.sysNot.tar.fillTree(health_monitor)

    def operate_last_event(self, trash_cat, trash_type, carrier, no_exit,
                           client_id, object, polygon,
                           *args, **kwargs):
        """ От AR пришла информация о последнем заезде авто """
        carrier = self.get_client_repr(carrier)
        trash_cat = self.get_trash_cat_repr(trash_cat)
        trash_type = self.get_trash_type_repr(trash_type)
        client = self.get_client_repr(client_id)
        pol_object = self.get_pol_object_repr(object)
        platform = self.get_polygon_platform_repr(polygon)
        if carrier != self.currentPage.contragentCombo.get():
            self.currentPage.contragentCombo.set(
                self.validate_last_event(carrier))
        self.currentPage.trashCatOm.set(self.validate_last_event(trash_cat))
        self.currentPage.trashTypeOm.set(self.validate_last_event(trash_type))
        self.currentPage.platform_choose_combo.set(
            self.validate_last_event(platform, message='Выберите площадку'))
        self.currentPage.objectOm.set(
            self.validate_last_event(pol_object,
                                     message='Выберите объект размещения'))
        if self.currentPage.clientOm.state() and \
                self.currentPage.clientOm.state()[0] == 'disable':
            pass
        else:
            if client != self.currentPage.clientOm.get():
                self.currentPage.clientOm.set(
                    self.validate_last_event(client,
                                             message='Выберите клиента (плательщика)'))

        self.currentPage.no_exit_var.set(no_exit)
        if trash_cat == "ТКО":
            self.currentPage.trash_cat_tko_react()

    def validate_last_event(self, num, message=0):
        if num:
            return num
        else:
            return message

    def operate_get_debtors(self, debtors_list):
        self.orup_error_manager.all_args['debtors_list'] = debtors_list

    def operate_gate_changes_command(self, gate_name, status, *args, **kwargs):
        """ Обработчик команды от GCore об изменении положении стрелы шлагбаума """
        if gate_name.lower() in (
                "entry", "внешний шлагбаум") and status == 'open':
            self.terminal.open_entry_gate_operation_start()
        elif gate_name.lower() in (
                "entry", "внешний шлагбаум") and status == 'close':
            self.terminal.close_entry_gate_operation_start()
        elif gate_name.lower() in (
                'exit', "внутренний шлагбаум") and status == 'open':
            self.terminal.open_exit_gate_operation_start()
        elif gate_name.lower() in (
                'exit', "внутренний шлагбаум") and status == 'close':
            self.terminal.close_exit_gate_operation_start()

    def update_cm(self, new_version=None):
        command = 'pip3 install --upgrade cm_two'
        if new_version:
            command += f'=={new_version}'
        command += ' --no-cache-dir'
        os.system(command)
        self.create_update_text()

    def create_update_text(self):
        self.terminal.can.create_text(self.terminal.w / 2,
                                      self.terminal.h / 20,
                                      text='ДОСТУПНО ОБНОВЛЕНИЕ! ПЕРЕЗАПУСТИТЕ ПРИЛОЖЕНИЕ!',
                                      fill='gray',
                                      font=fonts.loading_status_font)

    def operate_table_info(self, tables_info, general_tables_dict, tablename,
                           result, loading=True, *args, **kwargs):
        """ Когда пришли данные от GCore о содержимом таблицы tablename """
        # Получаем репрезентативное значние
        repr_value = tables_info[tablename]['repr']
        # Отформатировать данные, что бы получить данные типа {'repr':{col1:1'val1'}, 'repr':{'col2': val2}}
        formated = self.format_wdb_table_info(result, keyname=repr_value)
        # Добавить в словарь, содержащие содержимое всех таблиц инфу вида {'tablename': {repr: {...}, repr: {...} }}
        general_tables_dict[tablename] = formated
        if loading:
            self.create_loading_info(tablename, self.loadingcan)
        elif tablename == 'clients':
            self.orup_error_manager.all_args[
                'carriers_list'] = self.get_clients_reprs()
            self.statPage.full_clients()
            self.statPage.full_carriers()
        if tablename == 'clients':
            for name, info in self.general_tables_dict[
            'clients'].items():
                if info['region_operator']:
                    self.region_operators.append(name)
                if info['tko_carrier']:
                    self.tko_carriers.append(name)

    def create_loading_info(self, tablename, loadingcan):
        try:
            loadingcan.delete('loading_status')
            self.loading_repcentage += 100 / len(s.tables_info.keys())
            loading_percentage = str(int(self.loading_repcentage)) + '%'
            loadingcan.create_text(self.root.winfo_screenwidth() / 2,
                                   self.root.winfo_screenheight() / 2 * 1.32,
                                   text=s.tables_info[tablename][
                                       'loading_description'],
                                   font=fonts.loading_status_font,
                                   fill='white',
                                   tags=('loading_info', 'loading_status'))
            loadingcan.create_text(self.root.winfo_screenwidth() / 2,
                                   self.root.winfo_screenheight() / 2,
                                   text=loading_percentage,
                                   font=fonts.loading_percents_font,
                                   fill='white',
                                   tags=('loading_info', 'loading_status'))
        except _tkinter.TclError:
            pass

    def format_wdb_table_info(self, result: list, keyname: str, *args,
                              **kwargs):
        """ Создаем словарь, где ключом будет keyname записи, а значением - вся информация по записи
        (тоже в виде словаря)"""
        formated = {}
        print(locals())
        for record in result:
            key = record[keyname]
            formated[key] = record
        return formated

    def operate_get_unfinished_records(self, info, *args, **kwargs):
        if self.currentPage.blockImgDrawn or self.currentPage.cam_zoom:
            return
        if self.current == "Statistic":
            self.currentPage.get_history()
            return
        self.unfinished_records = info
        self.fill_current_treeview(info)


    def fill_current_treeview(self, info):
        first = False
        self.mainPage.tree.lower()
        self.mainPage.tar.clearTree()
        for rec in info:
            package_id = rec['package_id']
            if package_id:
                act_id = int(rec['act_number'])
            else:
                act_id = rec['id']
            if not rec['time_out'] or first:
                rec['trash_cat'] = self.get_trash_cat_repr(rec['trash_cat'])
                self.mainPage.tar.fillTree(id=act_id, brutto=rec['brutto'],
                                           tara=rec['tara'],
                                           cargo=rec['cargo'],
                                           time_in=rec['time_in'],
                                           trash_cat=rec['trash_cat'],
                                           car_number=rec['car_number'],
                                           notes=rec['full_notes'],
                                           record_id=rec['id'])
            else:
                rec['trash_cat'] = self.get_trash_cat_repr(rec['trash_cat'])
                self.mainPage.tar.fillTree(id=act_id, brutto=rec['brutto'],
                                           tara=rec['tara'],
                                           cargo=rec['cargo'],
                                           time_in=rec['time_in'],
                                           trash_cat=rec['trash_cat'],
                                           car_number=rec['car_number'],
                                           notes=rec['full_notes'],
                                           tags=('evenrow',),
                                           record_id=rec['id'])
                first = True
        self.mainPage.tar.sortId(self.mainPage.tree, '#0',
                                 reverse=True)
        self.mainPage.tree.lift()

    def open_manual_from_orup(self):
        self.currentPage.destroyORUP('total')
        self.manual_gate_control.openWin()

    def operate_get_history(self, records, tonnage, amount):
        """ От GCore пришел список, содержащий информацию обо всех заездов за запрашиваемый период в виде словарей """
        new_tree = self.statPage.create_tree()
        self.statPage.place_amount_info(tonnage, amount, tag='amount_info')
        uncount_records = []
        for record in records:
            if record['package_id']:
                act_number = record['act_number']
            else:
                act_number = record['record_id']
            self.statPage.tar.insertRec(
                id=act_number,
                car_number=record['car_number'],
                carrier=self.get_client_repr(
                    record.pop('carrier')),
                brutto=record['brutto'],
                tara=record['tara'],
                cargo=record['cargo'],
                trash_cat=self.get_trash_cat_repr(
                    record.pop('trash_cat')),
                trash_type=self.get_trash_type_repr(
                    record.pop('trash_type')),
                auto=self.get_auto_repr(
                    record.pop('auto')),
                time_in=record['time_in'],
                time_out=record['time_out'],
                notes=record['full_notes'],
                client=self.get_client_repr(
                    record.pop('client_id')),
                record_id=record['record_id'])
            self.statPage.history[record['record_id']] = record
            if record['tara'] == 0:
                uncount_records.append(act_number)
        #self.statPage.can.delete('tree')
        if self.current == "Statistic":
            self.statPage.place_uncount_records(uncount_records)
            self.statPage.draw_stat_tree(new_tree)
            self.statPage.mark_changed_rec()


    def operate_ar_sys_info(self, info):
        for k, v in info.items():
            if k == 'data' and 'Внешний' in v and 'открывается.' in v:
                #print('Внешний открывается')
                self.terminal.open_entry_gate_operation_start()
            elif k == 'data' and 'Внешний' in v and 'закрывается.' in v:
                #print('Внешний закрывается')
                self.terminal.close_entry_gate_operation_start()
            elif k == 'data' and 'Внутренний' in v and 'открывается.' in v:
               # print('Внутренний открывается')
                self.terminal.open_exit_gate_operation_start()
            elif k == 'data' and 'Внутренний' in v and 'закрывается.' in v:
               # print('Внутренний закрывается')
                self.terminal.close_exit_gate_operation_start()

    def update_status_operate(self, info):
        # Если получена команда на обновление статуса заезда
        if not info['status']:
            return
        self.status_ready = False
        self.road_anim_info['active'] = True
        if str(info['notes']).strip() == 'Запись обновлена':
            self.updateMainTree()
        try:
            for k, v in info.items():
                self.road_anim_info[k] = v
            if info[
                'status'] == 'Начало взвешивания' and self.currentPage.orupState:
                self.currentPage.destroyORUP('total')
            if (info[
                'status'].strip() == 'Ожидание пересечения фотоэлементов.'):
                self.mainPage.make_abort_active()
            if (info['protocol'].strip() == 'Машина заезжает.' or info[
                'protocol'].strip() == 'Машина выезжает.'):
                self.updateMainTree()
            self.drawStatus()
            if (
                    self.current == 'MainPage' or self.current == 'ManualGateControl') \
                    and not self.currentPage.blockImgDrawn:
                self.drawCarMoving()
            if (info['status'].strip() == 'Протокол завершен'
                    or info['status'].strip() == 'Время истекло!'
                    or info['status'].strip() == 'Заезд прерван вручную!'):
                self.operateStatusEnd()
        except:
            print(traceback.format_exc())

    def draw_road_anim(self):
        if self.road_anim_info['active']:
            self.drawCarMoving()
            self.drawStatus()

    def car_detected_operate(self, auto_id: int, client_id: int,
                             trash_cat_id: int, trash_type_id: int,
                             course: str, have_gross: bool, car_protocol,
                             polygon: id, pol_object: int, carrier_id: int,
                             source,
                             car_number: str = None, last_tare=None,
                             car_read_client_id=None, photo=None,
                             **kwargs):
        # Если получена команда на открытие ОРУП
        self.currentPage.orupState = True
        # Получить репрезентативные значения по ID
        client_repr = self.get_client_repr(client_id)
        carrier_repr = self.get_client_repr(carrier_id)
        trash_cat_repr = self.get_trash_cat_repr(trash_cat_id)
        trash_type_repr = self.get_trash_type_repr(trash_type_id)
        auto_repr = self.get_auto_repr(auto_id)
        if not auto_repr:
            auto_repr = car_number
        polygon = self.get_polygon_repr(polygon)
        pol_object = self.get_pol_object_repr(pol_object)
        self.currentPage.car_protocol = car_protocol

        if have_gross:
            # Если брутто взвешено, вывести ОРУП-тара
            self.currentPage.orupActExit(carnum=auto_repr, call_method="auto",
                                         course=course)
        else:
            # Если же нет (надо инициировать заезд), вывести ОРУП-брутто
            call_method = "auto"
            self.currentPage.orupAct(carnum=auto_repr, contragent=carrier_repr,
                                     trashType=trash_type_repr,
                                     trashCat=trash_cat_repr,
                                     call_method=call_method,
                                     car_protocol=car_protocol,
                                     course=course, polygon=polygon,
                                     pol_object=pol_object,
                                     client=client_repr,
                                     last_tare=last_tare,
                                     car_read_client_id=car_read_client_id,
                                     source=source
                                     )
            if trash_cat_repr == "ТКО": #or trash_cat_repr == "Хвосты":
                self.currentPage.trash_cat_tko_react()
            if photo:
                # call_method = 'photo'
                crop_tuple = self.settings.external_cam_frame
                if course == "OUT":
                    crop_tuple = self.settings.internal_cam_frame
                threading.Thread(target=self.draw_auto_entrance_pic,
                                 args=(photo, self.terminal.w / 6.4,
                                       self.terminal.h / 2,
                                       crop_tuple)).start()

    def fetch_if_record_init(self, carnum):
        active_cars = self.terminal.get_cars_inside()
        if carnum in active_cars:
            return True

    def fetch_car_protocol(self, carnum):
        try:
            car_protocol = self.general_tables_dict[s.auto_table][carnum][
                'id_type']
        except KeyError:
            car_protocol = 'tails'
        return car_protocol

    def open_entry_gate(self):
        self.ar_qdk.operate_gate_manual_control(operation='open',
                                                gate_name='entry')

    def close_entry_gate(self):
        self.ar_qdk.operate_gate_manual_control(operation='close',
                                                gate_name='entry')

    def open_exit_gate(self):
        self.ar_qdk.operate_gate_manual_control(operation='open',
                                                gate_name='exit')

    def close_exit_gate(self):
        self.ar_qdk.operate_gate_manual_control(operation='close',
                                                gate_name='exit')

    def ifORUPcanAppear(self, car_number):
        # Возвращает TRUE, если можно нарисовать окно ОРУП
        if (self.currentPage and self.current != 'AuthWin'
                and self.current != 'ManualGateControl'
                and self.status_ready and not self.currentPage.blockImgDrawn
                and self.orup_blacklist_can_init(car_number)):
            return True
        else:
            return False

    def getInfoFromDict(self, info, target):
        # Получить зачение словаря с информацией о команде по ключу
        goal = info[target]
        if goal == 'none':
            goal = 'Неизвестно'
        return goal

    def operateStatusEnd(self):
        '''Обработчик завершения заезда авто'''
        sleep(1)
        self.currentPage.can.delete('mtext', 'car_icon')
        self.status_ready = True
        self.road_anim_info['active'] = False
        self.mainPage.make_abort_unactive()

    def updateMainTree(self, mode='usual'):
        '''Обновить таблицу текущих записей'''
        if self.current == 'MainPage' and not self.mainPage.orupState \
                and not self.currentPage.cam_zoom:
            self.mainPage.updateTree()
            if mode == 'create':
                self.mainPage.drawMainTree()

    def getData(self, sock):
        '''Получает сериализированные данные и возвращает их в исходную форму'''
        data = sock.recv(4096)
        if data: data = pickle.loads(data)
        return data

    def getOrupMode(self, course, id_type):
        '''Определить атрибут, передаваемый ОРУПу, согласно курсу движения авто'''
        mode = '_'.join((id_type, course))
        return mode

    def drawStatus(self):
        '''Рисует статус заезда текстом при заезде-выезде на главном меню'''
        if self.currentPage.blockImgDrawn:
            return
        self.mainPage.can.delete('mtext')
        if self.current == 'MainPage' and self.mainPage.orupState == False:
            notes = f"Гос. номер:\n{self.road_anim_info['carnum']}\n" \
                    f"Cтатус:\n{self.road_anim_info['status']}\n"
            if self.road_anim_info['notes']:
                notes += f"Примечания:\n{self.road_anim_info['notes']}\n"
            self.mainPage.can.create_text(self.terminal.w / 9.15,
                                          self.terminal.h / 2.72,
                                          text=notes, font=fonts.status_text,
                                          tags=('mtext', 'statusel'),
                                          fill='#BABABA',
                                          anchor=NW)

    def drawCarMoving(self):
        """ Рисует грузовик на грузовой платформе при инициировании протокола
		заезда или выезда на главном меню """
        self.car_protocol = self.road_anim_info['protocol']
        self.car_direction = self.road_anim_info['course']

        car_direction_txt = self.road_anim_info['face']
        cur_pos_txt = self.road_anim_info['pos']

        cur_pos_cm = self.settings.car_poses[cur_pos_txt]
        obj = self.settings.car_face_info[car_direction_txt]
        obj = self.terminal.getAttrByName(obj)
        self.drawCarIcon(obj, cur_pos_cm)

    def drawCarIcon(self, obj, poses):
        self.mainPage.can.delete('car_icon')
        self.mainPage.can.create_image(poses, image=obj[3], anchor=NW,
                                       tag='car_icon')

    def try_login(self, status, id, *args, **kwargs):
        """ Обрабатывает результат авторизации от GravityCore """
        if status:
            self.current_userid = id
            self.currentPage.drawToolbar()
            self.authWin.rebinding()
            self.mainPage.openWin()
            self.status_ready = True
            if not self.currentPage.clockLaunched:
                self.currentPage.start_clock()
                self.currentPage.clockLaunched = True

    def get_gcore_status(self):
        # Запросить статус GCore
        self.ar_qdk.get_status()

    def close_record(self, record_id):
        """ Закрыть незаконченную запись (только раунд брутто) """
        self.ar_qdk.close_opened_record(record_id=record_id)
        self.currentPage.destroyBlockImg()

    def cancel_tare(self, record_id):
        self.ar_qdk.cancel_tare(record_id=record_id)
        self.currentPage.destroyBlockImg()

    def open_new_page(self, page):
        try:
            self.currentPage.page_close_operations()
        except:
            pass
        self.current = page.name
        self.currentPage = page

    def get_polygon_platforms_reprs(self, table_name=s.polygon_objects_table):
        """ Вернуть репрезентативные значения из таблицы организаций-пользователей весовой площадкой """
        return self.get_table_reprs(table_name)

    def get_polygon_platform_id(self, polygon_repr):
        return db_funcs.get_id_by_repr_table(self.general_tables_dict,
                                             s.polygon_objects_table,
                                             polygon_repr)

    def get_polygon_object_id(self, object_repr):
        return db_funcs.get_id_by_repr_table(self.general_tables_dict,
                                             'pol_objects',
                                             object_repr)

    def get_pol_object_repr(self, pol_object_id):
        """ Вернуть репрезентативные значения из таблицы юзеров """
        return db_funcs.get_repr_by_id_table(self.general_tables_dict,
                                             'pol_objects', pol_object_id)

    def get_pol_objects_reprs(self):
        """ Вернуть репрезентативные значения из таблицы pol_objects"""
        return self.get_table_reprs('pol_objects')

    def get_polygon_platform_repr(self, pol_platform_id):
        """ Вернуть репрезентативные значения из таблицы юзеров """
        return db_funcs.get_repr_by_id_table(self.general_tables_dict,
                                             s.polygon_objects_table,
                                             pol_platform_id)

    def get_auto_reprs(self, auto_table=s.auto_table):
        """ Вернуть репрезентативные значения из таблицы авто """
        return self.get_table_reprs(auto_table)

    def get_auto_repr(self, auto_id):
        """ Вернуть репрезентативные значения из таблицы юзеров """
        return db_funcs.get_repr_by_id_table(self.general_tables_dict,
                                             s.auto_table, auto_id)

    def get_auto_id(self, auto_repr):
        """ Вернуть id юзера с репрезегтативным значением auto_repr"""
        return db_funcs.get_id_by_repr_table(self.general_tables_dict,
                                             s.auto_table, auto_repr)

    def get_users_reprs(self, users_table=s.users_table):
        """ Вернуть репрезентативные значения из таблицы users"""
        return self.get_table_reprs(users_table)

    def get_user_repr(self, user_id):
        """ Вернуть репрезентативные значения из таблицы юзеров """
        return db_funcs.get_repr_by_id_table(self.general_tables_dict,
                                             s.users_table, user_id)

    def get_user_id(self, user_repr):
        """ Вернуть id юзера с репрезегтативным значением user_repr"""
        return db_funcs.get_id_by_repr_table(self.general_tables_dict,
                                             s.users_table, user_repr)

    def get_trash_types_reprs(self, trash_types_table=s.trash_types_table):
        """ Вернуть все репрезентативные значения из таблицы видов грузов """
        return self.get_table_reprs(trash_types_table)

    def get_trash_type_repr(self, trash_type_id):
        """ Вернуть репрезентативное название trash_type по его id """
        return db_funcs.get_repr_by_id_table(self.general_tables_dict,
                                             s.trash_types_table,
                                             trash_type_id)

    def get_polygon_repr(self, polygon_id):
        """ Вернуть репрезентативное название полигона по его id """
        return db_funcs.get_repr_by_id_table(self.general_tables_dict,
                                             s.polygon_objects_table,
                                             polygon_id)

    def get_trash_type_id(self, type_name):
        """ Вернуть id вида груза type_name"""
        return db_funcs.get_id_by_repr_table(self.general_tables_dict,
                                             s.trash_types_table, type_name)

    def get_trash_cats_reprs(self, trash_cats_table=s.trash_cats_table):
        """ Вернуть репрезентативные значения из таблицы категорий грузов """
        return self.get_table_reprs(trash_cats_table)

    def get_trash_cat_repr(self, trash_cat_id):
        """ Вернуть репрезентативное название trash_cat по его id """
        return db_funcs.get_repr_by_id_table(self.general_tables_dict,
                                             s.trash_cats_table,
                                             trash_cat_id)

    def get_trash_cat_id(self, cat_name):
        """ Вернуть id категории груза cat_name"""
        return db_funcs.get_id_by_repr_table(self.general_tables_dict,
                                             s.trash_cats_table,
                                             cat_name)

    def get_clients_reprs(self, clients_table=s.clients_table):
        """ Вернуть все репрезентативные значения из таблицы Клиенты"""
        return self.get_table_reprs(clients_table)

    def get_client_repr(self, client_id):
        """ Вернуть репрезентативное название client по его id """
        return db_funcs.get_repr_by_id_table(self.general_tables_dict,
                                             s.clients_table, client_id)

    def get_client_id(self, client):
        """ Вернуть id клиента client"""
        return db_funcs.get_id_by_repr_table(self.general_tables_dict,
                                             s.clients_table, client)

    def get_table_reprs(self, table_name):
        """ Вернуть репрезентативные (понтятные для людей) значения из таблицы tablename
         ( например cat_name из trash_cats) """
        return db_funcs.get_table_rerps(self.general_tables_dict, table_name)

    def get_trashtypes_by_trashcat_repr(self, trash_cat_repr):
        """ Вернуть список видов грузов, у которых trash_cat = trash_cat_repr[id]"""
        trash_types = db_funcs.get_trashtypes_by_trashcat_repr(
            self.general_tables_dict, s.trash_types_table,
            s.trash_cats_table, trash_cat_repr)
        return trash_types

    def get_gcore_health_monitor(self):
        """ Получить состояние GCore """
        self.ar_qdk.get_health_monitor()

    def get_wdb_tables_info(self):
        """ Сохранить все данные таблиц wdb в словарь вида {tablename0: [info0, info1], tablename1: [info4, info[2]}"""
        for tablename in list(s.tables_info.keys()):
            self.ar_qdk.get_table_info(table_name=tablename)
            while True:
                # response = self.recieve_ar_responses()
                response = self.recieve_ar_responses_two(self.ar_qdk)
                if response:
                    core_method, method_result = response
                    if core_method == 'get_table_info':
                        self.operate_ar_response(core_method, method_result)
                        break

    def orup_blacklist_new_car(self, car_num):
        self.orup_black_list[car_num] = {'declines': 1,
                                         'last_decline': datetime.datetime.now()}

    def orup_blacklist_increment(self, car_num):
        self.orup_black_list[car_num]['declines'] += 1
        self.orup_black_list[car_num]['last_decline'] = datetime.datetime.now()

    def orup_blacklist_del(self, car_num):
        try:
            self.orup_black_list.__delitem__(car_num)
        except KeyError:
            pass

    def orup_blacklist_can_init(self, car_number):
        """ Проверить, есть ли авто в blacklist и можно ли открыть для него
        ОРУП """
        try:
            blacklist_info = self.orup_black_list[car_number]
            if datetime.datetime.now() > (blacklist_info['last_decline']
                                          + datetime.
                                                  timedelta(0, 3)
                                          * blacklist_info['declines']):
                return True
        except KeyError:
            return True

    def set_cam_info(self, info):
        new_l = []
        for cam in info:
            cam['zoomed'] = False
            new_l.append(cam)
        self.cameras_info = new_l
        self.create_video_streams()

    def reboot(self):
        command = 'systemctl reboot'
        command = "echo {}|sudo -S {}".format('Assa+123', command)
        os.system(command)
