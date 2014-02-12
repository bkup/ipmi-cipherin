ipmi-cipherin
=============

Script to change IPMI credentials via Cipher 0 bypass.

A simple python script that uses a local ipmitool binary to dump user lists, change username, or change password.  Changing a password also results in escalting priviledges.  Once changed, a user can log into the web application assoicated with the BMC (ssh as well).

The local ipmitool included is from the Kali Linux repo.  Included in the package in case no internet connectivity is available.  

Quickly done, errors and bugs likely.  Feel free to improve.
