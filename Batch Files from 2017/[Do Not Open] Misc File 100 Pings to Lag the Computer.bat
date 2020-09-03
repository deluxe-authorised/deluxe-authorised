set /a count=0
set /a point=1
goto a
:a
set /a count=%count%+%point%
start ping localhost -t
if "%count%"=="100" exit
goto a