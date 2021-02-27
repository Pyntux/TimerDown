#!/usr/bin/env python

from PyQt5 import QtCore, QtGui, QtWidgets
# For tray icons etc...
from PyQt5.QtGui import *
from PyQt5.QtCore import QTime
import datetime
import os
import resources


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(850, 400, 411, 333)
        MainWindow.setFixedSize(411, 333)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/shutdown.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 9, 211, 231))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setObjectName("horizontalLayout")

        ##############################################################

        # TRAY:
        self.tray = QtWidgets.QSystemTrayIcon()
        # Ovu komandu dodati svuda dole da izmeni tooltip zavisno o komandi
        self.tray.setToolTip("TimerDown")
        self.icon = QIcon(":/icons/shutdown.ico")
        self.tray.setIcon(self.icon)
        self.tray.setVisible(True)

        # menu
        self.menu = QtWidgets.QMenu()
        self.tray.setContextMenu(self.menu)

        self.option1_icon = QIcon(":/icons/show.ico")
        self.option1 = QtWidgets.QAction("Show TimerDown")
        self.option1.setIcon(self.option1_icon)
        self.option1.triggered.connect(self.show_from_tray)
        self.menu.addAction(self.option1)

        self.option2_icon = QIcon(":/icons/reset.ico")
        self.option2 = QtWidgets.QAction("Reset schedule")
        self.option2.setIcon(self.option2_icon)
        self.option2.triggered.connect(self.reset_button)
        self.menu.addAction(self.option2)

        self.option3_icon = QIcon(":/icons/exit.ico")
        self.option3 = QtWidgets.QAction("Exit application")
        self.option3.setIcon(self.option3_icon)
        self.option3.triggered.connect(self.exit_app)
        self.menu.addAction(self.option3)

        ##############################################################

        # Za trenutno vreme
        # time = QTime.currentTime()
        time = datetime.datetime.now()

        self.groupBox_levi = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_levi.setTitle("")
        self.groupBox_levi.setObjectName("groupBox_levi")
        self.label_levo_gore = QtWidgets.QLabel(self.groupBox_levi)
        self.label_levo_gore.setGeometry(QtCore.QRect(50, 0, 111, 31))  # 101
        self.label_levo_gore.setObjectName("label_levo_gore")

        # Gornji spinbox, za minute ili sate, zavisno od toga šta je čekirano:
        self.spinBox_gornji = QtWidgets.QSpinBox(self.groupBox_levi)
        self.spinBox_gornji.setGeometry(QtCore.QRect(20, 40, 71, 41))
        self.spinBox_gornji.setMinimum(0)
        self.spinBox_gornji.setMaximum(1000)
        self.spinBox_gornji.setProperty("value", 15)
        self.spinBox_gornji.setObjectName("spinBox_gornji")
        # Checkbox za minute, gašenje za određeni broj minuta:
        self.checkBox_min = QtWidgets.QCheckBox(self.groupBox_levi)
        self.checkBox_min.setGeometry(QtCore.QRect(100, 40, 91, 21))
        self.checkBox_min.setChecked(True)
        self.checkBox_min.setAutoExclusive(True)
        self.checkBox_min.setObjectName("checkBox_min")
        # Checkbox za sate, gašenje za određeni broj sati:
        self.checkBox_hour = QtWidgets.QCheckBox(self.groupBox_levi)
        self.checkBox_hour.setGeometry(QtCore.QRect(100, 60, 91, 21))
        self.checkBox_hour.setAutoExclusive(True)
        self.checkBox_hour.setObjectName("checkBox_hour")

        # Linija za razdvajanje gornjeg dela od donjeg:
        self.line = QtWidgets.QFrame(self.groupBox_levi)
        self.line.setGeometry(QtCore.QRect(0, 95, 231, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        # Spinbox u donjem delu za sate:
        self.spinBox_donji_hour = QtWidgets.QSpinBox(self.groupBox_levi)
        self.spinBox_donji_hour.setGeometry(QtCore.QRect(30, 160, 71, 41))
        self.spinBox_donji_hour.setMaximum(23)
        self.spinBox_donji_hour.setMinimum(time.hour)  # ---> hour() ako koristiš qtime
        self.spinBox_donji_hour.setObjectName("spinBox_donji_hour")
        # Checkbox za gašenje računara u određeno vreme:
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_levi)
        self.checkBox.setGeometry(QtCore.QRect(40, 120, 131, 31))
        self.checkBox.setAutoExclusive(True)
        self.checkBox.setObjectName("checkBox")
        # Spinbox u donjem delu za minute:
        self.spinBox_donji_min = QtWidgets.QSpinBox(self.groupBox_levi)
        self.spinBox_donji_min.setGeometry(QtCore.QRect(100, 160, 71, 41))
        self.spinBox_donji_min.setMaximum(59)
        self.spinBox_donji_min.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.groupBox_levi)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(219, 9, 181, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_buttons = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_buttons.setTitle("")
        self.groupBox_buttons.setObjectName("groupBox_buttons")
        # Set up i Reset d:
        self.Button_set_up = QtWidgets.QPushButton(self.groupBox_buttons)
        self.Button_set_up.setGeometry(QtCore.QRect(17, 12, 141, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/set_up.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_set_up.setIcon(icon1)
        self.Button_set_up.setIconSize(QtCore.QSize(24, 24))
        self.Button_set_up.setObjectName("Button_set_up")
        self.Button_reset = QtWidgets.QPushButton(self.groupBox_buttons)
        self.Button_reset.setGeometry(QtCore.QRect(17, 55, 141, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/reset.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_reset.setIcon(icon2)
        self.Button_reset.setIconSize(QtCore.QSize(24, 24))
        self.Button_reset.setObjectName("Button_reset")
        self.verticalLayout_3.addWidget(self.groupBox_buttons)

        # Quick actions polje:
        self.groupBox_quick_actions = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_quick_actions.setObjectName("groupBox_quick_actions")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_quick_actions)
        self.comboBox.setGeometry(QtCore.QRect(7, 30, 161, 31))
        self.comboBox.setObjectName("comboBox")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/shutdown.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/reboot.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon4, "")
        self.apply_button = QtWidgets.QPushButton(self.groupBox_quick_actions)
        self.apply_button.setGeometry(QtCore.QRect(8, 66, 160, 31))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/apply.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.apply_button.setIcon(icon5)
        self.apply_button.setObjectName("apply_button")
        self.verticalLayout_3.addWidget(self.groupBox_quick_actions)

        # Exit app polje:
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 240, 211, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_bootom_levi = QtWidgets.QGroupBox(self.horizontalLayoutWidget_2)
        self.groupBox_bootom_levi.setTitle("")
        self.groupBox_bootom_levi.setObjectName("groupBox_bootom_levi")
        self.exit_app_button = QtWidgets.QPushButton(self.groupBox_bootom_levi)
        self.exit_app_button.setGeometry(QtCore.QRect(20, 10, 161, 31))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/exit.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_app_button.setIcon(icon6)
        self.exit_app_button.setObjectName("exit_app_button")
        self.horizontalLayout_3.addWidget(self.groupBox_bootom_levi)

        # Polje za sat:
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(219, 239, 181, 61))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(3, 4, 3, 2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_clock = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_clock.setTitle("")
        self.groupBox_clock.setObjectName("groupBox_clock")
        self.LCD = QtWidgets.QLCDNumber(self.groupBox_clock)
        self.LCD.setGeometry(QtCore.QRect(0, 2, 171, 51))
        self.LCD.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LCD.setObjectName("LCD")
        self.LCD.setDigitCount(8)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start()
        self.verticalLayout_4.addWidget(self.groupBox_clock)

        # Statusbar:
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.label_info = QtWidgets.QLabel(self.statusbar)
        self.label_info.setText("Welcome!")
        self.label_info.setObjectName("label_info")
        self.label_info.setGeometry(16, 0, 250, 17)
        MainWindow.setStatusBar(self.statusbar)

        # Postavlja spinere na trenutno vreme kad se podigne app
        self.reset_hm()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TimerDown"))
        self.label_levo_gore.setText(_translate("MainWindow", "Shutdown PC in:"))
        self.checkBox_min.setText(_translate("MainWindow", "minutes"))
        self.checkBox_hour.setText(_translate("MainWindow", "hours"))
        self.checkBox.setText(_translate("MainWindow", "Shutdown PC at:"))

        # Shedule i reset dugmići:
        self.Button_set_up.setText(_translate("MainWindow", "Set up"))
        self.Button_set_up.clicked.connect(self.schedule)
        self.Button_reset.setText(_translate("MainWindow", "Reset"))
        self.Button_reset.clicked.connect(self.reset_button)

        # Sekcija "Quick action"
        self.groupBox_quick_actions.setTitle(_translate("MainWindow", "Quick actions:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Quick shutdown"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Quick reboot"))
        self.apply_button.setText(_translate("MainWindow", "Apply Quick action"))
        self.apply_button.clicked.connect(self.drop_menu)

        # Exit button:
        self.exit_app_button.setText(_translate("MainWindow", "Exit from app"))
        self.exit_app_button.clicked.connect(self.exit_app)

##################################################################################################
    # Za prikaz sata u LCD polju:
    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm:ss')
        if (time.second() % 2) == 0:
            text = time.toString('hh:mm ss')
        self.LCD.display(text)

    # Podešava i namešta spinere za gašenje u određeno vreme na trenutno vreme kada se podigne app
    def reset_hm(self):
        time = datetime.datetime.now()
        # time = QTime.currentTime()
        self.spinBox_donji_hour.setValue(time.hour)  # hour() ako se koristi qtime
        self.spinBox_donji_min.setValue(time.minute)

    # Zakazuje izabranu akciju:
    def schedule(self):
        time = datetime.datetime.now()
        # time = QTime.currentTime()
        value = self.spinBox_gornji.value()
        h = self.spinBox_donji_hour.value()
        m = self.spinBox_donji_min.value()

        if self.checkBox_min.isChecked():
            os.system(f"shutdown -h {value}")
            self.label_info.setText(f"Your PC will shutdown in {value} minutes!")
            # Za disable dugme kad ga klikne
            self.Button_set_up.setEnabled(False)

        elif self.checkBox_hour.isChecked():
            value_h = value * 60
            os.system(f"shutdown -h {value_h}")
            self.label_info.setText(f"Your PC will shutdown in {value} hours!")
            self.Button_set_up.setEnabled(False)

        else:
            hm_min = h * 60 + m
            now_time_in_min = time.hour * 60 + time.minute  # hour() ako se koristi qtime
            final_num = hm_min - now_time_in_min
            if final_num < 0:
                self.label_info.setText("Time in past! Set up again!")
                self.reset_hm()
            else:
                # os.system(f"shutdown {h}:{m}")  --- Može i ovako
                os.system(f"shutdown -h {final_num}")
                self.Button_set_up.setEnabled(False)
                if m < 10:
                    self.label_info.setText(f"Your PC will shutdown at {h}:0{m} !")
                    self.tray.setToolTip(f"Your PC will shutdown at {h}:0{m} !")
                else:
                    self.label_info.setText(f"Your PC will shutdown at {h}:{m} !")
                    self.tray.setToolTip(f"Your PC will shutdown at {h}:{m} !")

        self.trayTooltip()

    # Za tray Tooltip:

    def trayTooltip(self):
        now = datetime.datetime.now()

        # Ako je odabrano gašenje za "X" minuta:
        if self.checkBox_min.isChecked():
            min_in_s = self.spinBox_gornji.value() * 60  # Prebacuje odabrani broj minuta u sekunde zbog timedelta
            action_time = now + datetime.timedelta(seconds=min_in_s)
            if action_time.day == now.day:
                self.tray.setToolTip(
                    f"Your PC will shutdown at {action_time.hour}:{action_time.minute} !")
            else:
                self.tray.setToolTip(
                    f"Your PC will shutdown on {action_time.day}/{action_time.month}/{action_time.year} at {action_time.hour}:{action_time.minute} !")

        # Ako je odabrano gašenje za "X" sati:
        elif self.checkBox_hour.isChecked():
            # Prebacuje izabrani broj sati u sekunde zbog timedelta
            hour_in_s = self.spinBox_gornji.value() * 3600
            action_time = now + datetime.timedelta(seconds=hour_in_s)
            if action_time.day == now.day:
                self.tray.setToolTip(
                    f"Your PC will shutdown at {action_time.hour}:{action_time.minute} !")
            else:
                self.tray.setToolTip(
                    f"Your PC will shutdown on {action_time.day}/{action_time.month}/{action_time.year} at {action_time.hour}:{action_time.minute} !")

    # Za reset dugme:
    def reset_button(self):
        # time = QTime.currentTime()
        time = datetime.datetime.now()
        if self.checkBox_min.isChecked():
            self.spinBox_gornji.setValue(15)
        elif self.checkBox_hour.isChecked():
            self.spinBox_gornji.setValue(1)
        self.spinBox_donji_hour.setValue(time.hour)  # hour() ako se koristi qtime
        self.spinBox_donji_min.setValue(time.minute)
        self.label_info.setText("Set up again!")
        self.tray.setToolTip("TimerDown")
        os.system("shutdown -c")
        self.Button_set_up.setEnabled(True)

    # Brze akcije iz padajućeg menija
    def drop_menu(self):
        item = self.comboBox.currentText()
        if item == "Quick shutdown":
            os.system("shutdown -h now")
        else:
            os.system("reboot")

    # Izlazi iz aplikacije na dugme Exit
    def exit_app(self):
        sys.exit()

    # Za prikaz aplikacije na "show" dugme u tray-u
    def show_from_tray(self):
        MainWindow.show()

    def proba(self):
        self.apply_button.setEnabled(False)

################################################################################################


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
