from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_HistorialApuestas(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 650)
        MainWindow.setStyleSheet("background-color: #1e1e1e;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #layout principal
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setContentsMargins(10, 10, 10, 10)
        self.mainLayout.setSpacing(10)

        # Título
        self.lblTitulo = QtWidgets.QLabel("Historial de Apuestas")
        self.lblTitulo.setStyleSheet("""
            color: #ffcc00;
            font-size: 24px;
            font-weight: bold;
            text-align: center;
        """)
        self.lblTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(self.lblTitulo)

        # Contenedor para la lista de apuestas
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setStyleSheet("background-color: #2e2e2e; border: none; border-radius: 10px;")
        self.scrollArea.setWidgetResizable(True)

        self.scrollContent = QtWidgets.QWidget()
        self.scrollArea.setWidget(self.scrollContent)

        self.apuestasLayout = QtWidgets.QVBoxLayout(self.scrollContent)
        self.apuestasLayout.setContentsMargins(10, 10, 10, 10)
        self.apuestasLayout.setSpacing(10)

        '''
        # Añadir apuestas de ejemplo
        for i in range(10):  # Simula 10 apuestas
            apuestaWidget = self.crearApuestaWidget(
                partido=f"Equipo A vs Equipo B {i + 1}",
                fecha="12/01/2025",
                hora="16:00",
                seleccion="Gana Equipo A",
                monto=10 + i,
                ganancia=(10 + i) * 3,
                estado="Ganada" if i % 3 == 0 else "Perdida" if i % 3 == 1 else "En juego"
            )
            self.apuestasLayout.addWidget(apuestaWidget)
        '''

        self.mainLayout.addWidget(self.scrollArea)

        # Botón para volver
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
        self.mainLayout.addWidget(self.btnVolver)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def crearApuestaWidget(self, partido, fecha, hora, seleccion, monto, ganancia, estado):
        widget = QtWidgets.QWidget()
        widget.setStyleSheet("""
            background-color: #3a3a3a;
            border-radius: 10px;
            padding: 10px;
        """)
        layout = QtWidgets.QVBoxLayout(widget)

        # Contenedor para el contenido de la apuesta y el estado
        containerLayout = QtWidgets.QHBoxLayout()

        # Información de la apuesta
        infoLayout = QtWidgets.QVBoxLayout()

        lblPartido = QtWidgets.QLabel(f"Partido: {partido}")
        lblPartido.setStyleSheet("color: #ffcc00; font-size: 16px; font-weight: bold;")
        infoLayout.addWidget(lblPartido)

        lblFecha = QtWidgets.QLabel(f"Fecha: {fecha}")
        lblFecha.setStyleSheet("color: #ffffff; font-size: 14px;")
        infoLayout.addWidget(lblFecha)

        lblHora = QtWidgets.QLabel(f"Hora: {hora}")
        lblHora.setStyleSheet("color: #ffffff; font-size: 14px;")
        infoLayout.addWidget(lblHora)

        lblSeleccion = QtWidgets.QLabel(f"Selección: {seleccion}")
        lblSeleccion.setStyleSheet("color: #00ff00; font-size: 14px; font-weight: bold;")
        infoLayout.addWidget(lblSeleccion)

        lblMonto = QtWidgets.QLabel(f"Monto apostado: ${monto}")
        lblMonto.setStyleSheet("color: #ffffff; font-size: 14px;")
        infoLayout.addWidget(lblMonto)

        lblGanancia = QtWidgets.QLabel(f"Ganancia: ${ganancia}")
        lblGanancia.setStyleSheet("color: #00ff00; font-size: 14px; font-weight: bold;")
        infoLayout.addWidget(lblGanancia)

        # Añadir la información de la apuesta al layout principal
        containerLayout.addLayout(infoLayout)

        # Estado de la apuesta en la esquina superior derecha
        lblEstado = QtWidgets.QLabel(estado)
        lblEstado.setStyleSheet("""
            color: white;
            font-size: 12px;
            background-color: rgba(0, 0, 0, 0.6);
            padding: 5px;
            border-radius: 5px;
        """)
        lblEstado.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        containerLayout.addWidget(lblEstado, alignment=QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignRight)

        # Añadir el contenedor con el estado al widget principal
        layout.addLayout(containerLayout)

        return widget

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Historial de Apuestas")
