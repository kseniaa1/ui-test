from .gui.application import Application


def help():
    app = Application([])
    quit(app.exec())