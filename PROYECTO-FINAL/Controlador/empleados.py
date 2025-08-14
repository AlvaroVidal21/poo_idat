class empleado():

    #Atributos Encapsulados (Privados)
    __dniEmpleado =""; __nombreEmpleado= ""
    __apellidoPatenoEmpleado =""; apellidoMaternoEmpleado= ""
    __direccionEmpleado= ""; __telefonoEmpleado=""

    #Construtor
    def __init__(self, dniEmpleado, nombresEmpleado, apellidopaternoEmpleado, apellidomaternoEmpleado, direccionEmpleado, telefonoEmpleado):
        self.__dniEmpleado = dniEmpleado
        self.__nombresEmpleado = nombresEmpleado
        self.__apellidoPaternoEmpleado = apellidopaternoEmpleado
        self.__apellidoMaternoEmpleado = apellidomaternoEmpleado
        self.__direccionEmpleado = direccionEmpleado
        self.__telefonoEmpleado = telefonoEmpleado

    def getDniEmpleado(self):
        return self.__dniEmpleado
    def setDniEmpleado(self, dniEmpleado):
        self.__dniEmpleado=dniEmpleado

    def getNombresEmpleado(self):
        return self.__nombresEmpleado
    def setNombresEmpleado(self, nombresEmpleado):
        self.__nombresEmpleado=nombresEmpleado

    def getApellidoPaternoEmpleado(self):
        return self.__apellidoPaternoEmpleado
    def setApellidoPaternoEmpleado(self, apellidoPaternoEmpleado):
        self.__apellidoPaternoEmpleado=apellidoPaternoEmpleado

    def getApellidoMaternoEmpleado(self):
        return self.__apellidoMaternoEmpleado
    def setApellidoMaternoEmpleado(self, apellidoMaternoEmpleado):
        self.__apellidoMaternoEmpleado=apellidoMaternoEmpleado

    def getDireccionEmpleado(self):
        return self.__direccionEmpleado
    def setDireccionEmpleado(self, direccionEmpleado):
        self.__direccionEmpleado=direccionEmpleado

    def getTelefonoEmpleado(self):
        return self.__telefonoEmpleado
    def setTelefonoEmpleado(self, telefonoEmpleado):
        self.__telefonoEmpleado=telefonoEmpleado
