import os
os.system("clear")

maiorNumero = min
menorNumero = max
soma = 0
media = 0
produto = 1.0

for i in range(2):
    numero = input(f"Digite o {i + 1}º Número: ")

    numeroValido = None
    
    try:
        numero = float(numero)
        soma += numero
        produto *= numero

        if numero > maiorNumero:
            maiorNumero = numero
        else:
            menorNumero = numero
        
        numeroValido = True
    
    except ValueError:
        numeroValido = False

media = soma / 2

if numeroValido == True:
    print(f"Média: {media:.2f}")
    print(f"Soma: {soma}")
    print(f"Produto: {produto}")
    print(f"Maior Valor: {maiorNumero}")
    print(f"Menor Valor: {menorNumero}")
else:
    print("Digite um número valído")