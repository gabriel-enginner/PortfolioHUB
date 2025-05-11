#teste 2
def calcula_triplo(valor):
   triplo = valor * 3
   return triplo


def calcula_dobro(p_valor):
   return p_valor * 2


if __name__ == '__main__':
   valor = int(input("valor inteiro: "))
   valor_retorno = calcula_dobro(valor)
   print("valor retornado pela função:", valor_retorno)
   valor = int(input("valor inteiro: "))
   valor_retorno = calcula_triplo(valor)
   print("valor retornado pela função:", valor_retorno)
   print("Valor retornado pela função calcula_dobro:", calcula_dobro(valor))
   print("Valor retornado pela função calacula_triplo:", calcula_triplo(valor))


