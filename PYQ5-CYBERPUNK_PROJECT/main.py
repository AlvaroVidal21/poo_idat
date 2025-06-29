import sys
import csv
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.QtCore import QDateTime

# Importar QHeaderView para ajustar el tamaño de las columnas
from PyQt5.QtWidgets import QHeaderView

# Mensaje de caja
from PyQt5.QtWidgets import QMessageBox


class Control_Nexus(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI/NEXUS_PANEL.ui", self)

        # Control de guardado de registros
        self.ultima_fila_guardada = 0

        # Agregar opciones al combobox
        self.box_operacion.addItems(["INGRESO", "SALIDA"])

        # Registrar el momento actual del tiempo
        self.dt_fecha.setDateTime(QDateTime.currentDateTime())
        

        # Conectar botones -------------------------------
        self.btn_registrar.clicked.connect(self.registrar_vuelo)
        self.btn_guardar.clicked.connect(self.guardar_csv)
        self.btn_borrar.clicked.connect(self.quitar_vuelo)


    def guardar_csv(self):

        # Verificar si existe el archivo csv
        archivo_nuevo = not os.path.exists("vuelos.csv")


        with open("vuelos.csv", mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            
            if archivo_nuevo:
                # Crear archivo nuevo
                writer.writerow(["Nave", "Operacion", "Fecha/Hora", "Destino/Origen", "Bitacora"])

            # Contenido
            for fila in range(self.ultima_fila_guardada, self.tb_vuelos.rowCount()):
                datos = []

                for columna in range(self.tb_vuelos.columnCount()):
                    item = self.tb_vuelos.item(fila, columna)
                    datos.append(item.text() if item else "")

                writer.writerow(datos)

                # Actualizar la última fila guardada
                self.ultima_fila_guardada = self.tb_vuelos.rowCount()


            # Mostrar mensaje de guardado
            QMessageBox.information(self, "NEXUS-01", "✅ Registros guardados exitosamente en 'registro_vuelos.csv'")


    def registrar_vuelo(self):
        
        hora_actual = QDateTime.currentDateTime().toString("dd/MM/yyyy hh:mm:ss")   

        fila = self.tb_vuelos.rowCount()
        self.tb_vuelos.setRowCount(fila +  1)

        self.tb_vuelos.setItem(fila, 0, QTableWidgetItem(self.txt_nave.text()))
        self.tb_vuelos.setItem(fila, 1, QTableWidgetItem(self.box_operacion.currentText()))
        self.tb_vuelos.setItem(fila, 2, QTableWidgetItem(hora_actual))
        self.tb_vuelos.setItem(fila, 3, QTableWidgetItem(self.txt_destino.text()))
        # toPlainText() aceptal múltiples líneas de texto
        self.tb_vuelos.setItem(fila, 4, QTableWidgetItem(self.txt_bitacora.toPlainText()))
        

        # Limpiar campos
        self.limpiar_campos()

        # Ajuste visual de la tabla
        header = self.tb_vuelos.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)  # Nave
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)  # Operación
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)  # Fecha/Hora
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)  # Origen/Destino
        header.setSectionResizeMode(4, QHeaderView.Stretch)           # Bitácora ocupa el resto


    def limpiar_campos(self):
        self.txt_nave.clear()
        self.box_operacion.setCurrentIndex(0)
        self.txt_destino.clear()
        self.txt_bitacora.clear()


    def quitar_vuelo(self):
        fila_actual = self.tb_vuelos.currentRow()

        if fila_actual != -1:
            self.tb_vuelos.removeRow(fila_actual)

            if fila_actual < self.ultima_fila_guardada:
                self.ultima_fila_guardada -= 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Control_Nexus()
    ventana.show()
    sys.exit(app.exec_())