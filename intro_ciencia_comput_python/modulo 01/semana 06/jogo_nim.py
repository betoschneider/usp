# -*- coding: utf-8 -*-

#jogo_nim.py

#https://www.coursera.org/learn/ciencia-computacao-python-conceitos/programming/yEPxE/programa-completo-jogo-do-nim

def computador_escolhe_jogada(n,m):
	lista = [n - ((2 * m) + 1), m]
    if n > ((2 * m) + 1):
        return min(lista)
    else
    
    


def usuario_escolhe_jogada(n,m):
    jogada = False
    while not jogada:
        z = int(input('Quantas peças você vai tirar? '))
        if z <= n and z <= m:
            jogada = True
            return z


def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    
    if n % (m + 1) == 0:
        print('Você começa')
        usuario_escolhe_jogada(n,m)
        
    else:
        print('Computador começa!')
        computador_escolhe_jogada(n,m)

    

print('Bem-vindo ao jogo do NIM! Escolha:\n','1 - para jogar uma partida isolada\n','2 - para jogar um campeonato')

opcao = False

while not opcao:
    x = int(input('Número da escolha: '))
    if x > 0 and x <= 2:
        opcao = True

if x == 2:
    x = 3
    print('Voce escolheu um campeonato!')
else:
    print('Voce escolheu uma partida isolada!')

rodada = 1 
while rodada <= x:
    print('\n**** Rodada',rodada,'****')
    rodada = rodada + 1
    
    partida()