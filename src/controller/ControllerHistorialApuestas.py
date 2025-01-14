from PyQt6 import QtWidgets
from src.view.Ui_HistorialApuestas import Ui_HistorialApuestas
from src.model.Apuesta.ManejoApuestas import ManejoApuestas

class ControllerHistorialApuestas(QtWidgets.QMainWindow, Ui_HistorialApuestas):

    def __init__(self, parent=None):
        super(ControllerHistorialApuestas,self).__init__(parent)
        self.setupUi(self)
        self.modelo = ManejoApuestas()
        self.apuestas = self.modelo.apuestas
        self.cargarApuestas()
        self.initAction()
        self.show()

    def initAction(self):
        self.btnVolver.clicked.connect(self.volver)

    def volver(self):
        from src.controller.ControllerEventosDeportivos import ControllerEventosDeportivos
        self.vPantallaPrincipal = ControllerEventosDeportivos()
        self.vPantallaPrincipal.show()
        self.close()

    def cargarApuestas(self):
        for i,apuesta in enumerate(self.apuestas):
            apuestaWidget = self.crearApuestaWidget(
                partido = f"{apuesta.eventosDeportivos.equipo1} vs {apuesta.eventosDeportivos.equipo2}",
                fecha = apuesta.eventosDeportivos.fecha,
                hora = apuesta.eventosDeportivos.hora,
                seleccion = apuesta.eleccion,
                monto = apuesta.montoApostado,
                ganancia = apuesta.ganacia,
                estado= apuesta.estado
            )
            self.apuestasLayout.addWidget(apuestaWidget)