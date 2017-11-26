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
    return tech

class tech(BaseFeedBook):
    title                 = u'Tech News'
    __author__            = 'calibre'
    description           = u'ÿ�ܿƼ����ž�ѡ��֪���ʴ�ѡ��Quora��ѡ�����꣬���ͣ�����ѧ��China��Tech���֣����ֿ��գ��������ģ���ҹʳ�ã���ѧ��ѡ��'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_technews.gif"
    coverfile             = "cv_technews.jpg"
    network_timeout       = 60
    oldest_article        = 7
    max_articles_per_feed = 9
    deliver_days          = ['Friday']
    feeds = [
        ('Ϲ��', 'http://zhihurss.miantiao.me/section/id/2'),
        (u'����һ��', 'http://yikerss.miantiao.me/rss'),
        (u'֪���ձ�', 'http://zhihurss.miantiao.me/dailyrss'),
        ('֪����ѡ', 'http://www.zhihu.com/rss'),
        ('��ҹʳ��', 'http://zhihurss.miantiao.me/section/id/1'),
        (u'Quora ', 'http://www.quora.com/rss'),
        (u'MIT�Ƽ�����', 'http://www.technologyreview.com/topnews.rss'),
        ]

    def url4forwarder(self, url):
        ' ���ɾ���ת������URL '
        return SHARE_FUCK_GFW_SRV % urllib.quote(url)

    def url4forwarder_backup(self, url):
        ' ���ɾ���ת������URL '
        return SHARE_SRV % urllib.quote(url)

    def fetcharticle(self, url, opener, decoder):
        """������ҳ��ȡһƪ����"""
        if self.fulltext_by_instapaper and not self.fulltext_by_readability:
            url = "http://www.instapaper.com/m?u=%s" % self.url_unescape(url)
        if "daily.zhihu.com" in url:
            url = self.url4forwarder(url)
        if "economist.com" in url:
            url = self.url4forwarder(url)
    
        return self.fetch(url, opener, decoder)