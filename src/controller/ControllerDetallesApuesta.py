from PyQt6 import QtWidgets, QtCore
from src.view.Ui_DetallesApuesta import Ui_DetalleApuesta
from src.model.Apuesta.ManejoApuestas import ManejoApuestas

class ControllerDetallesApuesta(QtWidgets.QMainWindow, Ui_DetalleApuesta):

    def __init__(self, eventoDeportivo, eleccion, parent=None):
        super(ControllerDetallesApuesta,self).__init__(parent)
        self.setupUi(self)
        self.modelo = ManejoApuestas()
        self.evento = eventoDeportivo
        self.cuota = 0
        self.opcion = ""
        self.cargarInformacion(eleccion)
        self.initAction()
        self.show()

    def initAction(self):
        self.btnVolver.clicked.connect(self.volver)
        self.btnApostar.clicked.connect(self.apostar)

    def apostar(self):
        self.modelo.crearApuesta(self.evento, self.sliderApuesta.value(), self.cuota, self.opcion)
        self.mostrarMensajeExito()


    def volver(self):
        from src.controller.ControllerEventosDeportivos import ControllerEventosDeportivos
        self.vPantallaPrincipal = ControllerEventosDeportivos()
        self.vPantallaPrincipal.show()
        self.close()

    def mostrarMensajeExito(self):
        ventana_exito = QtWidgets.QDialog(self)
        ventana_exito.setWindowTitle("Apuesta realizada")
        ventana_exito.setFixedSize(300, 150)  # Tamaño fijo de la ventana

        layout = QtWidgets.QVBoxLayout(ventana_exito)

        # Etiqueta para el mensaje
        lbl_mensaje = QtWidgets.QLabel("¡Apuesta realizada con éxito!", ventana_exito)
        lbl_mensaje.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        lbl_mensaje.setStyleSheet("color: white; font-size: 16px;")  # Letras en blanco
        layout.addWidget(lbl_mensaje)

        # Botón de cerrar
        btn_cerrar = QtWidgets.QPushButton("Aceptar", ventana_exito)
        btn_cerrar.clicked.connect(ventana_exito.accept)
        # Aplicar estilos al botón
        btn_cerrar.setStyleSheet("""
            QPushButton {
                background-color: #FFD700;  /* Amarillo */
                color: white;               /* Letras en blanco */
                border: none;
                padding: 8px 16px;
                font-size: 14px;
                font-weight: bold;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #FFC107;  /* Amarillo más oscuro al pasar el mouse */
            }
            QPushButton:pressed {
                background-color: #FFB300;  /* Amarillo aún más oscuro al presionar */
            }
        """)
        layout.addWidget(btn_cerrar)

        # Mostrar la ventana de diálogo
        ventana_exito.exec()
        self.volver()

    def cargarInformacion(self,eleccion):
        self.lblPartido.setText(f"Partido: {self.evento.equipo1} vs {self.evento.equipo2}")
        self.lblHora.setText(str(self.evento.hora))
        self.lblFecha.setText(self.evento.fecha)

        if eleccion == 1:
            self.opcion = f"Gana {self.evento.equipo1}"
            self.cuota = self.evento.cuotas.valor[0]
        elif eleccion == 0:
            self.opcion = "Empate"
            self.cuota = self.evento.cuotas.valor[1]
        else:
            self.opcion = f"Gana {self.evento.equipo2}"
            self.cuota = self.evento.cuotas.valor[2]

        self.lblSeleccion.setText(f"Tu elección: {self.opcion}")
        self.lblCuota.setText(f"Cuota: {self.cuota}")
        self.lblGanancia.setText(f"Cuota: {self.cuota}")