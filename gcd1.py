def gcd(x,y):
 l1=[]
 l2=[]
 c1=[]
 for i in range(1,x+1):
 	if x%i==0:
 		l1.append(i)
 		
 for i in range(1,y+1):
 	if y%i==0:
 		l2.append(i)
 		
 for i in l1:
 	if i in l2:
 		c1.append(i)		
 return c1[-1]
 
print gcd(16,4)
  
