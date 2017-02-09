def prime(n):
	if n<=1:
		return(False)
	for i in range(2,n):
		if n%i==0:
			return(False)
	return(True)

def sumprimes(l):
	s = 0
	for i in range(0,len(l)):
		if(prime(l[i])):
			s+=l[i]
	return s
