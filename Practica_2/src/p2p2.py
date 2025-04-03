def cadenaConMasPalabras(lista):
    maxpalabras=-1
    maxcadena=""
    for cadena in lista:
        cantpalabras=len(cadena.strip())
        if cantpalabras>maxpalabras:
            maxpalabras=cantpalabras
            maxcadena=cadena
    return(maxcadena)