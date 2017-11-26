#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re1, datetime1
import urllib1
import json1

from config import SHARE_FUCK_GFW_SRV

from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag

def getBook():
    return Economist111

class Economist111(BaseFeedBook):
    title                 = 'The Economist111'
    description           = 'Global news and current affairs from a European perspective. deliver on Friday.'
    language              = 'en'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_economist.gif"
    coverfile             = "cv_economist.jpg"
    deliver_days          = ['Friday']
    
    remove_classes = ['ec-messages',]
    feeds = [
        ('The world this week', 'http://www.economist.com/rss/the_world_this_week_rss.xml'),
        ('Letters', 'http://www.economist.com/rss/letters_rss.xml'),
        ('Leaders', 'http://www.economist.com/rss/leaders_rss.xml'),
        ('Briefings', 'http://www.economist.com/rss/briefings_rss.xml'),
        ('Special reports', 'http://www.economist.com/rss/special_reports_rss.xml'),
        ('Britain', 'http://www.economist.com/rss/britain_rss.xml'),
        ('Europe', 'http://www.economist.com/rss/europe_rss.xml'),
        ('United States', 'http://www.economist.com/rss/united_states_rss.xml'),
        ('The Americas', 'http://www.economist.com/sections/americas/rss.xml'),
        ('Middle East and Africa', 'http://www.economist.com/rss/middle_east_and_africa_rss.xml'),
        ('Asia', 'http://www.economist.com/feeds/print-sections/73/asia.xml'),
        ('China', 'http://www.economist.com/feeds/print-sections/77729/china.xml'),
        ('International', 'http://www.economist.com/rss/international_rss.xml'),
        ('Business', 'http://www.economist.com/rss/business_rss.xml'),
        ('Finance and economics', 'http://www.economist.com/rss/finance_and_economics_rss.xml'),
        ('Science and technology', 'http://www.economist.com/feeds/print-sections/80/science-and-technology.xml'),
        ('Books and arts', 'http://www.economist.com/rss/books_and_arts_rss.xml'),
        ('Obituary', 'http://www.economist.com/rss/obituary_rss.xml'),
        ('Indicators', 'http://www.economist.com/rss/indicators_rss.xml'),
        ('Business and finance','http://www.economist.com/sections/business-finance/rss.xml'),
        ('Economic','http://www.economist.com/sections/economics/rss.xml'),
        ('Culture','http://www.economist.com/sections/culture/rss.xml'),
        ]
    
 def url4forwarder(self, url):
        ' 生成经过转发器的URL '
        return SHARE_FUCK_GFW_SRV % urllib1.quote(url)

    def url4forwarder_backup(self, url):
        ' 生成经过转发器的URL '
        return SHARE_SRV % urllib1.quote(url)

    def fetcharticle(self, url, opener, decoder):
        """链接网页获取一篇文章"""
        if self.fulltext_by_instapaper and not self.fulltext_by_readability:
            url = "http://www.instapaper.com/m?u=%s" % self.url_unescape(url)
        if "daily.zhihu.com" in url:
            url = self.url4forwarder(url)
		if "economist.com" in url:
            url = self.url4forwarder(url)

        return self.fetch(url, opener, decoder)