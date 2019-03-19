#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Time    : 19-1-15
# Author  : Gao Peng
# Email   : gaopeng0214@126.com
# File    : test.py

import psutil

# 分区 挂载点 使用率
# for partition in psutil.disk_partitions():
#     print(partition.device, partition.mountpoint, psutil.disk_usage(partition.mountpoint).percent)

for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
    print(proc.info)

class bar(object):

    """Docstring for bar. """

    def __init__(self):
        """TODO: to be defined1. """
name = "helo"


