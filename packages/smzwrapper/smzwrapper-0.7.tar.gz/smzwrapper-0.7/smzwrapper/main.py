import datetime
import math
import re
import struct
from base64 import b64decode


class SMZDecoder:
    smz_codes = {b'\x01': ((1, 1, 4, 4, 4, 1, 1, 0), ('DATA_I [Инклинометр]#Id', '#Num', '>I#UTS', '>f#X', '>f#Y', '#Addr', '#Res', '#From|2')),
                 b'\x11': ((1, 4, 4, 4), ('DATA_I_N [Инклинометр]#Id', '>I#UTS', '>f#X', '>f#Y')),
                 b'\x05': ((1, 1, 1, 4, 2, 0), ('DATA_T [Термокоса]#Id', 'B#N1', 'B#NN', '>I#UTS', '>h#Tn#C°', '#From|4')),
                 b'\x06': ((1, 1, 4, 4, 4, 2, 0), ('DATA_L [Датчик перемещения/деформации]#Id', '#Num', '>I#UTS', '>f#X#мм|мкм/м', '>f#T#C°', '#Null', '#From|2')),
                 b'\x1a': ((1, 4, 4, 4), ('DATA_HG [Гигрометр]#Id', '>I#UTS', '>f#T#C°', '>f#Rh#% отн. вл.')),
                 b'\x1b': ((1, 4, 4, 4), ('DATA_PZ [Пьезометр]#Id', '>I#UTS', '>I#T#C°', '>I#P#Па')),
                 b'\x1c': ((1, 1, 4, 4, 4, 1, 1, 0), ('DATA_CU_VW#Id', '#Num', '>I#UTS', '>f#F#Гц', '>f#R#Ом', '#Addr', '#Res', '#From|2')),
                 b'\x02': ((1, 4, 1, 1, 1, 1, 1, 2, 1, 4, 2, 1, 1, 2, 1, 1),
                           ('INFO#Id', '>f#Vcc#В', '#P#%', '#Num', '#E', '#N1', '#N2', '>h#Rs#dBm', '#V#вер. протокола', '#UID', '#FSN', '#CNT', '#RES', '#FW_VER', '#Type', '#N3')),
                 b'\x12': ((1, 1, 2, 1, 2, 1, 2), ('SINFO#Id', '#E', '>h#Rs', '#V#вер. протокола', '#FW_VER', '#Type', '>H#S_VER')),
                 b'\x13': ((1, 4, 1), ('SBAT#Id', '>f#Vbat', '#Pbat#%')),
                 b'\x03': ((1, 4), ('TIME_RQ#Id', '>F#DUTS')),
                 b'\x04': ((1, 2, 2, 2, 1, 1, 2, 4, 4, 1, 2), ('SETTINGS#Id', '>H#MP', '>H#MT', '>H#LP', '#Num1', '#Num2', '#Dly', '>f#Xa', '>f#Ya', '#SW', '>H#IP')),
                 b'\x14': ((1, 2, 2, 1, 2), ('SETTINGS_1#Id', '>H#MP', '>H#LP', '#Num2', '#Dly')),
                 b'\x15': ((1, 1, 2), ('SETTINGS_2#Id', '>B#FT', '>H#TIME')),
                 b'\x16': ((1, 1, 1, 3, 1, 2, 1), ('SETTINGS_3#Id', '>B#FC', '>B#CH', '#NU', '>B#FT', '>H#TIME', '#CONF')),
                 b'\x18': ([1], ['BAT_REPLACE#Id']),
                 b'\x17': ([1], ['REBOOT_RQ#Id']),
                 b'\xfe': ((1, 2, 2, 1, 1, 0), ('TEST#Id', '>H#Num', '>h#RSSI#дБ', '#SNR#Сигнал/шум', '#DATA', '#From|4'))}

    errors_info = {0: 'Нет ошибок',
                   1: 'Датчик не отвечает',
                   2: 'Перегрузка питания датчика',
                   3: 'Напряжение питания ниже допустимого',
                   4: 'Утечка тока (для термокосы)',
                   5: 'Ошибка сканирования термокосы',
                   6: 'Термокоса отсутствует',
                   7: 'Ошибка данных 1-Wire',
                   8: 'Ошибка в калибровочных данных',
                   9: 'Заданный термодатчик не найден',
                   10: 'Слишком длинная термокоса',
                   20: 'Потеряны данные (переполнение очереди)',
                   30: 'Чип часов неисправен',
                   128: 'Ошибка модема Стриж', 129: 'Ошибка модема Стриж', 130: 'Ошибка модема Стриж',
                   131: 'Ошибка модема Стриж', 132: 'Ошибка модема Стриж', 133: 'Ошибка модема Стриж'}

    type_info = {1: 'Инклинометр',
                 2: 'Термокоса',
                 3: 'Датчик перемещения',
                 4: 'Скважинный инклинометр',
                 5: 'Тензометрический усилитель',
                 6: 'Датчик напряжения',
                 8: 'Цифровой струнный датчик деформации',
                 9: 'Датчик уровня жидкости (пьезометр)',
                 10: 'Датчик осадки',
                 11: 'Датчик влажности',
                 21: 'Цифровой датчик Modbus',
                 51: 'Аналоговый струнный датчик',
                 200: 'Произвольный тип, трактуется пользователем'}

    _raw_data = ''
    _result_data = ['No data']
    _packet = []
    _id_type = b'\x00'

    _packets_left = -1
    _packets_l_total = -1
    _packets_l_uts = ''
    _packets_l_id = ''
    _packets_l_n = ''
    sensor_quantity = 17

    def __check_data(func):
        def wrapper(self, *args, **kwargs):
            reason = ''
            if self._id_type not in self.smz_codes.keys():
                reason = f'Unknown ID code [{self._id_type.hex()}], decoding is not possible: lack of instructions'
            if not self._raw_data:
                reason = 'Empty data, please use .set_data()'
            if reason:
                print('\033[31m' + reason + '\033[39m')
            else:
                func(self, *args, **kwargs)
        return wrapper

    def set_data(self, b64_data):
        try:
            if b64_data:
                self._raw_data = b64decode(b64_data)
                self._id_type = self._raw_data[0:1]
                if self._id_type not in self.smz_codes.keys():
                    print(f'\033[31mUnknown ID code [{self._id_type.hex()}], decoding is not possible: lack of instructions\033[39m')
                    return False
                return True
            else:
                print('\033[31mEmpty data, please use .set_data()\033[39m')
                return False
        except:
            print('\033[31mInvalid data, decoding is not possible\033[39m')
            return False

    @__check_data
    def convert_data(self):
        #try:
            self._result_data = []
            if self._packets_left < 1:
                self._packet = []

            data_packet = []
            Ndata = ['', '']
            repeat_pos = 0

            instructions = self.smz_codes.get(self._id_type)[:]
            if 0 not in self.smz_codes.get(self._id_type)[:][0]:
                if len(self._raw_data) != sum(self.smz_codes.get(self._id_type)[:][0]):
                    instructions = ((1, 1), ('Error#Id', '#Err'))
            data_bytes = self._raw_data[:]

            def do_instructions(b_data, instr):
                if instr.count('#') < 2:
                    instr += '#'
                i_type, i_name, munit = instr.split('#')
                if munit:
                    munit = '\033[33m' + munit + '\033[39m'

                def dp_append(value_da):
                    data_packet.append(value_da)
                    self._result_data.append(f'[ {value_da} ]: \033[35m{i_name}\033[39m')
                    if munit:
                        self._result_data[-1] += f' — {munit}'

                def decode_b(dp_add):
                    if i_type:
                        value_ = struct.unpack(i_type, b_data)[0]
                    else:
                        value_ = b_data.hex()
                    if dp_add:
                        dp_append(value_)
                    return value_

                def Nd_append(tn=False):
                    if tn:
                        Ndata.append(decode_b(False) / 100)
                    else:
                        Ndata.append(decode_b(False))
                    if not Ndata[0]:
                        Ndata[0] = i_name
                        Ndata[1] = munit

                match i_name:
                    case 'Id':
                        self._result_data.append(f'[ {b_data.hex()} ]: \033[35mID, IDType\033[39m: \033[1;30;45m<{i_type}>\033[0;39;49m')
                        data_packet.append(b_data)
                    case 'Num':
                        if i_type:
                            decode_b(True)
                        else:
                            dp_append(int(decode_b(False), 16))
                    case 'UTS':
                        self._result_data.append(f'[ {datetime.datetime.utcfromtimestamp(decode_b(True))} ]: \033[35mDate-Time\033[39m')
                    case 'Tn':
                        Nd_append(tn=True)
                    case 'Type':
                        munit = '\033[33m' + self.type_info.get(int.from_bytes(b_data, 'big')) + '\033[39m'
                        decode_b(True)
                    case 'E':
                        munit = '\033[33m' + self.errors_info.get(int.from_bytes(b_data, 'big')) + '\033[39m'
                        decode_b(True)
                    case 'FW_VER':
                        dp_append(f'{int(b_data.hex()[0:2], 16)}.{int(b_data.hex()[2:], 16)}')
                    case 'DATA':
                        Nd_append()
                    case str() as s_from if 'From' in s_from:
                        nonlocal repeat_pos
                        repeat_pos = int(s_from.split('|')[1])
                    #case 'T':
                    #    рассчёты пьезометра
                    case _:
                        decode_b(True)

            while data_bytes:
                for i in range(repeat_pos, len(instructions[0])):
                    current_data = data_bytes[:instructions[0][i]]
                    data_bytes = data_bytes[instructions[0][i]:]
                    do_instructions(current_data, instructions[1][i])
                if data_packet:
                    self._packet.append(data_packet)
                data_packet = []

            if len(Ndata) > 2:
                nStr = f' {Ndata[1]}\n--| '.join(map(str, Ndata[2:]))
                self._result_data.append(f'\033[35m{Ndata[0]}\033[39m:\n--| {nStr} {Ndata[1]}')
                del Ndata[0:2]
                self._packet[-1].append(Ndata)

            def check_packet():
                def clear_l(message):
                    print(message)
                    self._packets_left = -1
                    self._packets_l_total = -1
                    self._packets_l_id = ''
                    self._packets_l_uts = ''
                    self._packets_l_n = ''

                if not self._packets_l_id or self._packets_l_id == self._id_type:
                    match self._id_type:
                        case b'\x05':
                            pck_plan = self._packet[-1][2] - (self._packet[-1][1] - 1)
                            pck_fact = len(self._packet[-1][-1])
                            if pck_plan != pck_fact:
                                print('Some packets has been lost')
                            if self._packet[-1][1] == 1 or self._packets_left < 0:
                                if self._packet[-1][1] != 1:
                                    print(f'Not a first packet, receiving started from N1: {self._packet[-1][1]}')
                                self._packets_l_total = math.ceil(self.sensor_quantity / self._packet[0][2])
                                if not self._packets_l_n:
                                    self._packets_l_n = self._packet[-1][1] - 1
                                self._packets_left = self._packets_l_total
                                self._packets_l_uts = self._packet[0][3]
                                self._packets_l_id = self._id_type
                            self._packets_left -= 1

                            if self._packets_l_n + 1 != self._packet[-1][1]:
                                clear_l(f'\033[31mError:\033[39m Wrong packet received, expected packet with N1: {self._packets_l_n + 1}')
                            elif self._packet[-1][3] != self._packets_l_uts:
                                clear_l(f'\033[31mError:\033[39m Wrong packet recieved, expected packet with UTS: {self._packets_l_uts}')
                            else:
                                self._packets_l_n = self._packet[-1][2]

                            if self._packets_left != -1:
                                if self._packets_left > 0:
                                    print(f'Waiting for next packet: [{self._packets_l_total - self._packets_left}/{self._packets_l_total}]')
                                else:
                                    clear_l(f'All packets received: [{self._packets_l_total - self._packets_left}/{self._packets_l_total}]')
                else:
                    clear_l(f'\033[31mError:\033[39m Wrong packet recieved, expected packet with ID: {self._packets_l_id}')
            check_packet()

        #except Exception as e:
        #    print(f'\033[31mDecoding stopped, error happened:\033[39m [{str(e)}]')
        #    self._packets_left = -1

    def get_raw_data(self):
        try:
            if not self._raw_data:
                print('\033[31mEmpty data, please use .set_data()\033[39m')
                return b'\x00'
            else:
                return self._raw_data
        except Exception as e:
            print(f'\033[31mNot a HEX data, source data is: {self._raw_data}, Error:\033[39m {e}')
            return b'\x00'

    def get_result_data(self):
        return self._result_data

    def get_packet(self):
        return self._packet

    def decode_data(self, *b64_adata, raw=False, packet=False, b64=False):
        if b64_adata:
            b64_uni = [[]]
            for data_a in b64_adata:
                if isinstance(data_a, str):
                    b64_uni[0].append(data_a)
                elif hasattr(data_a, '__iter__'):
                    b64_uni[0] = [*b64_uni[0], *data_a]
                else:
                    print(f'Wrong type: {data_a}')

            for i in range(len(b64_uni[0])):
                print('\n-------------------------------')
                if self.set_data(b64_uni[0][i]):
                    self.convert_data()
                    print('\n'.join(self.get_result_data()))
                if raw or packet or b64:
                    print()
                    if b64:
                        print(f'\033[34m----| Base64 data is: [{b64_uni[0][i]}]\033[39m')
                    if raw:
                        print(f'\033[34m----| Raw data is: [{self.get_raw_data().hex()}]\033[39m')
                    if packet:
                        print(f'\033[34m----| Packet data is: {self.get_packet()}\033[39m')
                print('-------------------------------')
        else:
            stop_i = False
            str_data = ''
            print('Data (double Enter to stop): ')
            while not stop_i:
                user_input = input()
                if user_input == '':
                    stop_i = True
                else:
                    str_data += user_input + '\n'

            delimiters = re.findall(r"[^ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=]", str_data)
            for delimiter in delimiters:
                str_data = " ".join(str_data.split(delimiter))

            self.decode_data(str_data.split(), raw=raw, packet=packet, b64=b64)


if __name__ == '__main__':
    st = True
    #smd = SMZDecoder()
    #smd.decode_data(raw=True, packet=True, b64=True)
    #smd.decode_data()
