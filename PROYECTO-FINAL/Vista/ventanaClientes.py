# Programando el comportamiento de la ventana ventanaClientes.py
# y su comportamiento inicial

from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui

from Controlador.arregloClientes import ArregloClientes, cliente
# Creamos el objeto aCli el cual podrá usar todos los metodos de arregloClientes
aCli = ArregloClientes()


# QtGui-->utiliza los botones del formulario

class VentanaClientes(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        super(VentanaClientes, self).__init__(parent)
        uic.loadUi("UI/ventanaClientes.ui",self) #---> se debe colocar el nombre y ruta del formulario
        #self.show()

        # Eventos
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnQuitar.clicked.connect(self.quitar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnListar.clicked.connect(self.listar)
        self.Carga_Clientes()
    
    # Es necesario tener algunos metodos a partir de aqui

    def Carga_Clientes(self):
        if aCli.tamañoArregloCliente()==0:
            objCli= cliente('08693923','Alberto','Cordero','Zamorano','Jr. Quezada 221','4585985')
            aCli.adicionaCliente(objCli)
            objCli= cliente('08693923','Juan','Perez','Sanchez','Jr. Cuzco 123','3722754')
            aCli.adicionaCliente(objCli)
            objCli= cliente('08693923','Cesar','Cespedes','Ramos','Av. Peru 162','2752854')
            aCli.adicionaCliente(objCli)
            objCli= cliente('08693923','Roberto','Chambi','Rojas','Jr. Cuzco 222','5714764')
            aCli.adicionaCliente(objCli)
            self.listar()
        else:
            self.listar()

    def obtenerDni(self):
        return self.txtDni.text()
    
    def obtenerNombres(self):
        return self.txtNombres.text()

    def obtenerApellidoPaterno(self):
        return self.txtApellidoPaterno.text()

    def obtenerApellidoMaterno(self):
        return self.txtApellidoMaterno.text()

    def obtenerDireccion(self):
        return self.txtDireccion.text()

    def obtenerTelefono(self):
        return self.txtTelefono.text()

    def limpiarTabla(self):
        self.tblClientes.clearContents()
        self.tblClientes.setRowCount(0)

    def valida(self):
        if self.txtDni.text() =="":
            self.txtDni.setFocus()
            return "DNI del cliente...!!!"
        elif self.txtNombres.text()=="":
            self.txtNombres.setFocus()
            return "Nombre del cliente...!!!"
        elif self.txtApellidoPaterno.text()=="":
            self.txtApellidoPaterno.setFocus()
            return "Apellido Paterno del cliente...!!!"
        elif self.txtApellidoMaterno.text()=="":
            self.txtApellidoMaterno.setFocus()
            return "Apellido Mateno del cliente...!!!"
        elif self.txtDireccion.text()=="":
            self.txtDireccion.setFocus()
            return "Direccion del cliente...!!!"
        elif self.txtTelefono.text()=="":
            self.txtTelefono.setFocus()
            return "Telefono del cliente...!!!"
        else:
            return ""

    def listar(self):
        self.tblClientes.setRowCount(aCli.tamañoArregloCliente())
        self.tblClientes.setColumnCount(6)
        #Cabecera
        self.tblClientes.verticalHeader().setVisible(False)
        for i in range (0, aCli.tamañoArregloCliente()):
            self.tblClientes.setItem(i, 0, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getDniCliente()))
            self.tblClientes.setItem(i, 1, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getNombresCliente()))
            self.tblClientes.setItem(i, 2, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getApellidoPaternoCliente()))
            self.tblClientes.setItem(i, 3, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getApellidoMaternoCliente()))
            self.tblClientes.setItem(i, 4, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getDireccionCliente()))
            self.tblClientes.setItem(i, 5, QtWidgets.QTableWidgetItem(aCli.devolverCliente(i).getTelefonoCliente()))

    def limpiarControles(self):
        self.txtDni.clear()
        self.txtNombres.clear()
        self.txtApellidoPaterno.clear()
        self.txtApellidoMaterno.clear()
        self.txtDireccion.clear()
        self.txtTelefono.clear()

# Mantenimientos ( Grabar (Registrar), Consutar, Modificar, Listar, Quitar)

    def registrar(self):
        if self.valida() == "":
            objCli= cliente(self.obtenerDni(), self.obtenerNombres(),
                            self.obtenerApellidoPaterno(),
                            self.obtenerApellidoMaterno(),
                            self.obtenerDireccion(),
                            self.obtenerTelefono())
            dni=self.obtenerDni()
            if aCli.buscarCliente(dni) == -1:
                aCli.adicionaCliente(objCli)
                #aCli.grabar()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Cliente",
                                                  "El DNI ingresado ya existe... !!!",
                                                  QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Cliente",
                                                  "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)

    def consultar(self):
        #self.limpiarTabla()
        if aCli.tamañoArregloCliente() == 0:
                QtWidgets.QMessageBox.information(self, "Consultar Cliente",
                                                  "No existe clientes a consultar... !!!",
                                                  QtWidgets.QMessageBox.Ok)
        else:
            dni, _ = QtWidgets.QInputDialog.getText(self, "Consultar Cliente",
                                                  "Ingrese el DNI a consultar")
            pos = aCli.buscarCliente(dni)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Cliente",
                                                  "El DNI ingresado no existe... !!!",
                                                  QtWidgets.QMessageBox.Ok)
            else:
                self.txtDni.setText(aCli.devolverCliente(pos).getDniCliente())
                self.txtNombres.setText(aCli.devolverCliente(pos).getNombresCliente())
                self.txtApellidoPaterno.setText(aCli.devolverCliente(pos).getApellidoPaternoCliente())
                self.txtApellidoMaterno.setText(aCli.devolverCliente(pos).getApellidoMaternoCliente())
                self.txtDireccion.setText(aCli.devolverCliente(pos).getDireccionCliente())
                self.txtTelefono.setText(aCli.devolverCliente(pos).getTelefonoCliente())

                self.tblClientes.setRowCount(1)
                self.tblClientes.setItem(0,0, QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getDniCliente()))
                self.tblClientes.setItem(0,1, QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getNombresCliente()))
                self.tblClientes.setItem(0,2, QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getApellidoPaternoCliente()))
                self.tblClientes.setItem(0,3, QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getApellidoMaternoCliente()))
                self.tblClientes.setItem(0,4, QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getDireccionCliente()))
                self.tblClientes.setItem(0,5, QtWidgets.QTableWidgetItem(aCli.devolverCliente(pos).getTelefonoCliente()))
    
    def eliminar(self):
        if self.obtenerDni() == "":
            QtWidgets.QMessageBox.information(self, "Consulte Cliente",
                                              "Por favor Consultar el dni",
                                              QtWidgets.QMessageBox.Ok)
        else:
            dni = self.txtDni.text()
            pos = aCli.buscarCliente(dni)
            aCli.eliminarCliente(pos)
            #aCli.grabar()
            self.limpiarControles()
            self.listar()

    def quitar(self):
        if aCli.tamañoArregloCliente() ==0:
            QtWidgets.QMessageBox.information(self, "Eliminar Cliente",
                                              "No existe clientes a eliminar... !!!",
                                              QtWidgets.QMessageBox.Ok)
        else:
            fila=self.tblClientes.selectedItems()
            if fila:
                indiceFila=fila[0].row()
                dni=self.tblClientes.item(indiceFila, 0).text()
                pos =aCli.buscarCliente(dni)
                aCli.eliminarCliente(pos)
                self.limpiarTabla()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Cliente",
                                                  "Debe seleccionar una fila... !!!",
                                                  QtWidgets.QMessageBox.Ok)
                
    def modificar(self):
        if aCli.tamañoArregloCliente() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Cliente",
                                                  "No existen clientes a Modificar... !!!",
						                          QtWidgets.QMessageBox.Ok)
        else:
            dni= self.obtenerDni()
            pos= aCli.buscarCliente(dni)
            if pos != -1:
                objCli= cliente(self.obtenerDni(), self.obtenerNombres(),
                                 self.obtenerApellidoPaterno(),
                                 self.obtenerApellidoMaterno(),
                                 self.obtenerDireccion(),self.obtenerTelefono())
                aCli.modificarCliente(objCli, pos)
                #aCli.grabar()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Modificar Cliente",
                                                      "El DNI ingresado no existe... !!!",
                                                      QtWidgets.QMessageBox.Ok)
