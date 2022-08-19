#Calculadora de quanto vai gastar de gasolina numa viagem
distancia = float(input("Qual é a distância total da viagem (em km)? "))
combustivel = float(input("Qual é o valor do combustível? "))
carro = float(input("Quantos km/l faz o carro? "))

valor = (distancia/carro)
valortotal = (valor * combustivel)

print('O valor total da sua viagem é de R${} '.format(valortotal))
