N = int(input())
qtd_in = 0
qtd_out = 0

for nmr in range(0, N):
    casos_teste = int(input())
    
    if casos_teste in range(10, 20):
        qtd_in = qtd_in + 1
    else:
        qtd_out = qtd_out + 1
        

print(f'{int(qtd_in)} in')         
print(f'{int(qtd_out)} out')         
