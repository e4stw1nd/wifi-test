#!/usr/bin/python

import sys
from scapy.all import *

broadcast = "ff:ff:ff:ff:ff:ff"
bssid = "aa:aa:aa:aa:aa:aa" 

pkt = RadioTap() / Dot11(addr1 = broadcast, addr2 = bssid, addr3 = bssid) /Dot11Beacon(cap = 0x1104) / Dot11Elt( ID=0, info = sys.argv[1]) / Dot11Elt (ID=1, info = "\x82\x84\x8b\x96\x24\x30\x48\x6c") / Dot11Elt (ID=3, info = "\x0b") / Dot11Elt (ID=5, info = "\x00\x01\x00\x00" )

sendp(pkt, iface = "wlan0mon", count = int (sys.argv[2]), inter = .2)


