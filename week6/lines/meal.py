def main():
    #Preguntamos al usuario la hora.
    answer = input("What time is it? ").lower()
    # Verificamos el tipo de horario utilizado.
    if 'pm' in answer:
        # Llamamos a la funcion n_convertir
        hora = n_convertir(answer)
    else:
        #Llamamos la funcion 'Convertir'.
        hora = convertir(answer)
    #Imprimimos la respuesta adecuada a cada caso.
    if hora >= 7 and hora <= 8:
        print("Breakfast time")
    elif hora >= 12 and hora <= 13:
        print("Lunch time")
    elif hora >= 18 and hora <= 19:
        print("Dinner time")


# Definimos la funcion convertir
def convertir(hora):
    #Conseguir la hora y, el minuto.
    horas, minutos = hora.split(':')
    #Convertir los minutos a un float.
    n_minutos = float(minutos) / 60
    #Retornamos el resultado al la funcion principal.
    return float(horas) + n_minutos


# Definimos la funcion n_convertir
def n_convertir(hora):
    #Eliminamos el 'Pm'
    nhora = hora.replace('pm','')
    #Conseguir la hora y, el minuto.
    horas, minutos = nhora.split(':')
    #Convertir los minutos a un float.
    n_minutos = float(minutos) / 60
    #Retornamos el resultado al la funcion principal.
    return (float(horas) + 12) + n_minutos

if __name__ == "__main__":
    main()