#Faça um Algoritmo para receber um Número qualquer e imprimir na tela se o Número é pár ou ímpar, positivo ou negativo!
Num = int(input("Digite um Número: "))
if Num % 2 == 0:
    if Num > 0:
        print(f"O {Num}, é PAR e POSITIVO!")
    else:
        print(f"O {Num}, é PAR e NEGATIVO!")
else:
    if Num > 0:
        print(f"O {Num}, é IMPAR e POSITIVO!")
    else:
        print(f"{Num}, é IMPAR e NEGATIVO!")  