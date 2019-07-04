#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys 
from .factory import Colormap,Work,Submap 
import matplotlib.pyplot as mp
import numpy as np
import math
import os 
#import threading
from multiprocessing import Process 
from .config import outlistrgb
#print("这是一个可以将ncl调色板套用到matplotlib调色板的第三方软件包")
class Cmaps(Submap,Colormap):
    # 打印该软件包所支持的ncl调色版
    def __str__(self):
        return str(outlistrgb())
    # 根据指定列表生成一个制定的Colormap，该调色板可以迭代
    def listmap(self):
        #self.open_file()
        self.sublist()
        result = Colormap(self.colors)
        return result
    # 产生所对应rgb文件所需要的所有文件
    def originalmap(self):
        self.open_file()
        result = Colormap(self.rgb)
        return result
    # 绘制所调用的ncl调色板
    def plot(self):
        cmaps=self.originalmap()
        self.row= math.ceil(self.number**0.5)
        mp.figure(self.filename, facecolor='lightgray')
        for i in range(self.number):
            fillcolor = np.outer(np.ones(10), np.arange(0, 1, 0.1))
            mp.subplot(self.row,self.row,i+1)
            mp.xticks([])
            mp.yticks([])
            mp.imshow(fillcolor, cmap=cmaps[i],aspect='auto',origin='lower')
            mp.text(5, 5, i, size=8, alpha=1,ha='center',va='center')
        mp.show()
    # 创建一个新的进程用来绘图，避免和原图产生冲突
    def show(self):
        print("begin to plot Colormap in another process")
        self.process= Process(target=self.plot,)
        self.process.start()