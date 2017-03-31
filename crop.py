# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 09:20:40 2017

@author: yiyi
"""
import json
from PIL import Image
import os
import os.path
from skimage import io,data
import numpy as np

def crop(images):
    for i in range(0,len(images)):
        fn=images[i]['file_name']
        for j in range(0,len(images[i]['targets'])):
            newfn=fn.replace('.jpg',str(j)+'.jpg')
            cropmake(fn,newfn,images[i]['targets'][j]['bbox'],images[i]['targets'][j]['attribute'])
def lv(x,y):
    return str(x)+' '+str(y)

def cropmake(fn,newfn,bbox,attribute):
    loc='D:/Epan/mul/Image/'
    im=Image.open(loc+fn)  
    #bbox[2]=bbox[0]+bbox[2]
    #bbox[3]=bbox[1]+bbox[3]
    left = bbox[0]
    top = bbox[1]
    width = bbox[2]
    height = bbox[3]
    bbox = (left, top, left+width,top+height)
    bbox=tuple(bbox)
    try:
        newim=im.crop(bbox)
        #newim=im[left:left+width,top:top+height]   
        newloc=loc+'newImage/'
        crop_fn=newloc+newfn
        newim.save(crop_fn)
        label_value=reduce(lv,attribute)
    except SystemError:
        print "Error: 没有找到图片或图片剪裁失败"
    
    else:
                
        if 'test/' in newfn:            
            f=open(newloc+'test.txt','a+')
            item='%s %s\n' % (newfn,label_value)
            f.write(item)
            f.close()
        '''else:
            f=open(newloc+'val.txt','a')
            f.write('%s %s\n' % (newfn,label_value))
            f.close()
            '''
path='D:/Epan/mul/test/extract/'
for num in range(0,30):
    fullpath=path+'extract'+str(num)+'.json'
    fp=open(fullpath,'r')
    images=json.load(fp)
    fp.close()
    crop(images)
    


            
            

        
        
         
    
'''    newim=crop(bbox)
    #newim=im[left:left+width,top:top+height]   
    newloc=loc+'newImage/'
    crop_fn=newloc+newfn
    os.makedirs(crop_fn)
    newim.save(crop_fn)
    label_value=reduce(lv,attribute)
    if 'train/' in newfn:
        f=open(newloc+'train.txt','a+')
        item='%s %s\n' % (newfn,label_value+r'\n')
        f.write(item)
        f.write(r'\n')
        f.close()
    else:
        
        f=open(newloc+'val.txt','a')
        f.write('%s %d' % (newfn,label_value))
        f.close()
        '''
  