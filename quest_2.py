import random
user = int(input('Escolha um valor de 1 a 6: '))
lanç = []
s = []
for c in range(3):
    for i in range(c):
        dados = random.randint(1,6)
        if dados == user:
            s.append(1)
        lanç.append(dados)
result = sum(s)
print(f'O resultado do rolamento dos dados foi: {lanç}')
if result == 0:
    print('Você não acertou nenhum número!')
elif result == 1:
    print('Você acertou uma vez!')
elif result == 2:
    print('Você acertou duas vez!')
elif result == 3:
    print('Você acertou três vezes. Sensacional!')


    