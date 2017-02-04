def gcd(x,y):
	if x<y:
		(x,y) = (y,x)
	if (x%y)==0:
		return (y)
	else:
		return (gcd((x-y),y))
	
