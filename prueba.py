l=[]
while (len(l)==0 or l[len(l)-1]!=0):
	l.append(int(input("Ingrese un numero: ")))
l.remove(0)
print(l)