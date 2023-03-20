#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# 歌词文本
text = """给你一瓶魔法药水

喝下去就不需要氧气

给你一瓶魔法药水

喝下去就不怕身体结冰

轻轻念着你懂的咒语

一扇门就通往银河系

给你一瓶魔法药水

我们一起去太空旅行

宇宙的有趣我才不在意

我在意的是 你牵我的手 而乱跳的心

宇宙的有趣我才不在意

我在意的是 你想跟着我 去月球谈心

拥有你 就不需要魔法给的勇气

轻轻念着你懂的咒语

一扇门就通往银河系

给你一瓶魔法药水

我们一起去太空旅行

宇宙的有趣我才不在意

我在意的是 你牵我的手 而乱跳的心

宇宙的有趣我才不在意

我在意的是 你想跟着我 去月球谈心

宇宙的有趣我才不在意

我在猜的是 前方的距离 几步走到你

宇宙的有趣我才不在意

我期待的是 今天的晚餐 你想吃哪里

拥有你就不需要魔法给的勇气

你走的方向最后到哪去

可能是火星或者是金星

不管多远多近多累都没关系

我的魔法只对你偏心

我偏心

我偏心

宇宙的有趣我才不在意

我在意的是 你牵我的手 而乱跳的心

宇宙的有趣我才不在意

我在意的是 你想跟着我 去月球谈心

宇宙的有趣我才不在意

我在猜的是 奔跑的距离 几步走到你

宇宙的有趣我才不在意

我期待的是 今天的晚餐 你想吃哪里

有你在

就不需要魔法给的勇气 
"""

# 获取形状
mask = np.array(Image.open('img/3.png'))

# 设置停用词
stopwords = set(["魔法", "宇宙", "有趣", "勇气"])

# 设置词云对象
wordcloud = WordCloud(width=800, height=800, background_color='white', font_path='C:\\Windows\\Fonts\\simsun.ttc', mask=mask, colormap='viridis', stopwords=set(stopwords)).generate(text)

# 绘制词云
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

# 显示词云
plt.show()