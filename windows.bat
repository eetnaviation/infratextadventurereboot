@echo off
:start
cls
title Infra Text Adventure
echo.
echo Welcome! Please choose an option to start playing.
echo.
echo 1 - Play without sounds
echo 2 - Play with sounds !!! THIS OPTION REQUIERES INFRA TO BE INSTALLED ON HOST SYSTEM !!!
echo.
set /p option=">"
if %option%==1 goto nosound
if %option%==2 goto sound
goto start
:nosound
cls
py execs\nosound.py
:sound
cls
py execs\sound.py