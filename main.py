print (''' 
░██╗░░░░░░░██╗██████╗░██████╗░    ██████╗░░█████╗░███╗░░██╗
░██║░░██╗░░██║██╔══██╗██╔══██╗    ██╔══██╗██╔══██╗████╗░██║
░╚██╗████╗██╔╝██████╔╝██████╔╝    ██████╦╝███████║██╔██╗██║
░░████╔═████║░██╔═══╝░██╔═══╝░    ██╔══██╗██╔══██║██║╚████║
░░╚██╔╝░╚██╔╝░██║░░░░░██║░░░░░    ██████╦╝██║░░██║██║░╚███║
░░░╚═╝░░░╚═╝░░╚═╝░░░░░╚═╝░░░░░    ╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝''')

print ('agradecimento: Abrobrinha#9699')
print ('           ')
print('''
░█████╗░██╗░░░██╗██╗░██████╗░█████╗░██╗
██╔══██╗██║░░░██║██║██╔════╝██╔══██╗██║
███████║╚██╗░██╔╝██║╚█████╗░██║░░██║██║
██╔══██║░╚████╔╝░██║░╚═══██╗██║░░██║╚═╝
██║░░██║░░╚██╔╝░░██║██████╔╝╚█████╔╝██╗
╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═════╝░░╚════╝░╚═╝''')
print('')
print('PROJETO FINALIZADO!')
print('''terminei esse projeto, nao ter mais nenhuma atualizaçao!''')
print('')
print('CASO QUEIRA COMPRAR ALGUM SCRIPT')
print('ME MANDE MSG VIA INSTAGRAM!')
print('@slayerkkk_')
print ('')

escolha = -1

while escolha < 1 or escolha > 6:
    escolha = int(input("""O que você deseja fazer?
[ 1 ] = Banir Numero
[ 2 ] = Desbanir Numero
[ 3 ] = Banir Numero ( Prime )
[ 4 ] = Desbanir Numero ( Prime )
[ 5 ] = Banir Numero (deluxe)
[ 6 ] = Desbanir Numero (deluxe)
Sua escolha: """))
    print('')
    print('')
    print('')
    

if escolha == 1:
    exec(open('ban.py', encoding="utf-8").read(), globals())

elif escolha == 2:
    exec(open('desban.py', encoding="utf-8").read(), globals())

elif escolha == 3:
    exec(open('ban-prime.py', encoding="utf-8").read(), globals())

elif escolha == 4:
    exec(open('desban-prime.py', encoding="utf-8").read(), globals())

if escolha == 5:
    exec(open('ban-deluxe.py', encoding="utf-8").read(), globals())

if escolha == 6:
    exec(open('desban-deluxe.py', encoding="utf-8").read(), globals())

else:
    print("Faça uma escolha valida")
    print('Inicie')