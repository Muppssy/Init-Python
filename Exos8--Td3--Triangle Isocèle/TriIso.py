def iso():
	a = int(input("entrez une valeur"))
	for i in range(a):
		print((a-i)*" ",end="")
		print((i*2+1)*"*",end="")	
		print((a-i)*" ")
iso()