nmr = float(input())

if nmr < 0 or nmr > 100:
    print(f'Fora do Intervalo')
else:
    if nmr >= 0 and nmr <= 25:
        print(f'Intervalo (0,25]')
    elif nmr >=25 and nmr <= 50:
        print(f'Intervalo (25,50]')
    elif nmr >= 50 and nmr <= 75:
        print(f'Intervalo (50,75]')
    elif nmr >= 75 and nmr <= 100:
        print(f'Intervalo (75,100]')           
 
            