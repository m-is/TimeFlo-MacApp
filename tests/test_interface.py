from timeflow.timer import (
    Timer,
    LONG_BREAK_TIME_MIN,
    WORK_UNIT_TIME_MIN,
    CYCLES_UNTIL_LONG_BREAK,
)

from PyQt5 import QtCore

AUDIO_ALERT_TIME_MILLISECONDS = 8000
MAXIUM_SHORT_BREAK_TIME_MILLISECONDS = 600000


def test_timer_flow(qtbot):
    widget = Timer()
    qtbot.addWidget(widget)

    def check_break_label():
        assert widget.ui.start_timer.text() == "Start Break"

    def check_work_label():
        assert widget.ui.start_timer.text() == "Start Timer"

    def check_long_break_label():
        assert widget.ui.start_timer.text() == "Start Long Break"

    # Assert start condition
    assert widget.ui.lcd_number.intValue() == WORK_UNIT_TIME_MIN

    for x in range(CYCLES_UNTIL_LONG_BREAK - 1):
        # Start unit of work and wait for break label
        print("start work")
        qtbot.mouseClick(widget.ui.start_timer, QtCore.Qt.LeftButton)
        assert widget.ui.lcd_number.intValue() == WORK_UNIT_TIME_MIN
        qtbot.waitUntil(
            check_break_label,
            timeout=(WORK_UNIT_TIME_MIN * 60000) + AUDIO_ALERT_TIME_MILLISECONDS,
        )
        print("start break")
        # Start short break and check for work label
        qtbot.mouseClick(widget.ui.start_timer, QtCore.Qt.LeftButton)
        assert widget.ui.lcd_number.intValue() in range(1, 2)
        qtbot.waitUntil(check_work_label, timeout=MAXIUM_SHORT_BREAK_TIME_MILLISECONDS)

    print("start final work")
    # Start final unit of work for the cycle & Check for long break
    qtbot.mouseClick(widget.ui.start_timer, QtCore.Qt.LeftButton)
    assert widget.ui.lcd_number.intValue() == WORK_UNIT_TIME_MIN
    qtbot.waitUntil(
        check_long_break_label,
        timeout=(WORK_UNIT_TIME_MIN * 60000) + AUDIO_ALERT_TIME_MILLISECONDS,
    )

    print("return to state")
    # return back to original state after a long break
    qtbot.mouseClick(widget.ui.start_timer, QtCore.Qt.LeftButton)
    assert widget.ui.lcd_number.intValue() == WORK_UNIT_TIME_MIN
    qtbot.waitUntil(
        check_work_label,
        timeout=(LONG_BREAK_TIME_MIN * 60000) + AUDIO_ALERT_TIME_MILLISECONDS,
    )
