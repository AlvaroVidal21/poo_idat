from Controlador.productos import producto
import csv
import os

# Mantenimiento para los productos

class ArregloProductos:

    def __init__(self):
        self.__archivo = os.path.join(os.path.dirname(__file__), 'productos.csv')
        self.dataProducto = []  # <-- Nuestra base de datos en memoria
        self.cargar()

    # ---------------------------
    # Métodos de persistencia
    # ---------------------------
    def cargar(self):
        if os.path.exists(self.__archivo):
            with open(self.__archivo, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    if row:
                        self.dataProducto.append(producto(*row))

    def grabar(self):
        with open(self.__archivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for pro in self.dataProducto:
                writer.writerow([
                    pro.getCodigoProducto(),
                    pro.getNombreProducto(),
                    pro.getDescripcionProducto(),
                    pro.getStockMinimoProducto(),
                    pro.getStockActualProducto(),
                    pro.getPrecioCostoProducto(),
                    pro.getPrecioVentaProducto(),
                    pro.getProveedorProducto(),
                    pro.getAlmacenProducto(),
                ])

    # ---------------------------
    # Métodos de gestión
    # ---------------------------
    def adicionaProducto(self, objpro):  # Graba los datos de los productos
        self.dataProducto.append(objpro)
        self.grabar()

    def devolverProducto(self, pos):  # Retorna los datos de los productos
        return self.dataProducto[pos]

    def tamañoArregloProducto(self):  # Devuelve los datos de los productos
        return len(self.dataProducto)

    def buscarProducto(self, codigo):  # Busca los productos por código
        for i in range(self.tamañoArregloProducto()):
            if codigo == self.dataProducto[i].getCodigoProducto():
                return i  # devuelve la posición del elemento encontrado
        return -1  # significa que no encontró ningún dato

    def eliminarProducto(self, pos):  # Elimina los productos
        del (self.dataProducto[pos])
        self.grabar()

    def modificarProducto(self, objpro, pos):  # Modifica datos de los productos
        self.dataProducto[pos] = objpro
        self.grabar()

    def retornarDatos(self):  # retorna los datos de los productos
        return self.dataProducto

