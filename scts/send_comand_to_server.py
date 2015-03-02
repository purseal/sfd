#!/usr/bin/env python3
''' This program sends a comand to the server
    and transform its output in a readable view.
'''

from subprocess import Popen, PIPE
import paramiko
import os
import sys

class DataGetter:
    ''' Abstract class for any data downloader. '''

    def get_data(self, string):
        ''' Dowload all informayion from given ip address.
            Return string value, containing downloaded data.
        '''
        pass

    def parse_data(self, data):
        ''' Parse given data. '''
        pass

class SshDataGetter(DataGetter):
    ''' Implementationt of DataGetter. '''

    def __init__(self):
        self.comand = ''
        self.username = ''
        self.ip = ''
        self.password = ''
        self.data = ''

    def split_to_values(self, given_string):
        ''' Method splits a string to list of values. '''
        given_string = given_string.strip()
        comand_begin = given_string.find("'")
        comand_end = given_string.find("'", comand_begin + 1)
        string = given_string[:comand_begin - 1] + given_string[comand_end + 1:]
        words = string.split(' ')
        for word in words:
            if word == "":
                words.remove(word)
        words.append(given_string[comand_begin + 1:comand_end])
        return words

    def get_values(self, string):
        ''' Method assigns data to specified fields. '''
        list_of_values = self.split_to_values(string)
        self.username = list_of_values[2]
        self.ip = list_of_values[3]
        self.password = list_of_values[4]
        self.comand = list_of_values[5]

    def get_my_data(self):
        my_file = open('/home/maria/prog/my_data', 'r')
        data = my_file.readlines()
        self.ip = data[0]
        self.username = data[1]
        self.password = data[2]
        my_file.close()


    def get_data(self):
        ''' Method connects to server and sends the comand. '''
     #этот способ выдает ошибку идентификации
     #File "/usr/local/lib/python3.4/dist-packages/paramiko/transport.py", line 1168, in auth_password
     #return self.auth_handler.wait_for_response(my_event)
     #File "/usr/local/lib/python3.4/dist-packages/paramiko/auth_handler.py", line 208, in wait_for_response
     #raise e
     #paramiko.ssh_exception.AuthenticationException: Authentication failed.

     #   ssh = paramiko.SSHClient()
     #   ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
     #   print ('before connection')
     #   ssh.connect(self.ip, username=self.username,
     #       password=self.password, look_for_keys=False
     #       )
     #   print ('after connection')
     #   stdin, stdout, stderr = ssh.exec_command(self.comand)
     #   self.data = stdout.read()
     #   ssh.close()

#        os.system('ssh ' + self.ip)
#        sys.stdin(bytes(self.password))
#        os.system(self.password)
#        proc = subprocess.Popen(self.command, stdout=subprocess.PIPE)
#        self.data = proc.stdout.read()

        #здесь выходит ошибка Permission denied (publickey,password).
        proc = Popen(['ssh', self.ip], stdin=PIPE)
        print('after ssh 127.0.0.1')
        proc.stdin.write(self.password)
        proc.stdin.flush()
        print('after stdin.write')
        proc = Popen(self.comand, stdout=PIPE)
        proc.wait()
        print('after command')
        self.data = proc.stdout.read()
        print('after stdout')
        return self.data