def matched(s):
	flag=0
	for i in range(0,len(s)):
		if s[i]=='(':
			flag+=1
		elif s[i]==')':
			flag-=1
		if flag<0:
			return(False)
	if flag>0:
		return(False)
	return(True)
