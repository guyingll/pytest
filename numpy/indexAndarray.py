# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import scipy.misc
import numpy as np
import matplotlib.pyplot as plt


face=scipy.misc.face()

#宽高
LENA_X=512
LENA_Y=512

# 设置调整系数，水平 3，竖直 2
yfactor = 2
xfactor = 3

# 调整图像尺寸，水平（沿轴 1）拉伸 3 倍，竖直（沿轴 0 ）拉伸两倍
resized = face.repeat(yfactor, axis=0).repeat(xfactor, axis=1)
              
# 绘制原图像（两行一列的第一个位置）
plt.subplot(211) 
plt.title("face") 
# plt.axis("off") 
plt.imshow(face)

# 绘制调整后图像（两行一列的第二个位置）
plt.subplot(212) 
plt.title("Resized") 
# plt.axis("off") 
plt.imshow(resized) 
plt.show()


