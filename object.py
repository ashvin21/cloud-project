#!/usr/bin/python2

import  cgi,cgitb
import  os,commands,time

cgitb.enable()

print  "content-type:text/html"
print  ""

x=cgi.FieldStorage()
d_name=x.getvalue('d')
d_size=x.getvalue('s')


print "<pre>"
print commands.getstatusoutput('sudo  lvcreate  --name '+d_name+'  --size '+d_size+'M  cloudstorage')
print commands.getstatusoutput('sudo mkfs.xfs   /dev/cloudstorage/'+d_name)
print commands.getstatusoutput('sudo mkdir  /server/'+d_name)
print commands.getstatusoutput('sudo mount  /dev/cloudstorage/'+d_name+'  /server/'+d_name)
print commands.getstatusoutput(' sudo echo "/server/'+d_name +' *(rw,no_root_squash)" >/etc/exports')
print commands.getstatusoutput('sudo exportfs -r')
print "</pre>"

print "successfully Done"

#####################client Side##################


commands.getstatusoutput("sudo touch client.py")
commands.getstatusoutput("sudo chmod 777 client.py")
f=open('clientobjectstorage.py','w')
f.write('#!/usr/bin/python\n')
f.write('import commands\n')
f.write("commands.getstatusoutput('mkdir /media/"+d_name+"')\n")
f.write("commands.getstatusoutput('mount 192.168.2.15:/server/"+d_name+" /media/"+d_name+"')\n")
f.close()


commands.getstatusoutput("sudo tar -cvf client.tar clientobjectstorage.py")
commands.getstatusoutput("sudo cp -rvf client.tar /var/www/html/")

time.sleep(4)

print   "<META HTTP-EQUIV=refresh CONTENT='0 ; URL=http://192.168.2.15/client.tar\n'>"



