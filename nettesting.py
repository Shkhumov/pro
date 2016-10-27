#!/usr/bin/python

from scapy.all import *
import threading
import unittest
import pscapy
#results = {}


def funTCP():
	ip = IP(dst = "0.0.0.0-100")
	protocol = TCP(dport = 80, flags = 'A')
	paket = ip/protocol
	packets1 = sr(paket,timeout = 30)
	#results["TCP pakets"] = packets1
	print("TCP complete:",packets1)

def funICMP():
	ip = IP(dst = "0.0.0.0-10")
	protocol =  ICMP(reserved = 20)
	paket = ip/protocol
	packets2 = sr(paket,timeout = 30)	
	#results["ICMP pakets"] = packets2
	print("ICMP was complete:", packets2)

def funUDP():
	ip = IP(dst = "0.0.0.0-49")
	protocol = UDP(sport = 20, dport = 80)
	paket = ip/protocol
	packets3 = sr(paket,timeout = 30)
	#results["UDP pakets"] = packets3
	print("UDP was complete:",packets3)

def send_catch():
	ip = IP(src="192.0.0.1",dst="192.0.0.2")
	protocol = TCP(sport=128, dport = 80,flags='S',seq=12345)
	status = "TEST"
	paket = ip/protocol/status
	packets4 = sr(paket, timeout = 7)
	for pac in packets4:
		pac1 = pac.summary()
		hexdump(pac)
		print("Send and cath packet :",pac1)	

def Main():
	thread1 = threading.Thread(target = funTCP)
	thread2 = threading.Thread(target = funICMP)
	thread3 = threading.Thread(target = funUDP)
	thread4 = threading.Thread(target = send_catch)

	thread1.start()
	thread2.start()
	thread3.start()
	thread4.start()

	thread1.join()
	thread2.join()
	thread3.join()
	thread4.join()


	#print("Main Complete")


if __name__ == '__main__':
	Main() 

