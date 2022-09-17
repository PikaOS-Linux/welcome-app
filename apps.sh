#! /bin/bash
if [[ "$XDG_SESSION_DESKTOP" == KDE ]];
then
/usr/bin/plasma-discover
else
/usr/bin/gnome-software
fi
