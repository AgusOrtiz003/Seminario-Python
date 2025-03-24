l=[]
while ((l[len(l)-1])!=0):
    l.append(int(input("Ingrese un numero: ")))
    if(l[len(l)-1]==0):
        break
l.remove(0)
for i in range(len(l)):
    if(l[i]<0):
        break
    print(l[i])