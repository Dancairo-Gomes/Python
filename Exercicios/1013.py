a = int(input())
b = int(input())
c = int(input())

maiorAB = (a + b + abs(a - b )) / 2
maiorABC = (maiorAB + c + abs(maiorAB - c)) / 2

print(f'{maiorABC:.0f} eh o maior')

