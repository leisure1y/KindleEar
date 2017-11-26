#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re, datetime
import urllib
import json
from bs4 import BeautifulSoup
from lib.urlopener import URLOpener
from base import BaseFeedBook
from config import SHARE_FUCK_GFW_SRV
from config import SHARE_SRV

def getBook():
    return DDgest

class DDgest(BaseFeedBook):
    title                 = u'Daily Digest'
    __author__            = 'calibre'
    description           = u'每周科技新闻精选，知乎问答精选，Quora精选，豆瓣，博客，经济学人China和Tech部分，各种科普，果壳天文，深夜食堂，数学精选。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_dailynews.gif"
    coverfile             = "cv_dailynews.jpg"
    network_timeout       = 60
    oldest_article        = 7
    max_articles_per_feed = 15
    deliver_days          = []
    feeds = [
        ('瞎扯', 'http://zhihurss.miantiao.me/section/id/2'),
        (u'豆瓣一刻', 'http://yikerss.miantiao.me/rss'),
        (u'知乎日报', 'http://zhihurss.miantiao.me/dailyrss'),
        ('知乎精选', 'http://www.zhihu.com/rss'),
        ('深夜食堂', 'http://zhihurss.miantiao.me/section/id/1'),
        (u'Quora ', 'http://www.quora.com/rss'，True),
        (u'MIT科技评论', 'http://www.technologyreview.com/topnews.rss',true),
        ]

    def url4forwarder(self, url):
        ' 生成经过转发器的URL '
        return SHARE_FUCK_GFW_SRV % urllib.quote(url)

    def url4forwarder_backup(self, url):
        ' 生成经过转发器的URL '
        return SHARE_SRV % urllib.quote(url)

    def fetcharticle(self, url, opener, decoder):
        """链接网页获取一篇文章"""
        if self.fulltext_by_instapaper and not self.fulltext_by_readability:
            url = "http://www.instapaper.com/m?u=%s" % self.url_unescape(url)
        if "daily.zhihu.com" in url:
            url = self.url4forwarder(url)
    
        return self.fetch(url, opener, decoder)