


"""
Autor: Alvaro Vidal
Descripcion: Clases para  la Gestion de Biblioteca
Fecha: 28-06-2025
"""

__all__ = ['Libro', 'LibroFisico', 'LibroDigital', 'Miembro', 'Biblioteca']

# --- LIBROS ---

class Libro:
    # Atributos
    def __init__(self, titulo: str, autor: str, isbn:str):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.__disponible = True


    # Metodos
    def prestar(self) -> bool:
        """
        Solo puede prestar si el libro esta disponible, obivo no?  
        """

        if self.__disponible:
            self.__disponible = False
            return True
        
        return False
    

    def devolver(self) -> bool:
        self.__disponible = True
        return True
    

    def consultar_disponibilidad(self) -> bool:
        return self.__disponible
    

    def get_info(self) -> str:
        estado = "Disponible" if self.__disponible else "No disponible"
        return f'{self.titulo} - {self.autor} - Estado: {estado} - ISBN: {self.isbn}'


    def get_isbn(self) -> str:
        return self.isbn
  

class LibroFisico(Libro):
    def get_info(self) -> str:
        return f'[FISICO] ' + super().get_info()
    

class LibroDigital(Libro):
    def get_info(self) -> str:
        return f'[DIGITAL] ' + super().get_info()


# ------------------------------------------------------------------------------

# --- MIEMBROS ---

class Miembro:
    
    # Atributos
    def __init__(self, nombre: str, id_miembro: str):
        self.nombre = nombre
        self.id_miembro = id_miembro
        self.__libros_prestados = []

    # Metodos
    def prestar_libro(self,  libro: Libro) ->  bool:
        if libro.prestar():
            self.__libros_prestados.append(libro)
            return True
        
        return False
    

    def devolver_libro(self, libro: Libro) -> bool:

        if libro in self.__libros_prestados:
            libro.devolver()
            self.__libros_prestados.remove(libro)
            return True
        
        return False
    
    def ver_libros_prestados(self) -> list:
        return [libro.get_info()  for libro in self.__libros_prestados]
    

# ------------------------------------------------------------------------------

# --- BIBLIOTECA ---

class Biblioteca:
    # Atributos
    def __init__(self):
        self.__libros = []
        self.__miembros = []


    def agregar_libro(self, libro: Libro):

        # Vamo a validar por  ISBN que no se repita el mismo libro a la hora de agregarlo, seria como un id unico o dni

        if any (el_libro.get_isbn() == libro.get_isbn() for el_libro in  self.__libros):
            raise Exception("El libro ya está en la biblio")
        
        # Sino  lo agregamos  pe
        self.__libros.append(libro)



    def agregar_miembro(self, miembro: Miembro):
        # Al igual que con los libros que usan isbn, con los miembros se usará el id_miembro

        if any(el_miembro.id_miembro == miembro.id_miembro for el_miembro in self.__miembros):
            raise Exception("El miembro ya está registrado")
        # Recién me doy cuenta que "El_miembro" suena gracioso, pido las disculpas del caso

        self.__miembros.append(miembro)


    def buscar_libro(self, isbn: str) -> Libro:
        return next((el_libro for el_libro in self.__libros if el_libro.get_isbn() == isbn), None)
    

    def buscar_miembro(self, id_miembro: str) -> Miembro:
        return next((el_miembro for el_miembro in self.__miembros if el_miembro.id_miembro == id_miembro), None)
    

    def listar_libros(self) -> list:
        # List comprehension, crea una lista mediante un for
        return [el_libro.get_info() for el_libro in self.__libros]
    

    # El libro debe de ser prestado a un miembro
    def prestar(self, isbn: str, id_miembro: str) -> bool:
        libro = self.buscar_libro(isbn)
        miembro = self.buscar_miembro(id_miembro)


        # O sea, si se  están ambos disponibles se procede a prestar el libro al miembro
        if libro and miembro:
            return miembro.prestar_libro(libro)
        
        return False


    # Ahora, todo libro prestado, en teoría, debe ser devuelto por el miembro que pidió el préstamo del libro, tons
    def devolver(self, isbn: str, id_miembro: str) -> bool:
        libro = self.buscar_libro(isbn)
        miembro = self.buscar_miembro(id_miembro)

        if libro and miembro:
            return miembro.devolver_libro(libro)
        

        return False