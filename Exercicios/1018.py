N = int(input())

notas_100 = N / 100
N = N % 100
notas_50 = N / 50
N = N % 50
notas_20 = N / 20 
N = N % 20
notas_10 = N / 10
N = N % 10
notas_5 = N / 5 
N = N % 5
notas_2 = N / 2
N = N % 2
notas_1 = N / 1  

print(f'{int(notas_100)} nota(s) de R$ 100,00')
print(f'{int(notas_50)} nota(s) de R$ 50,00')
print(f'{int(notas_20)} nota(s) de R$ 20,00')
print(f'{int(notas_10)} nota(s) de R$ 10,00')
print(f'{int(notas_5)} nota(s) de R$ 5,00')
print(f'{int(notas_2)} nota(s) de R$ 2,00')
print(f'{int(notas_1)} nota(s) de R$ 1,00')



