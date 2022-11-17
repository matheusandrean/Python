print('Meu primeiro programa!')


def menu():
    print('Conversor de velocidade')
    print('1. Converter m/s para km/h')
    print('2. Converter km/h para m/s')


def ms_for_km():
    ms = float(input('Entre com a velocidade em metros por segundo: '))
    km = ms * 3.6
    print('A velocidade é de {} quilômetros por hora.'.format(km))


def km_for_ms():
    km = float(input('Entre com a velocidade em quilômetros por hora: '))
    ms = km / 3.6
    print('A velocidade é de {} metros por segundo.'.format(ms))


if __name__ == '__main__':
    menu()
    escolha = input('Escolha o tipo de conversão que deseja realizar: ')

    if escolha == '1':
        ms_for_km()
    if escolha == '2':
        km_for_ms()
