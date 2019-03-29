#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Time    : 19-3-29
# Author  : Gao Peng
# Email   : gaopeng0214@126.com
# File    : commands.py

# 底层虚拟化  物理cpu个数 核数 逻辑cpu个数

physical_cpu="grep 'physical id' /proc/cpuinfo | sort | uniq | wc -l"
cores_cpu=""