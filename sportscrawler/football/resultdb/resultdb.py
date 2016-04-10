#!/usr/bin/env python
# coding=utf-8
from bs4 import BeautifulSoup
import requests

class Season:
    def __init__(self,year,teams,results):
        self.year=year
        self.teams=teams
        self.results=results

class League:
    def __init__(self,name,url,season):
        self.name=name
        self.url=url
        self.year=year
        self.season=season

    def __repr__(self):
        return "<% name={0}, url={1}%>".format(self.name,self.url)

class ResultDB:
    hostname='http://www.resultdb.com/'

    '''
    This will get league name and urls
    '''
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

    def getAvailableLeagueYears():
        print "This will return an array of years that represent available data for the provided league"

    def __getURLLeagueSeasons(self,league):
        print "This will get the seasons for a specific league"

    '''
    This will get a season for a specific league
    '''
    def getLeagueSeason(self,name,year):
        print "get league season"
