# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 19:28:12 2017

@author: yanpeng
"""

import scipy.misc
import matplotlib.pyplot as plt

face=scipy.misc.face()

plt.subplot(221) 
plt.title('Original') 
plt.axis('off') 
plt.imshow(face)


plt.subplot(222)
plt.title('Flipped')
plt.axis('off')
plt.imshow(face[:,::-1])


# 添加掩码，将偶数元素变为 0 
# 布尔数组可用作索引 
mask = face % 2 == 0 
masked_lena = face.copy()
masked_lena[mask] = 0 

# 绘制添加掩码后的图像（右下角）
plt.subplot(224) 
plt.title('Masked') 
plt.axis('off') 
plt.imshow(masked_lena)


plt.subplot(223)
plt.title('Sliced')
plt.axis('off')
print (face.shape[0]/2,face.shape[1]/2)
face_3=face[:int(face.shape[0]/2),:int(face.shape[1]/2)]
#face_3=face[:,:500]
plt.imshow(face_3)

plt.show()


#http://blog.csdn.net/wizardforcel/article/details/72793092