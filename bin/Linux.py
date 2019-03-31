#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Time    : 19-3-29
# Author  : Gao Peng
# Email   : gaopeng0214@126.com
# File    : commands.py

# 底层虚拟化  物理cpu个数 核数 逻辑cpu个数


hostname = "hostname"
os = "uname -o"
arch = "arch"
virtual = "dmidecode -s system-product-name 2> /dev/null || echo Unknown"
distribution = "lsb_release -is || awk -F [0-9] '{print $1}' /etc/issue  | head -n 1"
version = "lsb_release -rs || egrep -o [0-9]+\.?([0-9]+\.?[0-9]*)? /etc/issue"
kernel = "uname -r"
cpu_physical = "grep 'physical id' /proc/cpuinfo | sort | uniq | wc -l"
cpu_cores = "grep 'cpu cores' /proc/cpuinfo | sort  | uniq | awk '{print $4}'"
cpu_logical = "grep 'processor' /proc/cpuinfo  | wc -l"
memory_total = "awk '/MemTotal/ {print $2}' /proc/meminfo"
memory_available = "awk '/MemAvailable/ {print $2}' /proc/meminfo'}"
ip = "hostname -I"
disk_total = "lsblk -d | awk  '/disk/ {print $1,$4}' | sed -n 's/ /:/p' | tr '\n' ';'"
disk_used = "for disk in $(lsblk -d | awk '/disk/ {print $1}');do echo $disk:$(df -x tmpfs -x devtmpfs -x aufs " \
            "| awk   '/'$disk'/ {sum += $3;} END{print sum}');done"
filesystem = "df -x tmpfs -x devtmpfs -x aufs | awk '{print $1,$6,$5}'| sed -n 's/ /:/gp' | tr '\n' ';'"
open_port = "netstat  -lant | awk '/LISTEN/ {print $4}' | awk  -F : '{print $NF}' | tr '\n' ' '"


