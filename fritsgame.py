import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero = int(input('Elige un numero del 1 al 100: '))
    while numero != numero_aleatorio:
        if numero < numero_aleatorio:
            print('Busca un número mas grande')
        else:
            print('Busca un numero mas pequeño')
        numero = int(input('Elige otro numero:  '))
    print('Ganaste')


if __name__ == '__main__':
    run()