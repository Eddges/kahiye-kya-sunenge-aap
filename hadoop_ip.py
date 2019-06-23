#!/usr/bin/python36

import os
import socket
import subprocess as sp

s = socket.socket()
ip = "192.168.43.115"
port = 5
s.bind((ip,port))
while True:
	s.listen(5)
	session,addr = s.accept()
	ch = session.recv(1024).decode()
	print(ch)
	L = session.recv(1024).decode()
	print(L)	
	f = open("/etc/ansible/hosts","a")
	List = L.split(",")
	if List[-1] == '':
		List = List[0:-1]
	f.write("[" + ch + "]")
	for l in List:
		f.write(l + "\tansible_user=root" + "\tansible_ssh_pass=redhat\n")
	f.close()
	W = "host file set"
	session.send(W.encode())
	continue
