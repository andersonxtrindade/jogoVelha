from random import randint
import time
def menu():
    cont = 1
    while cont:
        escolha = int(input( "0. Sair \n"+
                             "1. Jogar 1 x 1\n" +
                             "2. Jogar contra computador\n"+
                             "Escolha: "))
        if escolha == 1:
            jogo1x1()
        elif escolha == 2:
            computador()
        else:
            print("Saindo...")
            break

def computador():
    print("\nJogo contra o computador!\n")
    tabuleiro_inicial = '''
--- COMO JOGAR ---
Quando for sua vez, digite a linha e a coluna correspondente à posição no tabuleiro para fazer sua jogada nela, conforme a tabela abaixo!
lin:0 |lin:0 |lin:0     
col:0 |col:1 |col:2    
______|______|_____
lin:1 |lin:1 |lin:1     
col:0 |col:1 |col:2   
______|______|_____
lin:2 |lin:2 |lin:2     
col:0 |col:1 |col:2
      |      |     
    '''

    print(tabuleiro_inicial)
    rodada = 0
    while vitoria() == 0:
        
        if rodada%2 == 0:
            print("Faça a sua jogada, jogador {}!".format(rodada%2+1))
            linha = int(input("Digite a linha, jogador {}: ".format(rodada%2+1)))
            coluna = int(input("Digite a coluna, jogador {}: ".format(rodada%2+1)))

            if rodada%2 == 0 and velha[linha][coluna] == 0:
                velha[linha][coluna] = 1
                exibir()
            else:
                print("\n Essa coluna está ocupada, por favor selecione outra! \n")
                rodada -= 1
        

        elif rodada%2 == 1:
            print("Jogada do computador")
            linha = randint(0,2)
            coluna = randint(0,2)                

            if rodada%2 == 1 and velha[linha][coluna] == 0:
                velha[linha][coluna] = -1
                exibir()
            else:
                print("\n Essa coluna está ocupada, por favor selecione outra! \n")
                rodada -= 1

        rodada += 1

        if vitoria() == 1 and rodada%2 == 1:
            rodada-=1
            print("Jogador {} ganhou após {} rodadas".format(rodada%2+1, rodada+1))

        elif vitoria() == 1 and rodada%2 == 0:
            rodada-=1
            print("Computador ganhou o jogo!")
        
        if rodada == 9:
            print("Fim de jogo, empate!")



def jogo1x1():
    print("\nJogo 1 X 1\n")
    tabuleiro_inicial = '''
--- COMO JOGAR ---
Quando for sua vez, digite a linha e a coluna correspondente à posição no tabuleiro para fazer sua jogada nela, conforme a tabela abaixo!
lin:0 |lin:0 |lin:0     
col:0 |col:1 |col:2    
______|______|_____
lin:1 |lin:1 |lin:1     
col:0 |col:1 |col:2   
______|______|_____
lin:2 |lin:2 |lin:2     
col:0 |col:1 |col:2
      |      |     
    '''

    print(tabuleiro_inicial)
    rodada = 0
    while vitoria() == 0:
        
        if rodada%2 == 0:
            print("Faça a sua jogada, jogador {}!".format(rodada%2+1))
            linha = int(input("Digite a linha, jogador {}: ".format(rodada%2+1)))
            coluna = int(input("Digite a coluna, jogador {}: ".format(rodada%2+1)))

            if rodada%2 == 0 and velha[linha][coluna] == 0:
                velha[linha][coluna] = 1
                exibir()
            else:
                print("\n Essa coluna está ocupada, por favor selecione outra! \n")
                rodada -= 1
        

        elif rodada%2 == 1:
            print("Faça a sua jogada, jogador {}!".format(rodada%2+1))
            linha = int(input("Digite a linha, jogador {}: ".format(rodada%2+1)))
            coluna = int(input("Digite a coluna, jogador {}: ".format(rodada%2+1)))  

            if rodada%2 == 1 and velha[linha][coluna] == 0:
                velha[linha][coluna] = -1
                exibir()
            else:
                print("\n Essa coluna está ocupada, por favor selecione outra! \n")
                rodada -= 1

        rodada += 1
        if vitoria() == 1:
            rodada-=1
            print("Jogador {} ganhou após {} rodadas".format(rodada%2+1, rodada+1))
            break
        
        if rodada == 9:
            print("Fim de jogo, empate!")
            break



#Iniciando a matriz
def matrizVelha(num_linha, num_coluna, valor):
    matriz = []
    for i in range(num_linha):
        linha = []
        for j in range(num_coluna):
            linha += [valor]
        matriz += [linha]
    return matriz

#Exibição da matriz
def exibir():
    for i in range(3):
        for j in range(3):
            if velha[i][j] == 0:
                print('_', end=' ')
            elif velha[i][j] == -1:
                print('O', end=' ')
            elif velha[i][j] == 1:
                print('X', end=' ')
        print()

#Função para definir vitória
def vitoria():
    for i in range(3):
        soma = velha[i][0] + velha[i][1] + velha[i][2]
        if soma == 3 or soma == -3:
            return 1
    for i in range(3):
        soma = velha[0][i] + velha[1][i] + velha[2][i]
        if soma == 3 or soma == -3:
            return 1
    
    verificarDiagonal1 = velha[0][0] + velha[1][1] + velha[2][2]
    verificarDiagonal2 = velha[0][2] + velha[1][1] + velha[2][0]
    
    if verificarDiagonal1 == 3 or verificarDiagonal1 == -3 or verificarDiagonal2 == 3 or verificarDiagonal2 == -3:
        return 1

    return 0
    
        

velha = matrizVelha(3, 3, 0)
menu()