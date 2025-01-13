from PyQt6 import QtWidgets, QtCore
from src.view.Ui_PantallaPrincipal import Ui_ApuestasApp
from src.controller.ControllerDetallesApuesta import ControllerDetallesApuesta
from src.model.EventoDeportivo import EventoDeportivo
from src.model.ManejoEventosDeportivos import ManejoEventosDeportivos

class ControllerMain(QtWidgets.QMainWindow, Ui_ApuestasApp):

    def __init__(self, parent=None):
        super(ControllerMain,self).__init__(parent)
        self.setupUi(self)
        self.cargarEventosDeportivos()
        self.initAction()
        self.show()

    def cargarEventosDeportivos(self):
        #ManejoEventos = ManejoEventosDeportivos()
        #eventos = ManejoEventos.eventos
        eventos = [
            EventoDeportivo("Fútbol", "España", "La Liga", "FC Barcelona", "Real Madrid", "Jornada 20"),
            EventoDeportivo("Fútbol", "Internacional", "Champions League", "Inter Milan", "PSG", "Cuartos de Final - Ida"),
            EventoDeportivo("Fútbol", "España", "La Liga", "Atletico de Madrid", "Sevilla", "Jornada 20"),
            EventoDeportivo("Fútbol", "Inglaterra", "Premier League", "Liverpool", "Manchester City", "Jornada 25"),
            EventoDeportivo("Fútbol", "Alemania", "Bundesliga", "Bayern Munich", "Ausburgo", "Jornada 17")
        ]
        for i, evento in enumerate(eventos):
            self.add_event_widget(
                evento.liga, evento.pais,
                f"{evento.equipo1} vs {evento.equipo2}",
                "1.8", "3.0", "2.5",
                "../resources/futbol.png",
                evento.jornada,  # Instancia de campeonato
                i+1
            )


    def initAction(self):
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn1_gana1").clicked.connect(self.detallesApuesta)
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn1_empate").clicked.connect(self.detallesApuesta)
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn1_gana2").clicked.connect(self.detallesApuesta)
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn2_gana1").clicked.connect(self.detallesApuesta)
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn2_empate").clicked.connect(self.detallesApuesta)
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn2_gana2").clicked.connect(self.detallesApuesta)
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn3_gana1").clicked.connect(self.detallesApuesta)
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn3_empate").clicked.connect(self.detallesApuesta)
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn3_gana2").clicked.connect(self.detallesApuesta)
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn4_gana1").clicked.connect(self.detallesApuesta)
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn4_empate").clicked.connect(self.detallesApuesta)
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn4_gana2").clicked.connect(self.detallesApuesta)
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn5_gana1").clicked.connect(self.detallesApuesta)
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn5_empate").clicked.connect(self.detallesApuesta)
        self.scrollContent.findChild(QtWidgets.QPushButton, "btn5_gana2").clicked.connect(self.detallesApuesta)


    def detallesApuesta(self):
        self.vDetallesApuesta = ControllerDetallesApuesta()
        self.vDetallesApuesta.show()
        self.close()
