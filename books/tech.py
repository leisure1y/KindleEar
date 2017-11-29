#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup

def getBook():
    return tech

class tech(BaseFeedBook):
    title                 = u'Tech News'
    description           = u'每周科技新闻精选，知乎问答精选，Quora精选，豆瓣，博客，经济学人China和Tech部分，各种科普，果壳天文，深夜食堂，数学精选。'
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
        (u'36kr', 'http://www.36kr.com/feed?1.0'),
        (u'TechCrunch 中国', 'http://techcrunch.cn/feed/'),
        (u'Quora', 'http://www.quora.com/rss', True),
        (u'The Economist: China', 'http://www.economist.com/feeds/print-sections/77729/china.xml'),
        (u'The Economist: Science and technology', 'http://www.economist.com/feeds/print-sections/80/science-and-technology.xml'),
        (u'The Economist: Asia', 'http://www.economist.com/feeds/print-sections/73/asia.xml'),
        (u'果壳网天文', 'http://feed43.com/3144628515834775.xml'),
        (u'Matrix67', 'http://www.matrix67.com/blog/feed')
        ]
