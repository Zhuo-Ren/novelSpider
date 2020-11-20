# -*- coding: utf-8 -*-
import _pickle as cPickle
from novelspider import novelSpider

# path to chromeDriver
path_to_chrome_driver = r'C:/ProgramFiles/chromedriver/chromedriver.exe'
# whether use headless module of chrome
headless = False
# 小说第一章的url
start_url = r'http://www.biquge.info/10_10581/5101997.html'

# 初始化浏览器driver
novelSpider.init_driver(path_to_chrome_driver, headless)

# 爬取
r = novelSpider.search_one_novel(start_url=start_url)

# 处理
with open('./r.pkl', 'wb') as pkl_file:
    cPickle.dump(r, pkl_file)

# 释放浏览器driver
novelSpider.close_driver()
