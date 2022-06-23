import random
R1,R2,R3 = [],[],[]
falha= []
for c in range(10000000):
        x=random.choices(['M1','M2','FALHA'],weights=[6,3,1])
        if x == ['M1'] :
                e=random.choices(['M3','M4','FALHA'],weights=[5,3,2])
                if e == ['M3']:
                    y=random.choices(['Destino','FALHA'],weights=[9,1])
                    if y == ['Destino']:
                        R1.append(1)
                    else:
                        falha.append(1)
                elif e == ['M4']:
                    y=random.choices(['Destino','FALHA'],weights=[8,2])
                    if y == ['Destino']:
                        R2.append(1)
                    else:
                        falha.append(1)
                else:
                    falha.append(1)
        elif x == ['M2']:
                e=random.choices(['M5','FALHA'],weights=[9.5,0.5])
                if e == ['M5']:
                    y=random.choices(['Destino','FALHA'],weights=[8.5,1.5])
                    if y == ['Destino']:
                        R3.append(1)
                    else:
                        falha.append(1)
                else:
                    falha.append(1)
        else:
            falha.append(1)

print('Estatísticas do envio de 10000000 pacotes:')
print(f'{sum(R1)} pacotes chegaram pela rota1;')
print(f'{sum(R2)} pacotes chegaram pela rota2;')
print(f'{sum(R3)} pacotes chegaram pela rota3;')
print(f'{sum(falha)} pacotes se perderam (falharam)')
