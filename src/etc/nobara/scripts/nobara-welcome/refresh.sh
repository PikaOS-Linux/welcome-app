#! /bin/bash

INTERNET="no"

internet_check() {
      # Check for internet connection
      wget -q --spider http://google.com
      if [ $? -eq 0 ]; then
          export INTERNET="yes"
      fi
}

install_progress() {	
	pkexec bash -c "sudo -S dnf distro-sync -y --refresh && sudo -S dnf update --refresh && touch /tmp/sync.success && chown $LOGNAME:$LOGNAME /tmp/sync.success"
}

internet_check
if [[ $INTERNET == yes ]]; then
	install_progress
 fi
fi

if cat /tmp/sync.success ; then
    if zenity --question --text='Sync Complete, If you encounter any issues, reboot your system.' 
    then
    	rm /tmp/sync.success
    	systemctl reboot
    else
    	rm /tmp/sync.success
    fi
else
	zenity --error --text="Failed to sync, make sure you have a stable internet connection."
	rm /tmp/sync.success
fi
rm /tmp/sync.success
