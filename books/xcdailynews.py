#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re, datetime
import urllib
import json
from bs4 import BeautifulSoup
from lib.urlopener import URLOpener
from base import BaseFeedBook
from config import SHARE_FUCK_GFW_SRV

def getBook():
    return tech

class tech(BaseFeedBook):
    title                 = u'ϯ���ձ�'
    __author__            = 'calibre'
    description           = u'ÿ�����š�Ӣ��ѧϰ!'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_xcnews.gif"
    coverfile             = "cv_xcnews.jpg"
    network_timeout       = 90
    oldest_article        = 1
    max_articles_per_feed = 15
    deliver_days          = []

    feeds = [
            (u'��Ѷ���', 'http://hanhanone.sinaapp.com/feed/dajia'),
            (u'BBC������', 'http://www.bbc.co.uk/zhongwen/simp/index.xml'),
            (u'֪���ձ�', 'http://zhihurss.miantiao.me/dailyrss'),
            (u'36�', 'http://36kr.com/feed'),
            (u'ѩ�к�����', 'http://www.8shuw.com/BookReader/8-8001.xml', True),
            (u'Oneһ��', 'http://onehd.herokuapp.com/', True),
            (u'����Ӣ��', 'http://www.hjenglish.com/new/rss/'),
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

        return self.fetch(url, opener, decoder)