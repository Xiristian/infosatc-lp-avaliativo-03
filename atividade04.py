idade = 0
peso = 0
horaSono = 0
idadeCheck = False
pesoCheck = False
sonoCheck = False
checklist = [idadeCheck,pesoCheck,sonoCheck]

idade = int(input("Quantos anos você tem? "))
peso = int(input("Quantos quilos você tem? "))
horaSono = int(input("Aproximadamente, quantas horas de sono você teve nas últimas 24 horas? "))

if idade > 15 and idade < 70 and peso > 50 and horaSono >= 6:
    print("Você pode doar sangue!")
else:
    print("Você não pode doar sangue pelos motivos abaixo:")

if idade <= 15 or idade >= 70:
    print("Idade fora do intervalo de 16 e 69 anos;")
if peso <= 50:
    print("Peso abaixo de 50kg;")
if horaSono < 6:
    print("Horas de sono das últimas 24 horas abaixo de 6;")