def compararPalabras(word1,word2):
    conj1=set()
    conj2=set()
    for char in word1:
        conj1.add(char)
    for char in word2:
        conj2.add(char)
    return(conj1==conj2)