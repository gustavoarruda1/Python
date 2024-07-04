# --------Calculadora simples em Python--------

# Definindo as funções para realizar as operações

# Função para somar dois números
def soma(a, b):
    return a + b

# Função para subtrair dois números
def subtrai(a, b):
    return a - b

# Função para multiplicar dois números
def multiplica(a, b):
    return a * b
    
# Função para dividir dois números    
def divide(a, b):
    return a / b

# Solicita ao usuário que escolha uma operação
print("Selecione a operação desejada: ")
print("1 - somar")
print("2 - subtrair")
print("3 - multiplicar")
print("4 - dividir")

# Entrada do usuário
operação_escolhida = input("Digite a operação desejada 1,2,3,4: ")

# Entrada dos números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Execução da operação escolhida
if operação_escolhida == "1":
    print(numero1, "+", numero2, "=", soma(numero1, numero2))

elif operação_escolhida == "2":
    print(numero1, "-", numero2, "=", subtrai(numero1, numero2))

elif operação_escolhida == "3":
    print(numero1, "*", numero2, "=", multiplica(numero1, numero2))

elif operação_escolhida == "4":
    print(numero1, "/", numero2, "=", divide(numero1, numero2))

else:
    print("Essa opção não existe.")
