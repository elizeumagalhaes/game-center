import time
import random
from cores import *

palavras = ['Bigorna', 'Caviar', 'Rucula', 'Palmilha', 'Balsa', 'Torneira', 'Google', 'Mamute', 'Pycharm', 'Capivara']
dicas = ['Objeto 📷', 'Comida 🍴', 'Comida 🍴', 'Vestuário 👗', 'Transporte 🚗', 'Objeto 📷', 'Tecnologia 💻', 'Animal 🐶', 'Tecnologia 💻', 'Animal 🐶']
letras_corretas = []
letras = []

letra_Errada = 0
acertos = 0

def verificar_tempo():
    fim = time.time()
    resultado_Tempo = fim - inicio
    return resultado_Tempo

def verificar_erro():
    global chute
    global letra_Errada
    global acertos
    rodada = 0

    while len(letras_corretas) != len(palavras[pos].lower()):
        if rodada > 0:
            print('\n' * 30)
            print(f'\nDica: \33[36m{dicas[pos]}\33[m')
            print('Chutes: ', ', '.join(letras))
        imprimir_forca()
        rodada += 1
        for letra in palavras[pos].lower():
            if letra in letras_corretas:
                print(letra, end=' ')
            else:
                print('_', end=' ')
        chute = input('\nChute uma letra: ').lower()
        tempo = verificar_tempo()
        if opcao == 3:
            if tempo > 60:
                print('Você excedeu o tempo limite!')
                print('\n\33[31m╔═╗╔═╗╔╦╗╔═╗  ╔═╗╦  ╦╔═╗╦═╗')
                print('║ ╦╠═╣║║║║╣   ║ ║╚╗╔╝║╣ ╠╦╝')
                print('╚═╝╩ ╩╩ ╩╚═╝  ╚═╝ ╚╝ ╚═╝╩╚═\33[m')
                exit()
        if opcao == 2:
            if tempo > 90:
                print('Você excedeu o tempo limite!')
                print('\n\33[31m╔═╗╔═╗╔╦╗╔═╗  ╔═╗╦  ╦╔═╗╦═╗')
                print('║ ╦╠═╣║║║║╣   ║ ║╚╗╔╝║╣ ╠╦╝')
                print('╚═╝╩ ╩╩ ╩╚═╝  ╚═╝ ╚╝ ╚═╝╩╚═\33[m')
                exit()
        if opcao == 1:
            if tempo > 120:
                print('Você excedeu o tempo limite!')
                print('\n\33[31m╔═╗╔═╗╔╦╗╔═╗  ╔═╗╦  ╦╔═╗╦═╗')
                print('║ ╦╠═╣║║║║╣   ║ ║╚╗╔╝║╣ ╠╦╝')
                print('╚═╝╩ ╩╩ ╩╚═╝  ╚═╝ ╚╝ ╚═╝╩╚═\33[m')
                exit()
        if chute in palavras[pos].lower():
            quantas_tem = palavras[pos].lower().count(chute)
            for i in range(quantas_tem):
                letras_corretas.append(chute)
            letras.append(chute)
        else:
            letra_Errada += 1
            letras.append(chute)

    print('\n' * 30)
    print(f'{cores["byellow"]}            ___________      ')
    print("           '._==_==_=_.'     ")
    print("           .-\\:      /-.    ")
    print("          | (|:.     |) |    ")
    print("           '-|:.     |-'     ")
    print("             \\::.    /      ")
    print("              '::. .'        ")
    print("                ) (          ")
    print("              _.' '._        ")
    print(f"             '-------'       ")
    print('╦  ╦╔═╗╔═╗╔═╗  ╔═╗╔═╗╔╗╔╦ ╦╔═╗╦ ╦┬')
    print('╚╗╔╝║ ║║  ║╣   ║ ╦╠═╣║║║╠═╣║ ║║ ║│')
    print(' ╚╝ ╚═╝╚═╝╚═╝  ╚═╝╩ ╩╝╚╝╩ ╩╚═╝╚═╝o')

def imprimir_forca():

    qntd_Letras = len(palavras[pos])

    if letra_Errada == 0:
        print('  +------+')
        print('  |/     |')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('\33[32mMmMMmMmMmmNMm\33[m')

    elif letra_Errada == 1:
        print('  +------+')
        print('  |/     |')
        print('  |     \33[35m( )\33[m')
        print('  |')
        print('  |')
        print('  |')
        print('\33[32mMmMMmMmMmmNMm\33[m')

    elif letra_Errada == 2:
        print('  +------+')
        print('  |/     |')
        print('  |     \33[35m( )\33[m')
        print('  |      \33[35m|\33[m')
        print('  |')
        print('  |')
        print('\33[32mMmMMmMmMmmNMm\33[m')

    elif letra_Errada == 3:
        print('  +------+')
        print('  |/     |')
        print('  |     \33[35m( )\33[m')
        print('  |     \33[35m/|\33[m')
        print('  |')
        print('  |')
        print('\33[32mMmMMmMmMmmNMm\33[m')

    elif letra_Errada == 4:
        print('  +------+')
        print('  |/     |')
        print('  |     \33[35m( )\33[m')
        print('  |     \33[35m/|\\\33[m')
        print('  |')
        print('  |')
        print('\33[32mMmMMmMmMmmNMm\33[m')

    elif letra_Errada == 5:
        print('  +------+')
        print('  |/     |')
        print('  |     \33[35m( )\33[m')
        print('  |     \33[35m/|\\\33[m')
        print('  |     \33[35m/\33[m')
        print('  |')
        print('\33[32mMmMMmMmMmmNMm\33[m')

    elif letra_Errada == 6:
        print('  +------+')
        print('  |/     |')
        print('  |     \33[35m( )\33[m')
        print('  |     \33[35m/|\\\33[m')
        print('  |     \33[35m/ \\\33[m')
        print('  |')
        print('\33[32mMmMMmMmMmmNMm\33[m')
        print(f'A palavra sorteada era: \33[35m{palavras[pos]}\33[m')
        print('\n\33[31m╔═╗╔═╗╔╦╗╔═╗  ╔═╗╦  ╦╔═╗╦═╗')
        print('║ ╦╠═╣║║║║╣   ║ ║╚╗╔╝║╣ ╠╦╝')
        print('╚═╝╩ ╩╩ ╩╚═╝  ╚═╝ ╚╝ ╚═╝╩╚═\33[m')
        exit()

def sortear():

    global pos

    print('Sorteando palavra para iniciar o jogo...')
    time.sleep(2)
    pos = random.randint(0, 9)
    print(f'Dica: \33[36m{dicas[pos]}\33[m')
    verificar_erro()

def game():

    global inicio
    global opcao

    print('\33[35m ╦╔═╗╔═╗╔═╗  ╔╦╗╔═╗  ╔═╗╔═╗╦═╗╔═╗╔═╗')
    print(' ║║ ║║ ╦║ ║   ║║╠═╣  ╠╣ ║ ║╠╦╝║  ╠═╣')
    print('╚╝╚═╝╚═╝╚═╝  ═╩╝╩ ╩  ╚  ╚═╝╩╚═╚═╝╩ ╩\33[m')
    time.sleep(2)
    print('Selecione a dificuldade do jogo:')
    print('<1> \33[32mFácil\33[m')
    print(f'<2> {cores["byellow"]}Médio{clear}')
    print('<3> \33[31mDifícil\33[m')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        inicio = time.time()
        sortear()
    elif opcao == 2:
        inicio = time.time()
        sortear()
    elif opcao == 3:
        inicio = time.time()
        sortear()
    else:
        while opcao != 1 and opcao != 2 and opcao != 3:
            opcao = int(input('Digite uma opção válida: '))

if __name__ == "__main__":
    game()