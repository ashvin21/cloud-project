#!/usr/bin/python2

import cgi
import  cgitb
import  commands,os,time
cgitb.enable()
from random import randint
print  "content-type:text/html"
print  ""

data=cgi.FieldStorage()

puser=data.getvalue('p')

a=randint (7777 , 9999)


if  puser == 'python':
	commands.getoutput('sudo docker run -itd  -p ' + str(a)+':4200 nn/hadoop2')
	print  "plz wait for python launch !!"
	print  "<a href='https://192.168.2.15:"+str(a)+"'>"
	print   "click here for python"
	print   "</a>"

elif  puser == 'ruby':
	commands.getoutput('sudo docker run -itd -p ' + str(a)+':4200 ruby')
	print  "plz wait for ruby launching !!"
	print  "<a href='https://192.168.2.15:"+str(a)+"'>"
	print   "click here for ruby"
	print   "</a>"
elif  puser == 'perl':
	print  "perl is reloading "
else :
	print  "wrong choice !!"
	



