# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blockchainsimulator.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
import os
from simulador.Simulador import Simulador
from datetime import datetime
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QCheckBox,QAction, QGridLayout, QGroupBox,
                             QMenu, QPushButton, QRadioButton, QVBoxLayout, QWidget, QSlider)

class Ui_SimuladorBlockchain(object):
    def setupUi(self, SimuladorBlockchain):
        SimuladorBlockchain.setObjectName("SimuladorBlockchain")
        SimuladorBlockchain.resize(633, 502)
        SimuladorBlockchain.setMouseTracking(True)
        SimuladorBlockchain.setTabletTracking(True)
        self.centralwidget = QtWidgets.QWidget(SimuladorBlockchain)
        self.centralwidget.setObjectName("centralwidget")
        self.labelTitulo = QtWidgets.QLabel(self.centralwidget)
        self.labelTitulo.setGeometry(QtCore.QRect(10, 10, 621, 61))
        self.labelTitulo.setObjectName("labelTitulo")
        
        self.hsCantidadUsuarios = QtWidgets.QSlider(self.centralwidget)
        self.hsCantidadUsuarios.setGeometry(QtCore.QRect(310, 80, 311, 20))
        self.hsCantidadUsuarios.setMinimum(100)
        self.hsCantidadUsuarios.setMaximum(500)
        self.hsCantidadUsuarios.setPageStep(5)
        self.hsCantidadUsuarios.setProperty("value", 250)
        self.hsCantidadUsuarios.setOrientation(QtCore.Qt.Horizontal)
        self.hsCantidadUsuarios.setObjectName("hsCantidadUsuarios")
        self.hsCantidadUsuarios.setTickPosition(QSlider.TicksBothSides)
        self.hsCantidadUsuarios.setTickInterval(10)
        
        self.labelCantidadUsuarios = QtWidgets.QLabel(self.centralwidget)
        self.labelCantidadUsuarios.setGeometry(QtCore.QRect(20, 80, 271, 16))
        self.labelCantidadUsuarios.setObjectName("labelCantidadUsuarios")
        
        self.labelNodosMineros = QtWidgets.QLabel(self.centralwidget)
        self.labelNodosMineros.setGeometry(QtCore.QRect(20, 130, 271, 16))
        self.labelNodosMineros.setObjectName("labelNodosMineros")
        self.hsPoolMineria = QtWidgets.QSlider(self.centralwidget)
        self.hsPoolMineria.setGeometry(QtCore.QRect(310, 130, 311, 20))
        self.hsPoolMineria.setMinimum(2)
        self.hsPoolMineria.setMaximum(5)
        self.hsPoolMineria.setSingleStep(1)
        self.hsPoolMineria.setPageStep(5)
        self.hsPoolMineria.setProperty("value", 3)
        self.hsPoolMineria.setOrientation(QtCore.Qt.Horizontal)
        self.hsPoolMineria.setObjectName("hsPoolMineria")
        self.hsPoolMineria.setTickPosition(QSlider.TicksBothSides)
        self.hsPoolMineria.setTickInterval(1)
        
        self.labelmaxtrans = QtWidgets.QLabel(self.centralwidget)
        self.labelmaxtrans.setGeometry(QtCore.QRect(20, 170, 271, 51))
        self.labelmaxtrans.setWordWrap(True)
        self.labelmaxtrans.setObjectName("labelmaxtrans")
        self.hsTransaccionesBloque = QtWidgets.QSlider(self.centralwidget)
        self.hsTransaccionesBloque.setGeometry(QtCore.QRect(310, 190, 311, 20))
        self.hsTransaccionesBloque.setMinimum(10)
        self.hsTransaccionesBloque.setMaximum(30)
        self.hsTransaccionesBloque.setPageStep(5)
        self.hsTransaccionesBloque.setProperty("value", 20)
        self.hsTransaccionesBloque.setOrientation(QtCore.Qt.Horizontal)
        self.hsTransaccionesBloque.setObjectName("hsTransaccionesBloque")
        self.hsTransaccionesBloque.setTickPosition(QSlider.TicksBothSides)
        self.hsTransaccionesBloque.setTickInterval(3)
        
        self.labelBloques = QtWidgets.QLabel(self.centralwidget)
        self.labelBloques.setGeometry(QtCore.QRect(20, 250, 271, 16))
        self.labelBloques.setObjectName("labelBloques")
        self.hsTotalBloques = QtWidgets.QSlider(self.centralwidget)
        self.hsTotalBloques.setGeometry(QtCore.QRect(310, 250, 311, 20))
        self.hsTotalBloques.setMinimum(1000)
        self.hsTotalBloques.setMaximum(3000)
        self.hsTotalBloques.setPageStep(5)
        self.hsTotalBloques.setProperty("value", 1500)
        self.hsTotalBloques.setOrientation(QtCore.Qt.Horizontal)
        self.hsTotalBloques.setObjectName("hsTotalBloques")
        self.hsTotalBloques.setTickPosition(QSlider.TicksBothSides)
        self.hsTotalBloques.setTickInterval(100)
        
        self.labelArchivoSalida = QtWidgets.QLabel(self.centralwidget)
        self.labelArchivoSalida.setGeometry(QtCore.QRect(20, 320, 271, 16))
        self.labelArchivoSalida.setObjectName("labelArchivoSalida")
        
        self.textArchivoSalida = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textArchivoSalida.setGeometry(QtCore.QRect(300, 310, 321, 31))
        self.textArchivoSalida.setObjectName("textArchivoSalida")
        
        self.progressProceso = QtWidgets.QProgressBar(self.centralwidget)
        self.progressProceso.setGeometry(QtCore.QRect(20, 380, 601, 23))
        self.progressProceso.setProperty("value", 0)
        self.progressProceso.setObjectName("progressProceso")
        
        self.botonProcesar = QtWidgets.QPushButton(self.centralwidget)
        self.botonProcesar.setGeometry(QtCore.QRect(110, 420, 121, 31))
        self.botonProcesar.setObjectName("botonProcesar")
        self.botonSalir = QtWidgets.QPushButton(self.centralwidget)
        self.botonSalir.setGeometry(QtCore.QRect(410, 420, 121, 31))
        self.botonSalir.setObjectName("botonSalir")
        SimuladorBlockchain.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(SimuladorBlockchain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 633, 20))
        self.menubar.setObjectName("menubar")
        self.menuMen = QtWidgets.QMenu(self.menubar)
        self.menuMen.setObjectName("menuMen")
        
        self.salir = QAction('Salir', self.menuMen) 
        self.menuMen.addAction(self.salir)
        self.salir.triggered.connect(self.accionSalir)
        
        
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        
        self.ayuda = QAction('Ver ayuda', self.menuAyuda) 
        self.menuAyuda.addAction(self.ayuda)
        self.ayuda.triggered.connect(self.verTutorial)
        
        SimuladorBlockchain.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SimuladorBlockchain)
        self.statusbar.setObjectName("statusbar")
        SimuladorBlockchain.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMen.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(SimuladorBlockchain)
        QtCore.QMetaObject.connectSlotsByName(SimuladorBlockchain)
        self.botonSalir.clicked.connect(self.accionSalir)
        self.botonProcesar.clicked.connect(self.accionProcesar)

    def retranslateUi(self, SimuladorBlockchain):
        _translate = QtCore.QCoreApplication.translate
        SimuladorBlockchain.setWindowTitle(_translate("SimuladorBlockchain", "Ventana Principal"))
        self.labelTitulo.setText(_translate("SimuladorBlockchain", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#00007f;\">SIMULADOR DEL COMPORTAMIENTO DE UNA CADENA DE BLOQUES</span></p></body></html>"))
        self.hsCantidadUsuarios.setAccessibleName(_translate("SimuladorBlockchain", "|"))
        self.labelCantidadUsuarios.setText(_translate("SimuladorBlockchain", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Cantidad de Usuarios</span></p></body></html>"))
        self.labelNodosMineros.setText(_translate("SimuladorBlockchain", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Cantidad de Pool de Minería</span></p></body></html>"))
        self.hsPoolMineria.setAccessibleName(_translate("SimuladorBlockchain", "|"))
        self.labelmaxtrans.setText(_translate("SimuladorBlockchain", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Número máximo de transacciones por bloque</span></p></body></html>"))
        self.hsTransaccionesBloque.setAccessibleName(_translate("SimuladorBlockchain", "|"))
        self.labelBloques.setText(_translate("SimuladorBlockchain", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Total Bloques en la Cadena</span></p></body></html>"))
        self.hsTotalBloques.setAccessibleName(_translate("SimuladorBlockchain", "|"))
        self.labelArchivoSalida.setText(_translate("SimuladorBlockchain", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Archivo de Salida</span></p></body></html>"))
        self.textArchivoSalida.setPlainText(_translate("SimuladorBlockchain", "< nombre del archivo>"))
        self.botonProcesar.setText(_translate("SimuladorBlockchain", "Procesar"))
        self.botonSalir.setText(_translate("SimuladorBlockchain", "Salir"))
        self.menuMen.setTitle(_translate("SimuladorBlockchain", "Menú"))
        self.menuAyuda.setTitle(_translate("SimuladorBlockchain", "Ayuda"))


    def accionSalir(self):
        mbox = QMessageBox()
        mbox.setWindowTitle('Simulador Blockchain')
        mbox.setText("Gracias por usar la aplicación")
        mbox.setIcon(QMessageBox.Information)
        mbox.setStandardButtons(QMessageBox.Ok)
        mbox.exec()
        sys.exit(0)
        
    def verTutorial(self):
        filename = os.path.join(os.path.dirname(__file__),"tutorial.pdf")
        #print("---"+filename+"---")
        if os.name == "posix":
            os.system("/usr/bin/xdg-open " + filename) 
        else :
            os.filestart(filename)

        
        
    def accionProcesar(self):
        self.botonSalir.setEnabled(False)
        sm = Simulador("Simulación del comportamiento de una cadena de bloques");
        cantidadUsuarios = int(self.hsCantidadUsuarios.value())
        sm.crearUsuarios(cantidadUsuarios);
        cantidadMineros = int(self.hsPoolMineria.value());
        maxTransaccionesPorBloque = int(self.hsTransaccionesBloque.value());
        totalBloquesCaena = int(self.hsTotalBloques.value())
        fsalida = self.textArchivoSalida.toPlainText()
        fsalida = fsalida.lstrip()
        fsalida = fsalida.rstrip()
        fsalida = fsalida.strip()
        mbox = QMessageBox()
        mbox.setWindowTitle('Simulador Blockchain')
        mbox.setText("Usuarios =" + str(cantidadUsuarios) + "\n" +
                     "Pools =" + str(cantidadMineros) + "\n" +
                     "Transacciones x Bloque=" + str(maxTransaccionesPorBloque) + "\n" +
                     "Total Bloques=" + str(totalBloquesCaena) + "\n" +
                     "Archivo de salida=" + str(fsalida))
        
        mbox.setIcon(QMessageBox.Information)
        mbox.setStandardButtons(QMessageBox.Ok)
        mbox.exec()
        sm.inicializarBlockchain(cantidadUsuarios,cantidadMineros);
        
        tsimulacion = open(fsalida + '.txt', 'a+');
        instanteInicial = datetime.now()
        sm.simular(maxTransaccionesPorBloque,totalBloquesCaena,cantidadUsuarios,self.progressProceso);
        instanteFinal = datetime.now()
        tiempo = instanteFinal - instanteInicial # Devuelve un objeto timedelta
        segundos = tiempo.seconds;
        tsimulacion.write("Simulacion \n");
        tsimulacion.write("cantidadUsuarios " + str(cantidadUsuarios) + "\n");
        tsimulacion.write("cantidadMineros " + str(cantidadMineros)+ "\n");
        tsimulacion.write("maxTransaccionesPorBloque " + str(maxTransaccionesPorBloque)+ "\n");
        tsimulacion.write("totalBloquesCadena " + str(totalBloquesCaena)+ "\n");
        tsimulacion.write("demoro " + str(segundos) + " segundos"+ "\n");
        tsimulacion.write("\nFin de la simulación: demoró " + str(segundos) + " segundos" + "\n");
        tsimulacion.write("Estado de los Nodos Mineros...");
        tsimulacion.write("{} , {} , {} , {}, {}".format(str("Descripción"),str("Direccion"), str("Utilidad"),str("Bloques"),str("Usuarios"))+ "\n")
        tsimulacion.write(str(sm.verNodosMineros()));
        tsimulacion.write("Estado de los Usuarios"+ "\n")
        tsimulacion.write("{}, {} , {} ".format(str("#id"),str("Direccion Hash del Usario"), str("Saldo"))+ "\n");
        tsimulacion.write(sm.verUsuarios()+ "\n");
        tsimulacion.write("Cadena de Bloques\n");
        tsimulacion.write(sm._blockchain.getCadenaSerializada()+ "\n");
        tsimulacion.close();
        mbox = QMessageBox()
        mbox.setWindowTitle('Proceso Finalizado')
        mbox.setText("Abrir el archivo " + fsalida + '.txt')
        mbox.setIcon(QMessageBox.Information)
        mbox.setStandardButtons(QMessageBox.Ok)
        mbox.exec()
        self.botonSalir.setEnabled(True)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    SimuladorBlockchain = QtWidgets.QMainWindow()
    ui = Ui_SimuladorBlockchain()
    ui.setupUi(SimuladorBlockchain)
    SimuladorBlockchain.show()
    sys.exit(app.exec_())

