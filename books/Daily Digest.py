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
    title                 = u'Daily Digest'
    __author__            = 'calibre'
    description           = u'瞎扯，豆瓣一刻，知乎日报，知乎精选，深夜食堂，Quora，MIT科技评论'
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
        ('瞎扯', 'http://zhihurss.miantiao.me/section/id/2'),
        (u'豆瓣一刻', 'http://yikerss.miantiao.me/rss'),
        (u'知乎日报', 'http://zhihurss.miantiao.me/dailyrss'),
        ('知乎精选', 'http://www.zhihu.com/rss'),
        ('深夜食堂', 'http://zhihurss.miantiao.me/section/id/1'),
        (u'Quora ', 'http://www.quora.com/rss'),
        (u'MIT科技评论', 'http://www.technologyreview.com/topnews.rss'),
        ]

   
