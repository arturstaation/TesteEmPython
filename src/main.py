from mathCore import (add, addWithException,addWithEnv)
import os

def main():
    try:

        valor1 = 5
        valor2 = 3
        result = add(valor1, valor2)
        if(result != (valor1 + valor2)):
            raise Exception("O resultado da adição não é o esperado.")
        print(f"Resultado da adição: {result}")
        result_with_exception = addWithException(valor1, valor2)
        if(result_with_exception != (valor1 + valor2)):
            raise Exception("O resultado da adição não é o esperado.")
        print(f"Resultado com exceção: {result_with_exception}")
        chamarUltimaFuncao = os.getenv('CHAMAR_ULTIMA_FUNCAO')
        if(chamarUltimaFuncao is not None and chamarUltimaFuncao):
            print("Chamando a última função...")
            result = addWithEnv(valor1, valor2)
            print(f"Resultado da última função: {result}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        raise e

if __name__ == "__main__":
    main()
