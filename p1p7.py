l=[]
x=1
cadena=""
while(x!=0):
    x=int(input("Ingrese un número: "))
    l.append(x)
for pos,i in enumerate(l):
    l[pos]=str(i)
for i in l:
    if(int(i)%3!=0):
        cadena+=(i+"-")
print(cadena)