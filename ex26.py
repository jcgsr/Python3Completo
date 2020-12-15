# 14.12.2020

numero = input('Informe um número inteiro: ')

if numero.isdigit():
    numero = int(numero)
    par = numero % 2
    if par == 0:
        print('É PAR!')
    else:
        print("É ÍMPAR!")
else:
    print('Não é número inteiro!')

print('****')

hora = input("Informe somente a hora atual: ")
if hora.isdigit():
    hora = int(hora)
    if hora >= 0 and hora <= 11:
        print("Bom dia!")
    elif hora >=12 and hora <= 17:
        print("Bom tarde!")
    elif hora >= 18 and hora <= 23:
        print("Bom noite!")
    else:
        print("Não é uma hora válida")

print('****')

nome = input("Informe seu primeiro nome: ")
qtd_letras = len(nome)

if qtd_letras <= 4:
    print('Seu nome é curto.')
elif qtd_letras == 5 or qtd_letras == 6:
    print("Seu nome é normal.")
else:
    print("Seu nome é muito grande.")

