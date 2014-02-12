ipmi-cipherin
=============

Script to change IPMI credentials via Cipher 0 bypass.

A simple python script that uses a local ipmitool binary to dump user lists, change username, or change password.  Changing a password also results in escalting priviledges.  Once changed, a user can log into the web application assoicated with the BMC (ssh as well).
