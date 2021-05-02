idade_dias = int(input())

anos = idade_dias / 365
idade_dias = idade_dias % 365
meses = idade_dias / 30
dias = idade_dias % 30

print(f'{int(anos)} ano(s)')
print(f'{int(meses)} mese(es)')
print(f'{int(dias)} dia(s)')