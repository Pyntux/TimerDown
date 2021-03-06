#!/usr/bin/env python

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import QTime
import datetime
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(700, 300, 582, 479)
        MainWindow.setFixedSize(582, 479)
        app_icon = QtGui.QIcon()
        app_icon.addPixmap(QtGui.QPixmap("/usr/share/timerdown/timerdown.ico"),
                           QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(app_icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 281, 371))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setObjectName("horizontalLayout")

        ###########
        ## TRAY: ##
        ###########

        self.tray = QtWidgets.QSystemTrayIcon()
        self.tray.setToolTip("TimerDown")
        self.icon = QIcon("/usr/share/timerdown/icons/shutdown.ico")
        self.tray.setIcon(self.icon)
        self.tray.setVisible(False)  # Tray is not visiable untill you click to minimise to tray

        # menu
        self.menu = QtWidgets.QMenu()
        self.tray.setContextMenu(self.menu)

        self.option1_icon = QIcon("/usr/share/timerdown/icons/show.ico")
        self.option1 = QtWidgets.QAction("Show TimerDown")
        self.option1.setIcon(self.option1_icon)
        self.option1.triggered.connect(self.show_from_tray)
        self.menu.addAction(self.option1)

        self.option2_icon = QIcon("/usr/share/timerdown/icons/reset.ico")
        self.option2 = QtWidgets.QAction("Reset schedule")
        self.option2.setIcon(self.option2_icon)
        self.option2.triggered.connect(self.reset_button)
        self.menu.addAction(self.option2)

        self.option3_icon = QIcon("/usr/share/timerdown/icons/exit.ico")
        self.option3 = QtWidgets.QAction("Exit application")
        self.option3.setIcon(self.option3_icon)
        self.option3.triggered.connect(self.exit_app)
        self.menu.addAction(self.option3)

        # /tray #############################################################

        # For current time
        # time = QTime.currentTime() - If you are usin QTime
        time = datetime.datetime.now()

        self.groupBox_left = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_left.setTitle("")
        self.groupBox_left.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_left.setCheckable(False)
        self.groupBox_left.setObjectName("groupBox_left")
        self.spinBox_top = QtWidgets.QSpinBox(self.groupBox_left)
        self.spinBox_top.setGeometry(QtCore.QRect(45, 88, 82, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.spinBox_top.setFont(font)
        self.spinBox_top.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_top.setMinimum(1)
        self.spinBox_top.setMaximum(1000)
        self.spinBox_top.setProperty("value", 15)
        self.spinBox_top.setObjectName("spinBox_top")
        self.checkBox_min = QtWidgets.QCheckBox(self.groupBox_left)
        self.checkBox_min.setGeometry(QtCore.QRect(149, 86, 88, 22))
        self.checkBox_min.setAutoFillBackground(False)
        self.checkBox_min.setChecked(True)
        self.checkBox_min.setAutoExclusive(True)
        self.checkBox_min.setTristate(False)
        self.checkBox_min.setObjectName("checkBox_min")
        self.checkBox_hour = QtWidgets.QCheckBox(self.groupBox_left)
        self.checkBox_hour.setGeometry(QtCore.QRect(149, 117, 88, 22))
        self.checkBox_hour.setAutoExclusive(True)
        self.checkBox_hour.setObjectName("checkBox_hour")
        self.line = QtWidgets.QFrame(self.groupBox_left)
        self.line.setGeometry(QtCore.QRect(0, 171, 274, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.checkBox_at_time = QtWidgets.QCheckBox(self.groupBox_left)
        self.checkBox_at_time.setGeometry(QtCore.QRect(97, 206, 131, 22))
        self.checkBox_at_time.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_at_time.setAutoExclusive(True)
        self.checkBox_at_time.setObjectName("checkBox_at_time")
        self.spinBox_hour = QtWidgets.QSpinBox(self.groupBox_left)
        self.spinBox_hour.setGeometry(QtCore.QRect(45, 270, 82, 52))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.spinBox_hour.setFont(font)
        self.spinBox_hour.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_hour.setMaximum(23)
        self.spinBox_hour.setMinimum(time.hour)
        self.spinBox_hour.setObjectName("spinBox_hour")
        self.spinBox_min = QtWidgets.QSpinBox(self.groupBox_left)
        self.spinBox_min.setGeometry(QtCore.QRect(145, 270, 82, 52))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.spinBox_min.setFont(font)
        self.spinBox_min.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_min.setMaximum(59)
        self.spinBox_min.setObjectName("spinBox_min")
        self.label_top = QtWidgets.QLabel(self.groupBox_left)
        self.label_top.setGeometry(QtCore.QRect(108, 24, 111, 18))
        self.label_top.setObjectName("label_top")
        self.label_2_tacke = QtWidgets.QLabel(self.groupBox_left)
        self.label_2_tacke.setGeometry(QtCore.QRect(128, 274, 16, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2_tacke.setFont(font)
        self.label_2_tacke.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2_tacke.setObjectName("label_2_tacke")
        self.frame = QtWidgets.QFrame(self.groupBox_left)
        self.frame.setGeometry(QtCore.QRect(38, 74, 196, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.line_min = QtWidgets.QFrame(self.frame)
        self.line_min.setGeometry(QtCore.QRect(86, 15, 41, 16))
        self.line_min.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_min.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_min.setObjectName("line_min")
        self.line_hour = QtWidgets.QFrame(self.frame)
        self.line_hour.setGeometry(QtCore.QRect(86, 46, 41, 16))
        self.line_hour.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_hour.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_hour.setObjectName("line_hour")
        self.line_hour.raise_()
        self.line_min.raise_()
        self.frame_2 = QtWidgets.QFrame(self.groupBox_left)
        self.frame_2.setGeometry(QtCore.QRect(38, 256, 196, 80))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.groupBox_left)
        self.frame_3.setGeometry(QtCore.QRect(98, 18, 121, 31))
        self.frame_3.setAutoFillBackground(True)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.groupBox_left)
        self.frame_4.setGeometry(QtCore.QRect(90, 202, 140, 31))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label = QtWidgets.QLabel(self.groupBox_left)
        self.label.setGeometry(QtCore.QRect(42, 14, 51, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/usr/share/timerdown/icons/hourglass.ico"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_left)
        self.label_2.setGeometry(QtCore.QRect(41, 196, 41, 41))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("/usr/share/timerdown/icons/timer.ico"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.frame_4.raise_()
        self.frame_3.raise_()
        self.frame_2.raise_()
        self.frame.raise_()
        self.spinBox_top.raise_()
        self.checkBox_min.raise_()
        self.checkBox_hour.raise_()
        self.line.raise_()
        self.checkBox_at_time.raise_()
        self.spinBox_hour.raise_()
        self.spinBox_min.raise_()
        self.label_top.raise_()
        self.label_2_tacke.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.horizontalLayout.addWidget(self.groupBox_left)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(290, 10, 281, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_right_top = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_right_top.setAutoFillBackground(False)
        self.groupBox_right_top.setTitle("")
        self.groupBox_right_top.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_right_top.setCheckable(False)
        self.groupBox_right_top.setChecked(False)
        self.groupBox_right_top.setObjectName("groupBox_right_top")
        self.button_set_up = QtWidgets.QPushButton(self.groupBox_right_top)
        self.button_set_up.setGeometry(QtCore.QRect(20, 10, 233, 51))
        icon_set_up = QtGui.QIcon()
        icon_set_up.addPixmap(QtGui.QPixmap("/usr/share/timerdown/icons/set_up.ico"),
                              QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_set_up.setIcon(icon_set_up)
        self.button_set_up.setIconSize(QtCore.QSize(24, 23))
        self.button_set_up.setCheckable(False)
        self.button_set_up.setAutoExclusive(False)
        self.button_set_up.setAutoDefault(False)
        self.button_set_up.setDefault(False)
        self.button_set_up.setFlat(False)
        self.button_set_up.setObjectName("button_set_up")
        self.button_reset = QtWidgets.QPushButton(self.groupBox_right_top)
        self.button_reset.setGeometry(QtCore.QRect(20, 65, 233, 51))
        icon_reset = QtGui.QIcon()
        icon_reset.addPixmap(QtGui.QPixmap("/usr/share/timerdown/icons/reset.ico"),
                             QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_reset.setIcon(icon_reset)
        self.button_reset.setIconSize(QtCore.QSize(24, 24))
        self.button_reset.setAutoExclusive(False)
        self.button_reset.setObjectName("button_reset")
        self.button_to_tray = QtWidgets.QPushButton(self.groupBox_right_top)
        self.button_to_tray.setGeometry(QtCore.QRect(20, 120, 233, 51))
        icon_to_tray = QtGui.QIcon()
        icon_to_tray.addPixmap(QtGui.QPixmap("/usr/share/timerdown/icons/go_to_tray.ico"),
                               QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_to_tray.setIcon(icon_to_tray)
        self.button_to_tray.setIconSize(QtCore.QSize(24, 24))
        self.button_to_tray.setAutoExclusive(False)
        self.button_to_tray.setObjectName("button_to_tray")
        self.verticalLayout.addWidget(self.groupBox_right_top)
        self.groupBox_right_bottom = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.groupBox_right_bottom.setFont(font)
        self.groupBox_right_bottom.setAutoFillBackground(False)
        self.groupBox_right_bottom.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_right_bottom.setCheckable(True)
        self.groupBox_right_bottom.setChecked(False)
        self.groupBox_right_bottom.setObjectName("groupBox_right_bottom")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_right_bottom)
        self.radioButton.setGeometry(QtCore.QRect(60, 43, 161, 22))
        self.radioButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon_qshutdown = QtGui.QIcon()
        icon_qshutdown.addPixmap(QtGui.QPixmap(
            "/usr/share/timerdown/icons/shutdown.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton.setIcon(icon_qshutdown)
        self.radioButton.setIconSize(QtCore.QSize(24, 24))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_right_bottom)
        self.radioButton_2.setGeometry(QtCore.QRect(60, 79, 141, 22))
        self.radioButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon_qreboot = QtGui.QIcon()
        icon_qreboot.addPixmap(QtGui.QPixmap("/usr/share/timerdown/icons/reboot.ico"),
                               QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radioButton_2.setIcon(icon_qreboot)
        self.radioButton_2.setIconSize(QtCore.QSize(24, 24))
        self.radioButton_2.setObjectName("radioButton_2")
        self.apply_Button = QtWidgets.QPushButton(self.groupBox_right_bottom)
        self.apply_Button.setGeometry(QtCore.QRect(20, 120, 233, 51))
        icon_apply = QtGui.QIcon()
        icon_apply.addPixmap(QtGui.QPixmap("/usr/share/timerdown/icons/apply.ico"),
                             QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.apply_Button.setIcon(icon_apply)
        self.apply_Button.setIconSize(QtCore.QSize(24, 24))
        self.apply_Button.setObjectName("apply_Button")
        self.frame_5 = QtWidgets.QFrame(self.groupBox_right_bottom)
        self.frame_5.setGeometry(QtCore.QRect(50, 32, 175, 81))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_5.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.apply_Button.raise_()
        self.verticalLayout.addWidget(self.groupBox_right_bottom)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(9, 380, 561, 71))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_exit = QtWidgets.QGroupBox(self.horizontalLayoutWidget_2)
        self.groupBox_exit.setTitle("")
        self.groupBox_exit.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_exit.setObjectName("groupBox_exit")
        self.exit_button = QtWidgets.QPushButton(self.groupBox_exit)
        self.exit_button.setGeometry(QtCore.QRect(20, 7, 233, 51))
        exit_icon = QtGui.QIcon()
        exit_icon.addPixmap(QtGui.QPixmap("/usr/share/timerdown/icons/exit.ico"),
                            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_button.setIcon(exit_icon)
        self.exit_button.setIconSize(QtCore.QSize(24, 24))
        self.exit_button.setObjectName("exit_button")
        self.horizontalLayout_2.addWidget(self.groupBox_exit)

        self.groupBox_LCD = QtWidgets.QGroupBox(self.horizontalLayoutWidget_2)
        self.groupBox_LCD.setTitle("")
        self.groupBox_LCD.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_LCD.setObjectName("groupBox_LCD")

        self.LCD = QtWidgets.QLCDNumber(self.groupBox_LCD)
        self.LCD.setGeometry(QtCore.QRect(4, 6, 265, 55))
        self.LCD.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LCD.setObjectName("LCD")
        self.LCD.setDigitCount(8)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start()
        self.horizontalLayout_2.addWidget(self.groupBox_LCD)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # For info in status bar:
        self.label_info = QtWidgets.QLabel(self.statusbar)
        self.label_info.setText("Welcome!")
        self.label_info.setObjectName("label_info")
        self.label_info.setGeometry(16, 0, 250, 17)
        MainWindow.setStatusBar(self.statusbar)

        # This set up hour & min spinBox to current time:
        self.reset_hm()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TimerDown"))
        self.checkBox_min.setText(_translate("MainWindow", "minutes"))
        self.checkBox_hour.setText(_translate("MainWindow", "hours"))
        self.checkBox_at_time.setText(_translate("MainWindow", "Shutdown PC at:"))
        self.label_top.setText(_translate("MainWindow", "Shutdown PC in:"))
        self.label_2_tacke.setText(_translate("MainWindow", ":"))

        # Set up button connected to schedule() function:
        self.button_set_up.setText(_translate("MainWindow", "Set up shutdown"))
        self.button_set_up.clicked.connect(self.schedule)

        # Reset button connected to reset_button() function:
        self.button_reset.setText(_translate("MainWindow", "Reset your set up"))
        self.button_reset.clicked.connect(self.reset_button)

        # Minimise to tray button:
        self.button_to_tray.setText(_translate("MainWindow", "Minimize to tray"))
        self.button_to_tray.clicked.connect(self.minimise)

        ##################
        # Quick actions: #
        ##################
        # Enable quick actions:
        self.groupBox_right_bottom.setTitle(_translate("MainWindow", "Enable Quick actions:"))
        # Quick actions radio buttons:
        self.radioButton.setText(_translate("MainWindow", "Quick shutdown"))
        self.radioButton_2.setText(_translate("MainWindow", "Quick reboot"))
        # Apply buuton for quick actions connected to functions quick()
        self.apply_Button.setText(_translate("MainWindow", "Apply quick action"))
        self.apply_Button.clicked.connect(self.quick)

        # Exit button:
        self.exit_button.setText(_translate("MainWindow", "Exit from TimerDown"))
        self.exit_button.clicked.connect(self.exit_app)

#######################################################################################

    ######################
    ###   OPERATIONS:  ###
    ######################

    ######################################
    ## Setup spinbox_hour & spinbox_min ##
    ##        to current time           ##
    ######################################

    def reset_hm(self):
        time = datetime.datetime.now()
        # time = QTime.currentTime() - You can use QTimer instead timedate
        self.spinBox_hour.setValue(time.hour)  # "hour()" if you are using qtime
        self.spinBox_min.setValue(time.minute)

    #################################
    ## Big schedule function which ##
    ##       do all the job        ##
    #################################

    def schedule(self):
        time = datetime.datetime.now()
        # time = QTime.currentTime() - You can use QTimer instead timedate
        value = self.spinBox_top.value()
        h = self.spinBox_hour.value()
        m = self.spinBox_min.value()

        if self.checkBox_min.isChecked():
            os.system(f"shutdown -h {value}")
            self.label_info.setText(f"Your PC will shutdown in {value} minutes!")
            # Za disable dugme kad ga klikne
            self.button_set_up.setEnabled(False)

        elif self.checkBox_hour.isChecked():
            value_h = value * 60
            os.system(f"shutdown -h {value_h}")
            self.label_info.setText(f"Your PC will shutdown in {value} hours!")
            self.button_set_up.setEnabled(False)

        else:
            hm_min = h * 60 + m
            now_time_in_min = time.hour * 60 + time.minute  # hour() ako se koristi qtime
            final_num = hm_min - now_time_in_min
            if final_num <= 0:
                self.label_info.setText("Time in past! Set up again!")
                self.reset_hm()
            else:
                # os.system(f"shutdown {h}:{m}")  --- You can do it this way also (maybe better, but who cares :) )
                os.system(f"shutdown -h {final_num}")
                self.button_set_up.setEnabled(False)
                if m < 10:
                    self.label_info.setText(f"Your PC will shutdown at {h}:0{m} !")
                    self.tray.setToolTip(f"Your PC will shutdown at {h}:0{m} !")
                else:
                    self.label_info.setText(f"Your PC will shutdown at {h}:{m} !")
                    self.tray.setToolTip(f"Your PC will shutdown at {h}:{m} !")

        self.trayTooltip()  # Function under

    #############################################################
    ##      Operation which is used in "schedule" function     ##
    ## to change Tray tooltip according to the given operation ##
    ##                 of "schedule" function                  ##
    #############################################################

    def trayTooltip(self):
        now = datetime.datetime.now()

        # If you choose to shutdown PC in "X" minutes:
        if self.checkBox_min.isChecked():
            # min_in_s = self.spinBox_top.value() * 60  # Min in sec, for using in timedelta
            #action_time = now + datetime.timedelta(seconds=min_in_s)
            action_time = now + datetime.timedelta(minutes=self.spinBox_top.value())
            if action_time.day == now.day:
                self.tray.setToolTip(
                    f"Your PC will shutdown at {action_time.hour}:{action_time.minute} !")
            else:
                self.tray.setToolTip(
                    f"Your PC will shutdown on {action_time.day}/{action_time.month}/{action_time.year} at {action_time.hour}:{action_time.minute} !")

        # If you choose to shutdown PC in "X" hours:
        elif self.checkBox_hour.isChecked():
            # hour_in_s = self.spinBox_top.value() * 3600  # Hours in sec, for using in timedelta
            #action_time = now + datetime.timedelta(seconds=hour_in_s)
            action_time = now + datetime.timedelta(hours=self.spinBox_top.value())
            if action_time.day == now.day:
                self.tray.setToolTip(
                    f"Your PC will shutdown at {action_time.hour}:{action_time.minute} !")
            else:
                self.tray.setToolTip(
                    f"Your PC will shutdown on {action_time.day}/{action_time.month}/{action_time.year} at {action_time.hour}:{action_time.minute} !")

    ########################################
    ## Reset all your schedule and set up ##
    ## returns every value to the default ##
    ########################################

    def reset_button(self):
        # time = QTime.currentTime() - You can use QTimer instead timedate
        time = datetime.datetime.now()
        if self.checkBox_min.isChecked():
            self.spinBox_top.setValue(15)
        elif self.checkBox_hour.isChecked():
            self.spinBox_top.setValue(2)
        self.reset_hm()
        self.label_info.setText("Set up again!")
        self.tray.setToolTip("TimerDown - there is no schedule!")
        os.system("shutdown -c")
        self.button_set_up.setEnabled(True)

    ##########################
    ## Minimise app to tray ##
    ##########################

    def minimise(self):
        MainWindow.hide()
        self.tray.setVisible(True)

    #################################
    ## Operation for Quick actions ##
    #################################

    def quick(self):
        if self.radioButton.isChecked():
            os.system("shutdown -h now")
        elif self.radioButton_2.isChecked():
            os.systemd("reboot")
        else:
            self.label_info.setText("No quick action selected!")

    #############################
    ## Functions for LCD clock ##
    ##     - using QTime -     ##
    #############################

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm:ss')
        if (time.second() % 2) == 0:
            text = time.toString('hh:mm ss')
        self.LCD.display(text)

    ########################################
    ## To show app when minimised in tray ##
    ########################################

    def show_from_tray(self):
        MainWindow.show()

    ###################
    ## Exit from app ##
    ###################

    def exit_app(self):
        sys.exit()

###########################################


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
