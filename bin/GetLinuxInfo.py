#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Time    : 19-3-30
# Author  : Gao Peng
# Email   : gaopeng0214@126.com
# File    : GetLinuxInfo.py

import Linux
from Connection import ConnectHost
from logger import logger
from ParseHostList import hosts


def getlinuxinfo(hostname, username, password, port, sudo=False):
    hostinfo = {}
    host = ConnectHost(host=hostname, user=username, passwd=password, port=port, sudo=sudo)
    try:
        host.conn()

        hostinfo["hostname"] = host.get(Linux.hostname)
        hostinfo["os"] = host.get(Linux.os)
        hostinfo["arch"] = host.get(Linux.arch)
        hostinfo["virtual"] = host.get(Linux.virtual)
        hostinfo["distribution"] = host.get(Linux.distribution)
        hostinfo["version"] = host.get(Linux.version)
        hostinfo["kernel"] = host.get(Linux.kernel)
        hostinfo["cpu_physical"] = host.get(Linux.cpu_physical)
        hostinfo["cpu_cores"] = host.get(Linux.cpu_cores)
        hostinfo["cpu_logical"] = host.get(Linux.cpu_logical)
        hostinfo["memory_total"] = host.get(Linux.memory_total)
        hostinfo["memory_available"] = host.get(Linux.memory_available)
        hostinfo["ip"] = host.get(Linux.ip)
        hostinfo["disk_total"] = host.get(Linux.disk_total)
        hostinfo["disk_used"] = host.get(Linux.disk_used)
        hostinfo["filesystem"] = host.get(Linux.filesystem)
        host.close()

        return hostinfo
    except Exception:
        msg = " Connect {} Failed".format(hostname)
        print(msg)
        logger.error(msg)


hostname = "192.168.1.41"
username = "shuowei"
password = "shuowei123"
port = 22


for host in hosts:
    hostname = host['hostname']
    username = host['username']
    password = host['password']
    port = int(host['port'])
    sudo = host['sudo']
    if sudo == "False" or sudo == "True":
        sudo = sudo
    logger.info("get {} info".format(hostname))
    info = getlinuxinfo(hostname=hostname, username=username, password=password, port=port, sudo=sudo)
    # print(info['disk_used'])
    print(info)
    logger.info("{} info {}".format(hostname, info))
