class Flash(object):
    '''Flash data from uart to be parsed into 3 current values'''

    def __init__(self):
        self.current_program = 0
        self.current_max = 0
        self.current_min = 0
        self.current_program_uart = 0
        self.current_max_uart = 0
        self.current_min_uart = 0

    def parse_flash(self, ten_bytes_hex):
        self.current_program_uart = ten_bytes_hex[2:6]
        self.current_max_uart = ten_bytes_hex[6:10]
        self.current_min_uart = ten_bytes_hex[10:14]
        self.current_program = str(int(self.current_program_uart, 16))
        self.current_max = str(int(self.current_max_uart, 16))
        self.current_min = str(int(self.current_min_uart, 16))



if __name__ == '__main__':
    flash = Flash()
    flash.parse_flash('e00abb0cdd0eff0000e0')
    print len('e00abb0cdd0eff0122e0')
    print "I program :", flash.current_program, "I max :", flash.current_max, "I min :", flash.current_min
