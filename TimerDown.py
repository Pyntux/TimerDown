#!/usr/bin/env python

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import datetime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(850, 400, 371, 265)
        MainWindow.setFixedSize(371, 265)
        #MainWindow.resize(371, 289)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/timerdown.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 171, 231))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_timer = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_timer.setTitle("")
        self.groupBox_timer.setObjectName("groupBox_timer")

        self.make_min = QtWidgets.QRadioButton(self.groupBox_timer)
        self.make_min.setGeometry(QtCore.QRect(20, 10, 131, 22))
        self.make_min.setChecked(True)
        self.make_min.setObjectName("make_min")
        self.spinBox_min = QtWidgets.QSpinBox(self.groupBox_timer)
        self.spinBox_min.setGeometry(QtCore.QRect(50, 40, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_min.setFont(font)
        self.spinBox_min.setMinimum(1)
        self.spinBox_min.setMaximum(1000)
        self.spinBox_min.setProperty("value", 15)
        self.spinBox_min.setObjectName("spinBox_min")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_timer)
        self.radioButton.setGeometry(QtCore.QRect(20, 120, 131, 31))
        self.radioButton.setObjectName("radioButton")
        self.line = QtWidgets.QFrame(self.groupBox_timer)
        self.line.setGeometry(QtCore.QRect(0, 96, 171, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        # Za trenutno vreme
        now = datetime.datetime.now()

        self.spinBox_th = QtWidgets.QSpinBox(self.groupBox_timer)
        self.spinBox_th.setGeometry(QtCore.QRect(10, 160, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.spinBox_th.setFont(font)
        self.spinBox_th.setMaximum(23)
        self.spinBox_th.setObjectName("spinBox_th")
        self.spinBox_tm = QtWidgets.QSpinBox(self.groupBox_timer)
        self.spinBox_tm.setGeometry(QtCore.QRect(81, 160, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.spinBox_tm.setFont(font)
        self.spinBox_th.setMinimum(now.hour)  # Minimalna vrednost sati je trenutna
        self.spinBox_tm.setMaximum(59)
        self.spinBox_tm.setObjectName("spinBox_tm")
        self.label_min = QtWidgets.QLabel(self.groupBox_timer)
        self.label_min.setGeometry(QtCore.QRect(60, 80, 51, 31))
        self.label_min.setObjectName("label_min")
        self.horizontalLayout.addWidget(self.groupBox_timer)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(180, 9, 181, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_buttons = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_buttons.setTitle("")
        self.groupBox_buttons.setObjectName("groupBox_buttons")
        self.shedule_button = QtWidgets.QPushButton(self.groupBox_buttons)
        self.shedule_button.setGeometry(QtCore.QRect(10, 10, 151, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/shedule.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shedule_button.setIcon(icon1)
        self.shedule_button.setIconSize(QtCore.QSize(20, 20))
        self.shedule_button.setObjectName("shedule_button")
        self.reset_button = QtWidgets.QPushButton(self.groupBox_buttons)
        self.reset_button.setGeometry(QtCore.QRect(10, 53, 151, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/cancel.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reset_button.setIcon(icon2)
        self.reset_button.setIconSize(QtCore.QSize(20, 20))
        self.reset_button.setObjectName("reset_button")

        self.verticalLayout.addWidget(self.groupBox_buttons)
        self.groupBox_quick = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_quick.setObjectName("groupBox_quick")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_quick)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 151, 31))
        self.comboBox.setObjectName("comboBox")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/shutdown.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/reboot.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon4, "")
        self.apply_button = QtWidgets.QPushButton(self.groupBox_quick)
        self.apply_button.setGeometry(QtCore.QRect(10, 70, 151, 31))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/apply.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.apply_button.setIcon(icon5)
        self.apply_button.setObjectName("apply_button")
        self.verticalLayout.addWidget(self.groupBox_quick)
        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setText("Welcome!")
        self.label_info.setObjectName("label_info")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.showMessage("   App notices :")
        self.statusbar.addPermanentWidget(self.label_info)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Postavlja spinere na trenutno vreme kad se podigne app
        self.reset_hm()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TimerDown"))
        self.make_min.setText(_translate("MainWindow", "Shutdown PC in:"))
        self.radioButton.setText(_translate("MainWindow", "Shutdown PC at:"))
        self.label_min.setText(_translate("MainWindow", "minutes"))

        self.shedule_button.setText(_translate("MainWindow", "Shedule"))
        self.shedule_button.clicked.connect(self.shedule)

        self.reset_button.setText(_translate("MainWindow", "Reset"))
        self.reset_button.clicked.connect(self.reset)

        self.groupBox_quick.setTitle(_translate("MainWindow", "Quick actions:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Quick shutdown"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Qucik restart"))
        self.apply_button.setText(_translate("MainWindow", "Apply"))
        self.apply_button.clicked.connect(self.drop_menu)

    # Zakazuje izabranu akciju:
    def shedule(self):
        value = self.spinBox_min.value()
        if self.make_min.isChecked():
            os.system(f"shutdown -h {value}")
            self.label_info.setText(f"Your PC will shutdown for {value} minutes!")
        else:
            h, m = self.spinBox_th.value(), self.spinBox_tm.value()
            hm_min = h * 60 + m
            now = datetime.datetime.now()
            now_hm_min = now.hour * 60 + now.minute
            final_num = hm_min - now_hm_min
            if final_num < 0:
                self.label_info.setText("Time in past! Please reset!")
                self.spinBox_th.setValue(now.hour)
                self.spinBox_tm.setValue(now.minute)
            else:
                os.system(f"shutdown -h {final_num}")
                self.label_info.setText(f"Your PC will shutdown at {h}:{m} !")

    # Resetuje prvi spinbox za minute i poništava komandu gašenja
    def reset(self):
        now = datetime.datetime.now()
        self.spinBox_min.setValue(15)
        self.spinBox_th.setValue(now.hour)
        self.spinBox_tm.setValue(now.minute)
        self.label_info.setText("Try again!")
        os.system("shutdown -c")

    # Resetuje H&M spinere na trenutno vreme
    def reset_hm(self):
        now = datetime.datetime.now()
        self.spinBox_th.setValue(now.hour)
        self.spinBox_tm.setValue(now.minute)

    # Brze akcije iz padajućeg menija

    def drop_menu(self):
        item = self.comboBox.currentText()
        if item == "Quick shutdown":
            os.system("shutdown -h now")
        else:
            os.system("reboot")

    # # Izlazi iz aplikacije
    # def exit_app(self):
    #     sys.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
