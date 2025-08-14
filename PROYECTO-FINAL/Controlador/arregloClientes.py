from Controlador.clientes import cliente
import csv
import os

#Mantenimiento para los clientes

class ArregloClientes:

    def __init__(self):
        # ruta del archivo csv donde se almacenarán los datos
        self.__archivo = os.path.join(os.path.dirname(__file__), 'clientes.csv')
        self.dataCliente = []  # <-- Nuestra base de datos en memoria
        self.cargar()  # Cargar datos existentes del archivo

    # ---------------------------
    # Métodos de persistencia
    # ---------------------------
    def cargar(self):
        """Carga los datos desde el archivo CSV."""
        if os.path.exists(self.__archivo):
            with open(self.__archivo, newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    if row:  # evitar filas vacías
                        obj = cliente(*row)
                        self.dataCliente.append(obj)

    def grabar(self):
        """Guarda los datos actuales en el archivo CSV."""
        with open(self.__archivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for cli in self.dataCliente:
                writer.writerow([
                    cli.getDniCliente(),
                    cli.getNombresCliente(),
                    cli.getApellidoPaternoCliente(),
                    cli.getApellidoMaternoCliente(),
                    cli.getDireccionCliente(),
                    cli.getTelefonoCliente(),
                ])

    # ---------------------------
    # Métodos de gestión
    # ---------------------------
    def adicionaCliente(self, objcli):  # Graba los datos de los clientes
        self.dataCliente.append(objcli)
        self.grabar()

    def devolverCliente(self, pos):  # Retorna los datos de los clientes
        return self.dataCliente[pos]

    def tamañoArregloCliente(self):  # Devuelve los datos de los clientes
        return len(self.dataCliente)

    def buscarCliente(self, dni):  # Busca los clientes por dni
        for i in range(self.tamañoArregloCliente()):
            if dni == self.dataCliente[i].getDniCliente():
                return i  # devuelve la posicion del elemento encontrado
        return -1  # signfica que no encontro ningun dato

    def eliminarCliente(self, pos):  # Elimina los clientes
        del (self.dataCliente[pos])
        self.grabar()

    def modificarCliente(self, objcli, pos):  # Modifica datos de los clientes
        self.dataCliente[pos] = objcli
        self.grabar()

    def retornarDatos(self):  # retorna los datos de los clientes
        return self.dataCliente

    
            
