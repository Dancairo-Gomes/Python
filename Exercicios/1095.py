"""

I=1 J=60
I=4 J=55
I=7 J=50
...
I=? J=0

"""

I = 1
J = 60
lista_I = []
lista_J = []

def logica_I():
    for nmr in range(0, 60, 3): 
        linha_baixo_I = I + nmr
        lista_I.append(linha_baixo_I)
        return f'I = {lista_I[nmr]}'   

def logica_J():
    for nmr in range(60, 0, -5): 
        linha_baixo_J = J - nmr
        lista_J.append(linha_baixo_J)
    return lista_J

        

listaI = logica_I()


listaI = logica_I()

print(lista_I)