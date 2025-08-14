# Programando el comportamiento de la ventana ventanaProductos.py
# y su comportamiento inicial

from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui

from Controlador.arregloProductos import ArregloProductos, producto
# Creamos el objeto aPro el cual podrá usar todos los metodos de arregloProductos
aPro = ArregloProductos()


# QtGui-->utiliza los botones del formulario

class VentanaProductos(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        super(VentanaProductos, self).__init__(parent)
        uic.loadUi("UI/ventanaProductos.ui",self) #---> se debe colocar el nombre y ruta del formulario
        #self.show()

        # Eventos
        self.btnRegistrar.clicked.connect(self.registrar)
        self.btnConsultar.clicked.connect(self.consultar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnQuitar.clicked.connect(self.quitar)
        self.btnModificar.clicked.connect(self.modificar)
        self.btnListar.clicked.connect(self.listar)
        self.Carga_Productos()

    # Es necesario tener algunos metodos a partir de aqui

    def Carga_Productos(self):
        if aPro.tamañoArregloProducto()==0:
            objPro= producto('001','Leche','Entera','10','50','2.50','3.50','Gloria','Lacteos')
            aPro.adicionaProducto(objPro)
            objPro= producto('002','Pan','Molde','5','30','1.00','1.50','Nicolini','Trigos')
            aPro.adicionaProducto(objPro)
            objPro= producto('003','Fideos','Tornillo','7','40','2.00','2.80','Alicorp','Trigos')
            aPro.adicionaProducto(objPro)
            objPro= producto('004','Jugo','Naranja','8','60','1.50','2.20','AJE','Frutas')
            aPro.adicionaProducto(objPro)
            self.listar()
        else:
            self.listar()

    def obtenerCodigo(self):
        return self.txtCodigo.text()

    def obtenerNombre(self):
        return self.txtNombre.text()

    def obtenerDescripcion(self):
        return self.txtDescripcion.text()

    def obtenerStockMinimo(self):
        return self.txtStockMinimo.text()

    def obtenerStockActual(self):
        return self.txtStockActual.text()

    def obtenerPrecioCosto(self):
        return self.txtPrecioCosto.text()

    def obtenerPrecioVenta(self):
        return self.txtPrecioVenta.text()

    def obtenerProveedor(self):
        return self.cboProveedor.currentText()

    def obtenerAlmacen(self):
        return self.cboAlmacen.currentText()

    def limpiarTabla(self):
        self.tblProductos.clearContents()
        self.tblProductos.setRowCount(0)

    def valida(self):
        if self.txtCodigo.text()=="":
            self.txtCodigo.setfocus()
            return "Codigo del producto...!!!"
        elif self.txtNombre.text()=="":
            self.txtNombre.setfocus()
            return "Nombre del producto...!!!"
        elif self.txtDescripcion.text()=="":
            self.txtDescripcion.setfocus()
            return "Descripcion del producto...!!!"
        elif self.txtStockMinimo.text()=="":
            self.txtStockMinimo.setfocus()
            return "Stock Minimo del producto...!!!"
        elif self.txtStockActual.text()=="":
            self.txtStockActual.setfocus()
            return "Stock Actual del producto...!!!"
        elif self.txtPrecioCosto.text()=="":
            self.txtPrecioCosto.setfocus()
            return "Precio Costo del producto...!!!"
        elif self.txtPrecioVenta.text()=="":
            self.txtPrecioVenta.setfocus()
            return "Precio Venta del producto...!!!"
        elif self.cboProveedor.currentIndex()==0:
            self.cboProveedor.setfocus()
            return "Proveedor del producto...!!!"
        elif self.cboAlmacen.currentIndex()==0:
            self.cboAlmacen.setfocus()
            return "Almacen del producto...!!!"
        else:
            return ""

    def listar(self):
        self.tblProductos.setRowCount(aPro.tamañoArregloProducto())
        self.tblProductos.setColumnCount(9)
        #Cabecera
        self.tblProductos.verticalHeader().setVisible(False)
        for i in range(0, aPro.tamañoArregloProducto()):
            self.tblProductos.setItem(i,0, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getCodigoProducto()))
            self.tblProductos.setItem(i,1, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getNombreProducto()))
            self.tblProductos.setItem(i,2, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getDescripcionProducto()))
            self.tblProductos.setItem(i,3, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getStockMinimoProducto()))
            self.tblProductos.setItem(i,4, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getStockActualProducto()))
            self.tblProductos.setItem(i,5, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getPrecioCostoProducto()))
            self.tblProductos.setItem(i,6, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getPrecioVentaProducto()))
            self.tblProductos.setItem(i,7, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getProveedorProducto()))
            self.tblProductos.setItem(i,8, QtWidgets.QTableWidgetItem(aPro.devolverProducto(i).getAlmacenProducto()))

    def limpiarControles(self):
        self.txtCodigo.clear()
        self.txtNombre.clear()
        self.txtDescripcion.clear()
        self.txtStockMinimo.clear()
        self.txtStockActual.clear()
        self.txtPrecioCosto.clear()
        self.txtPrecioVenta.clear()
        self.cboProveedor.setCurrentIndex(0)
        self.cboAlmacen.setCurrentIndex(0)

# Mantenimientos ( Grabar (Registrar), Consutar, Modificar, Listar, Quitar)

    def registrar(self):
        if self.valida()=="":
            objPro = producto(self.obtenerCodigo(), self.obtenerNombre(),
                              self.obtenerDescripcion(),
                              self.obtenerStockMinimo(),
                              self.obtenerStockActual(),
                              self.obtenerPrecioCosto(),
                              self.obtenerPrecioVenta(),
                              self.obtenerProveedor(),
                              self.obtenerAlmacen())
            cod = self.obtenerCodigo()
            if aPro.buscarProducto(cod) == -1:
                aPro.adicionaProducto(objPro)
                #aPro.grabar()
                self.limpiarControles()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Registrar Producto",
                                                  "El Codigo ingresado ya existe... !!!",
                                                  QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Producto",
                                                  "Error en " + self.valida(), QtWidgets.QMessageBox.Ok)

    def consultar(self):
        if aPro.tamañoArregloProducto()==0:
            QtWidgets.QMessageBox.information(self, "Consultar Producto",
                                              "No existe productos a consultar... !!!",
                                              QtWidgets.QMessageBox.Ok)
        else:
            cod, _ = QtWidgets.QInputDialog.getText(self, "Consultar Producto",
                                                    "Ingrese el Codigo a consultar")
            pos = aPro.buscarProducto(cod)
            if pos == -1:
                QtWidgets.QMessageBox.information(self, "Consultar Producto",
                                                  "El Codigo ingresado no existe... !!!",
                                                  QtWidgets.QMessageBox.Ok)
            else:
                self.txtCodigo.setText(aPro.devolverProducto(pos).getCodigoProducto())
                self.txtNombre.setText(aPro.devolverProducto(pos).getNombreProducto())
                self.txtDescripcion.setText(aPro.devolverProducto(pos).getDescripcionProducto())
                self.txtStockMinimo.setText(aPro.devolverProducto(pos).getStockMinimoProducto())
                self.txtStockActual.setText(aPro.devolverProducto(pos).getStockActualProducto())
                self.txtPrecioCosto.setText(aPro.devolverProducto(pos).getPrecioCostoProducto())
                self.txtPrecioVenta.setText(aPro.devolverProducto(pos).getPrecioVentaProducto())
                self.cboProveedor.setCurrentText(aPro.devolverProducto(pos).getProveedorProducto())
                self.cboAlmacen.setCurrentText(aPro.devolverProducto(pos).getAlmacenProducto())

                self.tblProductos.setRowCount(1)
                self.tblProductos.setItem(0,0, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getCodigoProducto()))
                self.tblProductos.setItem(0,1, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getNombreProducto()))
                self.tblProductos.setItem(0,2, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getDescripcionProducto()))
                self.tblProductos.setItem(0,3, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getStockMinimoProducto()))
                self.tblProductos.setItem(0,4, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getStockActualProducto()))
                self.tblProductos.setItem(0,5, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getPrecioCostoProducto()))
                self.tblProductos.setItem(0,6, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getPrecioVentaProducto()))
                self.tblProductos.setItem(0,7, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getProveedorProducto()))
                self.tblProductos.setItem(0,8, QtWidgets.QTableWidgetItem(aPro.devolverProducto(pos).getAlmacenProducto()))

    def eliminar(self):
        if self.obtenerCodigo()=="":
            QtWidgets.QMessageBox.information(self, "Consulte Producto",
                                              "Por favor Consultar el codigo",
                                              QtWidgets.QMessageBox.Ok)
        else:
            cod = self.txtCodigo.text()
            pos = aPro.buscarProducto(cod)
            aPro.eliminarProducto(pos)
            #aPro.grabar()
            self.limpiarControles()
            self.listar()

    def quitar(self):
        if aPro.tamañoArregloProducto()==0:
            QtWidgets.QMessageBox.information(self, "Eliminar Producto",
                                              "No existe productos a eliminar... !!!",
                                              QtWidgets.QMessageBox.Ok)
        else:
            fila = self.tblProductos.selectedItems()
            if fila:
                indiceFila = fila[0].row()
                cod = self.tblProductos.item(indiceFila,0).text()
                pos = aPro.buscarProducto(cod)
                aPro.eliminarProducto(pos)
                self.limpiarTabla()
                self.listar()
            else:
                QtWidgets.QMessageBox.information(self, "Eliminar Producto",
                                                  "Debe seleccionar una fila... !!!",
                                                  QtWidgets.QMessageBox.Ok)

    def modificar(self):
        if aPro.tamañoArregloProducto()==0:
            QtWidgets.QMessageBox.information(self, "Modificar Producto",
                                              "No existen productos a Modificar... !!!",
                                              QtWidgets.QMessageBox.Ok)
        else:
            cod = self.obtenerCodigo()
            pos = aPro.buscarProducto(cod)
            if pos != -1:
                objPro = producto(self.obtenerCodigo(), self.obtenerNombre(),
                                  self.obtenerDescripcion(),
                                  self.obtenerStockMinimo(),
                                  self.obtenerStockActual(),
                                  self.obtenerPrecioCosto(),
                                  self.obtenerPrecioVenta(),
                                  self.obtenerProveedor(),
                                  self.obtenerAlmacen())
                aPro.modificarProducto(objPro, pos)
                #aPro.grabar()
                self.limpiarControles()
                self.listar()

