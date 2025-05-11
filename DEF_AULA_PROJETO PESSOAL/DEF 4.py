def adicionar(x,y):
    return x + y
def subtrair(x, y):
    return x - y
def multiplicar(x, y):
    return x * y
def dividir(x, y):
    if y == 0:
        return "erro! divisão por zero."
    return x / y
print("selecionar a operação.")
print("1. adicionar")
print("2. subtrair")
print("3. multiplicar")
print("4. dividir")
while True:
    escolha = input("digite sua escolha (1/2/3/4): ")
    if escolha in ('1', '2', '3', '4'):
        try:
            num1 = float(input("digite o primeiro número: "))
            num2 = float(input("digite o segundo número:  "))
        except ValueError:
            print("entrada inválida. por favor, digite números.")
            continue
            if escolha == '1':
                print(num1, "+", num2, "=", adicionar(num1, num2))
            elif escolha == '2':
                print(num1, "-", num2, "=", subtrair(num1, num2))
            elif escolha == '3':
                print(num1, "*", num2, "=", multiplicar(num1, num2))
            elif escolha == '4':
                print(num1, "/", num2, "=", dividir(num1, num2))
                proxima_calculadora = input("deseja fazer outro calculo? (sim/não): ")
                if proxima_calculadora.lower() != "sim":
                    break
                else:
                    print("entrada inválida. por favor, digite um número entre 1 e 4.")




