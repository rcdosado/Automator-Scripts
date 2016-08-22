@echo off
REM for deleting files after compression
REM change python path if required
for /f "delims=|" %%f in ('type list.txt') do (c:\python27\python.exe search.py %%f)