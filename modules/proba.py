import time
from itertools import combinations
from modules.quigagnecode import *
import random as rd
import pandas as pd

def mainspotadv(board,cartemain):
    listecarte = [
    (14, "C"), (13, "C"), (12, "C"), (11, "C"), (10, "C"), (9, "C"), (8, "C"), (7, "C"), (6, "C"), (5, "C"), (4, "C"), (3, "C"), (2, "C"),
    (14, "D"), (13, "D"), (12, "D"), (11, "D"), (10, "D"), (9, "D"), (8, "D"), (7, "D"), (6, "D"), (5, "D"), (4, "D"), (3, "D"), (2, "D"),
    (14, "P"), (13, "P"), (12, "P"), (11, "P"), (10, "P"), (9, "P"), (8, "P"), (7, "P"), (6, "P"), (5, "P"), (4, "P"), (3, "P"), (2, "P"),
    (14, "T"), (13, "T"), (12, "T"), (11, "T"), (10, "T"), (9, "T"), (8, "T"), (7, "T"), (6, "T"), (5, "T"), (4, "T"), (3, "T"), (2, "T")
    ]
    for i in board:
        listecarte.remove(i)
    for i in cartemain:
        listecarte.remove(i)
    
    L = list(combinations(listecarte,7-len(board)))
    R = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for x in L:
        k = board.copy()
        for i in range(5-len(board)):
            k.append(x[i+2])
        k1 = [[x[0],x[1]]]
        q = quigagne(k,k1)
        if q[0][0] == 7 or q[0][0] == 3 or q[0][0] == 9:
            h = int(q[0][2][0])
        elif q[0][0] == 6:
            h = int(q[0][2][1])
        else:
            h = int(q[0][2])
        R[(q[0][0]-1)*13+(h-2)] += 1
    return R

def mainspot(board,cartemain):
    listecarte = [
    (14, "C"), (13, "C"), (12, "C"), (11, "C"), (10, "C"), (9, "C"), (8, "C"), (7, "C"), (6, "C"), (5, "C"), (4, "C"), (3, "C"), (2, "C"),
    (14, "D"), (13, "D"), (12, "D"), (11, "D"), (10, "D"), (9, "D"), (8, "D"), (7, "D"), (6, "D"), (5, "D"), (4, "D"), (3, "D"), (2, "D"),
    (14, "P"), (13, "P"), (12, "P"), (11, "P"), (10, "P"), (9, "P"), (8, "P"), (7, "P"), (6, "P"), (5, "P"), (4, "P"), (3, "P"), (2, "P"),
    (14, "T"), (13, "T"), (12, "T"), (11, "T"), (10, "T"), (9, "T"), (8, "T"), (7, "T"), (6, "T"), (5, "T"), (4, "T"), (3, "T"), (2, "T")
    ]
    for i in board:
        listecarte.remove(i)
    for i in cartemain:
        listecarte.remove(i)
    
    L = list(combinations(listecarte,5-len(board)))
    R = [ 0 for i in range(117) ] 
    for x in L:
        k = board.copy()
        for i in range(5-len(board)):
            k.append(x[i])
        k1 = [[cartemain[0],cartemain[1]]]
        q = quigagne(k,k1)
        if q[0][0] == 7 or q[0][0] == 3 or q[0][0] == 9:
            h = int(q[0][2][0])
        elif q[0][0] == 6:
            h = int(q[0][2][1])
        else:
            h = int(q[0][2])
        R[(q[0][0]-1)*13+(h-2)] += 1
    return R

def note(R):
    notesum = 0
    for i in range(len(R)):
        notesum += (i+1)*(R[i])
    return notesum/sum(R)

def notemedian(R):
    n=0
    for i in range(int(sum(R)/2)):
        if R[n] == 0:
            n+=1
        else:
            R[n] -=1
    return n+1

def comparaisonliste(list1, list2):
    x = 0 #Nombre de cas gagnant
    y = 0 #Nombre de cas gagnant a instant t 
    for n in range(len(list1)):
        for z in range(n+1):
            if n == z :
                y += list2[z]/2
            else :
                y += list2[z]
        x += list1[n]*y
        y = 0
    return round(x / (sum(list2)*sum(list1)),2)


def comparaisonlistenjoueur(list1,list2,nombredejoueur):
    nombre_de_manche_gagnante = 0
    sommelist1 = sum(list1)
    sommelist2 = sum(list2)
    for z in range(100000):
        pointx = 0
        pointy = 0
        resultatx = 0
        resultaty = 0 
        x = rd.randint(0,sommelist1)
        sommelist = []
        for z in range(nombredejoueur-1):
        
            sommelist.append(rd.randint(0,sommelist2))
        y = max(sommelist)
        while pointx < x:
            pointx += list1[resultatx]
            resultatx += 1
        while pointy < y:
            pointy += list2[resultaty]
            resultaty += 1
        if resultatx > resultaty:
            nombre_de_manche_gagnante += 1
        elif resultatx == resultaty:
            nombre_de_manche_gagnante += 0.5
    return nombre_de_manche_gagnante/100000

def probapreflop(main,nbj):
    if main[0][0] < main[1][0]:
        main = (main[1],main[0])
    mainL = [list(t) for t in main]

    dictAKQJ = {14 : 'A',13 : 'K',12 : 'Q',11 : 'J'}
    for i in range(len(mainL)):
        if mainL[i][0] > 10:
            mainL[i][0] = dictAKQJ[mainL[i][0]]

    if mainL[0][1] == mainL[1][1]:
        formatdict = '{}-{}s'.format(str(mainL[0][0]),str(mainL[1][0]))
    else:
        formatdict = '{}-{}'.format(str(mainL[0][0]),str(mainL[1][0]))
    
    df = pd.read_excel('data/probapreflop.xlsx', header=None)
    # Définir les colonnes à regrouper
    columns_to_group = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Regrouper et agréger en listes, puis accéder à la première valeur de la liste résultante
    res_list = [value[0] for value in df.groupby(0)[columns_to_group].agg(lambda x: x.tolist()).loc[formatdict].values]
    return res_list[nbj-2]

def algoproba1(nbj,jetons,miseasuivre,main,board,bluff,variablebluff,variablesurete,joueur):
    print(bluff)
    joueur += 1

    if len(board) < 3:
        proba = probapreflop(main,nbj)
    else:
        proba = probagagneralgo1(board,list(main),nbj)
    proba = proba**(1/variablesurete)
    if bluff < variablebluff and len(board) >= 3:
        print('Bluff')
        return [2,int(jetons*proba)]
    
    if miseasuivre/jetons < 0.03 and proba*nbj <1:
        return [1]
    if miseasuivre > 0 and proba*nbj <1:
        return [0]
    if proba*nbj <1:
        return [1]
    if proba*nbj>2:
        return [2,int(jetons)]
    if proba*nbj>1.5:
        return [2,int(proba*jetons)]
    if proba*nbj>1.2:
        return [2,int(proba*jetons*0.3)]
    return [1]