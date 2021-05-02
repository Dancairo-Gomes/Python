"""

Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles



"""

X = int(input('Digite o valor de X: '))
Y = int(input('Digite o valor de Y: '))

def soma_inpares_cons(inicio, fim):   
    soma = 0
    if inicio > fim:
        
        for n in range(inicio -1, fim, -1):
            if n % 2 == 1:
                soma += n
    else:
        for n in range(inicio -1, fim):
            if n % 2 == 1:
                soma += n            
    return soma
  #  return soma
            
soma_total = soma_inpares_cons(X, Y)

print(soma_total)            
            
            