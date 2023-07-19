def main():
    #Pido al usuario un input, luego cambio las caras felices por "🙂" y las caras tristes por " 🙁 " utilizando la funcion .replace.
    no_faces = input("Enter input: ")
    no_faces = no_faces.replace(":)", "🙂")
    print(no_faces.replace(":(", "🙁"))

main()