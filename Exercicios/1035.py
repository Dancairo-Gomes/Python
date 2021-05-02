A = int(input())
B = int(input())
C = int(input())
D = int(input())

if B > C and D > A and C > 0 and D > 0 and A % 2 == 0:
    soma_CD = C + D
    soma_AB = A + B
    if soma_AB < soma_CD:
        print(f'Valores Aceitos')
else:
    print(f'Valores não Aceitos')    