class ADC(object):
    '''ADC sensed data from uart to be parsed into 4 measurements'''

    def __init__(self):
        self.voltage_out_uart = 0
        self.voltage_in_uart = 0
        self.current_out_uart = 0
        self.current_in_uart = 0
        self.voltage_out = 0
        self.voltage_in = 0
        self.current_out = 0
        self.current_in = 0

    def parse_adc(self, ten_bytes_hex):
        self.voltage_out_uart = ten_bytes_hex[2:6]
        self.voltage_in_uart = ten_bytes_hex[6:10]
        self.current_out_uart = ten_bytes_hex[10:14]
        self.current_in_uart = ten_bytes_hex[14:18]
        self.voltage_out = str(int(self.voltage_out_uart, 16) * 330 / 0xfff)
        self.voltage_in = str(int(self.voltage_in_uart, 16) * 330 / 0xfff)
        self.current_out = str(int(self.current_out_uart, 16) * 330 / 0xfff)
        self.current_in = str(int(self.current_in_uart, 16) * 330 / 0xfff)


if __name__ == '__main__':
    adc = ADC()
    # adc.parse_adc('e10abb0cdd0eff0122e1')
    print len('e10abb0cdd0eff0122e1')
    print "Vout :", adc.voltage_out_uart, " Vin :", adc.voltage_in_uart, " Iout :", adc.current_out_uart, " Iin :", adc.current_in_uart
    # print str(int('0fff', 16)* 3300 / 0xfff)
    debug_str = type(hex(int('20')))
    print (debug_str)
