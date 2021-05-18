def run():
    opcion = 0
    while opcion != 4:
        menu = """
            Bienvenido al conversor de monedas🐺
            1 - Pesos Colombianos
            2 - Pesos Argentinos
            3 - Pesos mexicanos
            4 - Salir

            Elige una Opción:
            """
        
    
        opcion = int(input(menu))
    

        def conversor(tipo_pesos, valor_dolar):
            pesos = input("¿Cuantos pesos " + tipo_pesos + "quiere cambiar?: ")
            pesos = float(pesos)
            dolares = pesos / valor_dolar
            dolares = round(dolares, 2)
            dolares = str(dolares)
            print("Tienes $" + dolares + " dólares")
    

    
        if opcion == 1:
            conversor("Colombianos ", 3875)
        elif opcion == 2:
            conversor("Argentinos ", 142)
        elif opcion == 3:
            conversor('Mexicanos ', 19.82)
        elif opcion ==4:
            exit()
        else:
            print("Por favor elige una opción correcta")
        continue

if __name__ == '__main__':
    run()