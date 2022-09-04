def conversor_dolar(tipo_pesos, valor_dolar):
    pesos = float(input("¿Cuantos pesos " + tipo_pesos + " tienes?"))
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    print("Tienes $" + str(dolares) + "dolares")
    


moneda = """
Bienvenido al conversor de monedas 💵💸

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos
"""

opcion = int(input(moneda))

if opcion == 1:
    conversor_dolar("Colombianos", 3875)
elif opcion == 2:
    conversor_dolar("argentinos", 65)
elif opcion == 3:
    conversor_dolar("mexicanos", 24)
else:
    print("Opcion invalida!")