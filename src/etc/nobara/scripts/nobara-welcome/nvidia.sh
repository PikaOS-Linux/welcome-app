#! /bin/bash
/usr/bin/hwcheck
if [ $? -eq 0 ]; then
    zenity --error --text='No modern NVIDIA GPU found (only maxwell and later cards are supported)'
fi
