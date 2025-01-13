from PyQt6 import QtWidgets, QtCore
from src.view.Ui_PantallaPrincipal import Ui_ApuestasApp
from src.controller.ControllerDetallesApuesta import ControllerDetallesApuesta

class ControllerMain(QtWidgets.QMainWindow, Ui_ApuestasApp):

    def __init__(self, parent=None):
        super(ControllerMain,self).__init__(parent)
        self.setupUi(self)
        #self.initAction()
        self.show()

    def initAction(self):
        button_team1 = self.scrollContent.findChild(QtWidgets.QPushButton, "btnTeam1_Equipo 1 vs Equipo 2")
        button_team1.clicked.connect(self.detallesApuesta)
        #self.btnPlay.clicked.connect(self.pressPlay)
        #self.labelSenal.pressed.connect(self.pressMicro)
        #self.btnAlmacenamiento.clicked.connect(self.selectAudioFile)

    def detallesApuesta(self):
        self.vDetallesApuesta = ControllerDetallesApuesta()
        self.vDetallesApuesta.show()
        self.close()