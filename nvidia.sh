#! /bin/bash

if [[ "$(/usr/bin/hwcheck)" == "" ]];
then
zenity --error --text="No modern Nvidia hardware detected!"
fi
