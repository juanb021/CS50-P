# Crear un diccionario vacio.
lista = {}

# Hacer un loop.
while True:

    try:
        #Recibir el input del usuario.
        item = input().upper()

        #Revisar si el objeto esta en la lista de compras.
        if item in lista:
            #Si el objeto esta, anadir 1 a la cuenta del objeto.
            lista[item] += 1

        else:
            # Anadir el objeto a la lista.
            lista[item] = 1
    except EOFError:
        # Imprimir la lista en orden alfabetico
        for key in sorted(lista.keys()):
            print(lista[key], key)

        # Detener el loop
        break