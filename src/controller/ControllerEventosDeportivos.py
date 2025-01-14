from PyQt6 import QtWidgets
from src.view.Ui_PantallaPrincipal import Ui_ApuestasApp
from src.controller.ControllerDetallesApuesta import ControllerDetallesApuesta
from src.model.EventosDeportivos.ManejoEventosDeportivos import ManejoEventosDeportivos
from src.controller.ControllerHistorialApuestas import ControllerHistorialApuestas

class ControllerEventosDeportivos(QtWidgets.QMainWindow, Ui_ApuestasApp):

    def __init__(self, parent=None):
        super(ControllerEventosDeportivos,self).__init__(parent)
        self.setupUi(self)
        self.modelo = ManejoEventosDeportivos()
        self.eventos = self.modelo.eventos
        self.cargarEventosDeportivos()
        self.initAction()
        self.show()

    def cargarEventosDeportivos(self):
        #eventos = self.modelo.eventos
        for i, evento in enumerate(self.eventos):
            self.add_event_widget(
                evento.liga, evento.pais,
                f"{evento.equipo1} vs {evento.equipo2}",
                str(evento.cuotas.valor[0]), str(evento.cuotas.valor[1]), str(evento.cuotas.valor[2]),
                "../resources/futbol.png",
                evento.jornada,
                i+1
            )


    def initAction(self):
        self.centralwidget.findChild(QtWidgets.QPushButton, "btnApuestas").clicked.connect(self.historialApuestas)
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn1_gana1").clicked.connect(lambda: self.detallesApuesta(self.eventos[0],1))
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn1_empate").clicked.connect(lambda: self.detallesApuesta(self.eventos[0],0))
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn1_gana2").clicked.connect(lambda: self.detallesApuesta(self.eventos[0],2))
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn2_gana1").clicked.connect(lambda: self.detallesApuesta(self.eventos[1],1))
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn2_empate").clicked.connect(lambda: self.detallesApuesta(self.eventos[1],0))
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn2_gana2").clicked.connect(lambda: self.detallesApuesta(self.eventos[1],2))
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn3_gana1").clicked.connect(lambda: self.detallesApuesta(self.eventos[2],1))
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn3_empate").clicked.connect(lambda: self.detallesApuesta(self.eventos[2],0))
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn3_gana2").clicked.connect(lambda: self.detallesApuesta(self.eventos[2],2))
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn4_gana1").clicked.connect(lambda: self.detallesApuesta(self.eventos[3],1))
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn4_empate").clicked.connect(lambda: self.detallesApuesta(self.eventos[3],0))
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn4_gana2").clicked.connect(lambda: self.detallesApuesta(self.eventos[3],2))
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn5_gana1").clicked.connect(lambda: self.detallesApuesta(self.eventos[4],1))
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn5_empate").clicked.connect(lambda: self.detallesApuesta(self.eventos[4],0))
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn5_gana2").clicked.connect(lambda: self.detallesApuesta(self.eventos[4],2))


    def detallesApuesta(self, eventoDeportivo, eleccion):
        self.vDetallesApuesta = ControllerDetallesApuesta(eventoDeportivo, eleccion)
        self.vDetallesApuesta.show()
        self.close()

    def historialApuestas(self):
        self.vHistorialApuestas = ControllerHistorialApuestas()
        self.vHistorialApuestas.show()
        self.close()