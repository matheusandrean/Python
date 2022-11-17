print('Minha primeira Calculadora!')

operacao = input('''Selecione o tipo de operação matemática que deseja realizar:
1. Adição
2. Subtração
3. Multiplicação
4. Divisão
''')

num1 = float(input('Entre com o primeiro número: '))
num2 = float(input('Entre com o segundo número: '))

if operacao == '1':
    print('{} + {} = '.format(num1, num2), (num1 + num2))

if operacao == '2':
    print('{} - {} = '.format(num1, num2), (num1 - num2))

if operacao == '3':
    print('{} x {} = '.format(num1, num2), (num1 * num2))

if operacao == '4':
    print('{} / {} = '.format(num1, num2), (num1 / num2))

else:
    print('Você Digitou um valor de operação inválido!')





