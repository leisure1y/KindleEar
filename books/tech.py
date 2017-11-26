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
        ('36kr', 'http://www.36kr.com/feed?1.0'),
        (u'TechCrunch �й�', 'http://techcrunch.cn/feed/'),
        (u'������', 'http://www.ifanr.com/feed'),
        ('Top News - MIT Technology Review', 'http://www.technologyreview.com/topnews.rss'),
        ('Hacker News', 'https://news.ycombinator.com/rss'),
        (u'��ʡ�����Ƽ�����', 'http://zhihurss.miantiao.me/section/id/14'),
        (u'��˾�ձ�', 'http://zhihurss.miantiao.me/daily/id/5'),
        (u'С����Ϣ', 'http://hutu.me/feed'),
        (u'���͹�԰', 'http://www.geekpark.net/rss'),
        (u'���ͷ�', 'http://www.geekfan.net/feed/'),
        (u'���˶��ǲ�Ʒ����', 'http://iamsujie.com/feed/'),
        (u'�޽���Kant', 'http://kant.cc/feed'),
        ('warfalcon', 'http://ys.8wss.com/rss/oIWsFtxo3oqejVy4KaJ4RDMVIrE0/'),
        (u'����һ��', 'http://yikerss.miantiao.me/rss'),
        (u'�����ѧ', 'http://blog.sina.com.cn/rss/sciam.xml'),
        (u'���չ�԰', 'http://www.scipark.net/feed/'),
        (u'��ѧ�����', 'http://songshuhui.net/feed'),
        (u'����ѧ', 'http://pansci.tw/feed'),
        (u'������', 'http://www.guokr.com/rss/'),
        (u'��������ѧ��', 'http://feed43.com/8781486786220071.xml'),
        (u'�����Ƽ�', 'http://jianshu.milkythinking.com/feeds/recommendations/notes'),
        ('Quora', 'http://www.quora.com/rss', True),
        ('The Economist: China', 'http://www.economist.com/feeds/print-sections/77729/china.xml'),
        ('The Economist: Science and technology', 'http://www.economist.com/feeds/print-sections/80/science-and-technology.xml'),
        ('The Economist: Asia', 'http://www.economist.com/feeds/print-sections/73/asia.xml'),
        (u'֪���ձ�', 'http://zhihurss.miantiao.me/dailyrss'),
        (u'֪����ѡ', 'http://www.zhihu.com/rss'),
        (u'��ҹʳ��', 'http://zhihurss.miantiao.me/section/id/1'),
        (u'����������', 'http://feed43.com/3144628515834775.xml'),
        ('Matrix67', 'http://www.matrix67.com/blog/feed'),
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