#!/usr/bin/python2

import  cgi,cgitb
import  os,commands,time
from random import randint

cgitb.enable()

print  "content-type:text/html"
print  ""

data=cgi.FieldStorage()

osn=data.getvalue('osn')
osr=data.getvalue('r')
osc=data.getvalue('c')
osh=data.getvalue('h')
osp=data.getvalue('p')

a=randint (7777 , 9999)


print  "______________________"


print  commands.getstatusoutput('sudo virt-install --name ' + osn + ' --ram ' + osr + ' --vcpu ' + osc + ' --disk path=/var/lib/libvirt/images/'+osn + ' --graphics vnc,listen=0.0.0.0,port='+osp + '  --import  --noautoconsole')


print commands.getoutput('sudo websockify -D '+str(a)+'  192.168.0.110:'+osp)

time.sleep(2)

print  "plz wait for os "

print  "<a href='http://192.168.0.110/noVNC/vnc.html?host=ashvinee&port="+str(a)+"'target='_blank'>click here to access your os</a>"








