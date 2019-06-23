#!/usr/bin/python36	

import os 
import subprocess as sp
import socket 

s = socket.socket()
ip  = "192.168.43.115"
port = 4
s.bind((ip,port))
s.listen(5)
session , addr = s.accept()
ch = session.recv(100).decode()
	
sp.getoutput("cp /etc/hadoop/hdfs-site.xml /root/")
sp.getoutput("cp /etc/hadoop/core-site.xml /root/")

def master_node_setup(file_ip,hostname):
	n="name"	
	hdfs_site(file_ip,n)
	core_site(hostname)
	os.system('ansible master -m copy -a "src=/root/hdfs-site.xml dest=/etc/hadoop"')	
	os.system('ansible master -m copy -a "src=/root/core-site.xml dest=/etc/hadoop"')	
	#os.system(f"scp /root/hdfs-site.xml {mip}:/root/")
	#os.system(f"scp /root/core-site.xml {mip}:/root/")
	#print(subprocess.getoutput(f"ssh {mip} mv /root/hdfs-site.xml  /etc/hadoop"))
	#print(subprocess.getoutput(f"ssh {mip} mv /root/core-site.xml  /etc/hadoop"))
	os.system('ansible master -m command -a "hadoop namenode -format"')

def slave_node_setup(file_ip,hostname):
	n="data"	
	hdfs_site(file_ip,n)
	core_site(hostname)
	os.system('ansible slave -m copy -a "src=/root/hdfs-site.xml dest=/etc/hadoop"')	
	os.system('ansible slave -m copy -a "src=/root/core-site.xml dest=/etc/hadoop"')	
	os.system('ansible slave -m command -a "hadoop-daemon.sh start datanode"')
	os.system('ansible slave -m command -a "iptables -F"')
	os.system('ansible slave -m command -a "jps"')
	t = "Node successfully configured"	
	session.send(t.encode())

	"""os.system(f"scp /root/hdfs-site.xml {sip}:/root/")
	os.system(f"scp /root/core-site.xml {sip}:/root/")
	print(subprocess.getoutput(f"ssh {sip} mv /root/hdfs-site.xml  /etc/hadoop"))
	print(subprocess.getoutput(f"ssh {sip} mv /root/core-site.xml  /etc/hadoop"))
"""
def client_node_setup(hostname):
	#os.system("cd /root/Desktop")
	#print(subprocess.getoutput("cp /etc/hadoop/hdfs-site.xml /root/"))
	os.system(f"mkdir {file_ip}")
	no_of_replicas = input("enter no. of replicas : ")
	f = open("/root/hdfs-site.xml" ,"w")	
	f.write(f"""<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- 	Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>dfs.replication</name>\n<value>{no_of_replicas}</value>\n</property>\n\n</configuration>""")
	f.close()

	core_site(hostname)
	os.system('ansible client -m copy -a "src=/root/hdfs-site.xml dest=/etc/hadoop"')	
	os.system('ansible client -m copy -a "src=/root/core-site.xml dest=/etc/hadoop"')	
	t = "Node successfully configured"	
	session.send(t.encode())
	
	
	#os.system(f"scp /root/hdfs-site.xml {cip}:/root/")
	#os.system(f"scp /root/core-site.xml {cip}:/root/")
	#print(subprocess.getoutput(f"ssh {cip} mv /root/hdfs-site.xml  /etc/hadoop"))
	#print(subprocess.getoutput(f"ssh {cip} mv /root/core-site.xml  /etc/hadoop"))


def hdfs_site(file_ip,n):
	#os.system("cd /root/Desktop")
	#print(subprocess.getoutput("cp /etc/hadoop/hdfs-site.xml /root/"))
	os.system(f"mkdir {file_ip}")
	f = open("/root/hdfs-site.xml" ,"w")	
	f.write(f"""<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- 	Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>dfs.{n}.dir</name>\n<value>/{file_ip}</value>\n</property>\n\n</configuration>""")
	f.close()


def core_site(hostname):
	#os.system("cd /root/Desktop")
	#print(subprocess.getoutput("cp /etc/hadoop/core-site.xml /root/"))
	f = open("/root/core-site.xml" ,"w")	
	f.write(f"""<?xml version="1.0"?>\n<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n<!-- 	Put site-specific property overrides in this file. -->\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://{hostname}:9001</value>\n</property>\n\n</configuration>""")
	f.close()

while True:
	if ch == "master":
		file_ip = input("enter name of file : ")
		#master_ip=input("enter namenode's ip :")
		hostname = input("enter hostname : ")	
		master_node_setup(file_ip,hostname)
		report = sp.getoutput("hadoop dfsadmin -report")
		session.send(report.encode())
		continue
	
	elif ch == "slave":
		file_ip = input("enter name of file : ")
		#slave_ip=input("enter datanode's ip :")
		hostname = input("enter hostname : ")	
		slave_node_setup(file_ip,hostname)
		continue

	elif ch == "client":
		#client_ip=input("enter client's ip :")
		hostname = input("enter hostname : ")	
		client_node_setup(hostname)
		continue

	elif ch == "start":
		os.system('ansible master -m command -a "hadoop-daemon.sh start namenode"')
		os.system('ansible master -m command -a "iptables -F"')
		os.system('ansible master -m command -a "jps"')
		continue

	elif ch == "upload":
		filename = input("Enter the name of file you want to upload : ") 
		op = sp.getstatusoutput('ansible client -m command -a "hadoop fs -put {filename} /" ')
		if op[0] == 0:
			t = "File uploded"
		else:
			t = "File not uploaded"
		session.send(t.encode())
		continue
	elif ch == "read":
		filename = input("Enter the name of file you want to read : ") 
		op = sp.getoutput('ansible client -m command -a "hadoop fs -cat /{filename} " ')
		session.send(op.encode())
		continue
	
	elif ch == "delete":
		filename = input("Enter the name of file you want to remove : ") 
		op = sp.getstatusoutput('ansible client -m command -a "hadoop fs -rm /{filename} " ')
		if op[0] == 0:
			t = "File Deleted"
		else:
			t = "File not deleted"
		session.send(t.encode())
		continue
	
	elif ch == "list":
		op = sp.getoutput('ansible client -m command -a "hadoop fs -ls /" ')
		session.send(op.encode())
		continue
	













""" def r_node_setup():
	print(""
	press 1 : for master node setup
	press 2 : for slave node setup
	press 3 : for client node setup
	press 4 : to start master node
	press 5 : to upload a file via cloud
	press 6 : to read a file 
	press 7 : to remove a file 

	"")
	
	x = int(input("enter your choice : "))	
	subprocess.getoutput("cp /etc/hadoop/hdfs-site.xml /root/")
	subprocess.getoutput("cp /etc/hadoop/core-site.xml /root/")

	if x == 1: 
		file_ip = input("enter name of file : ")
		master_ip=input("enter namenode's ip :")
		hostname = input("enter hostname : ")	
		r_master_node_setup(master_ip,file_ip,hostname)
		#os.system("hadoop-daemon.sh start namenode ")
		#os.system("iptables - F")
		#os.system("jps")
		#os.system("hadoop dfsadmin -report")
	elif x == 2:
		file_ip = input("enter name of file : ")
		slave_ip=input("enter datanode's ip :")
		hostname = input("enter hostname : ")	
		r_slave_node_setup(slave_ip,file_ip,hostname)
		os.system("hadoop-daemon.sh start datanode ")
		os.system("iptables - F")
		os.system("jps")
	elif x == 3:
		client_ip=input("enter client's ip :")
		hostname = input("enter hostname : ")	
		r_client_node_setup(client_ip,hostname)

"""




