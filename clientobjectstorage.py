#!/usr/bin/python
import commands
commands.getstatusoutput('mkdir /media/rahul')
commands.getstatusoutput('mount 192.168.2.15:/server/rahul /media/rahul')
