@echo off

cls
set winrar="c:\Program Files\WinRAR"

REM for deleting files after compression 
for /f "delims=|" %%f in ('dir /ad /b') do (%winrar%\rar.exe a -df -m0 -ep1 -r "%%f.rar" "%%f\*")

shutdown after compression
shutdown /s /f /t 0