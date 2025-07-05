import sys
import os

from PyQt5 import uic
from PyQt5.QtWidgets import  QMainWindow, QMessageBox,  QTableWidgetItem


class  VentanaBiblioteca(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/panel.ui', self)


        # Valores del Box
        self.box_tipo.addItems(["FISICO", "DIGITAL"])


    # BOTONES:
    def conectar_botones_al_controlador(self, contolador):
        self.btn_registrar_libro.clicked.connect(contolador.registrar_libro)
        self.btn_registrar_miembro.clicked.connect(contolador.registrar_miembro)
        self.btn_prestar.clicked.connect(contolador.prestar_libro)
        self.btn_devolver.clicked.connect(contolador.devolver_libro)
    

    # Obtener datos de libro de la ventana
    def obtener_datos_libro(self) -> dict:
        return {
            "titulo": self.txt_titulo.text().strip(),
            "autor": self.txt_autor.text().strip(),
            "isbn": self.txt_isbn.text().strip(),
            "tipo_libro": self.box_tipo.currentText(),
        }
    
    # Obtener datos del miembro
    def obtener_datos_miembro(self) -> dict:
        return {
            "nombre": self.txt_nombre.text().strip(),
            "id_miembro": self.txt_id_miembro.text().strip(),
        }
    

    def obtener_isbn(self) -> str:
        return self.txt_isbn.text().strip()
    
    def obtener_id_miembro(self) -> str:
        return self.txt_id_miembro.text().strip()
    

    # ---

    # Mensajes
    def mostrar_mensaje(self, titulo: str, mensaje: str, es_error= False):
        if es_error:
            QMessageBox.critical(self, titulo, mensaje)
        else:
            QMessageBox.information(self, titulo, mensaje)
    # ------------

    # Limpiar los campos
    def limpiar_formulario(self):
        self.txt_titulo.clear()
        self.txt_autor.clear()
        self.txt_isbn.clear()
        self.txt_nombre.clear()
        self.txt_id_miembro.clear()
        self.box_tipo.setCurrentIndex(0)
    # -----

    # Actualizar tabla
    def actualizar_tabla(self, lista_libros: list):
        self.tb_data.setRowCount(len(lista_libros))

        for fila, texto in enumerate(lista_libros):
            partes = texto.split(" - ")
            for columna, valor in enumerate(partes):
                self.tb_data.setItem(fila, columna, QTableWidgetItem(valor.strip()))

        





    
