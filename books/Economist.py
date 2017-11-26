#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from base import BaseFeedBook, URLOpener, string_of_tag

def getBook():
    return Economist

class Economist(BaseFeedBook):
    title                 = 'The Economist'
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
    
    #下面是在其网站还没有提供RSS前的抓取方式，现在已经不需要了，因为直接有RSS源了
    """
    feeds = [
            ('Index', 'http://www.economist.com/printedition'),
           ]
    
    def ParseFeedUrls(self):
        #return list like [(section,title,url,desc),..]
        mainurl = 'http://www.economist.com/printedition'
        urls = []
        urladded = set()
        opener = URLOpener(self.host, timeout=30)
        result = opener.open(mainurl)
        if result.status_code != 200:
            self.log.warn('fetch rss failed:%s'%mainurl)
            return []
            
        content = result.content.decode(self.feed_encoding)
        soup = BeautifulSoup(content, "lxml")
        
        #GAE获取到的是移动端网页，和PC获取到的网页有些不一样
        for section in soup.find_all('section', attrs={'id':lambda x: x and 'section' in x}):
            h4 = section.find('h4')
            if h4 is None:
                self.log.warn('h4 is empty')
                continue
            sectitle = string_of_tag(h4).strip()
            if not sectitle:
                self.log.warn('h4 string is empty')
                continue
            #self.log.info('Found section: %s' % section_title)
            articles = []
            subsection = ''
            for node in section.find_all('article'):
                subsec = node.find('h5')
                if subsec:
                    subsection = string_of_tag(subsec)
                prefix = (subsection + ': ') if subsection else ''
                a = node.find('a', attrs={"href":True}, recursive=False)
                if a:
                    url = a['href']
                    if url.startswith(r'/'):
                        url = 'http://www.economist.com' + url
                    url += '/print'
                    title = string_of_tag(a)
                    if title:
                        title = prefix + title
                        #self.log.info('\tFound article:%s' % title)
                        if url not in urladded:
                            urls.append((sectitle,title,url,None))
                            urladded.add(url)
                            
        #有些人获取到的是PC端网页，怪了，再分析一次PC端网页吧  
        if len(urls) == 0:
            for section in soup.find_all('div', attrs={'id':lambda x: x and 'section' in x}):
                h4 = section.find('h4')
                if h4 is None:
                    self.log.warn('h4 is empty')
                    continue
                sectitle = string_of_tag(h4).strip()
                if not sectitle:
                    self.log.warn('h4 string is empty')
                    continue
                
                articles = []
                subsection = ''
                for node in section.find_all('div', attrs={'class':'article'}):
                    subsec = node.previous_sibling
                    if subsec and subsec.name == 'h5':
                        subsection = string_of_tag(subsec)
                    prefix = (subsection + ': ') if subsection else ''
                    a = node.find('a', attrs={'class':'node-link',"href":True}, recursive=False)
                    if a:
                        url = a['href']
                        if url.startswith(r'/'):
                            url = 'http://www.economist.com' + url
                        url += '/print'
                        title = string_of_tag(a)
                        if title:
                            title = prefix + title
                            #self.log.info('\tFound article:%s' % title)
                            if url not in urladded:
                                urls.append((sectitle,title,url,None))
                                urladded.add(url)
                                
        if len(urls) == 0:
            self.log.warn('len of urls is zero.')
        return urls
        """
