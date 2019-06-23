#!/usr/bin/python36

import os
import socket
import subprocess as sp

s = socket.socket()
ip = "192.168.43.115"
port = 1
s.bind((ip,port))
while True:
	s.listen(5)
	session,addr = s.accept()
	L = session.recv(1024).decode()
	print(L)	
	f1 = open("/etc/ansible/hosts","r")
	ips = f1.read()
	f1.close()
	f = open("/etc/ansible/hosts","a")
	List = L.split(",")
	if List[-1] == '':
		List = List[0:-1]
	for l in List:
		if l in ips:
			pass
		else:
			f.write(l + "\tansible_user=root" + "\tansible_ssh_pass=redhat\n")	
	f.close()
	W = "Welcome"
	session.send(W.encode())
	continue
