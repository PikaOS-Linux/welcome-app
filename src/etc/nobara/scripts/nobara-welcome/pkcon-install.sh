#! /bin/bash

INTERNET="no"

internet_check() {
      # Check for internet connection
      wget -q --spider http://google.com
      if [ $? -eq 0 ]; then
          export INTERNET="yes"
      fi
}

internet_check

if [[ $INTERNET == yes ]]; then
	/etc/nobara/scripts/nobara-welcome/xdg-terminal "pkcon $1 -y $2" && zenity --notification --text="$2 has been $1ed!" && export SUCCESS=yes
else
	zenity --error --text="No internet connection."
fi

if [[ $SUCCESS != yes ]]; then
	zenity --error --text="Failed to $1 $2! Make sure you have a stable internet connection."
fi

