#!/usr/bin/python3
import socket
import struct
import binascii
import sys
import re

s = socket.socket()
s.connect(("itsec.sec.in.tum.de", 7095))

def recv_until(spec):
    global s
    data = b''
    buf = b''
    while spec.encode() not in buf:
        buf = s.recv(1)
        if buf == b"":
            break
        data += buf

    return data

prompt = recv_until(": ")
print(prompt)

# Your exploit goes here

print(recv_until("}"))
