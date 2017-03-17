#!/usr/bin/python 
import commands,os 
a=commands.getstatusoutput('iscsiadm --mode discoverydb --type sendtargets --portal 192.168.2.15 --discover') 
b=commands.getstatusoutput('iscsiadm --mode node --targetname trt --portal 192.168.2.15:3260 --login') 
print a 
print b 
