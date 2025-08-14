# Programando el comportamiento de la ventana ventanaEmpleador.py
# y su comportamiento inicial

from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui

# QtGui-->utiliza los botones del formulario

class VentanaEmpleados(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        super(VentanaEmpleados, self).__init__(parent)
        uic.loadUi("UI/ventanaEmpleados.ui",self) #---> se debe colocar el nombre y ruta del formulario
        #self.show()