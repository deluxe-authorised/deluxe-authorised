@echo off
:a
cls
date /t & time /t
@echo on & ping localhost -n 1 -w 100
@echo off & timeout /t 3
goto a