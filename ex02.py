print('-' * 30)
print('Sequência de Fibonacci')
print("-" * 30)
num =  int(input('Informe a quantidade de termos: '))
t1 = 0
t2 = 1
print(t1, t2)
cont = 3
while cont <= num:
    t3 = t1 + t2
    print(t3)
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')