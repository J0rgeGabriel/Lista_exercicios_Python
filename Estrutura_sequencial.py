
# 1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print("Ola mundo")

# 2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
numero = float(input("Informe um numero: "))
print(f"O numero informado foi {numero}")

# 3. Faça um Programa que peça dois números e imprima a soma.
n1 = float(input("Informe o primeiro numero: "))
n2 = float(input("Informe o segundo numero: "))
soma = n1 + n2
print(f"A soma de {n1} + {n2} = {soma}")

# 4. Faca um Programa que peca as 4 notas bimestrais e mostre a média.
n1 = float(input("Informe a nota que você tirou na primeira prova: "))
n2 = float(input("Informe a nota que você tirou na segunda prova: "))
n3 = float(input("Informe a nota que você tirou na terceira prova: "))
n4 = float(input("Informe a nota que você tirou na quarta prova: "))
media = (n1 + n2 + n3 + n4) / 4
print(f"A sua media foi de {media}")

# 5. Faca um Programa que converta metros para centímetros:
metros = float(input("Informe quantos metros você deseja converter para centimetros: "))
conversao = metros * 100
print(f"{metros} metros é {conversao} centimetros")

# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio = float(input("Informe o raio do circulo: "))
area = 3.14 * raio ** 2
print(f"A area de circulo que tem um raio de {raio}cm é de {area}cm")

# 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
base = float(input("Informe a base do quadrado: "))
altura = float(input("Informe a altura do quadrado: "))
area = base * altura
print(f"A area de um quadrado que tem {base}cm de base e {altura}cm é de {area}, e o dobro dessa area é de {area * 2}cm")

# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês
valorHora = float(input("Informe quanto voce ganha por hora: R$"))
horaMes = float(input("Informe quantas horas você trabalhou esse mes: "))
salario = valorHora * horaMes
print(f"O seu salario esse mes será de R${salario}")

# 9. Faça um Programa que peça a temperatura em graus  Farenheit, transforme e mostre a temperatura em graus Celsius.
farenheit = float(input("Informe a temperatura em Farenheit: "))
celsius = (5 * (farenheit - 32) / 9)
print(f"{farenheit}°F é {round(celsius, 2)}°C")

# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
celsius = float(input("Informe a temperatura em Celsius: "))
farenheit = celsius * 1.8 + 32
print(f"{celsius}°C é {round(farenheit, 2)}°F")

# 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a. o produto do dobro do primeiro com metade do segundo.
# b. a soma do triplo do primeiro com o terceiro.
# c. o terceiro elevado ao cubo.
n1 = input("Informe um número inteiro: ")
while not n1.isdigit():
    n1 = input("Valor inválido! Informe um número inteiro: ")
n2 = input("Informe mais um número inteiro: ")
while not n2.isdigit():
    n2 = input("Valor inválido! Informe mais um número inteiro: ")
n3 = input("Informe um número real: ").replace(",", ".")
while "," in n3 or not n3.replace(".", "").isdigit():
    n3 = input("Valor inválido! Informe um número real: ").replace(",", ".")
questaoA = int(n1) * 2 * (int(n2) / 2)
print(
    f"O produto do dobro do primeiro com metade do segundo é igual a {questaoA}")
questaoB = int(n1) * 3 + float(n3)
print(f"A soma do triplo do primeiro com o terceiro é igual a {questaoB}")
questaoC = float(n3) ** 3
print(f"O terceiro elevado ao cubo é igual a {questaoC}")

# 12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7* altura) - 58
altura = float(input("Informa sua altura").replace(",", "."))
conversao = (72.7 * altura) - 58
print(f"De acordo com a sua altura, o seu peso ideal é de {round(conversao, 2)}Kg")

# 13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# a. Para homens: (72.7*h) - 58
# b. Para mulheres: (62.1*h) - 44.7
while True:
    sexualidade = int(input("\nInforme a sua sexualidade: \n"
                            "1 - Homem\n"
                            "2 - Mulher\n"
                            "3 - Parar o codigo"))
    if sexualidade == 1:
        altura = float(input("Informa sua altura").replace(",", "."))
        conversao = (72.7 * altura) - 58
        print(f"De acordo com a sua altura, o seu peso ideal é de {round(conversao, 2)}Kg")
    elif sexualidade == 2:
        altura = float(input("Informa sua altura").replace(",", "."))
        conversao = (62.1 * altura) - 44.7
        print(f"De acordo com a sua altura, o seu peso ideal é de {round(conversao, 2)}Kg")
    else:
        break

# 14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu
# trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de
# São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa
# que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos
# além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as
# mensagens adequadas.
limitePeso = 50
valorMulta = 4.00
peso = float(input("Infome o peso dos peixes (em quilos)").replace)
if peso > limitePeso:
    excesso = peso - limitePeso
    multa = valorMulta * excesso
    print(f"Voce excedeu {excesso}Kg do peso limite")
    print(f"A sua multa sera de R${multa}")
else:
    print("Peso dentro do limite, nenhuma multa será aplicada.")


# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
# 5% para o sindicato, faça um programa que nos dê
# a. salário bruto.
# b. quanto pagou ao INSS.
# c. quanto pagou ao sindicato.
# d. o salário líquido.
# e. calcule os descontos e o salário líquido,
# conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : RS
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

valorHora = float(input("Informe quanto você recebe por hora: R$").replace(",","."))
horasTrabalhadas = float(input("Informe quantas horas você trabalhou esse mês: ").replace(",","."))

salarioBruto = valorHora * horasTrabalhadas
IR = salarioBruto * 0.11
INSS = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
salarioliquido = salarioBruto - IR - INSS - sindicato

print(f"O seu salario bruto será de R${salarioBruto}")
print(f"Será descontado R${IR} referente ao IR")
print(f"Será descontado R${INSS} referente ao INSS")
print(f"(Será descontado R${sindicato} referente ao sindicato")
print(f"O seu salario será de R${salarioliquido}")
