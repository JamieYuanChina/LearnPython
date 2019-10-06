# LearnPython
这是一个学习Python的项目

#### 1、[黑马Python教程](./1黑马Python教程/README.md)


#### 2、[嵩天Python教程](./2嵩天Python教程/README.md)

学习Python过程用到过的库：

| 库名    | 功能         | 备注 |
| ------- | ------------ | ---- |
| random  | 随机数产生   | 标准库 |
| pygame  | 游戏编程     | 第三方库 |
| keyword | python关键字 | 标准库 |
| turtle | 绘图 | 第三方库python2.x |
| time | 时间相关 | 标准库，包括延时计时 |
| pyinstaller | 程序打包 | 第三方库 |
| jieba | 中文分词 | 第三方库python2.x |
| wordcloud | 词云展示库 | 第三方库 |
| os | 操作系统相关 | 标准库 |
| math | 数学库 | 比如pi |
| sys | 系统 | 比如sys.exit() |
| requests | 网页爬虫 | |
| beautiful soup | HTML，XML格式解析 | 美味汤 |
| re | 正则表达式 | 字符串操作，标准库 |
| traceback | 调试信息 | |
| Scrapy | 爬虫框架 | |
| numpy | 数据计算 | |
| PIL.Image | 图像 | |
| matplotlib | 数据绘图 | |
| pandas | 数据处理 | |
| django | web框架 | |
| scipy | 机器学习 | |
| VTK |  | |
| Mayavi |  | |
| Traits |  | |
| TraitsUI |  | |
| PyQt4 |  | |
|  |  | |




将pip源更换到国内镜像

用pip管理工具安装库文件时，默认使用国外的源文件，因此在国内的下载速度会比较慢，可能只有50KB/s。幸好，国内的一些顶级科研机构已经给我们准备好了各种镜像，下载速度可达2MB/s。
其中，比较常用的国内镜像包括：

（1）阿里云 http://mirrors.aliyun.com/pypi/simple/

（2）豆瓣http://pypi.douban.com/simple/

（3）清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/

（4）中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/

（5）华中科技大学http://pypi.hustunique.com/

注意：新版ubuntu要求使用https源。

设置方法：（以清华镜像为例，其它镜像同理）

（1）临时使用：

可以在使用pip的时候，加上参数-i和镜像地址(如https://pypi.tuna.tsinghua.edu.cn/simple)，

例如：pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas，这样就会从清华镜像安装pandas库。

（2）永久修改，一劳永逸：

（a）Linux下，修改 ~/.pip/pip.conf (没有就创建一个文件夹及文件。文件夹要加“.”，表示是隐藏文件夹)

内容如下：

```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = https://pypi.tuna.tsinghua.edu.cn
```

(b) windows下，直接在user目录中创建一个pip目录，如：C:\Users\xx\pip，然后新建文件pip.ini，即 %HOMEPATH%\pip\pip.ini，在pip.ini文件中输入以下内容（以豆瓣镜像为例）：

```
[global]
index-url = http://pypi.douban.com/simple
[install]
trusted-host = pypi.douban.com
```

