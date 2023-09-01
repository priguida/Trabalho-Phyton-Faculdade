# Solicita ao usuário que insira o peso em quilogramas
peso = float(input("Digite o seu peso em quilogramas: "))

# Solicita ao usuário que insira a altura em metros
altura = float(input("Digite a sua altura em metros: "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Exibe o resultado
print(f"Seu Índice de Massa Corporal (IMC) é: {imc:.2f}")

# Interpretação do IMC
if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 24.9:
    print("Seu peso está dentro da faixa saudável.")
elif imc < 29.9:
    print("Você está com sobrepeso.")
elif imc < 34.9:
    print("Você está com obesidade grau I.")
elif imc < 39.9:
    print("Você está com obesidade grau II.")
else:
    print("Você está com obesidade grau III (obesidade mórbida).")