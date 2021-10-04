texto ="Este texto es para que se reemplacen las volcales por letras"
letras=input("Ingrese 5 letras...")
texto = texto.replace ("a" , letras[0])
texto = texto.replace ("e" , letras[1])
texto = texto.replace ("i" , letras[2])
texto = texto.replace ("o" , letras[3])
texto = texto.replace ("u" , letras[4])

nTexto= texto + letras
texto = texto.split(" ")
print(texto)

