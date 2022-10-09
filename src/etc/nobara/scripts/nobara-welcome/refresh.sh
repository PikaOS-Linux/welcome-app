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
	pkexec bash -c "sudo dnf update -y rpmfusion-nonfree-release rpmfusion-free-release fedora-repos nobara-repos --refresh && sudo -S dnf distro-sync -y --refresh && sudo -S dnf update --refresh && touch /tmp/sync.success && chown $LOGNAME:$LOGNAME /tmp/sync.success" | tee /dev/tty | grep -i 'Running transaction check' && export STATE_CHANGE=true
}

internet_check
if [[ $INTERNET == yes ]]; then
	install_progress
fi

if cat /tmp/sync.success ; then
    if [[ $STATE_CHANGE == true ]]; then
    	if zenity --question --title='Update my system' --text='Update complete! It is recommended to reboot for changes to apply properly. Reboot now?' 
    	then
    		rm /tmp/sync.success
    		systemctl reboot
    	else
    		rm /tmp/sync.success
    	fi
    else
    	zenity --info --title='Update my system' --text='No updates required, your system is already up to date!' 
    fi
else
	zenity --error --title='Update my system' --text="Failed to update! Make sure you have a stable internet connection."
	rm /tmp/sync.success
fi
rm /tmp/sync.success
