from random import randint  #importa a função de randomizar
nu_secreto= randint(0, 100) #gera números int dentro do escopo (incluindo ambos os termos)
print('Boas vindas ao jogo de advinhação do número!')
chute=0 #cria a váriavel e guarda o valor
tentativas=0 #cria o contador

while True:
    try:
        chute = int(input('Escreva um número de 0 a 100: '))
    except ValueError:
        print('Por favor, digite um número inteiro válido!') #evita termos que não sejam int
        continue #ignora o resto do loop e volta pro início
    tentativas += 1 #aumenta o contador já definido
    if chute == nu_secreto:
        print(f'Parabéns! Você acertou o número {nu_secreto} em {tentativas} tentativas!')
        break  # Encerra o jogo
    elif chute > nu_secreto:
        print(f'O número é menor que {chute}')
    else:
        print(f'O número é maior que {chute}')

