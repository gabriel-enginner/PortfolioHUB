def retorna_soma(v1,v2):
   soma = v1 + v2
   return soma

def retorna_soma_2(v1, v2):
   return v1 + v2

if __name__ == '__main__':
   valor1 = int(input('primeiro valor: '))
   valor2 = int(input('segundo valor:  '))
   v_retorno = retorna_soma(valor1, valor2)
   print("soma = ",v_retorno)
   resultado_real = retorna_soma(2.1, 3.3)
   print("Soma =", resultado_real)



