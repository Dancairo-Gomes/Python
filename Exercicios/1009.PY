name = input()
salario_fixo = float(input())
vendas_efetuadas = float(input())
comissao = (15 * vendas_efetuadas) / 100
TOTAL = salario_fixo + comissao

print(f'TOTAL = R$ {TOTAL:.2f}')