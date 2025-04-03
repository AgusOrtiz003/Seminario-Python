def procesarCadena(menciones,l):
    music=0
    charla=0
    ent=0
    for palabra in l:
        if(palabra=="música"):
            menciones['música']+=1
        elif(palabra=="charla"):
            menciones['charla']+=1
        elif(palabra=="entretenimiento"):
            menciones['entretenimiento']+=1
    return(menciones)