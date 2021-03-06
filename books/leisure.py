﻿#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__      = "ptbsare"
__version__     = "0.1"

from base import BaseFeedBook

def getBook():
    return leisure

class leisure(BaseFeedBook):
    title                 = u'leisure'
    __author__            = 'calibre'
    description           = u'科技科普以及趣味精选。'
    language = 'zh-cn'
    feed_encoding = "utf-8"
    page_encoding = "utf-8"
    mastheadfile  = "mh_technews.gif"
    coverfile     = "cv_technews.jpg"
    network_timeout       = 60
    oldest_article        = 7
    max_articles_per_feed = 9
    deliver_days          = []
    feeds = [
	(u'36kr','http://www.36kr.com/feed?1.0'),
	(u'TechCrunch 中国', 'http://techcrunch.cn/feed/'),
	(u'爱范儿', 'http://www.ifanr.com/feed'),
	('Top News - MIT Technology Review', 'http://www.technologyreview.com/topnews.rss'),
	('Hacker News', 'https://news.ycombinator.com/rss'),
	(u'麻省理工科技评论', 'http://zhihurss.miantiao.me/section/id/14'),
	(u'大公司日报', 'http://zhihurss.miantiao.me/daily/id/5'),
	(u'小道消息', 'http://hutu.me/feed'),
	(u'极客公园', 'http://www.geekpark.net/rss'),
	(u'极客范', 'http://www.geekfan.net/feed/'),
	(u'人人都是产品经理', 'http://iamsujie.com/feed/'),
	(u'邹剑波Kant', 'http://kant.cc/feed'),
	('warfalcon', 'http://ys.8wss.com/rss/oIWsFtxo3oqejVy4KaJ4RDMVIrE0/'),
	(u'豆瓣一刻', 'http://yikerss.miantiao.me/rss'),
	(u'环球科学', 'http://blog.sina.com.cn/rss/sciam.xml'),
	(u'科普公园', 'http://www.scipark.net/feed/'),
	(u'科学松鼠会', 'http://songshuhui.net/feed'),
	(u'泛科学', 'http://pansci.tw/feed'),
	(u'果壳网', 'http://www.guokr.com/rss/'),
	(u'果壳网科学人', 'http://feed43.com/8781486786220071.xml'),
	(u'简书推荐', 'http://jianshu.milkythinking.com/feeds/recommendations/notes'),
	('Quora', 'http://www.quora.com/rss', True),
	('The Economist: China', 'http://www.economist.com/feeds/print-sections/77729/china.xml'),
	('The Economist: Science and technology', 'http://www.economist.com/feeds/print-sections/80/science-and-technology.xml'),
	('The Economist: Asia', 'http://www.economist.com/feeds/print-sections/73/asia.xml'),
	(u'知乎日报', 'http://zhihurss.miantiao.me/dailyrss'),
	(u'知乎精选', 'http://www.zhihu.com/rss'),
	(u'深夜食堂', 'http://zhihurss.miantiao.me/section/id/1'),
	(u'果壳网天文', 'http://feed43.com/3144628515834775.xml'),
	('Matrix67', 'http://www.matrix67.com/blog/feed'),	
	]
