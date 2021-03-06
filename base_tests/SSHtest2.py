#!/usr/bin/env python

import paramiko
from getpass import getpass

hostname = '192.168.0.11'
port = '22'
user = 'pi'

try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        passcode = getpass ('Ingrese su contraseña: ')
        client.connect (hostname, port = port, username = user, password = passcode)
        while True:
            try:
                cmd = input ("$> ")
                if cmd == "exit":break
                stdin,stdout,stderr = client.exec_command(cmd)
                print(stdout.read().decode())
            
            except KeyboardInterrupt:
                break
        client.close()
except Exception as err:
    print (str(err))