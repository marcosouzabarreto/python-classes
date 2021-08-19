# while = enquanto
# while <condição>:

# imprimir de 0 até 20, se o número for divisível por 4 digita 'haha' no lugar dele,
# e se for divisível por 10 digita hoho, se for divisivel por

contador = 0
while contador <= 20:
    if contador % 10 == 0 and contador % 4 == 0:
        print('hahahoho')

    elif contador % 4 == 0:
        print('HAHA')

    elif contador % 10 == 0:
        print('HOHO')

    else:
        print(contador)
    contador += 1
