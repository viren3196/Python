def alternating(l):
	flag=-1
	for i in range(len(l)-1):
	
		if l[i]>l[i+1]:
			if(flag==0):
				return(False)
			flag=0;
			
		elif l[i]<l[i+1]:
			if(flag==1):
				return(False)
			flag=1
			
		else:
			return(False)
	return(True)
		
