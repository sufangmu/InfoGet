#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Time    : 19-4-1
# Author  : Gao Peng
# Email   : gaopeng0214@126.com
# File    : ParseHostList.py

import csv

hostsfile = 'hosts.csv'


def host(hostsfile):
    hostslist = []
    with open(hostsfile, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            hostslist.append(row)

    return hostslist


hosts = host(hostsfile)
