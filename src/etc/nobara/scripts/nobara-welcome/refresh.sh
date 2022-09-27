#! /bin/bash

INTERNET="no"

passwd_check() {
	PASSWD="$(zenity --password)";
	if [[ $PASSWD != "" ]]; then
          export PASSWD_PRESENT="yes"
        fi	
}
internet_check() {
      # Check for internet connection
      wget -q --spider http://google.com
      if [ $? -eq 0 ]; then
          export INTERNET="yes"
      fi
}

install_progress() {	
	(
	echo "1"
	echo "# Syncing. (this might take while please be patient !)" ; sleep 2
	echo -e $PASSWD | sudo -S dnf distro-sync -y --refresh
	echo "45"
	echo "# Updating." ; sleep 2
	echo -e $PASSWD | sudo -S dnf update --refresh && touch /tmp/sync.success && chown $LOGNAME:$LOGNAME /tmp/sync.success
	echo "99"
	echo "#Finishing." ; sleep 2
	echo "# Done!" ; sleep 2
	echo "100"
	) | 
	zenity --progress \
	--title='Sync Progress' \
	--text='Syncing System, this might take while please be patient !'  \
	--percentage=0 \
	--auto-close \
	--auto-kill
}

internet_check
passwd_check
if [[ $INTERNET == yes ]]; then
 if [[ $PASSWD_PRESENT == yes ]]; then
	install_progress
 fi
fi

if cat /tmp/sync.success ; then
    if zenity --question --text='Sync Complete, Please reboot' 
    then
    	rm /tmp/sync.success
    	systemctl reboot
    else
    	rm /tmp/sync.success
    fi
else
zenity --error --text="Failed to sync, make sure you have a stable internet connection"
rm /tmp/sync.success
fi
