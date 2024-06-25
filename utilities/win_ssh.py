#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @Site: 
# @File: win_ssh.py.py
# @Author: PGQ
# @E-mail: panguoqing.pgq@sunyur.com
# @Time: 5月 28, 2021
# ---
import paramiko

class WinSSH:

    def __init__(self):
        self.server_ip = '47.103.49.219'
        self.server_user = 'viewlog'
        self.server_passwd = '1234@qwer'
        self.server_port = 22
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.server_ip, self.server_port, self.server_user, self.server_passwd)

    def ssh_disconnect(self):
        self.ssh.close()


    def exec_cmd(self ,command):
        '''
        windows客户端远程执行linux服务器上命令
        '''

        stdin, stdout, stderr = self.ssh.exec_command(command)
        err = stderr.readline()
        out = stdout.readline()
        self.ssh_disconnect()

        if "" != err:
            print("command: " + command + " exec failed!\nERROR :" + err)
            return err
        else:
            print("command: " + command + " exec success.")
            return out


    def win_to_linux(self,localpath, remotepath):
        '''
        windows向linux服务器上传文件.
        localpath  为本地文件的绝对路径。如：D:\test.py
        remotepath 为服务器端存放上传文件的绝对路径,而不是一个目录。如：/tmp/my_file.txt
        '''
        client = paramiko.Transport((self.server_ip, self.server_port))
        client.connect(username=self.server_user, password=self.server_passwd)
        sftp = paramiko.SFTPClient.from_transport(client)
        sftp.put(localpath, remotepath)
        client.close()


    def linux_to_win(self,localpath, remotepath):
        '''
        从linux服务器下载文件到本地
        localpath  为本地文件的绝对路径。如：D:\test.py
        remotepath 为服务器端存放上传文件的绝对路径,而不是一个目录。如：/tmp/my_file.txt
        '''
        client = paramiko.Transport((self.server_ip, self.server_port))
        client.connect(username=self.server_user, password=self.server_passwd)
        sftp = paramiko.SFTPClient.from_transport(client)
        sftp.get(remotepath, localpath)
        client.close()

if __name__ == '__main__':
    cm="cd ~ |sh test.sh 18206760713"
    sh=WinSSH()
    cl=sh.exec_cmd(cm)
    print(cl)

