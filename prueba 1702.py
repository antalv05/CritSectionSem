#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 10:40:31 2022

@author: alumno
"""

from multiprocessing import 
def f(l,i):
    l.acquire()
    try:
        print ('hello world',i)
    finally:
        l.release()
    if __name__=='__main__':
        lock=Lock()
        
        for num in range(10):
            Process(target=f,args(lock,num)).start()
        