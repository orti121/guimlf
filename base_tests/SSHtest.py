#!/usr/bin/env python

import paramiko

import time

from getpass import getpass

HOST = '192.168.0.11'
USER = 'pi'

if __name__ == "__main__":
    try:
        #paramiko.util.log_to_file('paramiko.log')

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy( paramiko.AutoAddPolicy())

        passwd = getpass ('Ingrese su contraseña: ')
        client.connect(HOST, username = USER, password = passwd)

        stdin, stdout, stderr = client.exec_command('ls')

        time.sleep(0.1)

        result = stdout.read().decode()

        print (result)

        client.close()

    except:
        print ('Autenticación Fallida')
