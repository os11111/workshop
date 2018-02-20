class Atm():
 #def bull(balance,request):
 def __init__(self,balance,bank_name):
  self.balance=balance
  self.bank_name=bank_name
 def bull(self,request):
   self.request=request

   list_count=[100,50,10,5,4,3,2,1]
   print 'welcom to'+' '+ 'bank'+ ' '+self.bank_name

   if self.balance>=request:
	  for amount in list_count:
		  while request>=amount:
			  print 'give',amount
		
			
			  request -=amount
			  self.balance -=amount

	  print 'you have now'+' '+(str (self.balance))+'$'
	  return self.balance

 		    			
   print 'you do not have enough mony'+"  " +'you have'+' '+str(self.balance)+'$'
atm1=Atm(500,'baraka')
atm2=Atm(200,'Alshark')
atm1.bull(277)
atm2.bull(209)


#balance=500
#balance=bull(balance,277)
#balance=bull(balance,30)
#balance=bull(balance,5)
#balance=bull(balance,188)
#balance=bull(balance,110)



	 
