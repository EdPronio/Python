# LIMITE = 1000
#     contador = 1
#     while contador < LIMITE:
#         contador += 1 
#         print(contador)

j = 0
j += 1
def run():
    for i in range(10):
        print(f'{tabla} x {i} = {tabla * i}')

menu = '''
    1) Tabla del 1
    2) Tabla del 2
    3) Tabla del 3
    4) Tabla del 4
    5) Tabla del 5
    6) Tabla del 6
    7) Tabla del 7
    8) Tabla del 8
    9) Tabla del 9

'''
tabla = int(input(menu))


if __name__ == '__main__':
    run()

