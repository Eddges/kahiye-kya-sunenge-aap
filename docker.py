#!/usr/bin/python36   


import subprocess 
import cgi  

print("content-type: text/html") 
print()   

form = cgi.FieldStorage()  

docker_name = form.getvalue("n") 
docker_image = form.getvalue("img")    


docker_run = "sudo docker run -d -i -t --name  {}  {}".format(docker_name ,  
docker_image)   


x = subprocess.getoutput(docker_run) 
print(x)
