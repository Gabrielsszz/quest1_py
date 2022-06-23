import random

navio = input('Digite aqui o nome do navio: ')
vkm = int(input('Digite a velocidade maxima do navio em Km/h: '))
cm= int(input('Digite a carga maxima do navio em t:'))
print()
qnct= []
peso=0
peso=sum(qnct)


while peso < cm:
    x=random.randint(1,100)
    if len(qnct) == 50:
        break

    elif peso < cm:
      if peso+x < cm:
       qnct.append(x)
       peso=sum(qnct)
      else:
        break

print((f'Levando em conta a carga maxima de {cm}t que o {navio.title()} suporta, ele pode carregar até {len(qnct)} conteiners '))
print()
calcdp= peso*0.01
distancia= 5840.86
redvel=distancia/(vkm-calcdp)
if calcdp > 20:
    qnct.remove(max(qnct))
    calcdp=sum(qnct)*0.01
    redvel=distancia/(vkm-calcdp)
    print(f'O {navio} está com sua velocidade reduzida em 20% devido a sua carga, então levará {redvel:.2f} horas, ou seja, cerca de  {redvel/24:.0f} dias para ir de Lisboa a Recife!')
    print()
else:
    print(f'O {navio} levará {redvel:.2f} horas, ou seja, cerca de {redvel/24:.0f} dias para ir de Lisboa a Recife!')
    print()
