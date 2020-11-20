# -*- coding: utf-8 -*-

from typing import Dict, List, Tuple, Union, Callable  # for type hinting
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
import re
import time


class novelSpider():
    # chrome driver
    driver = None  # webdriver.Chrome()

    # extract strategy
    extract_strategy = {
        "www.biquge.info": {
            "title_xpath": "//div[@class='bookname']/h1[1]",
            "content_xpath": "//div[@id='content']",
            "next_url_xpath": "//a[text()='下一章']"
        }
    }

    @staticmethod
    def init_driver(path_to_chrome_driver: str, headless: bool = True):
        """
        初始化chrome driver
        
        :param path_to_chrome_driver: The path to chrome driver.
        :param headless: Whether use headless module.
        :return: 
        """
        # 创建options
        options = Options()
        # options添加启动参数
        if headless:
            options.add_argument('--headless')  # 无头模式(不展示界面)
        options.add_argument('log-level=3')  # INFO = 0 WARNING = 1 LOG_ERROR = 2 LOG_FATAL = 3 default is 0
        # options添加试验选项
        prefs = {
            "profile.managed_default_content_settings.images": 2,  # 禁用图片
            'profile.default_content_setting_values': {'notifications': 2}  # 禁用弹窗
        }
        options.add_experimental_option("prefs", prefs)
        # 创建driver
        novelSpider.driver = webdriver.Chrome(
            options=options,
            executable_path=path_to_chrome_driver
        )

    @staticmethod
    def close_driver():
        # baidusearcher.driver.close()  # 关闭当前窗口，如果是当前打开的最后一个窗口，则退出浏览器（driver）
        novelSpider.driver.quit()  # 关闭所有相关的窗口，退出浏览器（driver）

    @staticmethod
    def search_one_novel(start_url):
        r = []
        next_url = start_url
        domain = re.search('(?<=//)[^/]*', start_url).group()
        while 1:
            # 访问
            novelSpider.driver.get(next_url)
            # 获取信息
            html_str = novelSpider.driver.page_source
            html_root = etree.HTML(html_str)
            cur_title = html_root.xpath(r"string(" + novelSpider.extract_strategy[domain]["title_xpath"] + ")")
            cur_content = html_root.xpath(r"string(" + novelSpider.extract_strategy[domain]["content_xpath"] + ")")
            # 结束
            if html_root.xpath(novelSpider.extract_strategy[domain]["next_url_xpath"]) == []:
                return r
            else:
                next_url = html_root.xpath(novelSpider.extract_strategy[domain]["next_url_xpath"])[0].attrib['href']
                time.sleep(3)
                r.append((cur_title, cur_content))


