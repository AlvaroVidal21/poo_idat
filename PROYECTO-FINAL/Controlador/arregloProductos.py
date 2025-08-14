from Controlador.productos import producto
import csv
import os

# Mantenimiento para los productos

class ArregloProductos:
    CAMPOS = [
        "codigo",
        "nombre",
        "descripcion",
        "stock_minimo",
        "stock_actual",
        "precio_costo",
        "precio_venta",
        "proveedor",
        "almacen",
    ]

    def __init__(self):
        self.__archivo = os.path.join(os.path.dirname(__file__), 'productos.csv')
        self.dataProducto = []  # <-- Nuestra base de datos en memoria
        self.cargar()

    # ---------------------------
    # Métodos de persistencia
    # ---------------------------
    def cargar(self):
        """Carga los datos desde el archivo CSV, creándolo si no existe."""
        if not os.path.exists(self.__archivo):
            with open(self.__archivo, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=self.CAMPOS)
                writer.writeheader()
            return

        with open(self.__archivo, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row:
                    self.dataProducto.append(producto.from_dict(row))

    def grabar(self):
        with open(self.__archivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.CAMPOS)
            writer.writeheader()
            for pro in self.dataProducto:
                writer.writerow(pro.to_dict())

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

