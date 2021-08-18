# Condicionais
# if, elif e else

# Usuário vai digitar uma nota, se ela for maior que 6 aparece aprovado
# se for entre 3 e 6 aparece recuperação
# se for menor que 3 aparece reprovado

# && = and = e
# || = ou

# if <condição>:
numero = int(input("Digite um numero\n"))

if numero >= 6:
    print('você foi aprovado')
elif 6 > numero > 3:
    print('você ficou de recuperação')
else:
    print('você foi reprovado')
