#!/usr/bin/env python

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTime
from PyQt5.QtCore import QDate
import datetime
import sys
import os

sys.path.append('/usr/share/timerdown/')
import gui


class App(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)

        ################################################################
        ## OVO ZA SAD NE TREBA ZBOG FUNKCIJE time_set() koja sve radi ##
        ## For current time:                                          ##
        ## time = QTime.currentTime() - If you are using QTime        ##
        ## time = datetime.datetime.now()                             ##
        ################################################################

        ###############################################
        ## Poziva time_set() funkciju koja je dole:  ##
        ###############################################
        self.time_set()

        ##################################
        ## Dodavanje timer-a za LCD sat ##
        ##################################
        self.timer_lcd = QtCore.QTimer()
        # vuče showTime() funkciju da prikaže sat i datum (u istoj je funkciji kod i za datum)
        self.timer_lcd.timeout.connect(self.showTime)
        self.timer_lcd.start()

        # Ovo je POKUŠAJ da se spinboxovi nameste kao sat, ali tad ne možeš da podesiš vreme kad da se gasi
        # self.timer_spinBox = QtCore.QTimer()
        # self.timer_spinBox.timeout.connect(self.time_set)
        # self.timer_spinBox.start()

        ##########################################
        ## Ubacivanje labela u status bar gui-a ##
        ##########################################
        self.label_info = QtWidgets.QLabel(self.statusbar)
        self.label_info.setText("Welcome!")
        self.label_info.setObjectName("label_info")
        self.label_info.setGeometry(16, 0, 350, 17)

        ##############################
        ## Ubacivanje TRAY-a u gui: ##
        ##############################
        self.tray = QtWidgets.QSystemTrayIcon()
        self.tray.setToolTip("TimerDown")
        self.icon = QIcon("/usr/share/timerdown/icons/shutdown.ico")
        self.tray.setIcon(self.icon)
        self.tray.setVisible(False)  # Tray nije vidljiv dok se ne klikne dugme "tray_button"

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
        self.option2.triggered.connect(self.reset)
        self.menu.addAction(self.option2)

        self.option3_icon = QIcon("/usr/share/timerdown/icons/exit.ico")
        self.option3 = QtWidgets.QAction("Exit application")
        self.option3.setIcon(self.option3_icon)
        self.option3.triggered.connect(self.exit)
        self.menu.addAction(self.option3)

        #########################################
        ## DUGMIĆI i povezivanje sa funckijama ##
        #########################################
        self.set_up_button.clicked.connect(self.schedule)

        self.reset_button.clicked.connect(self.reset)

        self.tray_button.clicked.connect(self.minimize)

        self.apply_button.clicked.connect(self.quick)

        self.exit_button.clicked.connect(self.exit)

        # self.spinBox_hour.setMinimum(time.hour) ' ovo ne treba zbog reset funkcije koja to radi'

################################################################################

    def schedule(self):
        time = datetime.datetime.now()
        # time = QTime.currentTime() - You can use QTimer instead timedate
        value = self.spinBox_hm.value()
        m = self.spinBox_min.value()
        h = self.spinBox_hour.value()

        if self.checkBox_min.isChecked():
            os.system(f"shutdown -h {value}")
            self.label_info.setText(f"Your PC will shutdown in {value} minutes!")
            # Za set_up_button dugme kad ga klikne
            self.set_up_button.setEnabled(False)

        elif self.checkBox_hour.isChecked():
            value_h = value * 60
            os.system(f"shutdown -h {value_h}")
            self.label_info.setText(f"Your PC will shutdown in {value} hours!")
            self.set_up_button.setEnabled(False)

        else:
            hm_min = h * 60 + m
            now_time_in_min = time.hour * 60 + time.minute  # hour() ako se koristi qtime
            final_num = hm_min - now_time_in_min
            if final_num <= 0:
                self.label_info.setText("Time in past! Set up again!")
                self.time_set()
            else:
                # os.system(f"shutdown {h}:{m}")  --- You can do it this way also (maybe better, but who cares :) )
                os.system(f"shutdown -h {final_num}")
                self.set_up_button.setEnabled(False)
                if m < 10:
                    self.label_info.setText(f"Your PC will shutdown at {h}:0{m} !")
                    self.tray.setToolTip(f"Your PC will shutdown at {h}:0{m} !")
                else:
                    self.label_info.setText(f"Your PC will shutdown at {h}:{m} !")
                    self.tray.setToolTip(f"Your PC will shutdown at {h}:{m} !")

        self.trayTooltip()  # Function under

    def trayTooltip(self):
        now = datetime.datetime.now()

        # Srediti obaveštenja kad je gašenje recimo u 23:07, da tako i prikazuje a ne 23:7

        # If you choose to shutdown PC in "X" minutes:
        if self.checkBox_min.isChecked():
            action_time = now + datetime.timedelta(minutes=self.spinBox_hm.value())
            if action_time.day == now.day:
                self.tray.setToolTip(
                    f"Your PC will shutdown at {action_time.hour}:{action_time.minute} !")
            else:
                self.tray.setToolTip(
                    f"Your PC will shutdown on {action_time.day}/{action_time.month}/{action_time.year} at {action_time.hour}:{action_time.minute} !")

        # If you choose to shutdown PC in "X" hours:
        elif self.checkBox_hour.isChecked():
            action_time = now + datetime.timedelta(hours=self.spinBox_hm.value())
            if action_time.day == now.day:
                self.tray.setToolTip(
                    f"Your PC will shutdown at {action_time.hour}:{action_time.minute} !")
            else:
                self.tray.setToolTip(
                    f"Your PC will shutdown on {action_time.day}/{action_time.month}/{action_time.year} at {action_time.hour}:{action_time.minute} !")

    def time_set(self):
        time = datetime.datetime.now()
        self.spinBox_hour.setValue(time.hour)
        self.spinBox_hour.setMinimum(time.hour)
        self.spinBox_min.setValue(time.minute)

    def showTime(self):
        date = QDate.currentDate()
        date_text = date.toString('dd MM yyyy')
        time = QTime.currentTime()
        time_text = time.toString('hh:mm:ss')
        if (time.second() % 2) == 0:
            time_text = time.toString('hh:mm ss')
        self.lcd_clock.display(time_text)
        self.lcd_date.display(date_text)

    def reset(self):
        time = datetime.datetime.now()
        os.system("shutdown -c")
        self.time_set()
        self.spinBox_hm.setValue(15)
        self.label_info.setText("Set up again!")
        self.tray.setToolTip("TimerDown - there is no schedule!")
        if self.groupBox_quick.isChecked():
            self.set_up_button.setEnabled(False)
        else:
            self.set_up_button.setEnabled(True)

    # Stara reset funkcija:
    # def reset(self):
    #     time = datetime.datetime.now()
    #     if self.checkBox_min.isChecked():
    #         self.spinBox_hm.setValue(15)
    #     elif self.checkBox_hour.isChecked():
    #         self.spinBox_hm.setValue(time.hour)
    #     self.time_set()
    #     self.label_info.setText("Set up again!")
    #     self.tray.setToolTip("TimerDown - there is no schedule!")
    #     os.system("shutdown -c")
    #     if self.groupBox_quick.isChecked():
    #         self.set_up_button.setEnabled(False)

    def quick(self):
        item = self.comboBox_quick_actions.currentText()
        if item == "Sleep":
            os.system("systemctl suspend")
        elif item == "Hibernate":
            os.system("systemctl hibernate")
        elif item == "Quick reboot":
            os.system("reboot")
        elif item == "Quick shutdown":
            os.system("shutdown -h now")
        # U slučaju da prebacim kod na "radio button", ako se ne odabere ništa, da to ispiše
        # else:
            #self.label_info.setText("No quick action selected!")

    def minimize(self):
        form.hide()
        self.tray.setVisible(True)

    def show_from_tray(self):
        form.show()

    def exit(self):
        sys.exit()

################################################################################


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    #app.setStyle("Fusion")
    form = App()
    form.show()
    app.exec_()
