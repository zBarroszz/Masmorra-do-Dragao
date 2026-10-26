

from time import sleep
import random
vida_heroi = 0
ataque_heroi = 0 
pocao_heroi = 2
pocao = 20
classe_heroi = ''
vida_maximo = 100
vida_arqueiro = 100
vida_mago = 80
vida_guerreiro = 120
print('===========================================')
print('            MASMORRA DO DRAGÃO             ')
print('===========================================')
nome_heroi = str(input('Qual o nome do seu heroi?:  '))
sleep(0.5)
print(f'\n\n\nBem vindo á masmorra, {nome_heroi}!.')
sleep(0.5)
print('Sua aventura está prestes a começar....')
sleep(0.5)

print('Mas primeiro, vamos escolher sua classe')
sleep(0.5)
escolher_classe = True
while escolher_classe:
    try:
        classe_heroi =  int(input('Escolha sua classe\n\n[1]Arqueiro (Vida inicial 100| Ataque 27)\n[2]Guerreiro (Vida inicial 120| Ataque 20)\n[3]Mago (Vida inicial 80| Ataque 35)\nEscolha:'))
        if classe_heroi == 1:
            print(f'Ótima escolha, você escolheu a classe Arqueiro, vamos começar sua jornada!')
            vida_heroi += 100
            ataque_heroi += 27
            escolher_classe = False
            classe_heroi = 'Arqueiro'
        elif classe_heroi == 2:
            print(f'Ótima escolha, você escolheu a classe Guerreiro, vamos começar sua jornada!')
            vida_heroi += 120
            ataque_heroi += 20
            escolher_classe = False
            classe_heroi = 'Guerreiro'
        elif classe_heroi == 3:
            print(f'Ótima escolha, você escolheu a classe Mago, vamos começar sua jornada!')
            vida_heroi += 80
            ataque_heroi += 35
            escolher_classe = False
            classe_heroi = 'Mago'
        else:
            print('Classe invalida, digite um numero valido(1/2/3): \n\n')
            sleep(2)
            escolher_classe = True
    except ValueError:
        print('Classe invalida!, digita um numero valido(1/2/3)')
sleep(1)
print('Mas antes vou lhe mostrar sua ficha de heroi...')
sleep(1)
print('====================== Ficha do jogador ======================')
print(f'Nome do heroi:{nome_heroi}\nClasse do heroi:{classe_heroi}\nVida inicial:{vida_heroi}\nAtaque inicial:{ataque_heroi}\n==============================================================')
sleep(2)
print(f'Agora a verdadeira aventura está prestes a começar... {nome_heroi} segue explorando quando encontra uma masmorra, {nome_heroi} fica indeciso e precisa decidir se entra ou não na masmorra ')
sleep(1)
aventura = True
escolher_masmora = True
while escolher_masmora: 
    entrar_masmorra = input('Você deseja explorar a masmorra?(s/n):  ').strip().upper()   

    if entrar_masmorra == 'S':
        escolher_masmora = False
        print('Sua aventura começou de verdade heroi, se prepare!!')
        
        

    elif entrar_masmorra == 'N':
        print('Tudo bem heroi, é bom saber a hora de estar preparado, quando estiver pronto estarei aqui para te guiar, até a proxima')
        aventura = False
        escolher_masmora = False            
    else:
        print('Resposta invalida, digite S ou N por favor')
        sleep(1)
if aventura:
    print(f'{nome_heroi} continua explorando a masmorra, são tantos andares e coisas desconhecidas que {nome_heroi} nunca viu na vida dele')
    sleep(1)
    print('...')
    sleep(1)
    print('.......')
    sleep(1)
    print('BOOMM!')
    sleep(0.5)
    print(f'UM GOBLIN APARECEU, e agora {nome_heroi}? oque vamos fazer?')
    vida_goblin = 60
    ataque_goblin = 10
    print(f'==========\nVida:{vida_goblin}\nAtaque:{ataque_goblin}\n==========')

    batalha = True
    while batalha:
        escolha_batalha = int(input('Escolhe a opção desejada:\n[1]Atacar Goblin\n[2]Curar poção(+20)\n[3]Fugir\n\nEscolha: '))
        if escolha_batalha == 1:
        
                if vida_heroi >=1:   
                    print('PAA')
                    sleep(1)
                    print(f'\nVocê atacou goblin e causou {ataque_heroi} de dano\n')
                    vida_goblin -= ataque_heroi
                
                    if vida_goblin <=0:
                        vida_goblin = 0
                        print(f'\nParabens!! Você derrotou o Goblin!!\n')
                        batalha = False
        
                            


        if escolha_batalha == 2:
            if pocao_heroi >=1:             
                if classe_heroi == ('Arqueiro'):    
                    if vida_heroi < vida_arqueiro:
                        sleep(1)
                        print('Tomando a poção**')
                        sleep(2)
                        print(f'Você curou {pocao} de HP\n')
                        vida_heroi += pocao                    
                        pocao_heroi -= 1
                        if vida_heroi > vida_arqueiro:
                            vida_heroi = 100
                            print(f'Você agora tem {vida_heroi}HP.\n')
                        else:
                            print(f'Seu HP atual agora é de {vida_heroi}HP.\n')    
                    else:
                        print('Sua vida está cheia!!!.\n')
                
                if classe_heroi == ('Guerreiro'):
                    if vida_heroi < vida_guerreiro:
                        sleep(1)
                        print('Tomando a poção**')
                        sleep(2)
                        print(f'Você curou {pocao} de HP\n')
                        vida_heroi += pocao                
                        pocao_heroi -= 1
                        if vida_heroi > vida_guerreiro:
                            vida_heroi = 120
                            print(f'Você agora tem {vida_heroi}HP.\n')
                        else:
                            print(f'Seu HP atual agora é de {vida_heroi}HP.\n')        
                    else:
                        print('Sua vida está cheia!!!.\n')
                                    
                        
                if classe_heroi == ('Mago'):
                    if vida_heroi < vida_mago:
                        sleep(1)
                        print('Tomando a poção**')
                        sleep(2)
                        print(f'Você curou {pocao} de HP\n')
                        vida_heroi += pocao
                        
                        
                        pocao_heroi -= 1
                        if vida_heroi > vida_mago:
                            vida_heroi = 80
                            print(f'Você agora tem {vida_heroi}HP.\n')
                        else:                   
                            print(f'Seu HP atual agora é de {vida_heroi}HP.\n')        
                    else:
                        print('Sua vida está cheia!!!.\n')
            elif pocao_heroi <= 0:
                print('Você não tem poçoes o suficiente!')

        if escolha_batalha == 3:
            escapar = random.randint(1, 4)
            if escapar == 1:
                print('\nVocê conseguiu escapar da luta!.\n')
                batalha = False
            else:
                print('*************\nGoblin impediu sua fuga!!\n*************')

        if vida_goblin >=1 and batalha:
                                    batalha = True
                        
                                    atq_critico_goblin = random.randint(1, 4)
                                    if atq_critico_goblin == 1:
                                                    sleep(2)
                                                    vida_heroi -= 15
                                                    print('O Goblin atacou!, causando 15 de dano!.')
                                                    sleep(1)
                                                    print(f'Vida atual do heroi:{vida_heroi}\n==========\nVida atual do inimigo:{vida_goblin}')
                                    elif atq_critico_goblin == 4:
                                                    sleep(2)
                                                    vida_heroi -= 30
                                                    print(f'*Goblin causou dano CRITICO!, causando 30 de dano. ')
                                                    sleep(1)
                                                    print(f'Vida atual do heroi:{vida_heroi}\n==========\nVida atual do inimigo:{vida_goblin}')
                                    elif atq_critico_goblin == 2 or atq_critico_goblin == 3:
                                        sleep(2)
                                        vida_heroi -= 10
                                        print('O Goblin atacou!, causando 10 de dano!.')
                                        sleep(1)
                                        print(f'Vida atual do heroi:{vida_heroi}\n==========\nVida atual do inimigo:{vida_goblin}')


        if vida_heroi <=0:
                        
                    print('Você foi derrotado pelo goblin, deseja tentar novamente?' )
                    tentar_denovo = input('(S/N): ').strip().upper()
                    if tentar_denovo == 'S':
                        sleep(1)
                        print('Reiniciando a batalha...')
                        sleep(1)
                        aventura = True
                        batalha = True
                        vida_goblin = 60
                        if classe_heroi == 'Arqueiro':
                            vida_heroi = 100
                        elif classe_heroi == 'Guerreiro':
                                vida_heroi = 120
                        elif classe_heroi == 'Mago':
                                vida_heroi = 80
                        else:
                            batalha = True

                    elif tentar_denovo == 'N':
                        print('Saindo do jogo....')
                        sleep(2)
                        quit()


        