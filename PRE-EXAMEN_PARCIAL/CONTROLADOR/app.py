
from MODELO.clases import Biblioteca, LibroFisico, LibroDigital, Miembro
from VISTA.vista_principal import VentanaBiblioteca

class ControladorApp:
    def __init__(self):
        self.bilibioteca = Biblioteca()
        self.vista = VentanaBiblioteca()
        self.vista.conectar_botones_al_controlador(self)
        self.vista.show()


    def registrar_libro(self):
        
        datos_del_libro = self.vista.obtener_datos_libro()

        # Recuerda que lo tengo como un diccionario, tons:
        titulo = datos_del_libro["titulo"]
        autor = datos_del_libro["autor"]
        isbn = datos_del_libro["isbn"]
        tipo_libro = datos_del_libro["tipo_libro"]

        # Toca validar:
        if not titulo or not autor or not isbn:
            self.vista.mostrar_mensaje("error", "Todos los campos son obligatorios", es_error=True)


        # Toca crear el libro:

        tipo_de_libro = datos_del_libro["tipo_libro"] # Por defaul estará en fisico

        if tipo_de_libro == "FISICO":
            libro = LibroFisico(titulo, autor, isbn)
        else:
            libro = LibroDigital(titulo, autor, isbn)


        # Agregar el libro a la biblio

        try:
            self.bilibioteca.agregar_libro(libro)
        except ValueError as e:
            self.vista.mostrar_mensaje("Error", str(e), es_error=True)
            return # Paramos la ejecu si hay un error
        
        # Mostrar mensaje de agreado
        self.vista.mostrar_mensaje("Todo bien", "Libro registrado correctamente")
        self.vista.limpiar_formulario()
        self.vista.actualizar_tabla(self.bilibioteca.listar_libros())


    def registrar_miembro(self):
        datos_del_miembro = self.vista.obtener_datos_miembro()

        nombre = datos_del_miembro["nombre"]
        id_miembro = datos_del_miembro["id_miembro"]

        # validamo
        if not nombre or not id_miembro:
            self.vista.mostrar_mensaje("Error", "Todos los campos son obligatorios", es_error=True)
            return
        
        # Creamos el miembro
        miembro = Miembro(nombre, id_miembro)

        # Agregamo
        try:
            self.bilibioteca.agregar_miembro(miembro)
        except ValueError as e:
            self.vista.mostrar_mensaje("Error", str(e), es_error=True)
            return
        
        # Mensaje
        self.vista.mostrar_mensaje("Todo bien", "Miembro registrado correctamente")
        self.vista.limpiar_formulario()


    def prestar_libro(self):
        isbn = self.vista.obtener_isbn()
        id_miembro = self.vista.obtener_id_miembro()

        # Validamo
        if not isbn or not id_miembro:
            self.vista.mostrar_mensaje("Error", "Todos los campos son obligatorios", es_error=True)
            return
        
        prestado = self.bilibioteca.prestar(isbn, id_miembro)

        if prestado:
            self.vista.mostrar_mensaje("Todo bien", "Libro prestado correctamente")
            self.vista.actualizar_tabla(self.bilibioteca.listar_libros())
        else:
            self.vista.mostrar_mensaje("Error", "No se pudo prestar el libro", es_error=True)


    def devolver_libro(self):
        isbn = self.vista.obtener_isbn()
        id_miembro = self.vista.obtener_id_miembro()

        if not isbn or not id_miembro:
            self.vista.mostrar_mensaje("Error", "Todos los campos son obligatorios", es_error=True)
            return
        
        devuelto = self.bilibioteca.devolver(isbn, id_miembro)

        if devuelto:
            self.vista.mostrar_mensaje("Todo bien", "Libro devuelto correctamente")
            self.vista.actualizar_tabla(self.bilibioteca.listar_libros())
        else:
            self.vista.mostrar_mensaje("Error", "No se pudo devolver el libro", es_error=True)




        



        