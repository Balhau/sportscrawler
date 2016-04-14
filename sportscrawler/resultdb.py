from football.resultdb.resultdb import *
import json

rdb=ResultDB()

l=rdb.getLeagues()
#print rdb.getLeagueForYear("asd","asd")
#print rdb.getAvailableLeagueYears(l[0])
print json.dumps(rdb.getLeagueSeason(l[0],"2000"),default=lambda o: o.__dict__,
            sort_keys=True, indent=4)
