def run():
    nombre = input('Escribe tu nombre: ')
    for letra in nombre:
        print(letra)

    frase = input('Escribe una frase: ')
    for caracter in frase:
        print(caracter.upper())

for contador in range(11):
    print(contador)

for i in range(10):
    print(11 * i)


if __name__ == '__main__':
    run()