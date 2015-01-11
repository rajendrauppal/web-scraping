#!/usr/bin/env python
# -*- coding: utf-8 -*-


import urllib
from bs4 import BeautifulSoup
import math

def scrapeProjectEuler(homeurl):
    """
    Scrape Project Euler website (https://projecteuler.net)
    get #solvers of the problems and sort them
    """
    # find problems in all 50 pages
    totalpages = 10
    problems = []
    for x in xrange(1, totalpages + 1):
        # get html source code of the current page
        currpageurl = homeurl + ";page=" + str(x)
        htmlfile = urllib.urlopen(currpageurl)
        htmlsource = htmlfile.read()

        soup = BeautifulSoup(htmlsource)
        t = soup.table

        for tr in t.findAll('tr'):
            problem = []
            for td in tr.findAll('td'):
                problem.append(td.string)
            if len(problem):
                problems.append(problem)

    problems = sorted( problems, key=lambda x: int(x[2]) )

    print "Number of solvers, Problem URL, Problem No."
    print "-------------------------------------------"
    for p in problems:
        numsolvers = p[2]
        pageno = int( math.ceil(int(p[0]) / 50.0) )
        print numsolvers + ", https://projecteuler.net/problems;page=" + str(pageno) + ", " + p[0]

def main():
    scrapeProjectEuler("https://projecteuler.net/problems")

if __name__ == '__main__':
    main()
