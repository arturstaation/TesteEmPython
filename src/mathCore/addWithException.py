def addWithException(a,b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Ambos parametros precisam ser numeros")
    return a + b