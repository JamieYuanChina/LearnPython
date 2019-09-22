from PIL import Image
import numpy as np
a = np.asarray(Image.open('an.jpg').convert('L')).astype('float')
# 利用像素之间的梯度值和虚拟深度值对图像进行重构，根据灰度变化来模拟人类视觉的明暗成都

depth = 10.   # 预设深度值为10，取值范围(0-100)
grad = np.gradient(a)  # 提取图像的灰度梯度值
grad_x,grad_y = grad  # 分别取横纵图像梯度值，也就是提取x和y方向的梯度值
grad_x = grad_x*depth/100.  # 根据深度调整x和y方向的梯度值，添加深度影响，除100归一化 
grad_y = grad_y*depth/100.
A = np.sqrt(grad_x**2 + grad_y**2 +1.)
uni_x = grad_x/A
uni_y = grad_y/A
uni_z = 1./A

vec_el = np.pi/2.2  # 光源的俯视角度，弧度值
vec_az = np.pi/4.  # 光源的方位角度，弧度值
dx = np.cos(vec_el)*np.cos(vec_az)  # 光源对x轴的影响
dy = np.cos(vec_el)*np.sin(vec_az)  # 光源对y轴的影响
dz = np.sin(vec_el)  # 光源对z轴的影响

b = 255*(dx*uni_x + dy* uni_y + dz*uni_z)  # 光源归一化
b = b.clip(0,255)

im = Image.fromarray(b.astype('uint8'))
im.save('er.jpg')
