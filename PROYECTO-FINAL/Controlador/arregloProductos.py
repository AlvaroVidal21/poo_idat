from Controlador.productos import producto
# Mantenimiento para los productos

class ArregloProductos():

    # Atributo
    dataProducto = []  # <-- Nuestra base de datos

    # Constructor (vacío)
    def __init__(self):
        pass

    def adicionaProducto(self, objpro):  # Graba los datos de los productos
        self.dataProducto.append(objpro)

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

    def modificarProducto(self, objpro, pos):  # Modifica datos de los productos
        self.dataProducto[pos] = objpro

    def retornarDatos(self):  # retorna los datos de los productos
        return self.dataProducto

