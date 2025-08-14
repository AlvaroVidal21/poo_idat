from Controlador.clientes import cliente
#Mantenimiento para los clientes

class ArregloClientes():

    #Atributo
    dataCliente = [] #<-- Nuestra base de datos

    #Constructor (vacio)
    def __init__(self):
        pass

    def adicionaCliente(self,objcli): # Graba los datos de los clientes
        self.dataCliente.append(objcli)

    def devolverCliente(self, pos): # Retorna los datos de los clientes
        return self.dataCliente[pos]

    def tamañoArregloCliente(self): # Devuelve los datos de los clientes
        return len(self.dataCliente)

    def buscarCliente(self, dni): # Busca los clientes por dni
        for i in range (self.tamañoArregloCliente()):
            if dni == self.dataCliente[i].getDniCliente():
                return i # devuelve la posicion del elemento encontrado
        return -1  # signfica que no encontro ningun dato

    def eliminarCliente(self, pos): # Elimina los clientes
        del(self.dataCliente[pos])

    def modificarCliente(self, objcli, pos): # Modifica datos de los clientes
        self.dataCliente[pos] = objcli

    def retornarDatos(self): # retorna los datos de los clientes
        return self.dataCliente

    
            
