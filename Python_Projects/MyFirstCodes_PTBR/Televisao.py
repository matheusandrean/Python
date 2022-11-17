# Aqui implementaremos a troca de canais na televisão.
class Televisao:

    def __init__(self):
        self.ligada = False
        self.canal = 5  # Definimos que sempre ao ser ligada a TV se encontrará no CANAL 5.

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def mais_canal(self):
        if self.ligada:
            self.canal += 1
        else:
            print('A televisão está desligada')

    def menos_canal(self):
        if self.ligada:
            self.canal -= 1
        else:
            print('A televisão está desligada')

if __name__ == '__main__':
televisao = Televisao()
print('Televisão está ligada: {}'.format(televisao.ligada))
televisao.power()
print('Televisão está ligada: {}'.format(televisao.ligada))
televisao.power()
print('Televisão está ligada: {}'.format(televisao.ligada))

# Aqui tentaremos mudar de canal, porém a televisão encontra-se desligada, deve-se apresentar a informação.
televisao.mais_canal()
print('Canal: {} '.format(televisao.canal))

# Neste comando, ligaremos a TV, apenas SE e apenas SE ela estiver ligada os canais serão mudados.
televisao.power()
print('Televisão está ligada: {}'.format(televisao.ligada))

# Aqui aumentaremos o canal duas vezes.
televisao.mais_canal()
televisao.mais_canal()
print('Canal: {} '.format(televisao.canal))

# Aqui diminuiremos o canal uma vez.
televisao.menos_canal()
print('Canal: {} '.format(televisao.canal))