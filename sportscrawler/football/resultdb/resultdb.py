#!/usr/bin/env python
# coding=utf-8
from bs4 import BeautifulSoup
import requests

class League:
    def __init__(self,name,url):
        self.name=name
        self.url=url

    def __repr__(self):
        return "<% name={0}, url={1}%>".format(self.name,self.url)

class ResultDB:
    hostname='http://www.resultdb.com/'

    def getLeagues(self):
         r = requests.get(self.hostname)
         html=r.text
         s = BeautifulSoup(html, 'html.parser')
         leftDiv=s.find_all(id='left')[0]
         leaguesBox=leftDiv.find_all('div','box')[0]
         leaguesLi=leaguesBox.find_all('li')
         leagues=[]
         for l in leaguesLi:
             a=l.find('a')
             leagues.append(League(a.text.encode("utf-8"),a['href']))
         return leagues

    def getLeagueYear(self,league,year):
        print "this will get league information for specific year"
        
