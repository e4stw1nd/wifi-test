#!/usr/bin/python
import os
import sys
from scapy.all import *
match=[]
def Handler(pkt):
    if pkt.haslayer(Dot11ProbeReq) and len(pkt.info)>0:
        
        if([pkt.addr2,pkt.info] not in match):
            match.append([pkt.addr2,pkt.info])
            print("New Probe Details:",len(match),'-->',pkt.addr2,',',str(pkt.info))
            

sniff(prn=Handler,iface=sys.argv[1],count=int(sys.argv[2]))