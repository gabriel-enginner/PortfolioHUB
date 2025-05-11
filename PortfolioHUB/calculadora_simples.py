def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisao por zero"

print("Calculadora Simples")
x = int(input("Digite o primeiro numero: "))
y = int(input("Digite o segundo numero: "))
operacao = input("Escolha a operacao (+, -, *, /): ")

if operacao == "+":
    print("Resultado:", somar(x, y))
elif operacao == "-":
    print("Resultado:", subtrair(x, y))
elif operacao == "*":
    print("Resultado:", multiplicar(x, y))
elif operacao == "/":
    print("Resultado:", dividir(x, y))
else:
    print("Operacao invalida")
