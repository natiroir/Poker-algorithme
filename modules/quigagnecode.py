import random as rd
from collections import Counter
from collections import defaultdict

def hauteur(liste):
    q=0
    for i in liste:
        if i[0] >= q:
            q = i[0]
    return q

def couleur(liste1):
    liste = [t[1] for t in liste1]
    valeur_avec_au_moins_5_occurrences = ([valeur for valeur, count in Counter(liste).items() if count >= 5])
    if valeur_avec_au_moins_5_occurrences == []:
        return (0,0)
    else:
        valeur_avec_au_moins_5_occurrences = valeur_avec_au_moins_5_occurrences[0]
        k=0
        for i in liste1:
            if i[1] == valeur_avec_au_moins_5_occurrences:
                if i[0]>=k:
                    k = i[0]
        return (valeur_avec_au_moins_5_occurrences,k)

def trouver_suite_de_5_valeurs(liste):
    liste = [t[0] for t in liste]
    for i in range(len(liste) - 4):
        if liste[i:i+5] == [liste[i] - j for j in range(5)]:
            return liste[i]
    return 0

def quinteflush(liste):
    color = couleur(liste)
    color = color[0]
    suite = trouver_suite_de_5_valeurs(liste)
    colorlist = []
    if suite != 0 and color != 0:
        for k in liste:
            if k[1] == color:
                colorlist.append(k[0])
        if len(colorlist) >= 5:
            for i in range(len(colorlist) - 4):
                if colorlist[i:i+5] == [colorlist[i] - j for j in range(5)]:
                    return (suite,color)
    return 0

def pairebrelancarre(liste):
    occurrences = defaultdict(int)
    
    for element in liste:
        premier_element = element[0]
        occurrences[premier_element] += 1

    paires = []
    brelans = []
    carres = 0

    for valeur, count in occurrences.items():
        if count == 2:
            paires.append(valeur)
        elif count == 3:
            brelans.append(valeur)
        elif count == 4:
            carres = valeur

    if paires == []:
        paires = 0
    elif len(paires) == 1:
        paires = paires[0]
    elif len(paires)==3:
        paires = sorted(paires,reverse=True)
        paires.pop(2)
    
    if brelans == []:
        brelans = 0
    elif len(brelans) == 1:
        brelans = brelans[0]
    elif len(brelans) == 2:
        brelans = sorted(brelans,reverse=True)

    return paires, brelans, carres


def quigagne(carteplateau, cartejoueur):
    mainsjoueurs = []
    mains = []
    for i in range(len(cartejoueur)):
        mains=[]
        for k in carteplateau:
            mains.append(k)
        mains.append(cartejoueur[i][0])
        mains.append(cartejoueur[i][1])
        mains = sorted(mains, key=lambda x: x[0], reverse=True)
        mainsjoueurs.append(mains)
    

    mainsgagnantes = []
    for l in mainsjoueurs:
        brelan = pairebrelancarre(l)[1]
        paire = pairebrelancarre(l)[0]
        fullhouse = 0
        if brelan != 0 and paire != 0:
            if isinstance(paire, list):
                fullhouse = (brelan,max(paire))
            else:
                fullhouse = (brelan,paire)
        elif isinstance(brelan, list):
            fullhouse = (max(brelan),min(brelan))
        mainsgagnantes.append((hauteur(l),paire,brelan,trouver_suite_de_5_valeurs(l),couleur(l),fullhouse,pairebrelancarre(l)[2],quinteflush(l)))
    
    hauteurv = []
    pairev = []
    brelanv = []
    suitev = []
    couleurv = []
    fullhousev = []
    carrev = []
    quinteflushv = []
    doublepairev = []
    for i in mainsgagnantes:
        hauteurv.append(i[0])
        if isinstance(i[1], list):
            doublepairev.append(i[1])
            pairev.append(0)
        else:
            pairev.append(i[1])
            doublepairev.append(0)
        brelanv.append(i[2])
        suitev.append(i[3])
        couleurv.append(i[4])
        fullhousev.append(i[5])
        carrev.append(i[6])
        quinteflushv.append(i[7])

    gagnant = []
    if quinteflushv.count(0) != len(quinteflushv):
        for i in range(len(quinteflushv)):
            if quinteflushv[i]!= 0:
                if gagnant != []:
                    if gagnant[0][2][0] < quinteflushv[i][0]:
                        gagnant = [(9, i, quinteflushv[i])]
                    elif gagnant[0][2][0] == quinteflushv[i][0]:
                        gagnant.append((9, i, quinteflushv[i]))
                else:
                    gagnant.append((9, i, quinteflushv[i]))

        return  gagnant
    
    if carrev.count(0) != len(carrev):
        for i in range(len(carrev)):
            if carrev[i]!= 0:
                if gagnant != []:
                    if gagnant[0][2] < carrev[i]:
                        gagnant = [(8, i, carrev[i])]
                    elif gagnant[0][2] == carrev[i]:
                        gagnant.append((8, i, carrev[i]))
                else:
                    gagnant.append((8, i, carrev[i]))

        return  gagnant
    
    if fullhousev.count(0) != len(fullhousev):
        for i in range(len(fullhousev)):
            if fullhousev[i]!= 0:
                if gagnant != []:
                    if gagnant[0][2][0] < fullhousev[i][0]:
                        gagnant = [(7, i, fullhousev[i])]
                    elif gagnant[0][2][0] == fullhousev[i][0]:
                        if gagnant[0][2][1] == fullhousev[i][1]:
                            gagnant.append((7, i, fullhousev[i]))
                        elif gagnant[0][2][1] < fullhousev[i][1]:
                            gagnant = [(7, i, fullhousev[i])]
                else:
                    gagnant.append((7, i, fullhousev[i]))

        return  gagnant

    if couleurv.count((0,0)) != len(couleurv):
        for i in range(len(couleurv)):
            if couleurv[i]!= (0,0):
                if gagnant != []:
                    if gagnant[0][2][1] < couleurv[i][1]:
                        gagnant = [(6, i, couleurv[i])]
                    elif gagnant[0][2][1] == couleurv[i][1]:
                        gagnant.append((6, i, couleurv[i]))
                else:
                    gagnant.append((6, i, couleurv[i]))

        return  gagnant
    
    if suitev.count(0) != len(suitev):
        for i in range(len(suitev)):
            if suitev[i]!= 0:
                if gagnant != []:
                    if gagnant[0][2] < suitev[i]:
                        gagnant = [(5, i, suitev[i])]
                    elif gagnant[0][2] == suitev[i]:
                        gagnant.append((5, i, suitev[i]))
                else:
                    gagnant.append((5, i, suitev[i]))

        return  gagnant
    
    if brelanv.count(0) != len(brelanv):
        for i in range(len(brelanv)):
            if brelanv[i]!= 0:
                if gagnant != []:
                    if gagnant[0][2] < brelanv[i]:
                        gagnant = [(4, i, brelanv[i])]
                    elif gagnant[0][2] == brelanv[i]:
                        if mainsgagnantes[gagnant[0][1]][0] < mainsgagnantes[i][0]:
                            gagnant = [(4, i, brelanv[i])]
                        elif mainsgagnantes[gagnant[0][1]][0] == mainsgagnantes[i][0]:
                            gagnant.append((4, i, brelanv[i]))
                else:
                    gagnant.append((4, i, brelanv[i]))
        return  gagnant
    
    if doublepairev.count(0) != len(doublepairev):
        for i in range(len(doublepairev)):
            if doublepairev[i]!= 0:
                if gagnant != []:
                    if gagnant[0][2][0] < doublepairev[i][0]:
                        gagnant = [(3, i, doublepairev[i])]
                    elif gagnant[0][2][0] == doublepairev[i][0]:
                        if gagnant[0][2][1] == doublepairev[i][1]:
                            if mainsgagnantes[gagnant[0][1]][0] < mainsgagnantes[i][0]:
                                gagnant = [(3, i, doublepairev[i])]
                            elif mainsgagnantes[gagnant[0][1]][0] == mainsgagnantes[i][0]:
                                gagnant.append((3, i, doublepairev[i]))
                        elif gagnant[0][2][1] < doublepairev[i][1]:
                            gagnant = [(3, i, doublepairev[i])]
                else:
                    gagnant.append((3, i, doublepairev[i]))
        return  gagnant

    if pairev.count(0) != len(pairev):
        for i in range(len(pairev)):
            if pairev[i]!= 0:
                if gagnant != []:
                    if gagnant[0][2] < pairev[i]:
                        gagnant = [(2, i, pairev[i])]
                    elif gagnant[0][2] == pairev[i]:
                        if mainsgagnantes[gagnant[0][1]][0] < mainsgagnantes[i][0]:
                            gagnant = [(2, i, pairev[i])]
                        elif mainsgagnantes[gagnant[0][1]][0] == mainsgagnantes[i][0]:
                            gagnant.append((2, i, pairev[i]))
                else:
                    gagnant.append((2, i, pairev[i]))
        return  gagnant
    
    if hauteurv.count(0) != len(hauteurv):
        for i in range(len(pairev)):
            if hauteurv[i]!= 0:
                if gagnant != []:
                    if gagnant[0][2] < hauteurv[i]:
                        gagnant = [(1, i, hauteurv[i])]
                    elif gagnant[0][2] == hauteurv[i]:
                        gagnant.append((1, i, hauteurv[i]))
                else:
                    gagnant.append((1, i, hauteurv[i]))
        return  gagnant

    return "probleme"

def classement_des_mains(quijoue,carteplateau,cartejoueurrestant1):
    value_2 = []
    pos = [i for i in range(len(quijoue)) if quijoue[i] == 1]
    while cartejoueurrestant1 != []:
        value = []
        quigagnev = quigagne(carteplateau,cartejoueurrestant1)
        joueurgagnantL = []
        for j in range(len(quigagnev)):
            (combinaison, joueurgagnant, detail) = quigagnev[j]
            joueurgagnantL.append(joueurgagnant)
            value.append((combinaison,pos[joueurgagnant],detail))
        p=0
        for m in joueurgagnantL:
            cartejoueurrestant1.pop(m-p)
            pos.pop(m-p)
            p +=1
        value_2.append(value)
    return value_2



def quigagne1(main1,main2): #Finir de patch le flush
    listemain1ordrep = []
    listemain2ordrep = []
    listemain1ordrec = [] #Coeur = 1, carreau = 2, pique = 3, trefle = 4
    listemain2ordrec = []
    for z in main1:
        listemain1ordrep.append(z[0])
        listemain1ordrec.append(z[1])
    for z in main2:
        listemain2ordrep.append(z[0])
        listemain2ordrec.append(z[1])

    listemain1ordrep.sort() 
    listemain2ordrep.sort()
    listemain1ordrep.reverse()
    listemain2ordrep.reverse()
    listemain1ordrec.sort()
    listemain2ordrec.sort()

    main1straight = [0,0]
    main2straight = [0,0]
    main1four = [0,0]
    main2four = [0,0]
    main1full = 0
    main2full = 0
    main1flush = 0
    main2flush = 0
    main1three = [0,0]
    main2three = [0,0]
    main1twopair = 0
    main2twopair = 0
    main1pair = [0,0]
    main2pair = [0,0]

    hauteurmain1four = -1
    hauteurmain2four = -1
    

    for n in range(4):
        if listemain1ordrep[n] == listemain1ordrep[n+1] == listemain1ordrep[n+2] == listemain1ordrep[n+3]:
            main1four = [1,listemain1ordrep[n]]
        if listemain2ordrep[n] == listemain2ordrep[n+1] == listemain2ordrep[n+2] == listemain2ordrep[n+3]:
            main2four = [1,listemain2ordrep[n]]
    
    if main1four[0] == 1:
        if main2four[0] == 1:
            if main1four[1] > main2four[1]:
                return 1
            elif main1four[1] < main2four[1]:
                return 0
            else:
                if listemain1ordrep[0] > listemain2ordrep[0]:
                    return 1
                elif listemain1ordrep[0] < listemain2ordrep[0]:
                    return 0
                return 0.5
        return 1
    elif main2four[0] == 1:
        return 0

    for  n in range(5):
        if listemain1ordrep[n] == listemain1ordrep[n+1] == listemain1ordrep[n+2]:
            main1three = [1, listemain1ordrep[n]]
        if listemain2ordrep[n] == listemain2ordrep[n+1] == listemain2ordrep[n+2]:
            main2three = [1, listemain2ordrep[n]]
    
    for n in range(6):
        if listemain1ordrep[n] == listemain1ordrep[n+1]:
            if main1pair[0] == 1:
                if main1twopair == 1:
                    if main1three[1] == listemain1ordrep[n]:
                        main1full = 1
                main1twopair = 1
            if main1pair[1] <= listemain1ordrep[n]:
                main1pair = [1,listemain1ordrep[n]]
        if listemain2ordrep[n] == listemain2ordrep[n+1]:
            if main2pair[0] == 1:
                if main2twopair == 1:
                    if main2three[1] == listemain2ordrep[n]:
                        main2full = 1
                main2twopair = 1
            if main2pair[1] <= listemain2ordrep[n]:
                main2pair = [1,listemain2ordrep[n]]
    
    if main1full == 1:
        if main2full == 1:
            if main1three[1] > main2three[1]:
                return 1
            elif main1three[1] < main2three[1]:
                return 0
            else:
                return 0.5
        return 1
    elif main2full == 1:

        return 0
        
    

    for n in range(3):
        if listemain1ordrep[0+n] == listemain1ordrep[1+n]+1 == listemain1ordrep[2+n]+2 == listemain1ordrep[3+n]+3 == listemain1ordrep[4+n]+4:
            main1straight = [1,listemain1ordrep[n]]
        if listemain2ordrep[0+n] == listemain2ordrep[1+n]+1 == listemain2ordrep[2+n]+2 == listemain2ordrep[3+n]+3 == listemain2ordrep[4+n]+4:
            main2straight = [1,listemain2ordrep[n]]
        if listemain1ordrec[n] == listemain1ordrec[n+1] == listemain1ordrec[n+2] == listemain1ordrec[n+3] == listemain1ordrec[n+4]:
            main1flush = 1
        if listemain2ordrec[n] == listemain2ordrec[n+1] == listemain2ordrec[n+2] == listemain2ordrec[n+3] == listemain2ordrec[n+4]:
            main2flush = 1
    
    
    if main1flush == 1:
        if main2flush == 1:
            if listemain1ordrep[0] > listemain2ordrep[0]:
                return 1
            elif listemain1ordrep[0] < listemain2ordrep[0]:
                return 0
            else:
                return 0.5
        return 1
    elif main2flush == 1:
        return 0

    if main1straight[0] == 1 :
        if main2straight[0] == 1:
            if main1straight[1] > main2straight[1]:
                return 1
            elif main1straight[1] < main2straight[1]:
                return 0
            else:
                return 0.5
        return 1 

        
    elif main2straight[0] == 1:
        return 0

    if main1three[0] == 1:
        if main2three[0] == 1:
            if main1three[1] > main2three[1]:
                return 1
            elif main1three[1] < main2three[1]:
                return 0
            else:
                if listemain1ordrep[0] > listemain2ordrep[0]:
                    return 1
                elif listemain1ordrep[0] < listemain2ordrep[0]:
                    return 0
                else:
                    return 0.5
        else :
            return 1
    elif main2three[0] == 1:
        return 0
    
    if main1twopair == 1:
        if main2twopair == 1:
            if main1pair[1] > main2pair[1]:
                return 1
            elif main1pair[1] < main2pair[1]:
                return 0
            else:
                return 0.5
        else:
            return 1
    elif main2twopair == 1:
        return 0
    
    if main1pair[0] == 1:
        if main2pair[0] == 1:
            if main1pair[1] > main2pair[1]:
                return 1
            elif main1pair[1] < main2pair[1]:
                return 0
            else:
                if listemain1ordrep[0] > listemain2ordrep[0]:
                    return 1
                elif listemain1ordrep[0] < listemain2ordrep[0]:
                    return 0
                else:
                    return 0.5
        else:
            return 1
    elif main2pair[0] == 1:
        return 0
    if listemain1ordrep[0] > listemain2ordrep[0]:
        return 1
    elif listemain1ordrep[0] < listemain2ordrep[0]:
        return 0
    else:
        return 0.5


def probagagneralgo1(carteflop,cartemain,nbjoueur):
    listecarte = [
    (14, "C"), (13, "C"), (12, "C"), (11, "C"), (10, "C"), (9, "C"), (8, "C"), (7, "C"), (6, "C"), (5, "C"), (4, "C"), (3, "C"), (2, "C"),
    (14, "D"), (13, "D"), (12, "D"), (11, "D"), (10, "D"), (9, "D"), (8, "D"), (7, "D"), (6, "D"), (5, "D"), (4, "D"), (3, "D"), (2, "D"),
    (14, "P"), (13, "P"), (12, "P"), (11, "P"), (10, "P"), (9, "P"), (8, "P"), (7, "P"), (6, "P"), (5, "P"), (4, "P"), (3, "P"), (2, "P"),
    (14, "T"), (13, "T"), (12, "T"), (11, "T"), (10, "T"), (9, "T"), (8, "T"), (7, "T"), (6, "T"), (5, "T"), (4, "T"), (3, "T"), (2, "T")
    ]
    for i in carteflop:
        listecarte.remove(i)
    for i in cartemain:
        listecarte.remove(i)
    mainjoueur = carteflop+cartemain
    nombredecartejoueur = 7-len(mainjoueur)
    nombredecarteadv = 7-len(carteflop)
    nombredevictoire = 0
    for i in range(10000):
        victoirejouere = []
        joueurmainactuelle = mainjoueur + rd.sample(listecarte,nombredecartejoueur)
        for z in range(nbjoueur):
            victoirejouere.append(quigagne1(joueurmainactuelle, carteflop + rd.sample(listecarte,nombredecarteadv)))
            if victoirejouere[z] == 0:
                break
        if min(victoirejouere) == 1:
            nombredevictoire += 1
        if min(victoirejouere) == 0.5:
            nombredevictoire += 0.5
    return nombredevictoire/10000
