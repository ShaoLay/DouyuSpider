#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Lay-Shao
from selenium import webdriver
import time
from bs4 import BeautifulSoup


class DouyuSpider(object):
    def __init__(self):
        self.url = 'https://www.douyu.com/directory/all'
        self.driver = webdriver.Chrome()
        self.count = 0

    def analysis_data(self, data):
        soup = BeautifulSoup(data, 'lxml')
        room_list = soup.select('.DyListCover-intro')
        user_list = soup.select('.DyListCover-user')
        hot_list = soup.select('.DyListCover-hot')
        for room, user, hot in zip(room_list, user_list, hot_list):
            print u"房间名: " + room.get_text() + u"主播名 ：" + user.get_text() + u"观看人数： " + hot.get_text()
            self.count += 1

    def run(self):
        self.driver.get(self.url)
        data = self.driver.page_source
        self.analysis_data(data)
        while True:
            if data.find('tabindex') != -1:
                next_element = self.driver.find_element_by_xpath('//li[@class=" dy-Pagination-next"]//span[@class="dy-Pagination-item-custom"]')
                next_element.click()
                time.sleep(1)
                data = self.driver.page_source
                self.analysis_data(data)
            else:
                break
        print '总个数:', self.count

if __name__ == '__main__':
    DouyuSpider().run()
