n=1

m=int(input('Enter M value'))

for x in range(m):
	for y in range(n):
		print('->',end = '')
	n=n+1
	print(end='\n')
for x in range(n):
	for y in range(n-1):
		print('->',end = '')
	print(end='\n')
	n=n-1
