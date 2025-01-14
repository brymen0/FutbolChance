from PyQt6.QtWidgets import QApplication
from controller.ControllerEventosDeportivos import ControllerEventosDeportivos

if __name__ == "__main__":
    app = QApplication([])
    mi_app = ControllerEventosDeportivos()
    mi_app.show()
    app.exec()