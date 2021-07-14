#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ctypes

if __name__ == '__main__':
    cLib = ctypes.CDLL("D:/1-nsfocus/0713_python调c库/libJITClientAPI64.so")


    hContext = ctypes.c_void_p()
    ServerPort = ctypes.c_long(60502)
    cLib.InitServerConnectEx(hContext, None, ServerPort)