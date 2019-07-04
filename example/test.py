#import ncmaps.Cmaps
from ncmaps import Cmaps
import os

'''
需求分析：
１．　解决包调用的问题 +

２．　解决其他调色板绘图时报错的问题

３．　解决路径的问题 +

４．　解决使用习惯的问题

5. 　使用文档


'''
#a=os.path.dirname(os.path.abspath(__file__))
#print(os.path.abspath())
#print(a)
l=[1,2]
#Cmaps('ncl_default',l).show()
#a=Cmaps('ncl_default',l).__str__()
print(Cmaps('ncl_default',l))
#Cmaps('ncl_default',l).show()
a=Cmaps().show()
