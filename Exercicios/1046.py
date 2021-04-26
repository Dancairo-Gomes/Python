"""

Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, 
tendo uma duração mínima de 1 hora e máxima de 24 horas.

Entrada
A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.

Saída
Apresente a duração do jogo conforme exemplo abaixo.


"""

hora_inicio = int(input())
hora_fim = int(input())
duracao_jogo = 1

def calc_time_game(hora_inicio, hora_fim):
    if hora_inicio >= hora_fim and hora_fim <= 12:
        hora_fim += 12
        duracao_jogo = hora_inicio - hora_fim
        return duracao_jogo
    else:
        hora_fim = hora_fim + 24
        duracao_jogo = hora_inicio - hora_fim
        return duracao_jogo
    
print(f'O JOGO DUROU {calc_time_game(hora_inicio, hora_fim)} HORA(S)')            

