from fbs_runtime.application_context.PySide2 import ApplicationContext
from PySide2.QtWidgets import QMainWindow, QDesktopWidget
import sys

from package.main_window import MainWindow

if __name__ == '__main__' :
    appctxt = ApplicationContext()  # 1. Instantiate ApplicationContext
    window = MainWindow(ctx=appctxt)
    # desktop_widget = QDesktopWidget()
    # size = QDesktopWidget.screenGeometry(desktop_widget)
    # window.resize(size.width(), size.height())
    window.showMaximized()
    exit_code = appctxt.app.exec_()  # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
