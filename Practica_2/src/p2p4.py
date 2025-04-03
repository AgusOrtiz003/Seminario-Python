def validarUsername(name):
    if(len(name)>=5):
        hayMayus=False
        hayNum=False
        cumple=True
        for char in name:
            if (char.isdigit()):
                hayNum=True
            elif(char.isupper()):
                hayMayus=True
            elif(char.islower()):
                continue
            else:
                cumple=False
                break
        return (cumple and hayMayus and hayNum)
    else:
        return False