def matmult(matrix1,matrix2):
	rmatrix = []
	#for i in range(len(matrix1[0])):
	#	for j in range(len(matrix2)):
	#		rmatrix[i][j]=0
	
	for i in range(len(matrix1)):
		temp = []
		for j in range(len(matrix2[0])):
			sum1=0
			for k in range(len(matrix2)):
				sum1 = sum1 + (matrix1[i][k] * matrix2[k][j])
			temp.append(sum1)
		rmatrix.append(temp)
	return rmatrix
	'''	
	for i in range(len(l1)):
		for j in range(len(l2)):
			for k in range(len(l1[j])):
				l3[i][j] += l1[i][k]*l2[k][j]
	return l3
	'''
