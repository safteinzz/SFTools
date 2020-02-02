# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 18:15:26 2020

@author: SaFteiNZz
"""

#Imports


import sys

#Procesos
import psutil
from subprocess import check_output,Popen, PIPE

#comandos cmd
import os
import win32com.shell.shell as shell


#youtube conversor
import youtube_dl


#Ventana
from PyQt5 import uic

#Messagebox
import ctypes

#Widgets pyQT5
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QApplication

#Importar interfaz
Ui_MainWindow, QtBaseClass = uic.loadUiType("interfazMain.ui")





# =============================================================================
# ~Funcion alertas messagebox
#
#            @text comentario del messagebox
#            @title titulo ventana messagebox
#            @style (INT) tipo de ventana
#                  0 : OK
#                  1 : OK | Cancel
#                  2 : Abort | Retry | Ignore
#                  3 : Yes | No | Cancel
#                  4 : Yes | No
#                  5 : Retry | No 
#                  6 : Cancel | Try Again | Continue
#            
# =============================================================================
def Messagebox(text, title, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)            


# =============================================================================
# ~Seleccionar Ruta de fichero/carpeta
#    
#             @filtro => Sera el tipo de extension
#             @guardar => Booleano para saber si se quiere cargar o guardar
#               - 1 = guardar
#               - 0 = cargar
#             Ejemplo filtro: "xls(*.xls);;csv(*.csv)"  
#    
# ============================================================================= 
def seleccionarFichero(filtro, guardar, carpetas):
    qFD = QFileDialog()
    if carpetas == 1:
         return QFileDialog.getExistingDirectory(qFD,"Seleccionar archivo", "", qFD.ShowDirsOnly)
    else:        
        if guardar == 0:                   
            return QFileDialog.getOpenFileName(qFD,"Seleccionar archivo", "",filtro)
        elif guardar == 1:
            return QFileDialog.getSaveFileName(qFD,"Seleccionar archivo", "",filtro)



def has_handle(fpath):
    for proc in psutil.process_iter():
        try:
            for item in proc.open_files():
                if fpath == item.path:
                    return True
        except Exception:
            pass

    return False



# =============================================================================
# ~Lanzar comando por cmd
#            
#            @myList => Array de comandos
#            
# =============================================================================
 
def lanzarComando(admin, myList = [], *args):
    filename = "C:/Users/SaFteiNZz/Documents/!testdelete/New Microsoft Word Document.docx"
    if has_handle(filename):
        print('holis')
    
#    for proc in psutil.process_iter():
#        try:
#            # this returns the list of opened files by the current process
#            flist = proc.open_files()
#            if flist:
#                print(proc.pid,proc.name)
#                for nt in flist:
#                    print("\t",nt.path)
#    
#        # This catches a race condition where a process ends
#        # before we can examine its files    
#        except psutil.NoSuchProcess as err:
#            print("****",err) 
    
#    if admin == 1:
#        for x in myList:
#            shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+x)
#    else:        
#        for x in myList:
#            os.system(x)


# =============================================================================
# ~Descargar url a mp3
        
#            @link url de youtube a descargar
#            @titulo titulo que poner a la cancion
# =============================================================================
def descargar(link): #(link, titulo)
    """
    Download a song using youtube url and song title
    """

#    outtmpl = titulo + '.%(ext)s'
    ydl_opts = {
        'format': 'bestaudio/best',
#        'outtmpl': outtmpl,
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }
        ],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(link, download=True) 




# =============================================================================
# ~Clase main
# =============================================================================
class mainClass(QMainWindow):
    def __init__(self):
        super(mainClass, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 
        
        
# =============================================================================
#         ~Eventos links
# =============================================================================
        #Boton resetear explorer
        self.ui.pBResetExplorer.clicked.connect(self.resetExplorerClicked)      
        #Boton seleccionar archivo borrar
        self.ui.pBSeleccionarArchivoBorrar.clicked.connect(self.seleccionarArchivoClicked)   
        #Boton forzar borrado archivo
        self.ui.pBForzarBorradoArchivo.clicked.connect(self.borrarArchivoClicked)  
        #Boton seleccionar carpeta borrar
        self.ui.pBSeleccionarCarpetaBorrar.clicked.connect(self.seleccionarCarpetaClicked)
        #Boton forzar borrado carpeta
        self.ui.pBForzarBorradoCarpeta.clicked.connect(self.borrarCarpetaClicked)
        #Boton bajar video
        self.ui.pBBajarVideo.clicked.connect(self.bajarVideoClicked)
  


# =============================================================================
# ~Evento clicar boton descarga
# =============================================================================
    def bajarVideoClicked( self ):
        descargar(self.ui.tEVideoBajar.toPlainText())
        
# =============================================================================
# ~Evento resetear explorer
#        
#        taskkill [/s <computer> [/u [<Domain>\]<UserName> [/p [<Password>]]]] {[/fi <Filter>] [...] [/pid <ProcessID> | /im <ImageName>]} [/f] [/t]
#        
#        /s <computer>	Specifies the name or IP address of a remote computer (do not use backslashes). The default is the local computer.
#        /u <Domain>\<UserName>	Runs the command with the account permissions of the user who is specified by UserName or Domain\UserName. /u can be specified only if /s is specified. The default is the permissions of the user who is currently logged on to the computer that is issuing the command.
#        /p <Password>	Specifies the password of the user account that is specified in the /u parameter.
#        /fi <Filter>	Applies a filter to select a set of tasks. You can use more than one filter or use the wildcard character (\*) to specify all tasks or image names. See the following table for valid filter names, operators, and values.
#        /pid <ProcessID>	Specifies the process ID of the process to be terminated.
#        /im <ImageName>	Specifies the image name of the process to be terminated. Use the wildcard character (\*) to specify all image names.
#        /f	Specifies that processes be forcefully terminated. This parameter is ignored for remote processes; all remote processes are forcefully terminated.
#        /t	Terminates the specified process and any child processes started by it.
#
# =============================================================================
    def resetExplorerClicked(self):
        comandos = ["taskkill /f /im explorer.exe", "start explorer.exe"]        
        lanzarComando(0, comandos)
        
        
        
# =============================================================================
# ~Evento borrar archivo
#        
#        del [/p] [/f] [/s] [/q] [/a[:]<attributes>] filename [/?]
#
#        Brush up on how to read command syntax if you're not sure how to interpret the del command syntax as it's described above or in the list below.
#        
#        /p = Prompts for confirmation before deleting each file.
#        /f = Force deletes read-only files.
#        /s = Deletes the specified files from all the subdirectories.
#        /q = Quiet mode; suppresses prompts for delete confirmations.
#        /a:<attributes> = Deletes files based on one of the following attributes:
#        r = Read-only files
#        h = Hidden files
#        i = Not content indexed files
#        s = System files
#        a = Files ready for archiving
#        l = Reparse points
#        
# =============================================================================     
    def borrarArchivoClicked(self):
        head, tail = os.path.split(self.ui.lEArchivoBorrar.text())
#        print(self.ui.lEArchivoBorrar.text())
#        print(head + "   "  + tail)
        print('del /f ' + self.ui.lEArchivoBorrar.text())
        comandos = ["taskkill /f /im explorer.exe"]
        lanzarComando(0, comandos)
        comandos = ["del /f " + self.ui.lEArchivoBorrar.text()]
        lanzarComando(1, comandos)
        comandos = ["start explorer.exe"]
        lanzarComando(0, comandos)
#        comandos = ["taskkill /f /im explorer.exe", "cd " + head, "del /f " + tail, "start explorer.exe"]
#        lanzarComando(1, comandos)
        
        
        
# =============================================================================
# ~Evento borrar carpeta
#        
#        RMDIR [/S] [/Q] [drive:]path
#
#        RD [/S] [/Q] [drive:]path
#        
#        /S Removes all directories and files in the specified directory in addition to the directory itself. Used to remove a directory tree.
#        
#        /Q Quiet mode, do not ask if ok to remove a directory tree with /S
#        
# =============================================================================
    def borrarCarpetaClicked(self):
        comandos = ["taskkill /f /im explorer.exe", "rd /s /q " + self.ui.lECarpetaBorrar.text(), "start explorer.exe"]
        lanzarComando(1, comandos)
        
        
        
# =============================================================================
# ~Evento seleccionar archivo
# =============================================================================     
    def seleccionarArchivoClicked(self):      
        self.ui.lEArchivoBorrar.setText(seleccionarFichero("", 0, 0)[0])
        
        
        
# =============================================================================
# ~Evento seleccionar carpeta
# =============================================================================   
    def seleccionarCarpetaClicked(self):        
        self.ui.lECarpetaBorrar.setText(seleccionarFichero("", 0, 1)[0])
  

##############################################################################################
#Fin de clase

      
##
# Función MAIN
##
def main():
    app = QApplication(sys.argv)
    window = mainClass()
    window.show()
    app.exec_()


#Ejecucion
if __name__ == '__main__':
    main()