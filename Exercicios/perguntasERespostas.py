perguntas = {
    'Pergunta 1:': {
        'pergunta': 'Quanto é 2 + 2',
        'respostas': {'a': '1', 'b': '4', 'c': '5'},
        'resposta_certa': 'b'
    },
    'Pergunta 2:': {
        'pergunta': 'Quanto é 5 * 5',
        'respostas': {'a': '1', 'b': '2', 'c': '25'},
        'resposta_certa': 'c'
    },
    
}
resposta_certas = 0

for pk, vk in perguntas.items():
    print(f'{pk} {vk["pergunta"]}')
    print('Respostas: ')
    
    for rk, rv in vk['respostas'].items():
        print(f'[{rk}]: {rv}')    
        
    resposta = input('A resposta correta é: ')
    if resposta == vk['resposta_certa']:
        print('UHUUUUU ACERTOUUU')
        resposta_certas += 1
    else:
        print('Voce errou, precisa estudar mais.')    
    print()
    
    qtd_perguntas = len(perguntas)
    porcentagem_acertos = resposta_certas / qtd_perguntas * 100
    
    print(f'Quantidade de acertos: {resposta_certas}')
    print(f'Porcentagem de acertos: {porcentagem_acertos}%')    