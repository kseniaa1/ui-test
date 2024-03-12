import logging
import sys

from .app import CalcApp


def help_gui():
    app = CalcApp(sys.argv)
    if "--log" in sys.argv:
        logging.info("Режим логгирования включен")
    quit(app.exec())