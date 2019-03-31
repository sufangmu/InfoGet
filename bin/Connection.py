#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import paramiko  
  
  
class Connect:  
  
    def __init__(self, hostname, username, password, port=22):  
        self.hostname = hostname  
        self.username = username  
        self.password = password  
        self.port = port  
  
    def connect(self):  
        t = paramiko.Transport((self.hostname, self.port))  
        t.connect(username=self.username, password=self.password)  
        self.__transport = t  
  
    def command(self, command):  
        ssh = paramiko.SSHClient()  
        ssh._transport = self.__transport  
        stdin, stdout, stderr = ssh.exec_command(command)  
  
        try:  
            result_out = stdout.readlines()  
            for line in result_out:  
                line = line.strip("\n")  
                print(line)  
  
        except Exception as e:  
            print(e)  
  
        finally:  
            result_err = stderr.readlines()  
            for line in result_err:  
                line = line.strip("\n")  
                print(line)  
  
    def upload(self, src, dest):  
        sftp = paramiko.SFTPClient.from_transport(self.__transport)  
        try:  
            sftp.put(src, dest)  
        except Exception as e:  
            print(e)  
  
    def close(self):  
        self.__transport.close()  
  
  
