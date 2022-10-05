#! /bin/bash
/usr/bin/codeccheck
if [ $? -eq 0 ]; then
    zenity --error --text='No Codec Change Required!'
fi
