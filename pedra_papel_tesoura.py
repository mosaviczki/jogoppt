import random
print("*********************************")
print("       PEDRA/PAPEL/TESOURA       ")
print("*********************************")

while True:
    opcao = ['pedra', 'papel', 'tesoura']

    bot = random.choice(['pedra','papel', 'tesoura'])
    hum = input("Sua jogada: ")
    print("O robo jogou ", bot)

    if bot == hum:
        print("empate")
    elif hum not in opcao:
        print("entrada invalida")
    elif (hum == 'pedra' and bot == 'tesoura') or (hum == 'papel' and bot == 'pedra') or (
                    hum == 'tesoura' and bot == 'papel'):
        print("você ganhou!")
    else:
        print("você perdeu")
        break
