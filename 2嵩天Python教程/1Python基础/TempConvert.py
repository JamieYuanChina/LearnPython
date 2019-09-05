# TempConver.py
Temp_str = input("请输入温度：")
if Temp_str[-1] in ['f', 'F']:
    # C = (int(Temp_str[0:-1])-32)/1.8
    # print("%s 华氏度等于 %.2f 摄氏度！" % (Temp_str[0:-1], C))
    C = (eval(Temp_str[0:-1])-32)/1.8  # 使用评估函数转换字符串为数字
    print("%s 华氏度等于 {:.2f} 摄氏度！".format(C) % Temp_str[0:-1])  # 使用槽格式化输出
elif Temp_str[-1] in ['c', 'C']:
    # F = (int(Temp_str[0:-1])*1.8)+32
    # print("%s 摄氏度等于 %.2f 华氏度！" % (Temp_str[0:-1], F))
    F = (eval(Temp_str[0:-1])*1.8)+32
    print("%s 摄氏度等于 {:.2f} 华氏度！".format(F) % Temp_str[0:-1])
else:
    print("请输入正确的温度值!")
