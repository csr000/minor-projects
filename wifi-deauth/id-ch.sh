#!/bin/bash

bssid=$1
mac=$2

airodump-ng wlp2s0mon --bssid $bssid --channel $mac
