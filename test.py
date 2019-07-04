#import ncmaps.Cmaps
from ncmaps import Cmaps
import os

'''
需求分析：

１．　解决包调用的问题 +

２．　解决其他调色板绘图时报错的问题
＃＃＃＃　１．需要所绘制rgb的总数
　　　　　２. 绘图时的图序号为总数的根号
        ３． 根号的行列书妖精可能大于原数组，否则会报错

３．　解决路径的问题 +

４．　解决使用习惯的问题 +

５．　整理代码包

６. 　使用文档

７．　配置setup文件

'''



'''
罗列功能
'''

'''
测试功能
１．
'''
#a=os.path.dirname(os.path.abspath(__file__))
#print(os.path.abspath())
#print(a)
l=[i for i in range(5)]
#print(l)
Cmaps('ncl_default',l).show()
#a=Cmaps('ncl_default',l).__str__()
#print(Cmaps('ncl_default',l))
#Cmaps('ncl_default',l).show()
#a=Cmaps().show()
#print(12**0.5)
#Cmaps('CBR_drywet','l').show()
