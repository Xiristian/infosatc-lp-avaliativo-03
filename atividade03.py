idade = 0
sexo = ""
i = 0
idadeMasculino = 0
idadeFeminino = 0
homens = 0
mulheres = 0
idadeTotal = 0

while i < 10:
    i += 1
    sexo = input("Qual o seu sexo? Masculino ou Feminino? (M/F) ")

    if sexo == "M":
        idade = int(input("Qual a sua idade? "))
        idadeMasculino += idade
        homens += 1
        idadeTotal += idade
    elif sexo == "F":
        idade = int(input("Qual a sua idade? "))
        idadeFeminino += idade 
        mulheres += 1
        idadeTotal += idade
    else:
        print("Digite somente 'M' ou 'F'")
        i -= 1

mediaM = idadeMasculino / homens
mediaF = idadeFeminino / mulheres
mediaT = idadeTotal / 10

print("Média da idade dos homens:", mediaM)
print("Média da idade das mulheres:",mediaF)
print("Média das idades de todos:",mediaT)