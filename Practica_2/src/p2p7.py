def generarCodigo(nom,fecha):
    import random
    import string
    code=nom
    code+='-'
    code=adjuntar(code,fecha)
    code+='-'
    code=adjuntar(code,random.choices((string.ascii_uppercase+string.digits),k=(30-len(code))))
    return code
def adjuntar(cadena,secuencia):
    if type(secuencia)==dict:
        for key in secuencia:
            cadena+=str(secuencia[key])
    else:
        for elem in secuencia:
            cadena+=elem
    return cadena