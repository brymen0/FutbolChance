from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_ApuestasApp(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 650)
        MainWindow.setStyleSheet("background-color: #1e1e1e;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Layout principal
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setContentsMargins(10, 10, 10, 10)
        self.mainLayout.setSpacing(10)

        # Título FutbolChance
        self.lblTitulo = QtWidgets.QLabel("FutbolChance")
        self.lblTitulo.setStyleSheet("""
            color: #ffcc00;
            font-size: 24px;
            font-weight: bold;
            text-align: center;
        """)
        self.lblTitulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mainLayout.addWidget(self.lblTitulo)

        # Saldo con botón de recarga
        saldoLayout = QtWidgets.QHBoxLayout()
        self.btnSaldo = QtWidgets.QPushButton("Saldo: $50.00")
        self.btnSaldo.setStyleSheet("""
            QPushButton {
                color: #ffffff;
                background-color: #ffcc00;
                border: none;
                padding: 5px 10px;
                border-radius: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #f5a623;
            }
        """)
        saldoLayout.addWidget(self.btnSaldo)

        self.btnRecargar = QtWidgets.QPushButton("Recargar")
        self.btnRecargar.setStyleSheet("""
            QPushButton {
                color: #ffffff;
                background-color: #0078d7;
                border: none;
                padding: 5px 10px;
                border-radius: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005bb5;
            }
        """)
        saldoLayout.addWidget(self.btnRecargar)
        self.mainLayout.addLayout(saldoLayout)

        # Navegación superior
        self.navLayout = QtWidgets.QHBoxLayout()
        self.navLayout.setSpacing(10)

        for option in ["Mi cuenta", "Bonos", "Apuestas", "Eventos deportivos"]:
            btnOption = self.create_nav_button(option)
            btnOption.setObjectName(f"btn{option}")
            self.navLayout.addWidget(btnOption)

        # Cerrar sesión como botón con icono
        self.btnCerrarSesion = QtWidgets.QPushButton()
        self.btnCerrarSesion.setIcon(QtGui.QIcon("../resources/cerrar_sesion.png"))  # Ruta de la imagen
        self.btnCerrarSesion.setIconSize(QtCore.QSize(24, 24))  # Tamaño del icono
        self.btnCerrarSesion.setStyleSheet("""
    QPushButton {
        color: #ffffff;
        background-color: #444444;
        border: none;
        padding: 8px;
        border-radius: 5px;
        font-size: 12px;
    }
    QPushButton:hover {
        background-color: #666666;
    }
""")

        self.navLayout.addWidget(self.btnCerrarSesion)


        self.mainLayout.addLayout(self.navLayout)

        # Contenedor de eventos deportivos
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setStyleSheet("background-color: #2e2e2e; border: none;")
        self.scrollContent = QtWidgets.QWidget()
        self.scrollContent.setGeometry(QtCore.QRect(0, 0, 380, 600))

        self.eventsLayout = QtWidgets.QVBoxLayout(self.scrollContent)

        '''
        # Crear eventos de ejemplo
        for i in range(5):  # Ejemplo con 5 eventos
            self.add_event_widget(
                f"Liga España", "España",
                f"Equipo {i+1} vs Equipo {i+2}",
                "1.8", "3.0", "2.5",
                "../resources/futbol.png",  # Imagen llamada futbol.png
                f"Jornada {i+1}",  # Instancia de campeonato
                i+1
            )
        '''
        self.scrollArea.setWidget(self.scrollContent)
        self.mainLayout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def create_nav_button(self, text):
        """Crea un botón de navegación."""
        button = QtWidgets.QPushButton(text)
        button.setStyleSheet("""
            QPushButton {
                color: #ffffff;
                background-color: #444444;
                border: none;
                padding: 8px 12px;
                border-radius: 5px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #666666;
            }
        """)
        return button

    def add_event_widget(self, league, country, match, odds1, oddsDraw, odds2, image_path, instance,event_id):
        """Agrega un evento deportivo en un bloque estilo móvil."""
        eventWidget = QtWidgets.QWidget()
        eventWidget.setStyleSheet("""
            background-color: #3e3e3e;
            border-radius: 10px;
            padding: 5px;
        """)
        eventLayout = QtWidgets.QVBoxLayout(eventWidget)
        eventLayout.setSpacing(5)  # Reducir el espaciado

        # Crear una layout horizontal para la imagen y el texto del partido
        topLayout = QtWidgets.QHBoxLayout()

        # Imagen del deporte (tamaño 24x24px, alineada a la izquierda)
        imgLabel = QtWidgets.QLabel()
        imgLabel.setPixmap(QtGui.QPixmap(image_path).scaled(24, 24, QtCore.Qt.AspectRatioMode.KeepAspectRatio))
        imgLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        topLayout.addWidget(imgLabel)

        # Agregar la layout de la imagen
        eventLayout.addLayout(topLayout)

        # Liga y país (centrados, en líneas separadas)
        lblLeague = QtWidgets.QLabel(league)
        lblLeague.setStyleSheet("color: #ffffff; font-size: 14px; font-weight: bold;")
        lblLeague.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        eventLayout.addWidget(lblLeague)

        lblCountry = QtWidgets.QLabel(country)
        lblCountry.setStyleSheet("color: #ffffff; font-size: 12px;")
        lblCountry.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        eventLayout.addWidget(lblCountry)

        # Instancia o jornada del campeonato (más grande)
        lblInstance = QtWidgets.QLabel(instance)
        lblInstance.setStyleSheet("color: #ffffff; font-size: 16px; font-weight: bold;")
        lblInstance.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        eventLayout.addWidget(lblInstance)

        # Equipos enfrentándose
        lblMatch = QtWidgets.QLabel(match)
        lblMatch.setStyleSheet("color: #ffcc00; font-size: 16px; font-weight: bold;")
        lblMatch.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        eventLayout.addWidget(lblMatch)

        # Botones de apuestas
        oddsLayout = QtWidgets.QHBoxLayout()

        # Crear botones con objectName único basado en el event_id
        btnTeam1 = self.create_odds_button(f"Gana 1 ({odds1}x)")
        btnTeam1.setObjectName(f"btn{event_id}_gana1")  # Asignar nombre único
        oddsLayout.addWidget(btnTeam1)

        btnDraw = self.create_odds_button(f"Empate ({oddsDraw}x)")
        btnDraw.setObjectName(f"btn{event_id}_empate")  # Asignar nombre único
        oddsLayout.addWidget(btnDraw)

        btnTeam2 = self.create_odds_button(f"Gana 2 ({odds2}x)")
        btnTeam2.setObjectName(f"btn{event_id}_gana2")  # Asignar nombre único
        oddsLayout.addWidget(btnTeam2)

        eventLayout.addLayout(oddsLayout)
        self.eventsLayout.addWidget(eventWidget)

    def create_odds_button(self, text):
        """Crea un botón de cuota."""
        button = QtWidgets.QPushButton(text)
        button.setStyleSheet("""
            QPushButton {
                color: #ffffff;
                background-color: #0078d7;
                border: none;
                padding: 8px;
                border-radius: 5px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #005bb5;
            }
        """)
        return button

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("FutbolChance")
