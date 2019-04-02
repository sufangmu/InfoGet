#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Time    : 19-1-28
# Author  : Gao Peng
# Email   : gaopeng0214@126.com
# File    : logger.py
import logging

logfile = "infoget.log"

# 创建一个 logger
logger = logging.getLogger('main')
# 设置一个总的日志级别
logger.setLevel(logging.DEBUG)
# 创建一个输出到控制台的handler并设置日志级别

# 设置日志格式
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(name)s %(levelname)s : %(message)s')

# 输出日志到文件
fh = logging.FileHandler(logfile)
fh.setLevel(logging.DEBUG)
# 设置日志的格式

fh.setFormatter(formatter)
# 将handler添加到logger
logger.addHandler(fh)
