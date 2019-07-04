# Packagename: ncmaps

#### a nc colormap used in matplotlib(python)

#### 一个将ncl的调色板自由的用在matplotlib上的库

#### 软件编写背景
目前ncl对python的支持并不完善,主要缺陷在于，所提供的pyngl库操作复杂，功能不全，且官方更新缓慢，在库开发前，国内一位大神[hhuangwx](https://github.com/hhuangwx/cmaps)开发了一套能在python上使用ncl调色板的第三方库cmaps,但是这个库只能调用所有颜色的调色板，对于当有需要自定义每条等值线内填充颜色的需求时，cmaps并不够用，并且其自带的show()方法过于简单，仅仅能够查看颜色阈，并不能精细的查找对应颜色的色号。鉴于本人没有找到能够比cmaps更好的第三方调色板，于是自己动手，借鉴[hhuangwx](https://github.com/hhuangwx/cmaps)和matplotlib源码，开发了ncmaps。目前仅支持颜色版的精细化使用，后续会进一步将ncl自带的气象统计方法集成出来，敬请期待！

#### python＆ncl使用ncl调色板绘图核心api的对比

## 所依赖的第三方库
1. matplotlib
    - ```python
      pip install matplotlib
      ```
2. numpy
    - ```python
      pip install numpy
      ```
## ncmaps安装方法

### 方法一

pip install 

### 方法二

python setup.py -install 

### 方法三

CV大法

## 功能核心类　Cmaps(rgbfilename,list)
**Cmaps(rgbfilename,list)**

- 参数：
    1.  rgbfilename : 所选用的ncl官方提供调色板的名称(区分大小写)，默认为ncl_default
    2.  list 自己定制的一个列表，该列表中存储所选用调色板对应颜色的色号
- 返回值：　
    -   返回一个colorbar

## Cmaps(filename,list)对应的方法和参数说明

1. 查找所支持的ncl调色板名称
    - 使用方法：
        - ```python
          from ncmaps import Cmaps
          #以下是核心api,实质为调用Cmaps基类的listmap()方法
          print(Cmaps())
          ```

2. 根据ncl调色板生成满足个性化需求的调色板
    - 使用方法：
        - ```python
          from ncmaps import Cmaps
          self_define_list = [2,10,12,50,90,255,155]
          rgb_file = 'ncl_default'
          #以下是核心api,实质为调用Cmaps基类的listmap()方法
          cmaps = Cmaps('ncl_default',l).listmap()
          ```


3. 使用ncl官网的调色板(以调用NCV_blu_red为例)
    - 使用方法：
        - ```python
          from ncmaps import Cmaps
          rgb_file = 'ncl_default'
          #以下是核心api,实质为调用Cmaps基类的originalmap()方法
          cmaps = Cmaps('NCV_blu_red').originalmap()
          ```

4. 可视化所选取ncl调色板的色号索引，方便自定义列表
    - 使用方法：
        - ```python
          from ncmaps import Cmaps
          #以下是核心api,实质为调用Cmaps基类的show()方法
          rgb_file = 'NCV_blu_red'
          cmaps = Cmaps('NCV_blu_red').show()
          ```


## 完整的绘图实例(以绘制slp为例)

```python
import os

```