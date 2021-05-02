tempo_segundos = int(input())

horas = tempo_segundos / 3600;
tempo_segundos = tempo_segundos % 3600;
minutos = tempo_segundos / 60;
segundos = tempo_segundos % 60;

print(f'{int(horas)}:{int(minutos)}:{int(segundos)}')