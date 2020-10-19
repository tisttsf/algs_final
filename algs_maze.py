def count_paths(m,n):
	results=[[1]*n]*m
	for i in range(1,m):
		for j in range(1,n):
			results[i][j]=results[i-1][j]+results[i][j-1]
	return results[-1][-1]

