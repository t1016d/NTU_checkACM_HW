import urllib.request
import json
import get_pid

jsonfile = open( 'set.json' , 'r' )
jsoncontent = jsonfile.read()
jsoncontent = jsoncontent[:-1]
#print(jsoncontent)
#print(jsoncontent.__class__)
set = json.loads( jsoncontent )
#print(set)
#print(set['contest'])

contest_num = len( set['contest'] )
#print(contest_num)

pid = [[] for _ in range(contest_num) ]
#print(pid)

for i in range( contest_num ):
	target_url = 'http://acm.csie.org/ntujudge/contest_index.php?contest_id=' + str( set['contest'][i] )
	response = 	urllib.request.urlopen( target_url )
	for line in response:
		line = line.decode( 'UTF-8' )
		list = get_pid.get( line )
		pid[i].extend( list )
print( pid )
