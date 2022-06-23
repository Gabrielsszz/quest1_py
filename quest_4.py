import random

jogador1= input('Insira o nome do primeiro jogador: ')
jogador2= input('Insira o nome do segundo jogador: ')
naipes= ['Copas','Ouro','Paus','Espadas']
cartas=[1,2,3,4,5,6,7,8,9,10,'Valete','Rei','Dama']
x= 0
y=0
m1=[]
for c in range(2):
    print(f'\nAs cartas do Jogador {c+1} são:')
    for i in range(3):
        x=random.sample(cartas,1)
        m1.extend(x)
        y=random.sample(naipes,1)

        print(end=''f'{x} de {y} \n')
        if 'Valete' in m1:
            m1.remove('Valete')
            m1.append(1)
        elif 'Dama' in m1:
            m1.remove('Dama')
            m1.append(1)
        elif 'Rei' in m1:
            m1.remove('Rei')
            m1.append(1)

somatoria1=(m1[0]+m1[1]+m1[2])
somatoria2=(m1[3]+m1[4]+m1[5])
print()
print(f'O jogador {jogador1} fez {somatoria1} pontos!')
print(f'O jogador {jogador2} fez {somatoria2} pontos!')
print()

if somatoria1 >= 21:
    print(f'O jogador {jogador1} estourou ao fazer uma quantia de pontos maior que 21!')
    print(f'O jogador {jogador2} fez {somatoria2} pontos e ganhou a rodada!')
elif somatoria2 >= 21:
    print(f'O jogador {jogador2} estourou ao fazer uma quantia de pontos maior que 21!')
    print(f'O jogador {jogador1} fez {somatoria1} e ganhou a rodada!!')
elif somatoria1 > somatoria2:
    print(f'O jogador {jogador1} ganhou ao fazer {somatoria1} pontos!')
    print(f'O jogador {jogador2} perdeu ao fazer apenas {somatoria2} pontos! ')
elif somatoria2 > somatoria1:
    print(f'O jogador {jogador2} ganhou ao fazer {somatoria2} pontos!')
    print(f'O jogador {jogador1} perdeu ao fazer apenas {somatoria1} pontos! ')



