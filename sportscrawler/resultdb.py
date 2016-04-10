from football.resultdb.resultdb import *

rdb=ResultDB()

l=rdb.getLeagues()
#print rdb.getLeagueForYear("asd","asd")
#print rdb.getAvailableLeagueYears(l[0])
print rdb.getLeagueSeason(l[0],"2000")
