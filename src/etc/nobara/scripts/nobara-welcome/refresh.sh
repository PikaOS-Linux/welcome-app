#! /bin/bash

INTERNET="no"
STATE_CHANGE=false

internet_check() {
      # Check for internet connection
      wget -q --spider http://google.com
      if [ $? -eq 0 ]; then
          export INTERNET="yes"
      fi
}

install_progress() {	
	pkexec bash -c "sudo -S dnf distro-sync -y --refresh && sudo -S dnf update --refresh && touch /tmp/sync.success && chown $LOGNAME:$LOGNAME /tmp/sync.success" | tee /dev/tty | grep -i 'Running transaction check' && export STATE_CHANGE=true
}

internet_check
if [[ $INTERNET == yes ]]; then
	install_progress
fi

if cat /tmp/sync.success ; then
    if [[ $STATE_CHANGE == true ]]; then
    	if zenity --question --title='Sync Repos and Packages' --text='Sync complete. For the best result, please reboot your system. Reboot now?' 
    	then
    		rm /tmp/sync.success
    		systemctl reboot
    	else
    		rm /tmp/sync.success
    	fi
    fi
else
	zenity --error --title='Sync Repos and Packages' --text="Failed to sync, make sure you have a stable internet connection."
	rm /tmp/sync.success
fi
rm /tmp/sync.success
