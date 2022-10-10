#! /bin/bash
nvgpu=$(lspci | grep -iEA3 '^[[:digit:]]{2}:[[:digit:]]{2}.*VGA|3D' | grep -i nvidia | cut -d ":" -f 3)
nvkernmod=$(lspci -k | grep -iEA3 '^[[:digit:]]{2}:[[:digit:]]{2}.*VGA|3D' | grep -iA3 nvidia | grep -i 'kernel driver' | grep -iE 'vfio-pci|nvidia')

/usr/bin/hwcheck
if [ $? -eq 0 ]; then
	if [[ -z $nvgpu ]]; then
    		zenity --info\
           	--title="No Nvidia GPU detected" \
           	--width=600 \
           	--text="`printf "No Nvidia GPU has been detected on the system.\n\n"`"
           	exit 0
        else
          if [[ ! -z $nvkernmod ]]; then
	    zenity --info\
               --title="Nvidia GPU driver already loaded" \
               --width=600 \
               --text="`printf "The Nvidia GPU driver is already loaded. Nothing to do!\n\n"`"
               exit 0
          fi
        fi
fi
