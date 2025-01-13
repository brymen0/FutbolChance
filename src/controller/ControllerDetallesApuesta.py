from PyQt6 import QtWidgets, QtCore
from src.view.Ui_DetallesApuesta import Ui_DetalleApuesta

class ControllerDetallesApuesta(QtWidgets.QMainWindow, Ui_DetalleApuesta):

    def __init__(self, parent=None):
        super(ControllerDetallesApuesta,self).__init__(parent)
        self.setupUi(self)
        self.initAction()
        self.show()

    def initAction(self):
        self.btnVolver.clicked.connect(self.close())