# -*- coding: utf-8 -*

import serial
import serial.tools.list_ports
import binascii
from adc import ADC
from flash import Flash

ser = serial.Serial()
flash = Flash()
adc = ADC()


class Serial_operation:
    def open_serial(self):
        port_list = list(serial.tools.list_ports.comports())
        if len(port_list) <= 0:
            return 'no serial device'
        else:
            port_list_0 = list(port_list[0])
            port_serial = port_list_0[0]
            ser.baudrate = 115200
            ser.port = port_serial
            try:
                ser.open()
                return ser.name
            except Exception, e:
                print e
                return ser.name

    def close_serial(self):
        try:
            ser.close()
            return "closed"
        except Exception, e:
            print e
            return "no serial to close"

    def read_ten_bytes(self):
        # while state :
        if ser.is_open:
            recv = ser.read(10)
            recv = binascii.b2a_hex(recv)
            print "check which port was really used >", ser.name
            print "data >", recv
            return recv
        else:
            print "serial is not open."

    def write_ten_bytes(self, payload):
        if ser.is_open:
            payload = bytes(bytearray.fromhex(payload))
            ser.write(payload)
        else:
            print "serial is not open."

    def parse_response(self, response):
        if response[0:2] == 'e0':
            flash.parse_flash(response)
            return flash
        elif response[0:2] == 'e1':
            adc.parse_adc(response)
            return adc

    def deci_to_hexi(self, decimal):
        hex_str = hex(int(decimal))[2:]
        while len(hex_str) < 4:
            hex_str = '0' + hex_str
        if len(hex_str) > 4:
            hex_str = 'ffff'
        return hex_str


if __name__ == '__main__':
    s = Serial_operation()
    print(s.open_serial())
    # write_ten_bytes('f0eeeeffff56780000f0')#program output current eeee,max current ffff ,min current 5678
    s.write_ten_bytes('f10000000000000000f1')  # inquiry programmed current
    # while read_ten_bytes()[0:2] != 'e0':
    s.read_ten_bytes()
    # parse_response('e00abb0cdd0eff0000e0')
