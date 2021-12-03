"""
    File name: timer.py
    Author: Andrew Free
    Date created: -
    Python Version: 3.6
    Alert Sounds Credits: https://freesound.org/people/CGEffex/sounds/94678/
"""
import random
import sys

from playsound import playsound
from PyQt5.QtWidgets import QDialog, QInputDialog, QLineEdit
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore

from ui import Ui


LONG_BREAK_TIME_MIN = 25
WORK_UNIT_TIME_MIN = 25
CYCLES_UNTIL_LONG_BREAK = 3


class Timer(QDialog):
    """
    Timer program to help manage time and break out of the flow state. 
    """

    def __init__(self):
        super(Timer, self).__init__()
        self.ui = Ui()
        self.ui.setupUi(self)

        self.task_count = 1
        self.alert_sound = "fog_alarm.wav"
        self.short_break_time = lambda: random.randrange(5, 11)
        self.task_break = None
        self.my_timer = QtCore.QTimer()

        self.ui.start_timer.clicked.connect(lambda: self.on_start_clicked())
        self.ui.end_timer.clicked.connect(lambda: self.on_end_clicked())
        self.ui.change_timer.clicked.connect(lambda: self.on_change_clicked())
        


        self.ui.lcd_number.display(WORK_UNIT_TIME_MIN)


    def countdown(self):
        self.ui.lcd_number.display(self.ui.lcd_number.intValue() - 1)
        if (
            self.ui.lcd_number.intValue() == 0
            and self.task_count == CYCLES_UNTIL_LONG_BREAK
        ):
            # Long break
            self.task_count = 0
            self.task_break = False
            self.ui.start_timer.setText("Start Long Break")
            self.ui.lcd_number.setStyleSheet("color: red;")

            self.ui.lcd_number.display(LONG_BREAK_TIME_MIN)
            self.my_timer.disconnect()
            playsound(self.alert_sound)
            return

        elif self.ui.lcd_number.intValue() == 0 and self.task_break in [True, None]:
            # Regular Break code
            self.task_break = False
            self.ui.start_timer.setText("Start Break")
            self.ui.lcd_number.setStyleSheet("color: red;")

            self.ui.lcd_number.display(self.short_break_time())
            self.my_timer.disconnect()
            playsound(self.alert_sound)
            return

        elif self.ui.lcd_number.intValue() == 0 and self.task_break is False:
            # Start task code
            self.task_break = True
            self.task_count += 1
            self.ui.start_timer.setText("Start Timer")
            self.ui.lcd_number.setStyleSheet("color: black;")

            self.ui.lcd_number.display(WORK_UNIT_TIME_MIN)
            self.my_timer.disconnect()
            playsound(self.alert_sound)
            return

    def on_end_clicked(self):
        sys.exit()

    def on_start_clicked(self):
        self.my_timer.timeout.connect(lambda: self.countdown())
        self.my_timer.start(60000)  # 1 min in milliseconds

    def on_change_clicked(self):
        num, result = QInputDialog.getInt(self, 'Timer Length Input Dialog', 'Enter the timer length:')

            



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Timer()
    window.show()
    app.exec()
