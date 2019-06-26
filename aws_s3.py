#!/usr/bin/python36

import subprocess as sp
import cgi,cgitb
cgitb.enable()

print("content-type:text/html\n")

data = cgi.FieldStorage()
access_key = data.getvalue('access')
secret_key = data.getvalue('secret')
bucketname = data.getvalue('name')


launch = sp.getstatusoutput(f"""sudo ansible-playbook aws_s3.yml --extra-vars 'access_key={access_key} secret_key={secret_key} bucketname={bucketname}'"""}

if launch[0] == 0:
	print("<h3>S3 Bucket created</h3>")
else:
	print("<h3>Unable to create S3 bucket</h3>")
