#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import colors
import os 

# 将列表变成可以迭代的cmaps
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


# 工厂函数，根据file 产生对应的rgb列表
class Work:
    def __init__(self,filename):
        self.absfile = os.path.dirname(os.path.abspath(__file__))
        self.path = os.path.join(self.absfile,'ncar_colormaps',filename+'.rgb')
        self.filename = filename
        self.rgb = None
        self.colors = None
        self.number = 0
    def open_file(self):
        file = open(self.path)
        data=file.readlines()
        n=len(data)
        self.number = n
        self.rgb=np.zeros((n,3))
        for i in np.arange(n):
            self.rgb[i][0]=data[i].strip().split(' ')[0]
            self.rgb[i][1]=data[i].strip().split(' ')[1]
            self.rgb[i][2]=data[i].strip().split(' ')[2]
        return self.rgb 

# 根据自定义的列表将原rgb文件中对应的颜色值映射到新的rgb列表中
# 添加了默认的配置项，使用默认的ncl_ffault 调色板,并默认产生前十号颜色的文件
class Submap(Work):
    def __init__(self,filename='ncl_default',subl=[i for i in range(10)]):
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


if __name__=='__main__':
    print("factory is being run directly")
    # product full rgb list based on rgbfile
    print(Work('ncl_default').open_file())


    # product sublist file based on rgbfile and list item
    l=[2,8,6,4,9,9,158]
    #print(Submap('ncl_default',l).sublist())

    # test work._call_
    #a=Work('ncl_default')
    #a()

