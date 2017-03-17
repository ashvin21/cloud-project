#!/usr/bin/python

import os,commands,cgi,cgitb,time

cgitb.enable()

print "content-type:text/html"
print ""

form=cgi.FieldStorage()

size=form.getvalue("size")
name=form.getvalue("name")

a=commands.getstatusoutput("sudo lvcreate   --size "+size+"M  --name  " + name + "  cloudstorage")
print a
if a[0]==0:
	ba=commands.getstatusoutput("sudo echo '<target " + name + ">\n backing-store /dev/cloudstorage/"+name+" \n</target>'  >> /etc/tgt/targets.conf")
	print ba
else :
	print "Error in LV creation"

commands.getstatusoutput("sudo systemctl restart tgtd ; iptables -F ; setenforce 0")

####################CLIENT SIDE CODE##################

if ba[0]==0:
	commands.getstatusoutput("sudo touch client.py")
	commands.getstatusoutput("sudo chmod 777 client.py")
	f=open('client.py','w')
	f.write("#!/usr/bin/python \n")
	f.write("import commands,os \n")
	f.write("a=commands.getstatusoutput('iscsiadm --mode discoverydb --type sendtargets --portal 192.168.2.15 --discover') \n")
	f.write("b=commands.getstatusoutput('iscsiadm --mode node --targetname " + name + " --portal 192.168.2.15:3260 --login') \n")
	f.write("print a \n")
	f.write("print b \n")
	f.close()

else :
	print "error in setting up tgtd"
time.sleep(4)
commands.getstatusoutput("sudo tar -cvf client.tar client.py")
commands.getstatusoutput("sudo cp -rvf client.tar /var/www/html/")

print   "<META HTTP-EQUIV=refresh CONTENT='0 ; URL=http://192.168.2.15/client.tar\n'>"



	





