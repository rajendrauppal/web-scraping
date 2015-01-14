#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Author : Rajendra Kumar Uppal
# Date   : 01/14/2014 8:00a
# This script fetches article links and their titles from entrepreneur.com


import urllib
from bs4 import BeautifulSoup


def normalize(s):
    result = ''
    for c in s:
        if c != '\n' and c != '\r' and c != '\t':
            result += c
    return result.rstrip().lstrip()


def scrape(url):
    num_articles = 300000
    for pageno in xrange(200000, num_articles + 1):
        currpageurl = url + "/article/" + str(pageno)
        htmlfile = urllib.urlopen(currpageurl)
        htmlsource = htmlfile.read()
        
        soup = BeautifulSoup(htmlsource)
        article_title = soup.h1.string
        article_title = normalize(article_title)
        if article_title.find('Page Not Found') == -1:
            print article_title + ' ( ' + currpageurl + ' )'


def main():
    scrape("https://entrepreneur.com")
    

if __name__ == '__main__':
    main()
