def main():
    # Crear el menu:
    menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

    # Marcar el precio inicial en '0'

    monto = 0

    # Hacer un ciclo que el usuario pueda romper con ctrl + D.
    while True:
        try:
            # Recibir input
            plato = input("Item: ").title()

            # Verificar si el objeto esta en el menu.
            if plato in menu:

                # Anadir el Valor al monto acual.
                monto =+ menu[plato]

                # Mostrar el monto actual.
                print("Total: $", end='')
                print('{:.2f}'.format(monto))

        except EOFError:
            # Imprimir una linea nueva y detener el ciclo.
            print()
            break

main()