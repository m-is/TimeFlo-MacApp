from timeflow.timer import Timer, LONG_BREAK_TIME_MIN, WORK_UNIT_TIME_MIN

from PyQt5 import QtCore


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

    # Start unit of work
    qtbot.mouseClick(widget.ui.start_timer, QtCore.Qt.LeftButton)
    assert widget.ui.lcd_number.intValue() == WORK_UNIT_TIME_MIN
    qtbot.waitUntil(check_break_label, timeout=(WORK_UNIT_TIME_MIN * 71000))

    # Start short break
    qtbot.mouseClick(widget.ui.start_timer, QtCore.Qt.LeftButton)
    assert widget.ui.lcd_number.intValue() in range(5, 10)
    qtbot.waitUntil(check_work_label, timeout=600100)

    # Start unit of work
    qtbot.mouseClick(widget.ui.start_timer, QtCore.Qt.LeftButton)
    assert widget.ui.lcd_number.intValue() == WORK_UNIT_TIME_MIN
    qtbot.waitUntil(check_break_label, timeout=(WORK_UNIT_TIME_MIN * 61000))

    # start short break
    qtbot.mouseClick(widget.ui.start_timer, QtCore.Qt.LeftButton)
    assert widget.ui.lcd_number.intValue() in range(5, 10)
    qtbot.waitUntil(check_work_label, timeout=600100)

    # start unit of work
    qtbot.mouseClick(widget.ui.start_timer, QtCore.Qt.LeftButton)
    assert widget.ui.lcd_number.intValue() == WORK_UNIT_TIME_MIN
    qtbot.waitUntil(check_break_label, timeout=(WORK_UNIT_TIME_MIN * 61000))

    # start short break
    qtbot.mouseClick(widget.ui.start_timer, QtCore.Qt.LeftButton)
    assert widget.ui.lcd_number.intValue() in range(5, 10)
    qtbot.waitUntil(check_work_label, timeout=600100)

    # start unit of work
    qtbot.mouseClick(widget.ui.start_timer, QtCore.Qt.LeftButton)
    assert widget.ui.lcd_number.intValue() == WORK_UNIT_TIME_MIN
    qtbot.waitUntil(check_long_break_label, timeout=(WORK_UNIT_TIME_MIN * 61000))

    # start long break
    qtbot.mouseClick(widget.ui.start_timer, QtCore.Qt.LeftButton)
    assert widget.ui.lcd_number.intValue() == LONG_BREAK_TIME_MIN
    qtbot.waitUntil(check_work_label, timeout=(LONG_BREAK_TIME_MIN * 61000))

    # return back to original state after a long break
    qtbot.mouseClick(widget.ui.start_timer, QtCore.Qt.LeftButton)
    assert widget.ui.lcd_number.intValue() == WORK_UNIT_TIME_MIN
    qtbot.waitUntil(check_break_label, timeout=(WORK_UNIT_TIME_MIN * 61000))
