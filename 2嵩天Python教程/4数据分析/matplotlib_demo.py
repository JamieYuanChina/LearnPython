#! /usr/bin/env python   
# -*- coding: utf-8 -*- 

import matplotlib.pyplot as plt

plt.plot([3,1,4,5,2])
plt.plot([0,2,4,6,8],[3,1,4,5,2]) # 当有两个以上参数时，按照x轴和y轴顺序绘制数据点
plt.ylabel("Grade")
plt.axis([-1,10,0,6])  # 设置x轴范围和y轴范围
plt.savefig('test',dpi=600)  # 保存为PNG文件
plt.show()