#! /bin/bash
nvgpu=$(lspci | grep -iEA3 '^[[:digit:]]{2}:[[:digit:]]{2}.*VGA|3D' | grep -i nvidia | cut -d ":" -f 3)

/usr/bin/hwcheck
if [ $? -eq 0 ]; then
	if [[ -z $nvgpu ]]; then
    		zenity --info\
           	--title="No Nvidia GPU detected" \
           	--width=600 \
           	--text="`printf "No Nvidia GPU has been detected on the system.\n\n"`"
           	exit 0
        fi
fi
