#!/usr/bin/python

import os,commands,cgi,cgitb

cgitb.enable()

print "content-type:text/html"
print ""

form=cgi.FieldStorage()

soft=form.getvalue("soft")
print soft

commands.getstatusoutput("sudo touch saasclient.py")
commands.getstatusoutput("sudo chmod 777 saasclient.py")
f=open('saasclient.py','w')
f.write("#!/usr/bin/python \n")
f.write("import commands,os \n")
f.write("commands.getstatusoutput('ssh -X root@192.168.122.1 " + soft + " ') \n")
#f.write("print a \n")
f.close()




commands.getstatusoutput("sudo tar -cvf saasclient.tar saasclient.py")
commands.getstatusoutput("sudo cp -rvf saasclient.tar /var/www/html/")

print   "<META HTTP-EQUIV=refresh CONTENT='0 ; URL=http://192.168.122.1/saasclient.tar\n'>"



	





