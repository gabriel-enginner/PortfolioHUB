#teste 1
def mostrar_valor(valor):
   print("parametro recebido:", valor)
def mostra_dois_valores(valor1, valor2):
   print("valor 1: ", valor1)
   print("valor 2: ", valor2)


if __name__ == '__main__':
   print("primeira forma de fazer")
   mostrar_valor(5)
   mostrar_valor(23)
   print("segunda forma de fazer")
   v_inteiro = 43
   mostrar_valor(v_inteiro)
   v_real = 37.4
   mostrar_valor(v_real)
   print("terceiro forma de fazer")
   v_inteiro = int(input("valor inteiro:"))
   mostrar_valor(v_inteiro)
   v_real = float(input("valor real:"))
   mostrar_valor(v_real)
   print("quarta forma de fazer")
   mostra_dois_valores( 5 , 10)
