from PyQt5.QtWidgets import *
from gui import Ui_MainWindow
from webscraper import *
from compare import *


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
