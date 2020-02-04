REM BORRAR ANTIGUO DIST
RD /S /Q "dist"

REM BUILDEAR APP
pyinstaller.exe --onefile --windowed --icon=sftoolsico.ico SFTools.py

REM COPIAR RESOURCES A DIST
ROBOCOPY resources dist/resources /mir

REM CREAR README
@echo off
set tab = "    "

echo SFTools > dist/readme.txt
echo. >> dist/readme.txt
echo What is? >> dist/readme.txt
echo This is a simple application with interface that features different fixes and tools mostly for windows operating system computers  >> dist/readme.txt

echo. >> dist/readme.txt
echo How to execute? >> dist/readme.txt
echo To execute just open SFTools.exe >> dist/readme.txt

echo. >> dist/readme.txt
echo Features >> dist/readme.txt

echo. >> dist/readme.txt
echo Deleting (work in progress) >> dist/readme.txt
echo. %tab%- Force deleting of files locked by the system for what ever reason >> dist/readme.txt
echo. %tab%- Force recursive deleting of folder locked for the system or that have inside them any file locked by the system >> dist/readme.txt

echo. >> dist/readme.txt
echo Fixes (work in progress) >> dist/readme.txt
echo. %tab%- Some of this changes requiere adding or editing the register of windows >> dist/readme.txt
echo. %tab%- Explorer or any kind of bug in navigation for the current session >> dist/readme.txt
echo. %tab%- Darklight not working properly >> dist/readme.txt
echo. %tab%- Get back old microsoft photo viewer from win 7 >> dist/readme.txt

echo. >> dist/readme.txt
echo Downloads (done) >> dist/readme.txt
echo. %tab%- Download youtube videos to mp3 (192Kbps) >> dist/readme.txt
echo. %tab%- Download youtube playlist to mp3 (192Kbps) in one go >> dist/readme.txt
