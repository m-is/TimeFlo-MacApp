"""
    File name: timer.py
    Author: Andrew Free
    Date created: -
    Python Version: 3.6
    Alert Sounds Credits: https://freesound.org/people/CGEffex/sounds/94678/
"""
import sys
from threading import Thread


from playsound import playsound
from PyQt5.QtWidgets import QDialog, QInputDialog
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore

from ui import Ui


MINUTE_MS = 60000
SPEED_MULTIPLIER = 100  # [1 for normal speed]


class Timer(QDialog):
    """
    Timer program to help manage time and break out of the flow state.
    """

    def __init__(self):
        super(Timer, self).__init__()
        self.ui = Ui()
        self.ui.setupUi(self)

        self.change_allowed = True  # whether or not change buttons can be clicked
        self.break_time = 5
        self.work_unit_time_min = 20
        self.task_count = 1
        self.alert_sound = "fog_alarm.wav"
        self.task_break = None
        self.my_timer = QtCore.QTimer()

        self.ui.start_timer.clicked.connect(lambda: self.on_start_clicked())
        self.ui.end_timer.clicked.connect(lambda: self.on_end_clicked())
        self.ui.change_timer.clicked.connect(lambda: self.on_change_clicked())
        self.ui.change_break.clicked.connect(lambda: self.on_break_clicked())

        self.ui.lcd_number.display(f"{self.work_unit_time_min}.00")

    def play_sound(self):
        t = Thread(target=self._sound)
        t.start()

    def _sound(self):
        playsound(self.alert_sound)

    def _countdown_time(self, minutes, seconds):
        if seconds == 0.0:
            minutes -= 1
            seconds = 0.60
        else:
            seconds -= 0.01
        return minutes, seconds

    def countdown(self):
        time = self.ui.lcd_number.value()
        minutes, seconds = self._countdown_time(int(time), round(time % 1, 2))

        seconds = "{:.2f}".format((seconds))[1::]
        self.ui.lcd_number.display(f"{minutes}{seconds}")

        if (minutes <= 0 and float(seconds) <= 0) and self.task_break in [
            True,
            None,
        ]:  # previously elif
            # Regular Break code
            self.task_break = False
            self.ui.start_timer.setText("Start Break")
            self.ui.lcd_number.setStyleSheet("color: red;")

            self.ui.lcd_number.display(f"{self.break_time}.00")
            self.my_timer.disconnect()
            self.play_sound()
            self.change_allowed = (
                True  # allows change buttons to work after timer finishes
            )
            return

        elif (minutes <= 0 and float(seconds) <= 0) and self.task_break is False:
            # Start task code
            self.task_break = True
            self.task_count += 1
            self.ui.start_timer.setText("Start Timer")
            self.ui.lcd_number.setStyleSheet("color: black;")

            self.ui.lcd_number.display(f"{self.work_unit_time_min}.00")
            self.my_timer.disconnect()
            self.play_sound()
            self.change_allowed = True
            return

    def on_end_clicked(self):
        sys.exit()

    def on_start_clicked(self):
        self.my_timer.timeout.connect(lambda: self.countdown())
        self.my_timer.start(
            round(MINUTE_MS / SPEED_MULTIPLIER)
        )  # 1 min in milliseconds

        self.change_allowed = (
            False  # change buttons will not work when timer is operating
        )

    def on_change_clicked(self):
        if self.change_allowed is True:
            num, result = QInputDialog.getInt(
                self, "Work Timer Length Input Dialog", "Enter the work timer length:"
            )  # popup window for user configuration
            if result is True:
                self.work_unit_time_min = num
                self.ui.lcd_number.display(self.work_unit_time_min)

    def on_break_clicked(self):
        if self.change_allowed is True:
            num, result = QInputDialog.getInt(
                self, "Break Timer Length Input Dialog", "Enter the break timer length:"
            )
            if result is True:
                self.break_time = num
                self.ui.lcd_number.display(self.break_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Timer()
    window.show()
    app.exec()
