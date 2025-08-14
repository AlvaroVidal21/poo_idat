from Controlador.empleados import empleado
#Mantenimiento para los empleados

class ArregloEmpleados():

    #Atributo
    dataEmpleado = [] #<-- Nuestra base de datos

    #Constructor (vacio)
    def __init__(self):
        pass

    def adicionaEmpleado(self,objcli): # Graba los datos de los Empleados
        self.dataEmpleado.append(objcli)

    def devolverEmpleado(self, pos): # Retorna los datos de los Empleados
        return self.dataEmpleado[pos]

    def tamañoArregloEmpleado(self): # Devuelve los datos de los Empleados
        return len(self.dataEmpleado)

    def buscarEmpleado(self, dni): # Busca los Empleados por dni
        for i in range (self.tamañoArregloEmpleado()):
            if dni == self.dataEmpleado[i].getDniEmpleado():
                return i # devuelve la posicion del elemento encontrado
        return -1  # signfica que n o encontro ningun dato

    def eliminarEmpleado(self, pos): # Elimina los Empleados
        del(self.dataEmpleado[pos])

    def modificarEmpleado(self, objcli, pos): # Modifica datos de los Empleados
        self.dataEmpleado[pos] = objcli

    def retornarDatos(self): # retorna los datos de los Empleados
        return self.dataEmpleado

    
            
