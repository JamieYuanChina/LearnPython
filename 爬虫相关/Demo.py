# 引入库
import requests
import re #正则表达式
# 写网站站点
url = "http://www.jingcaiyuedu.com/novel/GLSmM4.html"
# 写入headers模拟浏览器上网,避免出现个别网站拒绝访问的情况
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",}
# get发送请求
response = requests.get(url, headers=headers)
# 将网页编码方式转换为utf-8
response.encoding = 'utf-8'
# 网站源码
html = response.text
# re.findall获取小说的名字
title = re.findall(r'<meta property="og:title" content="(.*?)"/>', html)
print(title)
# 获取每一章的信息(章节的url)
dl = re.findall(r'<dl class="panel-body panel-chapterlist">.*?</dl>', html, re.S)

print(dl)
