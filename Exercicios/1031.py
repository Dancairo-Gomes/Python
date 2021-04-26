"""

A Federação Gaúcha de Futebol contratou você para escrever um programa para fazer uma estatística do resultado de vários GRENAIS.
Escreva um programa para ler o número de gols marcados pelo Inter e pelo Grêmio em um GRENAL. Logo após escrever a mensagem
"Novo grenal (1-sim 2-nao)" e solicitar uma resposta. Se a resposta for 1, o algoritmo deve ser executado novamente solicitando 
o número de gols marcados pelos times em uma nova partida, caso contrário deve ser encerrado imprimindo:

- Quantos GRENAIS fizeram parte da estatística.
- O número de vitórias do Inter.
- O número de vitórias do Grêmio.
- O número de Empates.
- Uma mensagem indicando qual o time que venceu o maior número de GRENAIS (ou "Nao houve vencedor", caso termine empatado).


Entrada
O arquivo de entrada contém 2 valores inteiros, correspondentes aos gols marcados pelo Inter e pelo Grêmio respectivamente. 
Em seguida háverá um inteiro (1 ou 2), correspondente à repetição do programa.

Saída
Após cada leitura dos gols, deve ser impressa a mensagem "Novo grenal (1-sim 2-nao)".
Quando o algoritmo for encerrado devem ser mostradas as estatísticas conforme a descrição apresentada acima. 
Obs: a palavra "Gremio" deve ser impressa sem acento, conforme o exemplo abaixo.

"""

def grenais(gols_inter=0, gols_gremio=0, novo_grenal=1):
    vitorias_inter = 0
    vitorias_gremio = 0
    empates = 0
    qtd_grenais = 1
    maior_vencedor = ''
    
    while novo_grenal == 1:
        gols_inter = int(input('Quantos gols o inter marcou: '))
        gols_gremio= int(input('Quantos gols o gremio marcou: '))
        novo_grenal = int(input('Novo grenal (1-sim 2-nao): '))
        
        if novo_grenal == 1:
            qtd_grenais += 1
        
        if gols_inter > gols_gremio:
            vitorias_inter += 1
        elif gols_inter < gols_gremio:
            vitorias_gremio += 1    
        else:
            empates += 1    
        
    

    print(f'Quantidade grenais é {qtd_grenais}')
    print(f'Vitorias Inter: {vitorias_inter}')
    print(f'Vitorias Gremio: {vitorias_gremio}')
    print(f'empates: {empates}')

resultado = grenais()

        
        