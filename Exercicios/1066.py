qtd_par = 0
qtd_impar = 0

qtd_positivos = 0
qtd_negativos = 0

for i in range(5):
    nmr = int(input())
    
    if nmr != 0 and nmr > 0:
        qtd_positivos = qtd_positivos + 1
    elif nmr !=0 and nmr < 0:
        qtd_negativos = qtd_negativos + 1    
    
    if nmr % 2 == 0:
        qtd_par = qtd_par + 1
    else:
        qtd_impar = qtd_impar + 1
        
        
print(f'{qtd_par} valor(es) par(es)')
print(f'{qtd_impar} valor(es) impar(es)')
print(f'{qtd_positivos} valor(es) positivo(s)')
print(f'{qtd_negativos} valor(es) negativos(s)')
