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
	# always refresh repo metadata first
	pkexec /usr/lib/pika/welcome/pkcon-do.sh $@

	if [[ $1 == 'install' ]]; then
		if [[ ! -z $(dpkg -l $2) ]]; then
			zenity --notification --text="$2 has been installed!" && export SUCCESS=yes
		else
			zenity --notification --text="$2 $1 has failed!" && export SUCCESS=no
		fi
	fi

	if [[ $1 == 'remove' ]]; then
		if [[ -z $(dpkg -l $2) ]]; then
			zenity --notification --text="$2 has been removed!" && export SUCCESS=yes
		else
			zenity --notification --text="$2 $1 has failed!" && export SUCCESS=no
		fi
	fi
else
	zenity --error --text="No internet connection."
fi


