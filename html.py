import ptime

def print_head():
	str1 = '<html><head><link href="ACM.css" rel="stylesheet" /></head><body>'
	str2 = '<table><tr><td> </td>'
	str3 = '</tr>'
	
	print( str1 )
	ptime.print_time()
	print( str2 )
	for i in range(10):
		print( '<td class=\'Prob\'>' + str( chr( ord('A') + i ) ) +'</td>' )
	print( str3 )

def print_HW( num , cid ):
	str1 = '<tr><td class=\'HW\'><a href=\'http://acm.csie.org/ntujudge/contest_index.php?contest_id='
	str2 = '\'>HW'
	str3 = '</a></td>'
	print( str1, cid, str2, num, str3, sep='')
	#<td class='HW'><a href='http://acm.csie.org/ntujudge/contest_index.php?contest_id=407'>HW1</a></td>

def print_prob( pid , who ):
	str1 = '<td class=\''
	str2 = 'AC\'><a href=\'http://acm.csie.org/ntujudge/problem.php?id='
	str3 = '\'>'
	str4 = '</a></td>'
	print( str1, who, str2, pid, str3, pid, str4, sep='')

def print_endHW():
	print('</tr>')

def print_tail( my , team , no ):
	str1 = '</table>color:<table><td class=\'myAC\'>I accepted it('
	str2 = ')</td><td class=\'teamAC\'>My teammate accepted it('
	str3 = ')</td><td class=\'noAC\'>QAQ('
	str4 = ')</td></table></body></html>'
	print( str1, my, str2, team, str3, no, str4 )
