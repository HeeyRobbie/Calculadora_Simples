
def soma(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def mult(a, b):
    return a * b
def divisao(a, b):
    if a!=0:
        return a / b
    else:
        return "Erro de divisão"




while True:
    print("\n*** Calculadora Simples ***")
    print("Escolha a operação: ")
    print("1. Soma")
    print("2. Subtração")
    print("3. multiplicação")
    print("4. divisão")
    print("5. sair")

    escolha = int(input("digite o numero da operação Desejada: "))

    if escolha == 5:
        print("Saindo")
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == 1:
        resultado = soma(num1, num2)
    elif escolha == 2:
        resultado = subtracao(num1, num2)
    elif escolha == 3:
        resultado = mult(num1, num2)
    elif escolha == 4:
        resultado = divisao(num1, num2)
    else:
        print("Opção Invalida")
        continue
    print("Resultado: ", resultado)



