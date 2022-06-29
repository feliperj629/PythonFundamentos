# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

print('Selecione o número da operação desejada:')
print('1- Soma')
print('2- Subtração')
print('3- Multiplicação')
print('4- Divisão')

op = int(input('Digite sua opção (1/2/3/4): '))
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if op == 1:
    print('{} + {} = {}'.format(n1, n2, n1+n2))
elif op == 2:
    print('{} - {} = {}'.format(n1, n2, n1-n2))
elif op == 3:
    print('{} x {} = {}'.format(n1, n2, n1*n2))
elif op == 4:
    print('{} / {} = {}'.format(n1, n2, n1/n2))
else:
    print('Opção invalida!')
