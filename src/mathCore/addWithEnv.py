import os

def addWithEnv():
    valor1 = os.getenv('VALOR1')
    valor2 = os.getenv('VALOR2')
    if valor1 is None or valor2 is None:
        raise ValueError("As variáveis de ambiente VALOR1 e VALOR2 devem estar definidas.")
    return int(valor1) + int(valor2)