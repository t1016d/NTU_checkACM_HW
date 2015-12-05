import urllib.request
import json
import get_pid
import html

jsonfile = open( 'python/NTU_checkACM_HW/set.json' , 'r' )
jsoncontent = jsonfile.read()
jsoncontent = jsoncontent[:-1]
#print(jsoncontent)
#print(jsoncontent.__class__)
setting = json.loads( jsoncontent )
#print(set)
#print(set['contest'])

contest_num = len( setting['contest'] )
#print(contest_num)

pid = [[] for _ in range(contest_num) ]
#print(pid)

for i in range( contest_num ):
	target_url = 'http://acm.csie.org/ntujudge/contest_index.php?contest_id=' + str( setting['contest'][i] )
	response = 	urllib.request.urlopen( target_url )
	for line in response:
		line = line.decode( 'UTF-8' )
		list = get_pid.get( line )
		pid[i].extend( list )
#print( pid )

mysolve = []

target_url = 'http://acm.csie.org/ntujudge/user_info.php?user_id=' + str( setting['uid'] )
response = 	urllib.request.urlopen( target_url )
for line in response:
	line = line.decode( 'UTF-8' )
	list = get_pid.get( line )
	mysolve.extend( list )

#print( len( mysolve ) )
#print( mysolve )
mysolve = set( mysolve )


teamsolve = []

target_url = 'http://acm.csie.org/ntujudge/user_info.php?teamname=' + setting['team_name']
response = 	urllib.request.urlopen( target_url )
for line in response:
	line = line.decode( 'UTF-8' )
	list = get_pid.get( line )
	teamsolve.extend( list )

#print( len( teamsolve ) )
#print( teamsolve )
teamsolve = set( teamsolve )
#print( len( teamsolve ) )
#print( teamsolve )


html.print_head()
my = 0
team = 0
no = 0

for i in range( contest_num ):
	html.print_HW( i+1 , setting['contest'][i] )
	for j in range( len( pid[i] ) ):
		if pid[i][j] in mysolve:
			html.print_prob( pid[i][j] , 'my' )
			my += 1
		elif pid[i][j] in teamsolve:
			html.print_prob( pid[i][j] , 'team' )
			team += 1
		else:
			html.print_prob( pid[i][j] , 'no' )
			no += 1
	html.print_endHW()
html.print_tail( my , team , no )
