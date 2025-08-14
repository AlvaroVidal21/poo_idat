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
        for i in range(self.tamañoArregloEmpleado()):
            if dni == self.dataEmpleado[i].getDniEmpleado():
                return i  # devuelve la posicion del elemento encontrado
        return -1  # significa que no encontro ningun dato

    def eliminarEmpleado(self, pos): # Elimina los Empleados
        del(self.dataEmpleado[pos])

    def modificarEmpleado(self, objcli, pos): # Modifica datos de los Empleados
        self.dataEmpleado[pos] = objcli

    def retornarDatos(self): # retorna los datos de los Empleados
        return self.dataEmpleado


if __name__ == "__main__":
    # Prueba manual: insertar dos empleados y buscar el segundo
    arreglo = ArregloEmpleados()
    emp1 = empleado("111", "Juan", "Perez", "Lopez", "Calle 1", "999999")
    emp2 = empleado("222", "Ana", "Gomez", "Diaz", "Calle 2", "888888")
    arreglo.adicionaEmpleado(emp1)
    arreglo.adicionaEmpleado(emp2)
    resultado = arreglo.buscarEmpleado("222")
    print(f"Posición del empleado con DNI 222: {resultado}")

    
            
