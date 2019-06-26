#!/usr/bin/python36

import subprocess as sp
import cgi,cgitb
cgitb.enable()

print("content-type:text/html\n")

data = cgi.FieldStorage()
access_key = data.getvalue('access')
secret_key = data.getvalue('secret')
bucketname = data.getvalue('name')
filename = data.getvalue('filename')


launch = sp.getstatusoutput(f"""sudo ansible-playbook s3_put.yml --extra-vars 'access_key={access_key} secret_key={secret_key} bucketname={bucketname} filename={filename}'"""}

if launch[0] == 0:
	print("<h3>'File uploaded successfully</h3>")
else:
	print("<h3>Unable to upload file</h3>")
