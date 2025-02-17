#!/usr/bin/python3
import sys
from scapy.all import *
hidden_bssid=[]
def Handler(pkt):
    if pkt.haslayer(Dot11Beacon)  and not pkt.info:
        if not pkt.addr3 in hidden_bssid:
            hidden_bssid.append(pkt.addr3)
            print(" Hidden BSSID:",len(hidden_bssid),hidden_bssid[-1])
    elif pkt.haslayer(Dot11ProbeResp) and pkt.addr3 in hidden_bssid:
        print("Hidden SSID:",pkt.info,'-> Hidden BSSID:',pkt.addr3)
sniff(iface=sys.argv[1],count=int(sys.argv[2]),prn=Handler)