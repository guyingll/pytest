# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 19:03:35 2017

@author: yanpeng
"""

import scipy.misc
import numpy as np
import matplotlib.pyplot as plt

face=scipy.misc.face()

# copy 创建副本，Python 对象复制，内部内存复制
acopy = face.copy() 

# view 创建视图，Python 对象复制，内部内存共享
aview = face.view()

# 绘制 Lena 图像（左上角）
plt.subplot(221) 
plt.imshow(face)


# 绘制副本（右上角） 
plt.subplot(222) 
plt.imshow(acopy)


# 绘制视图（左下角）
plt.subplot(223) 
plt.imshow(aview)


# 将副本所有元素清零
# 由于数组的数据保存在内部内存中
# 副本不受影响，视图（以及引用）会跟着变化
aview.flat = 0


plt.subplot(224)

plt.imshow(aview)