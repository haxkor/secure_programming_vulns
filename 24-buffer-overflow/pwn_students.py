#!/usr/bin/env python3

import socket
import telnetlib

def interact(s):
	t = telnetlib.Telnet()
	t.sock = s
	t.interact()

s = socket.socket()
s.connect(("itsec.sec.in.tum.de", 7080))

# Your exploit goes here

# For debugging, you might want to comment this out for your final submission
interact(s)
