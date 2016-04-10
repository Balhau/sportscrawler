#!/usr/bin/env python
# coding=utf-8
from bs4 import BeautifulSoup
import requests

class Result:
    def __init__(self,teamHome,pointHome,teamAway,pointAway):
        self.teamAway=teamAway
        self.teamHome=teamHome
        self.pointHome=pointHome
        self.pointAway=pointAway

class Season:
    def __init__(self,year,teams,results):
        self.year=year
        self.teams=teams
        self.results=results

    def __repr__(self):
        return "<% year={0}%>".format(self.year)

class League:
    def __init__(self,name,url,season=None):
        self.name=name
        self.url=url
        self.season=season

    def __repr__(self):
        return "<% name={0}, url={1}%>".format(self.name,self.url)

def req(url):
    return requests.get(url)

def post(url,data):
    return requests.post(url,data)

def soup(html):
    return BeautifulSoup(html,'html.parser')

class ResultDB:
    hostname='http://www.resultdb.com'

    '''
    This will get league name and urls
    '''
    def getLeagues(self):
         r = req(self.hostname)
         s = soup(req(self.hostname).text)
         leftDiv=s.find_all(id='left')[0]
         leaguesBox=leftDiv.find_all('div','box')[0]
         leaguesLi=leaguesBox.find_all('li')
         leagues=[]
         for l in leaguesLi:
             a=l.find('a')
             leagues.append(League(a.text.encode("utf-8"),a['href']))
         return leagues

    def getAvailableLeagueYears(self,league):
        return self.__getURLLeagueSeasons(league)

    def __getURLLeagueSeasons(self,league):
        s=soup(req(self.hostname+league.url).text)
        t=s.find_all('table',{ "class" : "results" })[0]
        tr=t.find_all('tr')[1:]
        seasons=[]
        for r in tr:
            a=r.find("a")
            el={"url":a['href'],'name':a.text}
            seasons.append(el)
        return seasons


    '''
    This will get a season for a specific league
    '''
    def getLeagueSeason(self,league,year,gamelimit=380):
        s=soup(post(self.hostname+league.url+year,{'gamelimit':gamelimit}).text)
        return s
