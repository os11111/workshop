
def bull(balance,request):
 list_count=[100,50,10,5,4,3,2,1]

 if balance>=request:
	for amount in list_count:
		while request>=amount:
			print 'give',amount
		
			
			request -=amount
			balance -=amount


	print 'you have now'+' '+(str (balance))+'$'
	return balance

 		    			
 print 'you do not have enough mony'+"  " +'you have'+' '+str(balance)+'$'
balance=500
balance=bull(balance,277)
balance=bull(balance,30)
balance=bull(balance,5)
balance=bull(balance,188)
balance=bull(balance,110)



	 
