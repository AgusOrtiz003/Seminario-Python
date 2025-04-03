def cadenasConPalabra(secuencia,word):
    l=[]
    for cadena in secuencia.split("\n"):
        if word in cadena:
            l.append(cadena)
    return tuple(l)