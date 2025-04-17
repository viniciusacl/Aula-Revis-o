#Calculando IMC do Usuário e dizendo sua condição de saúde!

IMC_P = float(input("Digite seu Peso: "))
IMC_A = float(input("Digite seu Altura: "))
IMC_T = IMC_P / (IMC_A ** 2)
print(f"Seu IMC é: {IMC_T:.1f}")

if IMC_T <= 18.6:
    print(f"Seu IMC é de: {IMC_T:.1f} e você está ABAIXO DO PESO!")
elif IMC_T >= 18.6 and IMC_T <= 24.9:
    print(f"PARABÉNS, Você está no PESO IDEAL!")
elif IMC_T >= 25.0 and IMC_T <= 29.9:
    print(f"Você está Levemente ACIMA DO PESO!")
elif IMC_T >= 30.0 and IMC_T <= 34.9:
    print(f"Você está com OBESIDADE GRAU1!")
elif IMC_T >= 35.0 and IMC_T <= 39.9:
    print(f"Você está com OBESIDADE GRAU2!,(SEVERA)")
else:
    print(f"OBESIDADE GRAU3!,(MÓRBIDA)") 