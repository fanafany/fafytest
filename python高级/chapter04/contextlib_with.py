# _*_ coding: utf-8 _*_
__author__ = 'fanafany'
__date__ = '2019-08-07 15:32 '

import contextlib

@contextlib.contextmanager
def file_open(file_name):
    print("file open")
    yield {}
    print("file end")

with file_open("fanafany.txt")as f_opend:
    print("file processing")