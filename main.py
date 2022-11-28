escolha = -1

while escolha < 1 or escolha > 4:
    escolha = int(input("""O que você deseja fazer?
[ 1 ] = Banir Numero
[ 2 ] = Desbanir Numero
[ 3 ] = Banir Numero ( Prime )
[ 4 ] = Desbanir Numero ( Prime )
Sua escolha: """))
    print('')
    print('')
    print('')

if escolha == 1:
    exec(open('./ban.py', encoding="utf-8").read(), globals())

elif escolha == 2:
    exec(open('./desban.py', encoding="utf-8").read(), globals())

elif escolha == 3:
    exec(open('./ban-prime.py', encoding="utf-8").read(), globals())

elif escolha == 4:
    exec(open('./desban-prime.py', encoding="utf-8").read(), globals())

else:
    print("Faça uma escolha valida")
    print('Inicie')

