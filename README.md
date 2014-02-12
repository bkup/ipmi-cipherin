ipmi-cipherin
=============

Script to change IPMI credentials via Cipher 0 bypass

A simply python script that uses a local ipmitool binary to dump user lists, change username, or change password.  Changing password results in also escalting priviledges.  Once change a user can log into the web application assoicated with the BMC (ssh as well)
