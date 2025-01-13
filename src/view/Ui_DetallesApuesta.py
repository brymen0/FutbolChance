from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DetalleApuesta(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 650)
        MainWindow.setStyleSheet("background-color: #1e1e1e;")  # Fondo oscuro

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Layout principal
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setContentsMargins(10, 10, 10, 10)
        self.mainLayout.setSpacing(10)

        # Título
        self.lblTitulo = QtWidgets.QLabel("Detalles de la Apuesta")
        self.lblTitulo.setStyleSheet("""
            color: #ffcc00;
            font-size: 24px;
            font-weight: bold;
            text-align: center;
        """)
        self.lblTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(self.lblTitulo)

        # Información del partido
        self.infoContainer = QtWidgets.QWidget()
        self.infoContainer.setStyleSheet("""
            background-color: #2e2e2e;
            border-radius: 10px;
            padding: 10px;
        """)
        infoLayout = QtWidgets.QVBoxLayout(self.infoContainer)

        self.lblPartido = QtWidgets.QLabel("Partido: Equipo A vs Equipo B")
        self.lblPartido.setStyleSheet("color: #ffcc00; font-size: 18px; font-weight: bold;")
        infoLayout.addWidget(self.lblPartido)

        self.lblFecha = QtWidgets.QLabel("Fecha: 12/01/2025")
        self.lblFecha.setStyleSheet("color: #ffffff; font-size: 16px;")
        infoLayout.addWidget(self.lblFecha)

        self.lblHora = QtWidgets.QLabel("Hora: 16:00")
        self.lblHora.setStyleSheet("color: #ffffff; font-size: 16px;")
        infoLayout.addWidget(self.lblHora)

        self.lblSeleccion = QtWidgets.QLabel("Tu selección: Gana Equipo A")
        self.lblSeleccion.setStyleSheet("color: #ffffff; font-size: 16px;")
        infoLayout.addWidget(self.lblSeleccion)

        self.lblCuota = QtWidgets.QLabel("Cuota ofrecida: 3x")
        self.lblCuota.setStyleSheet("color: #00ff00; font-size: 16px; font-weight: bold;")
        infoLayout.addWidget(self.lblCuota)

        self.mainLayout.addWidget(self.infoContainer)

        # Espaciador para separar el deslizador del cuadro de información
        self.mainLayout.addSpacing(20)

        # Deslizador para cantidad a apostar
        self.sliderApuesta = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self.sliderApuesta.setMinimum(1)
        self.sliderApuesta.setMaximum(100)
        self.sliderApuesta.setValue(1)
        self.sliderApuesta.setStyleSheet("""
            QSlider::groove:horizontal {
                background: #3a3a3a;
                height: 6px;
                border-radius: 3px;
            }
            QSlider::handle:horizontal {
                background: #ffcc00;
                border: none;
                width: 14px;
                height: 14px;
                margin: -4px 0;
                border-radius: 7px;
            }
        """)
        self.mainLayout.addWidget(self.sliderApuesta)

        # Contenedor para monto y ganancia
        self.apuestaContainer = QtWidgets.QWidget()
        self.apuestaContainer.setStyleSheet("background-color: transparent;")
        apuestaLayout = QtWidgets.QVBoxLayout(self.apuestaContainer)
        apuestaLayout.setContentsMargins(0, 0, 0, 0)

        self.lblMonto = QtWidgets.QLabel("Cantidad a apostar: $1")
        self.lblMonto.setStyleSheet("color: #ffffff; font-size: 16px;")
        self.lblMonto.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        apuestaLayout.addWidget(self.lblMonto)

        self.lblGanancia = QtWidgets.QLabel("Ganancia potencial: $3")
        self.lblGanancia.setStyleSheet("color: #00ff00; font-size: 16px; font-weight: bold;")
        self.lblGanancia.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        apuestaLayout.addWidget(self.lblGanancia)

        self.mainLayout.addWidget(self.apuestaContainer)

        # Espaciador para separar los botones
        self.mainLayout.addSpacing(20)

        # Botones de acción
        self.buttonsLayout = QtWidgets.QHBoxLayout()
        self.buttonsLayout.setSpacing(10)

        self.btnVolver = QtWidgets.QPushButton("Volver")
        self.btnVolver.setStyleSheet("""
            QPushButton {
                color: #ffffff;
                background-color: #ff0000;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #cc0000;
            }
        """)
        self.buttonsLayout.addWidget(self.btnVolver)

        self.btnApostar = QtWidgets.QPushButton("Apostar")
        self.btnApostar.setStyleSheet("""
            QPushButton {
                color: #ffffff;
                background-color: #0078d7;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005bb5;
            }
        """)
        self.buttonsLayout.addWidget(self.btnApostar)

        self.mainLayout.addLayout(self.buttonsLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        # Conexiones
        self.sliderApuesta.valueChanged.connect(self.actualizarGanancia)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def actualizarGanancia(self):
        valor = self.sliderApuesta.value()
        cuota = 3  # Cuota fija para el ejemplo
        ganancia = valor * cuota
        self.lblMonto.setText(f"Cantidad a apostar: ${valor}")
        self.lblGanancia.setText(f"Ganancia potencial: ${ganancia}")

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Detalles de la Apuesta")
