#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import colors
import os 

# 将列表编程可以迭代的cmaps
class Colormap(colors.ListedColormap):
    def __init__(self, c, name='from_list', n=None):
        '''Initialization'''
        self._colors = c
        self._name = name
        self._N = n

        # call parent __init__
        super(Colormap, self).__init__(self._colors, name=self._name, N=self._N)

    def __getitem__(self, item):
        return Colormap(self._colors[item], name='sliced_' + self._name)


# 工厂函数，根据
class Work:
    def __init__(self,filename):
        self.path = os.path.join('ncar_colormaps',filename+'.rgb')
        self.filename = filename
        self.rgb = None
        self.colors = None
    def open_file(self):
        file = open(self.path)
        data=file.readlines()
        n=len(data)
        self.rgb=np.zeros((n,3))
        for i in np.arange(n):
            self.rgb[i][0]=data[i].strip().split(' ')[0]
            self.rgb[i][1]=data[i].strip().split(' ')[1]
            self.rgb[i][2]=data[i].strip().split(' ')[2]
        return self.rgb 
#    def __call__(self):
#        print("666")
#        self.open_file()

class Submap(Work):
    def __init__(self,filename,subl):
        super().__init__(filename)
        self.l=subl
    def sublist(self):
        self.rgb = self.open_file()
        n = len(self.l)
        self.colors = np.zeros((n,3))
        for i in range(n):
            j = self.l[i]
            self.colors[i]=self.rgb[j]
        return self.colors

def show():
    pass

if __name__=='__main__':
    print("factory is being run directly")
    # product full rgb list based on rgbfile
    #print(Work('ncl_default').open_file())


    # product sublist file based on rgbfile and list item
    l=[2,8,6,4,9,9,158]
    #print(Submap('ncl_default',l).sublist())

    # test work._call_
    #a=Work('ncl_default')
    #a()

## ncmaps(ncl_default,list)

## 产生一个新的map

## ncmaps(ncl_default,list).show()

## 绘制一个map地图


## Colormap的作用

# 两个类 

# 1 cmaps 的colormap 
## 用来装饰转换好的rgb文件

# 2 读取已有的文件，讲rgb文件转化成列表

## 1. 读取rgb文件并转换成数组
## 2. 将rgb文件转换成