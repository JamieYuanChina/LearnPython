import jieba
import wordcloud
txt = "程序设计语言是计算机能够理解和识别用户操作意图的一中交互体系，\
它按照戈丁规则组织计算机指令，使计算机能够自动进行跟中运算处理。"
w = wordcloud.WordCloud(width=1000, font_path="msmincho.ttc", height=700)
w.generate(" ".join(jieba.cut(txt)))
w.to_file("pywcloud.png")