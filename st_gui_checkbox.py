# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'STM32GUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
from serial_operation import Serial_operation
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(606, 359)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(40, 124, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 94, 121, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(240, 94, 111, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(440, 94, 111, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 124, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(440, 124, 113, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 190, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 240, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(200, 200, 54, 12))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(200, 270, 54, 12))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(300, 200, 54, 12))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(300, 270, 54, 12))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(400, 270, 54, 12))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(400, 200, 54, 12))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(500, 270, 54, 12))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(500, 200, 54, 12))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 290, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 300, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(320, 300, 75, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 34, 75, 23))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(280, 40, 171, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(50, 150, 54, 12))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(250, 150, 54, 12))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(450, 150, 54, 12))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(200, 240, 54, 12))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(Dialog)
        self.label_17.setGeometry(QtCore.QRect(300, 240, 54, 12))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(Dialog)
        self.label_18.setGeometry(QtCore.QRect(500, 240, 54, 12))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(Dialog)
        self.label_19.setGeometry(QtCore.QRect(400, 240, 54, 12))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(160, 270, 18, 12))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(160, 240, 54, 12))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(Dialog)
        self.label_22.setGeometry(QtCore.QRect(170, 40, 81, 16))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.checkBox = QtGui.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(50, 70, 141, 16))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.pushButton_7 = QtGui.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(350, 34, 75, 23))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit.clear)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_2.clear)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_3.clear)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_13.clear)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_14.clear)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_15.clear)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.read_flash)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.write_flash)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.update_adc)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.reset_adc)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL(_fromUtf8("clicked()")), self.connect_serial)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.close_serial)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "STM32", None))
        self.label.setText(_translate("Dialog", "Current Program (mA)", None))
        self.label_2.setText(_translate("Dialog", "Current Max (mA)", None))
        self.label_3.setText(_translate("Dialog", "Current Min (mA)", None))
        self.pushButton.setText(_translate("Dialog", "Read", None))
        self.pushButton_2.setText(_translate("Dialog", "Write", None))
        self.label_4.setText(_translate("Dialog", "Vout (V)", None))
        self.label_5.setText(_translate("Dialog", "ADC1", None))
        self.label_6.setText(_translate("Dialog", "Vin (V)", None))
        self.label_7.setText(_translate("Dialog", "ADC2", None))
        self.label_8.setText(_translate("Dialog", "ADC3", None))
        self.label_9.setText(_translate("Dialog", "Iout (mA)", None))
        self.label_10.setText(_translate("Dialog", "ADC4", None))
        self.label_11.setText(_translate("Dialog", "Iin (mA)", None))
        self.pushButton_3.setText(_translate("Dialog", "Clear", None))
        self.pushButton_4.setText(_translate("Dialog", "Update ADC", None))
        self.pushButton_5.setText(_translate("Dialog", "Reset ADC", None))
        self.pushButton_6.setText(_translate("Dialog", "Connect", None))
        self.label_12.setText(_translate("Dialog", "initial", None))
        self.label_13.setText(_translate("Dialog", "hex prog", None))
        self.label_14.setText(_translate("Dialog", "hex max", None))
        self.label_15.setText(_translate("Dialog", "hex min", None))
        self.label_16.setText(_translate("Dialog", "ADC1v", None))
        self.label_17.setText(_translate("Dialog", "ADC2v", None))
        self.label_18.setText(_translate("Dialog", "ADC4v", None))
        self.label_19.setText(_translate("Dialog", "ADC3v", None))
        self.label_20.setText(_translate("Dialog", "Hex", None))
        self.label_21.setText(_translate("Dialog", "Value", None))
        self.label_22.setText(_translate("Dialog", "Serial Info:", None))
        self.checkBox.setText(_translate("Dialog", "program max current", None))
        self.pushButton_7.setText(_translate("Dialog", "Disconnect", None))

    def read_flash(self):
        # flash = Flash()
        self.close_serial()
        self.connect_serial()
        s.write_ten_bytes('f10000000000000000f1')  # inquiry programmed current
        read_str = s.read_ten_bytes()
        print 'string from uart 1', read_str
        while read_str[0:2] != 'e0':
            s.write_ten_bytes('f10000000000000000f1')
            read_str = s.read_ten_bytes()
            print 'string from uart', read_str
        flash = s.parse_response(read_str)
        self.label_13.setText(_translate("Dialog", flash.current_program_uart, None))
        self.label_14.setText(_translate("Dialog", flash.current_max_uart, None))
        self.label_15.setText(_translate("Dialog", flash.current_min_uart, None))
        self.lineEdit.setText(_translate("Dialog", flash.current_program, None))
        self.lineEdit_2.setText(_translate("Dialog", flash.current_max, None))
        self.lineEdit_3.setText(_translate("Dialog", flash.current_min, None))

    def write_flash(self):

        I_prog = '03e8'
        I_max = '03e8'
        I_min = '0032'
        try:
            I_prog = s.deci_to_hexi(str(self.lineEdit.text()))
            I_max = s.deci_to_hexi(str(self.lineEdit_2.text()))
            I_min = s.deci_to_hexi(str(self.lineEdit_3.text()))
            self.label_13.setText(_translate("Dialog", I_prog, None))
            self.label_14.setText(_translate("Dialog", I_max, None))
            self.label_15.setText(_translate("Dialog", I_min, None))
        except Exception, e:
            print e;
        if int(I_prog, 16) > int(I_max, 16) or int(I_prog, 16) < int(I_min, 16):
            print 'outside range'
            qtm = QtGui.QMessageBox
            msg_box = qtm(qtm.Warning, "Warning", 'Current is out of range.')
            msg_box.exec_()
        elif self.checkBox.checkState() == 0:
            print "progrma output current"
            print 'f0' + I_prog + I_max + I_min + '0000f0'
            s.write_ten_bytes('f0' + I_prog + I_max + I_min + '0000f0')
        else:
            print "program factory current"
            print 'f0' + I_prog + I_max + I_min + '0100f0'
            s.write_ten_bytes('f0' + I_prog + I_max + I_min + '0100f0')
            # print self.checkBox.checkState()
            #     s.write_ten_bytes('f0' + I_prog + I_max + I_min + '0000f0')
            #     serial_operation.write_ten_bytes('')

    def update_adc(self):
        str_adc = s.read_ten_bytes()
        while str_adc[0:2] != 'e1':
            str_adc = s.read_ten_bytes()
        adc1 = s.parse_response(str_adc)
        self.label_5.setText(_translate("Dialog", adc1.voltage_out_uart, None))
        self.label_7.setText(_translate("Dialog", adc1.voltage_in_uart, None))
        self.label_8.setText(_translate("Dialog", adc1.current_out_uart, None))
        self.label_10.setText(_translate("Dialog", adc1.current_in_uart, None))
        self.label_16.setText(_translate("Dialog", adc1.voltage_out, None))
        self.label_17.setText(_translate("Dialog", adc1.voltage_in, None))
        self.label_19.setText(_translate("Dialog", adc1.current_out, None))
        self.label_18.setText(_translate("Dialog", adc1.current_in, None))

    def reset_adc(self):
        self.label_5.setText(_translate("Dialog", "ADC1", None))
        self.label_7.setText(_translate("Dialog", "ADC2", None))
        self.label_8.setText(_translate("Dialog", "ADC3", None))
        self.label_10.setText(_translate("Dialog", "ADC4", None))
        self.label_16.setText(_translate("Dialog", "ADC1v", None))
        self.label_17.setText(_translate("Dialog", "ADC2v", None))
        self.label_18.setText(_translate("Dialog", "ADC4v", None))
        self.label_19.setText(_translate("Dialog", "ADC3v", None))

    def connect_serial(self):
        self.label_12.setText(_translate("Dialog", s.open_serial(), None))

    def close_serial(self):
        self.label_12.setText(_translate("Dialog", s.close_serial(), None))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(Form)
    Form.show()
    s = Serial_operation()
    ui.connect_serial()
    sys.exit(app.exec_())
