# Programando el comportamiento de la ventana ventanaPrincipal.py
# y su comportamiento inicial

from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui

from Vista.ventanaClientes import VentanaClientes
from Vista.ventanaEmpleados import VentanaEmpleados
from Vista.ventanaProductos import VentanaProductos


# QtGui-->utiliza los botones del formulario

class VentanaPrincipal(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        super(VentanaPrincipal, self).__init__(parent)
        uic.loadUi("UI/ventanaPrincipal.ui",self) #---> se debe colocar el nombre y ruta del formulario
        #self.show()

    # Eventos
        self.btnClientes.clicked.connect(self.abrirVentanaClientes)
        self.btnEmpleados.clicked.connect(self.abrirVentanaEmpleados)
        self.btnProductos.clicked.connect(self.abrirVentanaProductos)
        self.btnSalir.clicked.connect(self.cerrar)
    
    def abrirVentanaClientes(self):
        vclientes = VentanaClientes(self)
        vclientes.show()
    
    def abrirVentanaEmpleados(self):
        vempleados = VentanaEmpleados(self)
        vempleados.show()
    
    def abrirVentanaProductos(self):
        vproductos = VentanaProductos(self)
        vproductos.show()
    
    def cerrar(self):
        self.close()
