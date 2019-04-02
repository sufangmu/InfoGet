#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import paramiko


class ConnectHost:

    def __init__(self, host, user, passwd, port=22, sudo=False):
        self.hostname = host
        self.username = user
        self.password = passwd
        self.port = port
        self.sudo = sudo
    def conn(self):
        try:
            t = paramiko.Transport((self.hostname, self.port))
            t.connect(username=self.username, password=self.password)
            self.__transport = t
        except Exception as e:
            print(e)

    def get(self, command):
        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport
        feed_password = False
        if self.sudo and self.username != "root":
            # command = "echo {} | sudo -S -p '' {}".format(self.password, command)
            command = '''sudo -S -p '' bash -c "{}"'''.format(command)
            feed_password = self.password is not None and len(self.password) > 0
        stdin, stdout, stderr = ssh.exec_command(str(command))
        # print(command)
        if feed_password:
            stdin.write(self.password + '\n')
            stdin.flush()

        try:
            result_out = stdout.readlines()
            for line in result_out:
                line = line.strip("\n")
                return line

        except Exception as e:
            print(e)

        finally:
            result_err = stderr.readlines()
            for line in result_err:
                line = line.strip("\n")
                return line

    def upload(self, src, dest):
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        try:
            sftp.put(src, dest)
        except Exception as e:
            print(e)

    def close(self):
        self.__transport.close()
