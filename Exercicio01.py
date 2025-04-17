#Gerar um Algoritmo que leia os Valores de A,B,C e diga se a soma entra A e B é menor que C.
Valor1 = float(input("Digite um Número: "))
Valor2 = float(input("Digite um Número: "))
Valor3 = float(input("Digite um Número: "))
Soma = Valor1 + Valor2

if Soma < Valor3 :
    print(f"A soma, {Soma}, é menor que {Valor3}!")
else:
    print(f"A soma, {Soma}, NÃO é Menor que {Valor3}!")
