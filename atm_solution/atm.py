
list_count=[100,50,10,5,4,3,2,1]
def bull():
 balance=500
 request=277
 if balance>request:
	for amount in list_count:
		while request>=list_count[0]:
			print 'give 100'
			request -=100
		while request>=list_count[1]:
			print 'give 50'
			request-=50
		while request>=list_count[2]:
			print 'give 10'
			request-=10
		while request>=list_count[3]:
			print 'give 5'
			request-=5
		while request>=list_count[4]:
			print 'give 4'
			request-=4

		while request>=list_count[5]:
			print 'give 3'
			request-=3
		while request>=list_count[6]:
			print 'give 2'
			request-=2
		while request>=list_count[7]:
		    print 'give 1'
		    request-=1	
		return    			
 print 'you do not have enough mony'
bull()
	 
