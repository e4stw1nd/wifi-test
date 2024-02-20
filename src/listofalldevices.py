#!/usr/bin/python3
import os
import sys
from scapy.all import *
#from scapy.layers.inet import Dot11
device_mac=[]
def Handler(pkt):
    print(pkt)
    if pkt.haslayer(Dot11):
        dot_layer=pkt.getlayer(Dot11)
        if dot_layer.addr2 and dot_layer.addr2 not in device_mac:
            device_mac.append(dot_layer.addr2)
            print(dot_layer.info)
conf.iface=sys.argv[1]
sniff(count=int(sys.argv[2]),prn=Handler)
