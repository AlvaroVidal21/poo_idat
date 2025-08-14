# Programando el comportamiento de la ventana ventanaProductos.py
# y su comportamiento inicial

from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui

# QtGui-->utiliza los botones del formulario

class VentanaProductos(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        super(VentanaProductos, self).__init__(parent)
        uic.loadUi("UI/ventanaProductos.ui",self) #---> se debe colocar el nombre y ruta del formulario
        #self.show()