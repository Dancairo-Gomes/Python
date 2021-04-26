N = int(input())
quadrado_nrm = 1

for nmr in range(0, N):
    if nmr % 2 != 1:
        print(f'{nmr} ^ 2 = {nmr ** 2}')