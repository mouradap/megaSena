import pandas as pd
from random import randint
import numpy as np
import sys

megaSena = pd.read_html('d_megasc.htm')
megaSena = megaSena[0]

first = []
second = []
third = []
fourth = []
fifth = []
sixth = []

for i in megaSena['Concurso']:
    first.append(megaSena['1ª Dezena'][i])
    second.append(megaSena['2ª Dezena'][i])
    third.append(megaSena['3ª Dezena'][i])
    fourth.append(megaSena['4ª Dezena'][i])
    fifth.append(megaSena['5ª Dezena'][i])
    sixth.append(megaSena['6ª Dezena'][i])


def getRepeats(lista):
    lista = np.array(lista)
    unique, counts = np.unique(lista, return_counts=True)
    repeats = dict(zip(unique, counts))
    return repeats

d1 = getRepeats(first)
d2 = getRepeats(second)
d3 = getRepeats(third)
d4 = getRepeats(fourth)
d5 = getRepeats(fifth)
d6 = getRepeats(sixth)

def getCutoff(dictionary):
    cutoff = []
    repeats = []
    for key in dictionary:
        repeats.append(dictionary[key])
        
    cutOff = np.percentile(repeats, 70)
    
    for key in dictionary:
        if dictionary[key] >= cutOff:
            cutoff.append(key)
    return cutoff

def drawJogo(n_de_jogos):
    jogos = []
    for i in range(n_de_jogos):
        jogo = []
        
        randomPick = randint(1,len(getCutoff(d1))) - 1
        n1 = getCutoff(d1)[randomPick]
        
        jogo.append(n1)
        
        randomPick = randint(1,len(getCutoff(d2))) - 1
        n2 = getCutoff(d2)[randomPick]
        
        if n2 in jogo:
            randomPick = randint(1,len(getCutoff(d2))) - 1
            n2 = getCutoff(d2)[randomPick]
            jogo.append(n2)
        else:
            jogo.append(n2)
        
        randomPick = randint(1,len(getCutoff(d3))) - 1
        n3 = getCutoff(d3)[randomPick]
        
        if n3 in jogo:
            randomPick = randint(1,len(getCutoff(d3))) - 1
            n3 = getCutoff(d3)[randomPick]
            jogo.append(n3)
        else:
            jogo.append(n3)
        
        randomPick = randint(1,len(getCutoff(d4))) - 1
        n4 = getCutoff(d4)[randomPick]
        
        if n4 in jogo:
            randomPick = randint(1,len(getCutoff(d4))) - 1
            n4 = getCutoff(d4)[randomPick]
            jogo.append(n4)
        else:
            jogo.append(n4)
        
        randomPick = randint(1,len(getCutoff(d5))) - 1
        n5 = getCutoff(d5)[randomPick]
        
        if n5 in jogo:
            randomPick = randint(1,len(getCutoff(d5))) - 1
            n5 = getCutoff(d5)[randomPick]
            jogo.append(n5)
        else:
            jogo.append(n5)
        
        randomPick = randint(1,len(getCutoff(d6))) - 1
        n6 = getCutoff(d6)[randomPick]
        
        if n6 in jogo:
            randomPick = randint(1,len(getCutoff(d6))) - 1
            n6 = getCutoff(d6)[randomPick]
            jogo.append(n6)
        else:
            jogo.append(n6)
                
        jogos.append(jogo)
        
    print(jogos)


if __name__ == '__main__':
	n_de_jogos = int(sys.argv[1])
	drawJogo(n_de_jogos)