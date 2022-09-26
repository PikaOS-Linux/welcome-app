#! /bin/bash
(
echo "1"
echo "# Syncing." ; sleep 2
pkexec env PATH=$PATH DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY LOGNAME=$LOGNAME bash -c "sudo dnf distro-sync -y --refresh && sudo dnf update --refresh && touch /tmp/sync.success & chown $LOGNAME:$LOGNAME /tmp/sync.success"
echo "# Done!" ; sleep 2
echo "100"
) | 
zenity --progress \
--title='Sync Progress' \
--text='Syncing System, this might take while please be patient !'  \
--percentage=0 \
--auto-close \
--auto-kill

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
