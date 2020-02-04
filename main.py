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

#sleep y threading
from threading import Thread
from time import sleep
from queue import Queue
from qtpy.QtCore import Qt, QFileSystemWatcher, QSettings, Signal

#youtube conversor (https://github.com/ytdl-org/youtube-dl)
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
#    @filtro => Sera el tipo de extension
#    @titulo  => Titulo de la ventana
#    @guardar => Booleano para saber si se quiere cargar o guardar
#    - 1 = guardar
#    - 0 = cargar
#    Ejemplo filtro: "xls(*.xls);;csv(*.csv)"  
#
# ============================================================================= 
def seleccionarFichero(filtro, titulo, guardar, carpetas):
    qFD = QFileDialog()
    if carpetas == 1:
         return QFileDialog.getExistingDirectory(qFD, titulo, "", qFD.ShowDirsOnly)
    else:        
        if guardar == 0:                   
            return QFileDialog.getOpenFileName(qFD, titulo, "",filtro)
        elif guardar == 1:
            return QFileDialog.getSaveFileName(qFD, titulo, "",filtro)


# =============================================================================
# ~Buscar proceso en los procesos del sistema
# =============================================================================
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
# ~Logger descargador
# =============================================================================
class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)
        
##############################################################################################
#Fin de clase
     







# =============================================================================
# ~Clase main
# =============================================================================
class mainClass(QMainWindow):
    
    finished = Signal()
    updateProgress = Signal(str)

    def __init__(self):
        super(mainClass, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 
        self.updateProgress.connect(self.ui.pTEStatus.appendPlainText)
        
# =============================================================================
#         ~Eventos links
# =============================================================================
        #Botones
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
        #Boton bajar playlist
        self.ui.pBPlaylistBajar.clicked.connect(self.bajarPlaylistClicked)
        
        #Text edit video bajar
#        self.ui.tEVideoBajar.clicked.connect(self.tEVideoBajarClicked)

# =============================================================================
#     ~Hook para estado descargas
#            Funciona como worker (threading queue)
#                @q => cola
#
# =============================================================================
    def myHook( self, d):
        if d['status'] == 'downloading':
            self.updateProgress.emit('Downloading ' +  os.path.splitext(os.path.basename(os.path.normpath(d['filename'])))[0] + '(' + d['_percent_str'] + ' )')      
           
        elif d['status'] == 'finished':
            self.updateProgress.emit('! Done downloading ' +  os.path.splitext(os.path.basename(os.path.normpath(d['filename'])))[0] + ', now deleting additional files...')
            
        elif d['status'] == 'error':
            self.updateProgress.emit('ERROR WHILE DOWNOLOADING ' +  os.path.splitext(os.path.basename(os.path.normpath(d['filename'])))[0])

   
# =============================================================================
#     ~Convertir playlist a urls
#        
#            @link es la url de la playlist
#            @return retorna una lista de url de cada video de la playlist de manera individual
#        
# =============================================================================
    def getPlaylistVideosURL(self, link):
        results = youtube_dl.YoutubeDL({'quiet': True}).extract_info(link, download=False)
        return [i['webpage_url'] for i in results['entries']] 
    
    
    def worker( self, que):
        while True:
            args = que.get()
            self.getMp3FromURL(args[1], args[0])
            que.task_done()
    
# =============================================================================
#     ~Descargar url a mp3
#    
# =============================================================================
    def getMp3FromURL( self, rutaGuardado, enlace):         
#        print(' -' + args[0] + '- ')
#        filetmpl = u'%(id)s_%(uploader_id)s_%(title)s.%(ext)s'
#        print(rutaGuardar + "/")
    
        outtmpl = rutaGuardado + '/%(title)s.%(ext)s'
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': outtmpl,
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }
            ],
            'progress_hooks': [self.myHook],
        }
    
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([enlace])
#            info_dict = ydl.extract_info(link, download=True)  
            
#        print(info_dict)
    
# =============================================================================
#     ~Programador de descargas
# =============================================================================
    def downloadPlaylist(self, playlist, rutaGuardar):
        
        length = len(playlist)
        
        if length <= 1:               
            num_threads = 1
        elif length <= 3:
            num_threads = length
        #Maximo de hilos 3
        else:
            num_threads = 3
            
        que = Queue() 
        for i in range(num_threads):
            worker = Thread(target=self.worker, args=(que,))
            worker.setDaemon(True)
            worker.start()
            
#        self.updateProgress.emit('Begining download ..\n')
        
        for video in playlist:
#            print(video) #printear url (debug)
            que.put((video, rutaGuardar))     
        
        self.updateProgress.emit('Download of ' + str(que.qsize()) + ' files started !')
        que.join()
    
    
    
    def bajarVideo( self , rutaGuardar):
        self.downloadPlaylist([self.ui.tEVideoBajar.toPlainText()], rutaGuardar)
        
# =============================================================================
#     ~Evento clicar boton descarga video
# =============================================================================
    def bajarVideoClicked( self ): 
        rutaGuardar = seleccionarFichero("", "Extract path", 1, 1)
        mainWorker = Thread(target=self.bajarVideo, args=(rutaGuardar,))
        mainWorker.start()
        


    def bajarPlaylist( self ):
        
        self.updateProgress.emit('Begining Download...')
        self.updateProgress.emit('Extracting URLs...')
        playlist = self.getPlaylistVideosURL(self.ui.tEPlaylistBajar.toPlainText())        
        self.downloadPlaylist(playlist, rutaGuardar)
        
# =============================================================================
#     ~Evento clicar boton descarga playlist
# =============================================================================
    def bajarPlaylistClicked( self ): 
        rutaGuardar = seleccionarFichero("", "Extract path", 1, 1)
        mainWorker = Thread(target=self.bajarPlaylist)
        mainWorker.start()
        
        
        
    
        
        
        
        
# =============================================================================
#     ~Evento resetear explorer
#        
#            taskkill [/s <computer> [/u [<Domain>\]<UserName> [/p [<Password>]]]] {[/fi <Filter>] [...] [/pid <ProcessID> | /im <ImageName>]} [/f] [/t]
#        
#            /s <computer>	Specifies the name or IP address of a remote computer (do not use backslashes). The default is the local computer.
#            /u <Domain>\<UserName>	Runs the command with the account permissions of the user who is specified by UserName or Domain\UserName. /u can be specified only if /s is specified. The default is the permissions of the user who is currently logged on to the computer that is issuing the command.
#            /p <Password>	Specifies the password of the user account that is specified in the /u parameter.
#            /fi <Filter>	Applies a filter to select a set of tasks. You can use more than one filter or use the wildcard character (\*) to specify all tasks or image names. See the following table for valid filter names, operators, and values.
#            /pid <ProcessID>	Specifies the process ID of the process to be terminated.
#            /im <ImageName>	Specifies the image name of the process to be terminated. Use the wildcard character (\*) to specify all image names.
#            /f	Specifies that processes be forcefully terminated. This parameter is ignored for remote processes; all remote processes are forcefully terminated.
#            /t	Terminates the specified process and any child processes started by it.
#
# =============================================================================
    def resetExplorerClicked(self):
        comandos = ["taskkill /f /im explorer.exe", "start explorer.exe"]        
        lanzarComando(0, comandos)
        
        
        
# =============================================================================
#     ~Evento borrar archivo
#        
#            del [/p] [/f] [/s] [/q] [/a[:]<attributes>] filename [/?]
#
#            Brush up on how to read command syntax if you're not sure how to interpret the del command syntax as it's described above or in the list below.
#        
#            /p = Prompts for confirmation before deleting each file.
#            /f = Force deletes read-only files.
#            /s = Deletes the specified files from all the subdirectories.
#            /q = Quiet mode; suppresses prompts for delete confirmations.
#            /a:<attributes> = Deletes files based on one of the following attributes:
#            r = Read-only files
#            h = Hidden files
#            i = Not content indexed files
#            s = System files
#            a = Files ready for archiving
#            l = Reparse points
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
#     ~Evento borrar carpeta
#        
#            RMDIR [/S] [/Q] [drive:]path
#            RD [/S] [/Q] [drive:]path        
#            /S Removes all directories and files in the specified directory in addition to the directory itself. Used to remove a directory tree.        
#            /Q Quiet mode, do not ask if ok to remove a directory tree with /S
#        
# =============================================================================
    def borrarCarpetaClicked(self):
        comandos = ["taskkill /f /im explorer.exe", "rd /s /q " + self.ui.lECarpetaBorrar.text(), "start explorer.exe"]
        lanzarComando(1, comandos)
        
        
        
# =============================================================================
#     ~Evento seleccionar archivo
# =============================================================================     
    def seleccionarArchivoClicked(self):
        self.ui.lEArchivoBorrar.setText(seleccionarFichero("", "Seleccionar Archivo", 0, 0)[0])
        
        
        
# =============================================================================
#     ~Evento seleccionar carpeta
# =============================================================================   
    def seleccionarCarpetaClicked(self):        
        self.ui.lECarpetaBorrar.setText(seleccionarFichero("", "Seleccionar carpeta", 0, 1)[0])
  

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