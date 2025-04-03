def imprimirSegundaPalabraConVocal(cadena):
    vocales=("a","e","i","o","u")
    l=cadena.split("\n")
    for elem in l: 
        aux=elem.split()
        if(aux[1].lower().startswith(vocales)):
            print (elem)