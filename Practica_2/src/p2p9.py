def quitarInvalidos(l):
    import string
    letras=set(string.ascii_letters)
    for elem in l:
        if (elem==None) or (letras.issuperset(elem.strip())):
            l.remove(elem)
def quitarEspacios(cadena):
    while(cadena.startswith(' ')):
        cadena=cadena[1:]
    while(cadena.endswith(' ')):
        cadena=cadena[:-1]
    return cadena    
def estandarizar (lista):
    aux=set()
    quitarInvalidos(lista)
    for i,elem in enumerate(lista):
      lista[i]=quitarEspacios(lista[i])
      lista[i]=lista[i].title()
      aux.add(lista[i])
    return sorted(list((aux)-{''}))