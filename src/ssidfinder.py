#!/usr/bin/python3
import os
import sys
from scapy.all import *
#from scapy.layers.inet import Dot11
ssid=[]
def Handler(pkt):
    
    if pkt.haslayer(Dot11Beacon):
        #dot_layer=pkt.getlayer(Dot11)
        if pkt.info and pkt.info not in ssid:
            ssid.append(pkt.info)
            print(len(ssid)+1,pkt.info,pkt.addr3)
conf.iface=sys.argv[1]
sniff(count=int(sys.argv[2]),prn=Handler)
