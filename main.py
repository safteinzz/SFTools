# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 18:15:26 2020

@author: SaFteiNZz
"""

#Imports

import sys

#comandos cmd
import os

#Ventana
from PyQt5 import uic

#Arrays
from itertools import product

#Messagebox
import ctypes

#Widgets pyQT5
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication








Ui_MainWindow, QtBaseClass = uic.loadUiType("interfazMain.ui")


##
# función Messagebox para alertas
##
def Messagebox(text, title, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)            
##############################################################################################
#Fin de metodo
    
##
# Seleccionar Ruta de fichero
# @filtro => Sera el tipo de extension
# @guardar => Booleano para saber si se quiere cargar o guardar
#   - 1 = guardar
#   - 0 = cargar
# Ejemplo filtro: "xls(*.xls);;csv(*.csv)" 
##  
def seleccionarFichero(filtro, guardar, carpetas):
    qFD = QFileDialog()
    if carpetas == 1:
         return QFileDialog.getExistingDirectory(qFD,"Seleccionar archivo", "", qFD.ShowDirsOnly)
    else:        
        if guardar == 0:                   
            return QFileDialog.getOpenFileName(qFD,"Seleccionar archivo", "",filtro)
        elif guardar == 1:
            return QFileDialog.getSaveFileName(qFD,"Seleccionar archivo", "",filtro)
##############################################################################################
#Fin de metodo  


def lanzarComando(myList = [], *args):
    for x in myList:
        os.system(x)



class mainClass(QMainWindow):
    def __init__(self):
        super(mainClass, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 
        
        self.ui.pBResetExplorer.clicked.connect(self.resetExplorerClicked)
        
        self.ui.pBSeleccionarArchivoBorrar.clicked.connect(self.seleccionarArchivoClicked)
        
        self.ui.pBForzarBorradoArchivo.clicked.connect(self.borrarArchivoClicked)
        
        self.ui.pBSeleccionarCarpetaBorrar.clicked.connect(self.seleccionarCarpetaClicked)
        
        self.ui.pBForzarBorradoCarpeta.clicked.connect(self.borrarCarpetaClicked)
        
    def resetExplorerClicked(self):
        comandos = ["taskkill /f /im explorer.exe", "start explorer.exe"]        
        lanzarComando(comandos)
        
    def borrarArchivoClicked(self):
        comandos = ["taskkill /f /im explorer.exe", "del /f " + self.ui.lEArchivoBorrar.Text(), "start explorer.exe"]
        lanzarComando(comandos)
        
    def borrarCarpetaClicked(self):
        comandos = ["taskkill /f /im explorer.exe", "rd /s /q " + self.ui.lECarpetaBorrar.Text(), "start explorer.exe"]
        lanzarComando(comandos)
        
    def seleccionarArchivoClicked(self):      
        self.ui.lEArchivoBorrar.setText(seleccionarFichero("", 0, 0)[0])
        
    def seleccionarCarpetaClicked(self):        
        self.ui.lECarpetaBorrar.setText(seleccionarFichero("", 0, 1)[0])
        
##
# Función MAIN
##
def main():
    app = QApplication(sys.argv)
    window = mainClass()
    window.show()
    app.exec_()
##############################################################################################
#Fin de metodo
  

## pythonlike
if __name__ == '__main__':
    main()