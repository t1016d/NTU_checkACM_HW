import time

def print_time(): 
	now_time = time.localtime( time.time() )
	date_str = str(now_time.tm_year).zfill(4) + '-' + str(now_time.tm_mon).zfill(2) + '-' + str(now_time.tm_mday).zfill(2)
	time_str = str(now_time.tm_hour).zfill(2) + ':' + str(now_time.tm_min).zfill(2) + ':' + str(now_time.tm_sec).zfill(2)
	print( 'Last Update:', date_str, time_str )
