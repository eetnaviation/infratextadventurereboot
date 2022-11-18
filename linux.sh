#!/bin/bash
clear
echo ""
echo "Welcome! Please choose an option to start playing."
echo ""
echo "1 - Play without sounds"
echo "2 - Play with sounds !!! THIS OPTION REQUIERES INFRA TO BE INSTALLED ON HOST SYSTEM !!!"
echo ""
read option
if [ $option -eq 1 ]:
	clear
	py nosound.py
if [ $option -eq 2 ]:
	clear
	py sound.py