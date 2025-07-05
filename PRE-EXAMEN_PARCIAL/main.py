
import sys
from PyQt5.QtWidgets import QApplication
from CONTROLADOR.app import ControladorApp

# Lanzador
if __name__ == '__main__':
    app = QApplication(sys.argv)
    controlador = ControladorApp()
    sys.exit(app.exec_())

