meses = [
    "Janeiro","Fevereiro","Março","Abril","Maio","Junho",
    "Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

numero = int(input("Digite um número para saber que mês ele se refere: "))

if numero > 0 and numero <= 12:
    numero -= 1
    print("O número digitado se refere ao mês de", meses[numero])
else:
    print("O número digitado não se refere à nenhum mês")