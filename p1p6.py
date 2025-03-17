l=[]
pares=[]
impares=[]
x=-1
while(x!=0):
    x=int(input("Ingrese números (el corte es 0): "))
    l.append(x)
l.remove(0)
for i in range(len(l)):
    if ((l[i]%2)!=0):
        impares.append(l[i])
    else:
        pares.append(l[i])
print(pares)
print(impares)