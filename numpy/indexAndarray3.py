# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 20:32:15 2017

@author: yanpeng
"""

import scipy.misc
import matplotlib.pyplot as plt


# 加载 Lena 图像
# Load the Lena array
face=scipy.misc.face()
height = face.shape[0] 
width = face.shape[1]
width = face.shape[0]
#ymax = face.shape[1]报错
# 使用花式索引将对角线上的元素设为 0
# x 为 0 ~ width - 1 的数组
# y 为 0 ~ height - 1 的数组
face[range(height), range(width)] = 0


# 将副对角线上元素也设为 0
# x 为 width - 1 ~ 0 的数组
# y 为 0 ~ height - 1 的数组
face[range(height), range(width - 1, -1, -1)] = 0

# 画出带对角线的 Lena 图像
plt.imshow(face) 
plt.show()