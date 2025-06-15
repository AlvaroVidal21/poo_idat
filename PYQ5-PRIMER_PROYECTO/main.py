import sys

from PyQt5 import uic # Permite cargar archivos .ui de Qt Designer
from PyQt5.QtWidgets import QMainWindow, QApplication
#  QMainWindow -> Ventana Principal
#  QApplication -> Inicia y ejecuta todo el programa


class main_gui(QMainWindow):

    # Constructor de la clase
    def __init__(self):
        super().__init__()
        uic.loadUi("UI/calculadora_diezmo_ui.ui", self)

        # Conectar botones a sus funciones
        self.btn_calcular.clicked.connect(self.calcular_diezmo)
        self.btn_calcular.clicked.connect(self.mostrar_diezmo)
    



    # Obtener variables de la interfaz
    def  lectura_datos(self):
        self.sueldo = float(self.txt_sueldo.text())

    # Calcular el diezmo
    def calcular_diezmo(self):
        self.lectura_datos()
        self.diezmo = self.sueldo * 0.10

    # Mostrar el resultado
    def mostrar_diezmo(self):

        self.lbl_resultado.setText(f"Tu diezmo es S/.{self.diezmo:.2f}")





    





if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = main_gui()
    GUI.show()
    sys.exit(app.exec_())