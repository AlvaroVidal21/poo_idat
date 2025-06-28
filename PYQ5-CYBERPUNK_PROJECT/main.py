import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


class Control_Nexus(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI/NEXUS_PANEL.ui", self)
        

        # Conectar boton
        self.btn_registrar.clicked.connect(self.registrar_vuelo)

    def registrar_vuelo(self):
        fila = self.tb_vuelos.rowCount()
        self.tb_vuelos.setRowCount(fila +  1)

        self.tb_vuelos.setItem(fila, 0, QTableWidgetItem(self.txt_nave.text()))
        self.tb_vuelos.setItem(fila, 1, QTableWidgetItem(self.box_operacion.currentText()))
        self.tb_vuelos.setItem(fila, 2, QTableWidgetItem(self.dt_fecha.text()))
        self.tb_vuelos.setItem(fila, 3, QTableWidgetItem(self.txt_destino.text()))
        # toPlainText() aceptal múltiples líneas de texto
        self.tb_vuelos.setItem(fila, 4, QTableWidgetItem(self.text_bitacora.toPlainText()))
        

        # Limpiar campos
        self.limpiar_campos()

        def limpiar_campos(self):
            self.txt_nave.clear()
            self.box_operacion.setCurrentIndex(0)
            self.txt_destino.clear()
            self.txt_bitacora.clear()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Control_Nexus()
    ventana.show()
    sys.exit(app.exec_())