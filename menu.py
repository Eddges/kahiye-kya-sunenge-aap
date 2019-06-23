#!/usr/bin/python36

import subprocess as sp
import os
import socket 

s = socket.socket()
ip = "192.168.43.115"
port = 3
s.bind((ip,port))
while True:
	s.listen(5)
	session,addr = s.accept()
	ch = session.recv(1024).decode()

#ch = input("Enter your choice: ")

	if ch == "yum":
		op = sp.getstatusoutput("ansible-playbook /root/Desktop/project/playbooks/yum.yml")
		if op[0] == 0:
			t = "yum is successfully  configured"
		else:
			t = "yum could not be configured"
		session.send(t.encode())
		continue
	elif ch == "python":
		op = sp.getstatusoutput("ansible-playbook /root/Desktop/project/playbooks/python.yml")
		if op[0] == 0:
			t = "python is successfully installed"
		else:
			t = "python could not be installed"
		session.send(t.encode())
		continue

	elif ch == "java":
		os.system(""" echo "export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/" >> /root/.bashrc """)
		os.system(""" echo "export PATH=/usr/java/jdk1.8.0_171-amd64/bin/:$PATH" >> /root/.bashrc """)
		op = sp.getstatusoutput("ansible-playbook /root/Desktop/project/playbooks/java.yml")
		
		if op[0] == 0:
			t = "python is successfully installed"
		else:
			t = "python could not be installed"
		session.send(t.encode())			
		continue
			
	elif ch == "library":
		op = sp.getstatusoutput('ansible-playbook /root/Desktop/project/playbook/python_lib.yml')
		if op[0] == 0:
			t = "library is successfully installed"
		else:
			t = "library could not be installed"
		session.send(t.encode())
		continue
			
	elif ch == "jupyter":
		op = sp.getstatusoutput('ansible localhost -m command -a "jupyter notebook --allow-root &"')
		if op[0] == 0:
			t = "jupyter notebook has been launched"
		else:
			t = "jupyter notebook could not be launched"
		session.send(t.encode())
		continue
			
	elif ch == "hadoop":
		os.system("ansible-playbook /root/Desktop/project/playbooks/java.yml")
		os.system(""" echo "export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/" 	>> /root/.bashrc """)
		os.system(""" echo "export PATH=/usr/java/jdk1.8.0_171-amd64/bin/:$PATH" >> /root/.bashrc """)
		op = sp.getstatusoutput("ansible-playbook /root/Desktop/project/playbooks/hadoop.yml")	
		if op[0] == 0:
			t = "hadoop is successfully installed"
		else:
			t = "hadoop could not be installed"
		session.send(t.encode())
		continue
	
	elif ch == "master":
		os.system("ansible-playbook /root/Desktop/project/playbooks/java.yml")
		os.system(""" echo "export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/" >>/root/.bashrc """)
		os.system(""" echo "export PATH=/usr/java/jdk1.8.0_171-amd64/bin/:$PATH" >> /root/.bashrc """)
		os.system("ansible-playbook /root/Desktop/project/playbooks/hadoop.yml")		
		p = socket.socket()
		p.connect(("192.168.43.115",4))
		t = "master"
		p.send(t.encode())
		session.send(p.recv(1024))
		continue
	
	elif ch == "slave":
		os.system("ansible-playbook /root/Desktop/project/playbooks/java.yml")
		os.system(""" echo "export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/" >> /root/.bashrc """)
		os.system(""" echo "export PATH=/usr/java/jdk1.8.0_171-amd64/bin/:$PATH" >> /root/.bashrc """)
		os.system("ansible-playbook /root/Desktop/project/playbooks/hadoop.yml")		
		p = socket.socket()
		p.connect(("192.168.43.115",4))
		t = "slave"
		p.send(t.encode())
		session.send(p.recv(1024))
		continue
	
	elif ch == "client":
		os.system("ansible-playbook /root/Desktop/project/playbooks/java.yml")
		os.system(""" echo "export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/" >> /root/.bashrc """)
		os.system(""" echo "export PATH=/usr/java/jdk1.8.0_171-amd64/bin/:$PATH" >> /root/.bashrc """)
		os.system("ansible-playbook /root/Desktop/project/playbooks/hadoop.yml")		
		p = socket.socket()
		p.connect(("192.168.43.115",4))
		t = "client"
		p.send(t.encode())
		session.send(p.recv(1024))
		continue

	elif ch == "start":
		os.system("ansible-playbook /root/Desktop/project/playbooks/java.yml")
		os.system(""" echo "export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/" >>/root/.bashrc """)
		os.system(""" echo "export PATH=/usr/java/jdk1.8.0_171-amd64/bin/:$PATH" >> /root/.bashrc """)
		os.system("ansible-playbook /root/Desktop/project/playbooks/hadoop.yml")		
		p = socket.socket()
		p.connect(("192.168.43.115",4))
		t = "start"
		p.send(t.encode())
		session.send(p.recv(1024))
		continue
	
	elif ch == "list":
		os.system("ansible-playbook /root/Desktop/project/playbooks/java.yml")
		os.system(""" echo "export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/" >> /root/.bashrc """)
		os.system(""" echo "export PATH=/usr/java/jdk1.8.0_171-amd64/bin/:$PATH" >> /root/.bashrc """)
		os.system("ansible-playbook /root/Desktop/project/playbooks/hadoop.yml")		
		p = socket.socket()
		p.connect(("192.168.43.115",4))
		t = "list"
		p.send(t.encode())
		session.send(p.recv(1024))
		continue

	elif ch == "upload":
		os.system("ansible-playbook /root/Desktop/project/playbooks/java.yml")
		os.system(""" echo "export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/" >> /root/.bashrc """)
		os.system(""" echo "export PATH=/usr/java/jdk1.8.0_171-amd64/bin/:$PATH" >> /root/.bashrc """)
		os.system("ansible-playbook /root/Desktop/project/playbooks/hadoop.yml")		
		p = socket.socket()
		p.connect(("192.168.43.115",4))
		t = "upload"
		p.send(t.encode())
		session.send(p.recv(1024))
		continue

	elif ch == "read":
		os.system("ansible-playbook /root/Desktop/project/playbooks/java.yml")
		os.system(""" echo "export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/" >> /root/.bashrc """)
		os.system(""" echo "export PATH=/usr/java/jdk1.8.0_171-amd64/bin/:$PATH" >> /root/.bashrc """)
		os.system("ansible-playbook /root/Desktop/project/playbooks/hadoop.yml")		
		p = socket.socket()
		p.connect(("192.168.43.115",4))
		t = "read"
		p.send(t.encode())
		session.send(p.recv(1024))
		continue

	elif ch == "delete":
		os.system("ansible-playbook /root/Desktop/project/playbooks/java.yml")
		os.system(""" echo "export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/" >> /root/.bashrc """)
		os.system(""" echo "export PATH=/usr/java/jdk1.8.0_171-amd64/bin/:$PATH" >> /root/.bashrc """)
		os.system("ansible-playbook /root/Desktop/project/playbooks/hadoop.yml")		
		p = socket.socket()
		p.connect(("192.168.43.115",4))
		t = "delete"
		p.send(t.encode())
		session.send(p.recv(1024))
		continue
	
		
	elif ch == "install":
		op = sp.getstatusoutput("ansible-playbook /root/Desktop/project/playbooks/docker.yml")
		if op[0] == 0:
			t = "Docker installed"
		else:
			t = "Docker not installed"
		session.send(t.encode())
		continue
	
	elif ch == "docker":
		op = sp.getstatusoutput("ansible-playbook /root/Desktop/project/playbooks/docker_start.yml")
		if op[0] == 0:
			t = "Your container has been started"
		else:
			t = "We were unable to start your container"
		session.send(t.encode())
		continue

	elif ch == "httpd":
		op = sp.getstatusoutput("ansible-playbook /root/Desktop/project/playbooks/web.yml")
		if op[0] == 0:
			t = "Httpd service is configured"
		else:
			t = "Httpd service cannot be configured"
		session.send(t.encode())
		continue

	elif ch == "vlc":
		op = sp.getstatusoutput("ansible-playbook /root/Desktop/project/playbooks/vlc.yml")
		if op[0] == 0:
			t = "VLC launched"
		else:
			t = "VLC was not launched"
		session.send(t.encode())
		continue

	elif ch == "mail":
		op = sp.getstatusoutput("ansible-playbook /root/Desktop/project/playbooks/mail.yml")
		if op[0] == 0:
			t = "Mail has been sent"
		else:
			t = "Mail can not be sent"
		session.send(t.encode())		
		continue

	elif ch == "udev":
		p = socket.socket()
		p.connect(("192.168.43.115",5))
		t = "udev"
		p.send(t.encode())
		session.send(p.recv(1024))
		continue

#elif ch == "saas":
		

	elif ch == "s3":
		op = sp.getstatusoutput("ssh 192.168.43.22 ansible-playbook /root/Desktop/myansiblecode/s3.yml")
		if op[0] == 0:
			t = "S3 bucket is successfully created"
		else:
			t = "S3 bucket could not be created"
		session.send(t.encode())	
		continue

	elif ch == "upload s3":
		op = sp.getstatusoutput("ssh 192.168.43.22 ansible-playbook /root/Desktop/myansiblecode/s3_put.yml")
		if op[0] == 0:
			t = "data is successfully uploaded"
		else:
			t = "data could not be uploaded"
		session.send(t.encode())
		continue

	elif ch == "download s3":
		op = sp.getstatusoutput("ssh 192.168.43.22 ansible-playbook /root/Desktop/myansiblecode/s3_download.yml")
		if op[0] == 0:
			t = "data is successfully downloaded"
		else:
			t = "data could not be downloaded"
		session.send(t.encode())
		continue
	
	elif ch == "delete s3":
		op = sp.getstatusoutput("ssh 192.168.43.22 ansible-playbook /root/Desktop/myansiblecode/s3_delobj.yml")
		if op[0] == 0:
			t = "data is successfully deleted"
		else:
			t = "data could not be deleted"
		session.send(t.encode())
		continue
	
	elif ch == "ec2":
		op = sp.getstatusoutput("ssh 192.168.43.22 ansible-playbook /root/aws.yml")
		if op[0] == 0:
			t = "EC2 instance is successfully launched"
		else:
			t = "EC2 instance could not be launched"
		session.send(t.encode())	
		continue

	elif ch == "firefox":
		op = sp.getstatusoutput("ansible-playbook /root/Desktop/project/playbooks/firefox.yml")
		if op[0] == 0:
			t = "firefox successfully launched"
		else:
			t = "firefox was not launched"
		session.send(t.encode())
		continue

	elif ch == "user":
		op = sp.getstatusoutput("ansible-playbook /root/Desktop/project/playbooks/user.yml")
		if op[0] == 0:
			t = "user successfully added"
		else:
			t = "user not added"
		session.send(t.encode())
		continue

	elif ch == "exit":
		f = open("/etc/ansible/hosts" , "w")
		f.write("localhost" + "\tansible_user=root" + "\tansible_ssh_pass=redhat\n")
		f.close()
		continue

