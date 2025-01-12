from PyQt6 import QtWidgets, QtCore
from src.view.Ui_PantallaPrincipal import Ui_ApuestasApp


class ControllerMain(QtWidgets.QMainWindow, Ui_ApuestasApp):

    def __init__(self, parent=None):
        super(ControllerMain,self).__init__(parent)
        self.setupUi(self)
        #self.initAction()
        self.show()

    #def initAction(self):
        #self.btnPlay.clicked.connect(self.pressPlay)
        #self.labelSenal.pressed.connect(self.pressMicro)
        #self.btnAlmacenamiento.clicked.connect(self.selectAudioFile)