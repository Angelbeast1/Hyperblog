def run():
    diccionario = {
        'llave': 1,
        'llave2': 2,
        'llave3': 'hola',
    }
    print(diccionario['llave'])
    print(diccionario['llave2'])
    print(diccionario['llave3'])

    poblacion = {
        'ARGENTINA': 44938712,
        'BRASIL': 210147125,
        'COLOMBIA': 50372445,
    }

    #for pais in poblacion.keys():
    #    print(pais)

    #for pais in poblacion.values():
    #    print(pais)

    for pais, poblacio in poblacion.items():
        print(pais + ' tiene ' + str(poblacio) + ' habitantes')


if __name__ == '__main__':
    run()