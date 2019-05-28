# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 07:02:33 2018

@author: sandh
"""
from scipy import stats
import numpy as np
nor_left_cl=[]
i=1
while(i<31):
    data=[]
    f=open('G:\Major project\Depression work data\\normal-mat\\leftclosed'+str(i)+'.txt')
    for line in f:
        data.append(line.rstrip("\n").strip(" "))
    data = list(filter(None,data))
    data=np.asarray(data[:60000]).astype(float)
    data = stats.zscore(data, axis=0)
    temp=np.array_split(data,100)
    nor_left_cl.extend(temp)
    i=i+1
    
nor_right_cl=[]
i=1
while(i<31):
    data=[]
    f=open('G:\Major project\Depression work data\\normal-mat\\leftclosed'+str(i)+'.txt')
    for line in f:
        data.append(line.rstrip("\n").strip(" "))
    data = list(filter(None,data))
    data=np.asarray(data[:60000]).astype(float)
    data = stats.zscore(data, axis=0)
    temp=np.array_split(data,100)
    nor_right_cl.extend(temp)
    i=i+1
    
nor_left_op=[]
i=1
while(i<31):
    data=[]
    f=open('G:\Major project\Depression work data\\normal-mat\\leftclosed'+str(i)+'.txt')
    for line in f:
        data.append(line.rstrip("\n").strip(" "))
    data = list(filter(None,data))
    data=np.asarray(data[:60000]).astype(float)
    data = stats.zscore(data, axis=0)
    temp=np.array_split(data,100)
    nor_left_op.extend(temp)
    i=i+1

nor_right_op=[]
i=1
while(i<31):
    data=[]
    f=open('G:\Major project\Depression work data\\normal-mat\\leftclosed'+str(i)+'.txt')
    for line in f:
        data.append(line.rstrip("\n").strip(" "))
    data = list(filter(None,data))
    data=np.asarray(data[:60000]).astype(float)
    data = stats.zscore(data, axis=0)
    temp=np.array_split(data,100)
    nor_right_op .extend(temp)
    i=i+1
