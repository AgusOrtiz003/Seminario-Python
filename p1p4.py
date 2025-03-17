l=[]
x=-1
while(x!=0):
    x=int(input("Ingrese números (el corte es 0): "))
    l.append(x)
for i in range(len(l)):
    if (l[i] or (l[i]%2)!=0):
        continue
    print(l[i])