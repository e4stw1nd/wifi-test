#!/usr/bin/python3
from scapy.all import *
import sys
broadcast='ff:ff:ff:ff:ff:ff'
my_mac='12:34:56:78:90:ab'
def brutehiddenssid(file,iface):
    file=open(file,'r')
    global broadcast,my_mac
    for ssid in file.readlines():
        pkt=RadioTap() / Dot11(type=0, subtype=4, addr1=broadcast, addr2=my_mac, addr3=broadcast) /Dot11ProbeReq() /Dot11Elt(ID=0, info = ssid.strip()) /  Dot11Elt(ID=1, info = "\x02\x04\x0b\x16") / Dot11Elt(ID=3, info = "\x08")
        print "\nTrying SSID : ", ssid
	    sendp(pkt, iface = iface, count = 5, inter = .5)
brutehiddenssid(sys.argv[2],sys.argv[1])
