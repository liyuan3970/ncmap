from factory import * 


import matplotlib.pyplot as mp


'''
需求分析
# 这是一个包装工厂函数的类
## 具体功能如下

### 1. 讲work 和　submap的list功能利用Colormap函数封装成对应的画图map

### 2. 将 work方法所对应的颜色绘制出来，方便查询

### 3. 提供查阅所有支持的调色板方法列表

## 所需要的数据

### 1. 颜色版对应的名字字符串

### 2. 定制颜色所需的列表

'''
class Cmaps(Submap,Colormap):
    def __str__(self):
    	filepath = os.listdir('ncar_colormaps')
    	return str(filepath)
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
    def show(self):
        cmaps=self.originalmap()
        mp.figure(self.filename, facecolor='lightgray')
        for i in range(254):
            a = np.outer(np.ones(10), np.arange(0, 1, 0.1))
            mp.subplot(16,16,i+1)
            mp.xticks([])
            mp.yticks([])
            mp.imshow(a, cmap=cmaps[i],aspect='auto',origin='lower')
            mp.text(5, 5, i, size=8, alpha=1,ha='center',va='center')
        mp.show()

        



if __name__=='__main__':
    print('这是一个测试包函数的代码')
    l=[2,8,6,4,9,9,158]
    #print(Cmaps('ncl_default',l).sublist())
    #print(Cmaps('ncl_default',l))
    #help(Cmaps('ncl_default',l))
    #print(Cmaps('ncl_default',l).listmap().N)
    Cmaps('ncl_default',l).show()
