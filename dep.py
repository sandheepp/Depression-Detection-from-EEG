from scipy import stats
import numpy as np

dep_left_cl=[]
i=1
while(i<31):
    data=[]
    f=open('G:\Major project\Depression work data\depression-mat\\leftclosed'+str(i)+'.txt')
    for line in f:
        data.append(line.rstrip("\n").strip(" "))
    data = list(filter(None, data))
    data=np.asarray(data[:60000]).astype(float)
    data = stats.zscore(data, axis=0)
    temp=np.array_split(data,100)
    dep_left_cl.extend(temp)
    i=i+1

   
dep_right_cl=[]
i=1
while(i<31):
    data=[]
    f=open('G:\Major project\Depression work data\depression-mat\\leftclosed'+str(i)+'.txt')
    for line in f:
        data.append(line.rstrip("\n").strip(" "))
    data = list(filter(None,data))
    data=np.asarray(data[:60000]).astype(float)
    data = stats.zscore(data, axis=0)
    temp=np.array_split(data,100)
    dep_right_cl.extend(temp)
    i=i+1
    
dep_left_op=[]
i=1
while(i<31):
    data=[]
    f=open('G:\Major project\Depression work data\depression-mat\\leftclosed'+str(i)+'.txt')
    for line in f:
        data.append(line.rstrip("\n").strip(" "))
    data = list(filter(None,data))
    data=np.asarray(data[:60000]).astype(float)
    data = stats.zscore(data, axis=0)
    temp=np.array_split(data,100)
    dep_left_op.extend(temp)
    i=i+1

dep_right_op=[]
i=1
while(i<31):
    data=[]
    f=open('G:\Major project\Depression work data\depression-mat\\leftclosed'+str(i)+'.txt')
    for line in f:
        data.append(line.rstrip("\n").strip(" "))
    data = list(filter(None,data))
    data=np.asarray(data[:60000]).astype(float)
    data = stats.zscore(data, axis=0)
    temp=np.array_split(data,100)
    dep_right_op .extend(temp)
    i=i+1

