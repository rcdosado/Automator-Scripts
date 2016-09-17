@echo off

cls

REM for deleting files after compression 
for /f "delims=|" %%f in ('type %1') do (mkdir "%%f")

dir /w
echo Finished