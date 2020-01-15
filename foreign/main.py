# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2020-01-07 14:12 '

from scrapy.cmdline import execute

import sys
import os


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

execute(["scrapy","crawl","Investing"])