# Programando el comportamiento de la ventana ventanaEmpleados.py
# y su comportamiento inicial

from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui

from Controlador.arregloEmpleados import ArregloEmpleados, empleado
# Creamos el objeto aEmp el cual podrá usar todos los metodos de arregloEmpleados
aEmp = ArregloEmpleados()


# QtGui-->utiliza los botones del formulario

class VentanaEmpleados(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        super(VentanaEmpleados, self).__init__(parent)
        uic.loadUi("UI/ventanaEmpleados.ui",self) #---> se debe colocar el nombre y ruta del formulario
        #self.show()

        # Eventos
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnQuitar.clicked.connect(self.quitar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnListar.clicked.connect(self.listar)
        self.Carga_Empleados()

    # Es necesario tener algunos metodos a partir de aqui

    def Carga_Empleados(self):
        if aEmp.tamañoArregloEmpleado()==0:
            objEmp= empleado('08693923','Alberto','Cordero','Zamorano','Jr. Quezada 221','4585985')
            aEmp.adicionaEmpleado(objEmp)
            objEmp= empleado('08693923','Juan','Perez','Sanchez','Jr. Cuzco 123','3722754')
            aEmp.adicionaEmpleado(objEmp)
            objEmp= empleado('08693923','Cesar','Cespedes','Ramos','Av. Peru 162','2752854')
            aEmp.adicionaEmpleado(objEmp)
            objEmp= empleado('08693923','Roberto','Chambi','Rojas','Jr. Cuzco 222','5714764')
            aEmp.adicionaEmpleado(objEmp)
            self.listar()
        else:
            self.listar()

    def obtenerDni(self):
        return self.txtDni.text()

    def obtenerNombres(self):
        return self.txtNombre.text()

    def obtenerApellidoPaterno(self):
        return self.txtApellidoPaterno.text()

    def obtenerApellidoMaterno(self):
        return self.txtApellidoMaterno.text()

    def obtenerDireccion(self):
        return self.txtDireccion.text()

    def obtenerTelefono(self):
        return self.txtTelefono.text()

    def limpiarTabla(self):
        self.tblEmpleados.clearContents()
        self.tblEmpleados.setRowCount(0)

    def valida(self):
        if self.txtDni.text() =="":
            self.txtDni.setfocus()
            return "DNI del empleado...!!!"
        elif self.txtNombre.text()=="":
            self.txtNombre.setfocus()
            return "Nombre del empleado...!!!"
        elif self.txtApellidoPaterno.text()=="":
            self.txtApellidoPaterno.setfocus()
            return "Apellido Paterno del empleado...!!!"
        elif self.txtApellidoMaterno.text()=="":
            self.txtApellidoMaterno.setfocus()
            return "Apellido Mateno del empleado...!!!"
        elif self.txtDireccion.text()=="":
            self.txtDireccion.setfocus()
            return "Direccion del empleado...!!!"
        elif self.txtTelefono.text()=="":
            self.txtTelefono.setfocus()
            return "Telefono del empleado...!!!"
        else:
            return ""

    def listar(self):
        self.tblEmpleados.setRowCount(aEmp.tamañoArregloEmpleado())
        self.tblEmpleados.setColumnCount(6)
        #Cabecera
        self.tblEmpleados.verticalHeader().setVisible(False)
        for i in range (0, aEmp.tamañoArregloEmpleado()):
            self.tblEmpleados.setItem(i, 0, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getDniEmpleado()))
            self.tblEmpleados.setItem(i, 1, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getNombresEmpleado()))
            self.tblEmpleados.setItem(i, 2, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getApellidoPaternoEmpleado()))
            self.tblEmpleados.setItem(i, 3, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getApellidoMaternoEmpleado()))
            self.tblEmpleados.setItem(i, 4, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getDireccionEmpleado()))
            self.tblEmpleados.setItem(i, 5, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(i).getTelefonoEmpleado()))

    def limpiarControles(self):
        self.txtDni.clear()
        self.txtNombre.clear()
        self.txtApellidoPaterno.clear()
        self.txtApellidoMaterno.clear()
        self.txtDireccion.clear()
        self.txtTelefono.clear()

# Mantenimientos ( Grabar (Registrar), Consutar, Modificar, Listar, Quitar)

    def registrar(self):
        if self.valida() == "":
            objEmp= empleado(self.obtenerDni(), self.obtenerNombres(),
                            self.obtenerApellidoPaterno(),
                            self.obtenerApellidoMaterno(),
                            self.obtenerDireccion(),
                            self.obtenerTelefono())
            dni=self.obtenerDni()
            if aEmp.buscarEmpleado(dni) == -1:
                aEmp.adicionaEmpleado(objEmp)
                #aEmp.grabar()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Empleado",
                                                  "El DNI ingresado ya existe... !!!",
                                                  QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Empleado",
                                                  "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)

    def consultar(self):
        #self.limpiarTabla()
        if aEmp.tamañoArregloEmpleado() == 0:
                QtWidgets.QMessageBox.information(self, "Consultar Empleado",
                                                  "No existe empleados a consultar... !!!",
                                                  QtWidgets.QMessageBox.Ok)
        else:
            dni, _ = QtWidgets.QInputDialog.getText(self, "Consultar Empleado",
                                                  "Ingrese el DNI a consultar")
            pos = aEmp.buscarEmpleado(dni)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Empleado",
                                                  "El DNI ingresado no existe... !!!",
                                                  QtWidgets.QMessageBox.Ok)
            else:
                self.txtDni.setText(aEmp.devolverEmpleado(pos).getDniEmpleado())
                self.txtNombre.setText(aEmp.devolverEmpleado(pos).getNombresEmpleado())
                self.txtApellidoPaterno.setText(aEmp.devolverEmpleado(pos).getApellidoPaternoEmpleado())
                self.txtApellidoMaterno.setText(aEmp.devolverEmpleado(pos).getApellidoMaternoEmpleado())
                self.txtDireccion.setText(aEmp.devolverEmpleado(pos).getDireccionEmpleado())
                self.txtTelefono.setText(aEmp.devolverEmpleado(pos).getTelefonoEmpleado())

                self.tblEmpleados.setRowCount(1)
                self.tblEmpleados.setItem(0,0, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(pos).getDniEmpleado()))
                self.tblEmpleados.setItem(0,1, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(pos).getNombresEmpleado()))
                self.tblEmpleados.setItem(0,2, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(pos).getApellidoPaternoEmpleado()))
                self.tblEmpleados.setItem(0,3, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(pos).getApellidoMaternoEmpleado()))
                self.tblEmpleados.setItem(0,4, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(pos).getDireccionEmpleado()))
                self.tblEmpleados.setItem(0,5, QtWidgets.QTableWidgetItem(aEmp.devolverEmpleado(pos).getTelefonoEmpleado()))

    def eliminar(self):
        if self.obtenerDni() == "":
            QtWidgets.QMessageBox.information(self, "Consulte Empleado",
                                              "Por favor Consultar el dni",
                                              QtWidgets.QMessageBox.Ok)
        else:
            dni = self.txtDni.text()
            pos = aEmp.buscarEmpleado(dni)
            aEmp.eliminarEmpleado(pos)
            #aEmp.grabar()
            self.limpiarControles()
            self.listar()

    def quitar(self):
        if aEmp.tamañoArregloEmpleado() ==0:
            QtWidgets.QMessageBox.information(self, "Eliminar Empleado",
                                              "No existe empleados a eliminar... !!!",
                                              QtWidgets.QMessageBox.Ok)
        else:
            fila=self.tblEmpleados.selectedItems()
            if fila:
                indiceFila=fila[0].row()
                dni=self.tblEmpleados.item(indiceFila, 0).text()
                pos =aEmp.buscarEmpleado(dni)
                aEmp.eliminarEmpleado(pos)
                self.limpiarTabla()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Empleado",
                                                  "Debe seleccionar una fila... !!!",
                                                  QtWidgets.QMessageBox.Ok)

    def modificar(self):
        if aEmp.tamañoArregloEmpleado() == 0:
            QtWidgets.QMessageBox.information(self, "Modificar Empleado",
                                                  "No existen empleados a Modificar... !!!",
                                                                          QtWidgets.QMessageBox.Ok)
        else:
            dni= self.obtenerDni()
            pos= aEmp.buscarEmpleado(dni)
            if pos != -1:
                objEmp= empleado(self.obtenerDni(), self.obtenerNombres(),
                                 self.obtenerApellidoPaterno(),
                                 self.obtenerApellidoMaterno(),
                                 self.obtenerDireccion(),self.obtenerTelefono())
                aEmp.modificarEmpleado(objEmp, pos)
                #aEmp.grabar()
                self.limpiarControles()
                self.listar()

