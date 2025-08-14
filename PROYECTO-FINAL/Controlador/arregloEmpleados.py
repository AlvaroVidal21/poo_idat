from Controlador.empleados import empleado
import csv
import os

#Mantenimiento para los empleados

class ArregloEmpleados:

    def __init__(self):
        self.__archivo = os.path.join(os.path.dirname(__file__), 'empleados.csv')
        self.dataEmpleado = []  # <-- Nuestra base de datos en memoria
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
                        self.dataEmpleado.append(empleado(*row))

    def grabar(self):
        with open(self.__archivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for emp in self.dataEmpleado:
                writer.writerow([
                    emp.getDniEmpleado(),
                    emp.getNombresEmpleado(),
                    emp.getApellidoPaternoEmpleado(),
                    emp.getApellidoMaternoEmpleado(),
                    emp.getDireccionEmpleado(),
                    emp.getTelefonoEmpleado(),
                ])

    # ---------------------------
    # Métodos de gestión
    # ---------------------------
    def adicionaEmpleado(self, objcli):  # Graba los datos de los Empleados
        self.dataEmpleado.append(objcli)
        self.grabar()

    def devolverEmpleado(self, pos):  # Retorna los datos de los Empleados
        return self.dataEmpleado[pos]

    def tamañoArregloEmpleado(self):  # Devuelve los datos de los Empleados
        return len(self.dataEmpleado)

    def buscarEmpleado(self, dni):  # Busca los Empleados por dni
        for i in range(self.tamañoArregloEmpleado()):
            if dni == self.dataEmpleado[i].getDniEmpleado():
                return i  # devuelve la posicion del elemento encontrado
        return -1  # signfica que no encontro ningun dato

    def eliminarEmpleado(self, pos):  # Elimina los Empleados
        del (self.dataEmpleado[pos])
        self.grabar()

    def modificarEmpleado(self, objcli, pos):  # Modifica datos de los Empleados
        self.dataEmpleado[pos] = objcli
        self.grabar()

    def retornarDatos(self):  # retorna los datos de los Empleados
        return self.dataEmpleado

    
            
