# 1. Faça um Programa que peça dois números e imprima o maior deles:

n1 = float(input("Informe o primeiro número: ").replace(",", "."))
n2 = float(input("Informe o segundo número: ").replace(",", "."))
print(f"O maior número entre {n1} e {n2} é {max(n1, n2)}")

# 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo:
numero = float(input("Informe um número: ").replace(",", "."))
if numero >= 0:
    print(f"{numero} é positivo")
else:
    print(f"{numero} é negativo")

# 3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino, M Masculino. Sexo Inválido.
sexo = input("Informe o seu sexo [M/F]: ").upper()
if sexo == "M":
    print("O seu sexo é masculino")
elif sexo == "F":
    print("O seu sexo é feminino")
else:
    sexo = input("Sexo invalido! Informe o seu sexo novamente[M/F]: ")

# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante:
letra = input("Digite uma letra: ").upper()
if letra == ("A") or letra == ("E") or letra == ("I") or letra == ("O") or letra == ("U"):
    print(f"[{letra}] é vogal")
else:
    print(f"[{letra}] é consoante")

# 5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por
# aluno e apresentar:
# • A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# • A mensagem "Reprovado", se a média for menor do que sete;
# • A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input("Informe a nota da primeira prova: "))
nota2 = float(input("Informe a nota da segunda prova: "))
media = (nota1 + nota2) / 2
if media == 10:
    print("Aprovado com distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")


# 6. Faca um Programa que leia três números e mostre o maior deles.

n1 = float(input("Informe o primeiro numero: ").replace(",", "."))
n2 = float(input("Informe o segundo numero: ").replace(",", "."))
n3 = float(input("Informe o terceiro numero: ").replace(",", "."))
print(f"O maior número é {max(n1, n2, n3,)}")


# 7. Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = float(input("Informe o primeiro numero: ").replace(",", "."))
n2 = float(input("Informe o segundo numero: ").replace(",", "."))
n3 = float(input("Informe o terceiro numero: ").replace(",", "."))
print(f"Maior: {max(n1, n2, n3,)}\n"
    f"Menor: {min(n1, n2, n3,)}")


# 8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a
# decisão é sempre pelo mais barato.
p1 = float(input("Informe o preço do primeiro produto: R$").replace(",", "."))
p2 = float(input("Informe o preço do segundo produto: R$").replace(",", "."))
p3 = float(input("Informe o preço do terceiro produto: R$").replace(",", "."))
menor_preco = min(p1, p2, p3)
print(f"O produto mais barato está R${menor_preco:.2f}")


# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
n1 = float(input("Informe o primeiro numero: ").replace(",", "."))
n2 = float(input("Informe o segundo numero: ").replace(",", "."))
n3 = float(input("Informe o terceiro numero: ").replace(",", "."))
numeros = [n1, n2, n3]  # lista
decrescente = numeros.sort(reverse=True)  # numeros em ordem decrescente
print(f"A ordem decrescente desses números é {numeros}")


# 10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

while True:
    turno = input(
        "Em qual turno você estuda? [ M-matutino - V-Vespertino - N- Noturno]: ").upper()
    if turno == "M" or turno == "MATUTINO":
        print("Bom dia!")
        break
    elif turno == "V" or turno == "VESPERTINO":
        print("Boa tarde!")
        break
    elif turno == "N" or turno == "NOTURNO":
        print("Boa noite!")
        break
    else:
        input(
            "Valor invalido! Em qual turno você estuda? [ M-matutino - V-Vespertino - N- Noturno]: ").upper()
        continue

# 11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para
# desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no
# salário atual
# • salários até R$ 280,00 (incluindo) : aumento de 20%
# • salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# • salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# • salários de R$ 1500,00 em diante: aumento de 5%
# Após o aumento ser realizado, informe na tela:
# • o salário antes do reajuste;
# • o percentual de aumento aplicado;
# • o valor do aumento;
# • o novo salário, após o aumento.

salario = float(input("Informe o seu salario: R$").replace(",", "."))
if salario <= 280:
    salario_aumento = salario * 1.2
    print(
        f"Após o aumento de 20%, o seu salario será de R${salario_aumento:.2f}")
elif salario > 280 and salario <= 700:
    salario_aumento = salario * 1.15
    print(
        f"Após o aumento de 15%, o seu salario será de R${salario_aumento:.2f}")
elif salario > 700 and salario < 1500:
    salario_aumento = salario * 1.10
    print(
        f"Após o aumento de 10%, o seu salario será de R${salario_aumento:.2f}")
else:
    salario_aumento = salario * 1.05
    print(
        f"Após o aumento de 5%, o seu salario será de R${salario_aumento:.2f}")
