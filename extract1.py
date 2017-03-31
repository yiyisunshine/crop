# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 09:11:10 2017

@author: yiyi

This is a extract multi-label file.
"""
#读取.json文件遍历每个场景
import json

for number in range(0,30):
    path='D:/Epan/mul/test/'
    fullpath=path+str(number)+'.json'
    fh=open(fullpath,'rb')
    images=json.load(fh)
    #提取前四个标签
    def exlabel(n,*a):        
        if  a[0]*a[1]*a[2]*a[3]!=0:
            b=[a[0],a[1],a[2],a[3]]
            b=[0 if i==-1 else i for i in b]
            return b
        else:       
            return n    
    #遍历每个file_name,取出可用的b-box和对应的标签        
    for i in range(0,len(images)):
        filename=images[i]['file_name']
        dellist=[]
        images[i].pop('scene_id') 
        
        for j in range(0,len(images[i]['targets'])):
            label=images[i]['targets'][j]['attribute']
            k=exlabel(j,*label)
            if isinstance(k,int)==True:
                dellist.append(k)  
            else:            
                images[i]['targets'][j]['attribute']=k
        #删除不明确图片 
        ex=[]          
        for d in dellist:        
            ex.append(images[i]['targets'][d])
        for e in ex:   
            images[i]['targets'].remove(e)
    #创建并写入
    newpath=path+'extract/'+'extract'+str(number)+'.json'
    fp=open(newpath,'w')
    json.dump(images,fp)
    fp.close()