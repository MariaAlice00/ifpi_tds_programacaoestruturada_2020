from time import sleep

print('''
Q1 - Quantos zeros tem o número UM BILHÃO?
a - seis
b - sete
c - dez
''')
q1 = input('>>> ').lower()
sleep(1)
if q1 == 'a':
    print('Correto!!!')
elif q1 == 'b':
    print('Quase!')
elif q1 == 'c':
    print('Um pouco demais, não acha?')
else:
    print('Você não escolheu a, b ou c')
print('='*20)


print('''
Q2 - Em que ano foi assinada a Lei Áurea no Brasil?
a - 1788
b - 1888
c - 2000
''')
q2 = input('>>> ').lower()
sleep(1)
if q2 == 'a':
    print('Acrescente mais 100 anos e teria a resposta certa!')
elif q2 == 'b':
    print('Correto!!!')
elif q2 == 'c':
    print('Faz mais tempo que isso!')
else:
    print('Você não escolheu a, b ou c')
print('='*20)


print('''
Q3 - É uma cidade do Piauí?
a - Maceió
b - Gramado
c - Parnaíba
''')
q3 = input('>>> ').lower()
sleep(1)
if q3 == 'a':
    print('Não! Maceió é a caoital de Alagoas.')
elif q3 == 'b':
    print('Não! Gramado fica no Rio Grande do Sul.')
elif q3 == 'c':
    print('Correto!!!')
else:
    print('Você não escolheu a, b ou c')
print('='*20)


print('Obrigada por jogar!!!')