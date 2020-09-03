@echo off
goto menu

:a
echo Choice 1
goto menu

:b
echo Choice 2
goto menu

:c
echo Choice 3
goto menu

:cal
set /p num1="num1 > "
set /p num2="num2 > "
set /a nadd=%num1%+%num2%
set /a nsub=%num1%-%num2%
set /a nmul=%num1%*%num2%
set /a ndiv=%num1%/%num2%
echo %num1% + %num2% = %nadd%
echo %num1% - %num2% = %nsub%
echo %num1% * %num2% = %nmul%
echo %num1% / %num2% = %ndiv%
goto menu

:menu
echo Welcome
echo 0 to exit
set /p choice="Enter Choice: "
echo %choice%
if "%choice%"=="0" goto exit
if "%choice%"=="1" goto a
if "%choice%"=="2" goto b
if "%choice%"=="3" goto c
if "%choice%"=="cal" goto cal
goto menu