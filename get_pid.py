def get( s ):
	Identify_Strings = [ 'problem.php?id=', 'contest_view.php?id=' ]
	result = []
	for identify_string in Identify_Strings:
		ids_len = len( identify_string )
		begin = 0
		while begin >= 0 :
			begin = s.find( identify_string , begin )
			if begin >= 0 :
				end = begin + ids_len
				#print( s[ end ] )
				#print( end , begin )
				while s[end] >= '0' and s[end] <= '9':
					end = end + 1
				#print( s[begin:end] )
				result.append( int( s[begin + ids_len : end] ) )
				begin = begin + 1
	return result
