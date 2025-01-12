from PyQt6.QtWidgets import QApplication
from controller.ControllerMain import ControllerMain


if __name__ == "__main__":
    app = QApplication([])
    mi_app = ControllerMain()
    mi_app.show()
    app.exec()