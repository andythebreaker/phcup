#=======================================
#@file phcup.py
#@brief hronhub熱線擷取

#爬蟲pronhub影片
#取得熱線
#繪製熱線圖
#需求:py3.7.6
#環境:win10
#需要先安裝import的一堆東西

#@project phcup
#@company Koyonia, zzct, andythebreaker
#@author andythebreaker
#@date 2020/10/10
#=======================================

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from bs4 import BeautifulSoup
import urllib
import re
import csv
import sys

#轉換非ascii字元(預動作)
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

#get html
r = requests.get("")#請放置pronhub某影片的網址

#解析html
r.encoding = 'utf-8'#字元編碼轉換
soup = BeautifulSoup(r.text, "html.parser")#解析

#尋找影片長度關鍵字
m = re.search('\"video_duration\"\:\"(.+?\"', r.text)#使用正則表達式
if m:#如果成功找到影片長度
    found = m.group(1)#取第一個群組

#解析時間為時分秒格式
ound=int(found)
sec=ound%60
mint=(ound//60)%60#這裡使用取int商運算子
hr=(ound//60)//60

#尋找熱線(以svg點表示)
hot=re.search('\"hotspots\"\:\[(.+?)\]', r.text)#使用正則表達式
if hot:#如果成功找到影片熱線
    hott=hot.group(1)#取第一個群組

#取得熱線數據
my_list=hott.split(",")#將數據分點取出
#這裡變數的定義我忘了
hint=[]
lix=[]
det=ound/len(my_list)#因為熱線的數據點是不隨影片時長改變的，所以用平均的去求一個svg刻度代表多長的時間
idx=0
for sht in my_list:
    hint.append(int(sht))
    lix.append(idx*det)
    idx=idx+1

#建置熱線圖表
plt.plot(lix, hint)
plt.ylabel('hotline')
plt.xlable('time(sec)')
plt.title("video_time = "+str(hr)+":"+str(mint)+":"+str(sec))
plt.show()#繪圖
