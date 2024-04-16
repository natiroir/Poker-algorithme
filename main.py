from random import *
from collections import defaultdict
from collections import Counter
import tkinter as tk
from modules.proba import *
import time
import threading
import sys


carte = [
    (14, "C"), (13, "C"), (12, "C"), (11, "C"), (10, "C"), (9, "C"), (8, "C"), (7, "C"), (6, "C"), (5, "C"), (4, "C"), (3, "C"), (2, "C"),
    (14, "D"), (13, "D"), (12, "D"), (11, "D"), (10, "D"), (9, "D"), (8, "D"), (7, "D"), (6, "D"), (5, "D"), (4, "D"), (3, "D"), (2, "D"),
    (14, "P"), (13, "P"), (12, "P"), (11, "P"), (10, "P"), (9, "P"), (8, "P"), (7, "P"), (6, "P"), (5, "P"), (4, "P"), (3, "P"), (2, "P"),
    (14, "T"), (13, "T"), (12, "T"), (11, "T"), (10, "T"), (9, "T"), (8, "T"), (7, "T"), (6, "T"), (5, "T"), (4, "T"), (3, "T"), (2, "T")
]

# C = Coeur, D = Diamonds (carreaux), P = Pique, T = Trêfle et carte De 2 à 10   11 = Valet   12 = Dame   13 = Roi    14 = As

imgcarte = {
    (14, "C"): "assets/cartes\\01-coeur.png", (13, "C"): "assets/cartes\\R-coeur.png", (12, "C"): "assets/cartes\\D-coeur.png", (11, "C"): "assets/cartes\\V-coeur.png", (10, "C"): "assets/cartes\\10-coeur.png",
    (9, "C"): "assets/cartes\\09-coeur.png", (8, "C"): "assets/cartes\\08-coeur.png", (7, "C"): "assets/cartes\\07-coeur.png", (6, "C"): "assets/cartes\\06-coeur.png", (5, "C"): "assets/cartes\\05-coeur.png",
    (4, "C"): "assets/cartes\\04-coeur.png", (3, "C"): "assets/cartes\\03-coeur.png", (2, "C"): "assets/cartes\\02-coeur.png",
    (14, "D"): "assets/cartes\\01-carreau.png", (13, "D"): "assets/cartes\\R-carreau.png", (12, "D"): "assets/cartes\\D-carreau.png", (11, "D"): "assets/cartes\\V-carreau.png", (10, "D"): "assets/cartes\\10-carreau.png",
    (9, "D"): "assets/cartes\\09-carreau.png", (8, "D"): "assets/cartes\\08-carreau.png", (7, "D"): "assets/cartes\\07-carreau.png", (6, "D"): "assets/cartes\\06-carreau.png", (5, "D"): "assets/cartes\\05-carreau.png",
    (4, "D"): "assets/cartes\\04-carreau.png", (3, "D"): "assets/cartes\\03-carreau.png", (2, "D"): "assets/cartes\\02-carreau.png",
    (14, "P"): "assets/cartes\\01-pique.png", (13, "P"): "assets/cartes\\R-pique.png", (12, "P"): "assets/cartes\\D-pique.png", (11, "P"): "assets/cartes\\V-pique.png", (10, "P"): "assets/cartes\\10-pique.png",
    (9, "P"): "assets/cartes\\09-pique.png", (8, "P"): "assets/cartes\\08-pique.png", (7, "P"): "assets/cartes\\07-pique.png", (6, "P"): "assets/cartes\\06-pique.png", (5, "P"): "assets/cartes\\05-pique.png",
    (4, "P"): "assets/cartes\\04-pique.png", (3, "P"): "assets/cartes\\03-pique.png", (2, "P"): "assets/cartes\\02-pique.png",
    (14, "T"): "assets/cartes\\01-trefle.png", (13, "T"): "assets/cartes\\R-trefle.png", (12, "T"): "assets/cartes\\D-trefle.png", (11, "T"): "assets/cartes\\V-trefle.png", (10, "T"): "assets/cartes\\10-trefle.png",
    (9, "T"): "assets/cartes\\09-trefle.png", (8, "T"): "assets/cartes\\08-trefle.png", (7, "T"): "assets/cartes\\07-trefle.png", (6, "T"): "assets/cartes\\06-trefle.png", (5, "T"): "assets/cartes\\05-trefle.png",
    (4, "T"): "assets/cartes\\04-trefle.png", (3, "T"): "assets/cartes\\03-trefle.png", (2, "T"): "assets/cartes\\02-trefle.png"
}

#Affichage

def affichageinterface():
    global window
    # Crée une fenêtre tkinter

    def carteboard():
        img_path = "assets/cartes\\dos-bleu.png"
        listX = [549, 640, 735, 824, 914]
        for i in range(5):
            img = tk.PhotoImage(file=img_path)
            # Redimensionne l'image en réduisant le facteur de sous-échantillonnage
            img = img.subsample(2, 2)
            label = tk.Label(window, image=img)
            label.image = img
            label.place(x=listX[i], y=383)
        
    def cartedos(j,couleur):

        listCord = {
            2: [(422,644),(512,644)],
            3: [(72,385),(165,385)],
            4: [(422,126),(510,126)],
            5: [(954,125),(1047,125)],
            6: [(1303,385),(1393,385)]
        }

        if couleur == 0:
            img_path = "assets/cartes\\dos-gris.png"
        else:
            img_path = "assets/cartes\\dos-bleu.png"

        if j>=2 and j<=6:
            for i in range(2):
                img = tk.PhotoImage(file=img_path)
                # Redimensionne l'image en réduisant le facteur de sous-échantillonnage
                img = img.subsample(2, 2)
                label = tk.Label(window, image=img)
                label.image = img
                label.place(x=listCord[j][i][0], y=listCord[j][i][1])

    def update_interface():
        for widget in window.winfo_children():
            if not isinstance(widget, (tk.Button,tk.Entry)):
                widget.destroy()

        img = tk.PhotoImage(file="assets/bg.png")
        label = tk.Label(window, image=img)
        label.image = img
        label.place(x=0, y=0)
        bouttonfold.lift()
        bouttoncall.lift()
        bouttonbet.lift()
        entreebet.lift()

        if quijouepartie[0] == 0:
            texte = "Vous avez perdu !"
            label = tk.Label(window, text=texte, font=("Arial", 23),fg="#a80602",bg="white")
            label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        elif vinterfaffichage[0] != 0:

            carteboard()

            s = -1
            for i in range(len(vinterfaffichage[9])):
                if vinterfaffichage[9][i]==1:
                    cartedos(i+1,1)
                    s+=1
                if vinterfaffichage[9][i]==0:
                    cartedos(i+1,0)
                if vinterfaffichage[3][s]==0:
                    cartedos(i+1,0)

            texts = [["J1 : Patrick Bruel", "15", (952, 748)], ["J2 : Betrand Grospellier", "19", (393, 748)], ["J3 : Johan Guilbert", "15", (68, 490)], ["J4 : Benjamin Pollak", "16", (410, 96)], ["J5 : Antoine Saout", "16", (946, 96)], ["J6 : Sylvain Loosli", "15", (1298, 490)]]

            if len(quijouepartie)>=2:
                for i in range(len(quijouepartie)):
                    pseudoj = tk.Label(window, text=texts[i][0], fg="#340c02",bg="#c6a355" ,width= texts[i][1],borderwidth=2, font=("bold Arial", 14))
                    pseudoj.place(x=texts[i][2][0], y=texts[i][2][1])

            # Affiche les cartes des joueurs
            img_path = imgcarte[vinterfaffichage[1][0][0]]
            img = tk.PhotoImage(file=img_path)
            # Redimensionne l'image en réduisant le facteur de sous-échantillonnage
            img = img.subsample(2, 2)  # Par exemple, réduit l'image de moitié en largeur et en hauteur
            label = tk.Label(window, image=img)
            label.image = img
            label.place(x=954, y=644)  # Exemple de coordonnées, ajustez selon vos besoins

            img_path = imgcarte[vinterfaffichage[1][0][1]]
            img = tk.PhotoImage(file=img_path)
            # Redimensionne l'image en réduisant le facteur de sous-échantillonnage
            img = img.subsample(2, 2)  # Par exemple, réduit l'image de moitié en largeur et en hauteur
            label = tk.Label(window, image=img)
            label.image = img
            label.place(x=1047, y=644)

            textepot = tk.Label(window, text=vinterfaffichage[4], bg="#afdab1",fg="#080b0a",width= "7",font="Helvetica 20 bold")
            textepot.place(x=707, y=237)
            w =  1

            textejetonsj1 = tk.Label(window, text=vinterfaffichage[6][0], bg="#a80602",fg="white" , width= "5" ,borderwidth=2,font=("Arial", 15))
            textejetonsj1.place(x=959, y=600)
            textemisej1 = tk.Label(window, text=vinterfaffichage[5][0], fg="#a80602",bg="white" , width= "5",borderwidth=2, font=("Arial", 15))
            textemisej1.place(x=1053, y=600)

            if len(vinterfaffichage[9]) >= 2 and vinterfaffichage[9][1] == 1:
                textejetonsj2 = tk.Label(window, text=vinterfaffichage[6][w], bg="#a80602",fg="white" ,width= "5",borderwidth=2, font=("Arial", 15)) 
                textejetonsj2.place(x=427, y=600)
                textemisej2 = tk.Label(window, text=vinterfaffichage[5][w], fg="#a80602",bg="white" ,width= "5",borderwidth=2, font=("Arial", 15))
                textemisej2.place(x=515, y=600)
                w += 1
            if len(vinterfaffichage[9]) >= 3 and vinterfaffichage[9][2] == 1:
                textejetonsj3 = tk.Label(window, text=vinterfaffichage[6][w], bg="#a80602",fg="white" , width= "5" ,borderwidth=2,font=("Arial", 15))
                textejetonsj3.place(x=77, y=340)
                textemisej3 = tk.Label(window, text=vinterfaffichage[5][w], fg="#a80602",bg="white" , width= "5",borderwidth=2, font=("Arial", 15))
                textemisej3.place(x=170, y=340)
                w+=1
            
            if len(vinterfaffichage[9]) >= 4 and vinterfaffichage[9][3] == 1:
                textejetonsj3 = tk.Label(window, text=vinterfaffichage[6][w], bg="#a80602",fg="white" , width= "5" ,borderwidth=2,font=("Arial", 15))
                textejetonsj3.place(x=427, y=240)
                textemisej3 = tk.Label(window, text=vinterfaffichage[5][w], fg="#a80602",bg="white" , width= "5",borderwidth=2, font=("Arial", 15))
                textemisej3.place(x=515, y=240)
                w+=1

            if len(vinterfaffichage[9]) >= 5 and vinterfaffichage[9][4] == 1:
                textejetonsj3 = tk.Label(window, text=vinterfaffichage[6][w], bg="#a80602",fg="white" , width= "5" ,borderwidth=2,font=("Arial", 15))
                textejetonsj3.place(x=959, y=240)
                textemisej3 = tk.Label(window, text=vinterfaffichage[5][w], fg="#a80602",bg="white" , width= "5",borderwidth=2, font=("Arial", 15))
                textemisej3.place(x=1053, y=240)
                w+=1
            
            if len(vinterfaffichage[9]) >= 6 and vinterfaffichage[9][5] == 1:
                textejetonsj3 = tk.Label(window, text=vinterfaffichage[6][w], bg="#a80602",fg="white" , width= "5" ,borderwidth=2,font=("Arial", 15))#x=1310, y=340 x=1400, y=340 / x=959, y=240 x=1053, y=240 / x=427, y=240 x=515, y=240 / x=77, y=340 x=170, y=340 / x=427, y=600 x=515, y=600
                textejetonsj3.place(x=1310, y=340)
                textemisej3 = tk.Label(window, text=vinterfaffichage[5][w], fg="#a80602",bg="white" , width= "5",borderwidth=2, font=("Arial", 15))
                textemisej3.place(x=1400, y=340)

            if vinterfaffichage[0] >= 2:

                img_path = imgcarte[vinterfaffichage[2][0]]
                img = tk.PhotoImage(file=img_path)
                # Redimensionne l'image en réduisant le facteur de sous-échantillonnage
                img = img.subsample(2, 2)  # Par exemple, réduit l'image de moitié en largeur et en hauteur
                label = tk.Label(window, image=img)
                label.image = img
                label.place(x=549, y=383)

                img_path = imgcarte[vinterfaffichage[2][1]]
                img = tk.PhotoImage(file=img_path)
                # Redimensionne l'image en réduisant le facteur de sous-échantillonnage
                img = img.subsample(2, 2)  # Par exemple, réduit l'image de moitié en largeur et en hauteur
                label = tk.Label(window, image=img)
                label.image = img
                label.place(x=640, y=383)

                img_path = imgcarte[vinterfaffichage[2][2]]
                img = tk.PhotoImage(file=img_path)
                # Redimensionne l'image en réduisant le facteur de sous-échantillonnage
                img = img.subsample(2, 2)  # Par exemple, réduit l'image de moitié en largeur et en hauteur
                label = tk.Label(window, image=img)
                label.image = img
                label.place(x=735, y=383)
            
            if vinterfaffichage[0] >= 3:
                img_path = imgcarte[vinterfaffichage[2][3]]
                img = tk.PhotoImage(file=img_path)
                # Redimensionne l'image en réduisant le facteur de sous-échantillonnage
                img = img.subsample(2, 2)  # Par exemple, réduit l'image de moitié en largeur et en hauteur
                label = tk.Label(window, image=img)
                label.image = img
                label.place(x=824, y=383)

            if vinterfaffichage[0] >= 4:
                img_path = imgcarte[vinterfaffichage[2][4]]
                img = tk.PhotoImage(file=img_path)
                # Redimensionne l'image en réduisant le facteur de sous-échantillonnage
                img = img.subsample(2, 2)  # Par exemple, réduit l'image de moitié en largeur et en hauteur
                label = tk.Label(window, image=img)
                label.image = img
                label.place(x=914, y=383)

            if ((vinterfaffichage[8] > 0 or vinterfaffichage[8] == -1 ) and vinterfaffichage[0]==5):

                w = 1
                if len(vinterfaffichage[9]) >= 2 and vinterfaffichage[9][1] == 1 and vinterfaffichage[3][w] == 1:
                    img_path = imgcarte[vinterfaffichage[1][w][0]]
                    img = tk.PhotoImage(file=img_path)
                    # Redimensionne l'image en réduisant le facteur de sous-échantillonnage
                    img = img.subsample(2, 2)  # Par exemple, réduit l'image de moitié en largeur et en hauteur
                    label = tk.Label(window, image=img)
                    label.image = img
                    label.place(x=422, y=644)  # Exemple de coordonnées, ajustez selon vos besoins 

                    img_path = imgcarte[vinterfaffichage[1][w][1]]
                    img = tk.PhotoImage(file=img_path)
                    # Redimensionne l'image en réduisant le facteur de sous-échantillonnage
                    img = img.subsample(2, 2)  # Par exemple, réduit l'image de moitié en largeur et en hauteur 
                    label = tk.Label(window, image=img)
                    label.image = img
                    label.place(x=512, y=644)
                
                try:
                    if len(vinterfaffichage[9]) >= w+1 and vinterfaffichage[9][1] == 1:
                        w+=1
                except:
                    pass

                if len(vinterfaffichage[9]) >= 3 and vinterfaffichage[9][2] == 1 and vinterfaffichage[3][w] == 1:
                    img_path = imgcarte[vinterfaffichage[1][w][0]]
                    img = tk.PhotoImage(file=img_path)
                    # Redimensionne l'image en réduisant le facteur de sous-échantillonnage
                    img = img.subsample(2, 2)  # Par exemple, réduit l'image de moitié en largeur et en hauteur
                    label = tk.Label(window, image=img)
                    label.image = img
                    label.place(x=72, y=385)  # Exemple de coordonnées, ajustez selon vos besoins

                    img_path = imgcarte[vinterfaffichage[1][w][1]]
                    img = tk.PhotoImage(file=img_path)
                    # Redimensionne l'image en réduisant le facteur de sous-échantillonnage
                    img = img.subsample(2, 2)  # Par exemple, réduit l'image de moitié en largeur et en hauteur
                    label = tk.Label(window, image=img)
                    label.image = img
                    label.place(x=165, y=385)
                
                try:
                    if len(vinterfaffichage[9]) >= w+1 and vinterfaffichage[9][2] == 1:
                        w+=1
                except:
                    pass

                if len(vinterfaffichage[9]) >= 4 and vinterfaffichage[9][3] == 1 and vinterfaffichage[3][w] == 1:
                    img_path = imgcarte[vinterfaffichage[1][w][0]]
                    img = tk.PhotoImage(file=img_path)
                    # Redimensionne l'image en réduisant le facteur de sous-échantillonnage
                    img = img.subsample(2, 2)  # Par exemple, réduit l'image de moitié en largeur et en hauteur
                    label = tk.Label(window, image=img)
                    label.image = img
                    label.place(x=422, y=126)  # Exemple de coordonnées, ajustez selon vos besoins
                    img_path = imgcarte[vinterfaffichage[1][w][1]]
                    img = tk.PhotoImage(file=img_path)
                    # Redimensionne l'image en réduisant le facteur de sous-échantillonnage
                    img = img.subsample(2, 2)  # Par exemple, réduit l'image de moitié en largeur et en hauteur
                    label = tk.Label(window, image=img)
                    label.image = img
                    label.place(x=510, y=126)
                
                try :
                    if len(vinterfaffichage[9]) >= w+1 and vinterfaffichage[9][3] == 1:
                        w+=1
                except:
                    pass
                
                if len(vinterfaffichage[9]) >= 5 and vinterfaffichage[9][4] == 1 and vinterfaffichage[3][w] == 1:
                    img_path = imgcarte[vinterfaffichage[1][w][0]]
                    img = tk.PhotoImage(file=img_path)
                    # Redimensionne l'image en réduisant le facteur de sous-échantillonnage
                    img = img.subsample(2, 2)  # Par exemple, réduit l'image de moitié en largeur et en hauteur
                    label = tk.Label(window, image=img)
                    label.image = img
                    label.place(x=954, y=125)  # Exemple de coordonnées, ajustez selon vos besoins

                    img_path = imgcarte[vinterfaffichage[1][w][1]]
                    img = tk.PhotoImage(file=img_path)
                    # Redimensionne l'image en réduisant le facteur de sous-échantillonnage
                    img = img.subsample(2, 2)  # Par exemple, réduit l'image de moitié en largeur et en hauteur
                    label = tk.Label(window, image=img)
                    label.image = img
                    label.place(x=1047, y=125)
                
                try :
                    if len(vinterfaffichage[9]) >= w+1 and vinterfaffichage[9][4] == 1:
                        w+=1
                except:
                    pass

                if len(vinterfaffichage[9]) >= 6 and vinterfaffichage[9][5] == 1 and vinterfaffichage[3][w] == 1:
                    img_path = imgcarte[vinterfaffichage[1][w][0]]
                    img = tk.PhotoImage(file=img_path)
                    # Redimensionne l'image en réduisant le facteur de sous-échantillonnage
                    img = img.subsample(2, 2)  # Par exemple, réduit l'image de moitié en largeur et en hauteur 
                    label = tk.Label(window, image=img)
                    label.image = img
                    label.place(x=1303, y=385)  # Exemple de coordonnées, ajustez selon vos besoins

                    img_path = imgcarte[vinterfaffichage[1][w][1]]
                    img = tk.PhotoImage(file=img_path)
                    # Redimensionne l'image en réduisant le facteur de sous-échantillonnage
                    img = img.subsample(2, 2)  # Par exemple, réduit l'image de moitié en largeur et en hauteur
                    label = tk.Label(window, image=img)
                    label.image = img
                    label.place(x=1393, y=385)

            if vinterfaffichage[8] > 0:
                dictcartejoueur2 = []
                for m in range(len(vinterfaffichage[9])):
                    if vinterfaffichage[9][m] == 1:
                        dictcartejoueur2.append(m)
                texte = "Le joueur numero {} a gagné".format(dictcartejoueur2[vinterfaffichage[8]]+1)
                label = tk.Label(window, text=texte, font=("Arial", 23),fg="#a80602",bg="white")
                label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            elif vinterfaffichage[8] == -1:
                dictcartejoueur2 = []
                for m in range(len(vinterfaffichage[9])):
                    if vinterfaffichage[9][m] == 1:
                        dictcartejoueur2.append(m)
                jegalitegagne = []
                cartejoueurv2 = []
                dictcartejoueur = []
                for m in range(len(vinterfaffichage[3])):
                    if vinterfaffichage[3][m] == 1:
                        cartejoueurv2.append(cartejoueur[m])
                        dictcartejoueur.append(m)

                quigagnevaffiche = quigagne(carteplateau, cartejoueurv2)
                if len(quigagnevaffiche) == 1:
                    texte = "Le joueur numero {} a gagné".format(dictcartejoueur2[dictcartejoueur[quigagnevaffiche[0][1]]]+1)
                else:
                    for i in quigagnevaffiche:
                        jegalitegagne.append(dictcartejoueur2[dictcartejoueur[i[1]]]+1)
                    texte = "Les joueurs numeros {} ont gagné".format(jegalitegagne)
    
                label = tk.Label(window, text=texte, font=("Arial", 23),fg="#a80602",bg="white")
                label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        else:
            texte = "Vous avez gagné !"
            label = tk.Label(window, text=texte, font=("Arial", 23),fg="#a80602",bg="white")
            label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        window.after(100, update_interface)

    window = tk.Tk()
    window.title("Poker")
    window.geometry("1536x880+300+100")
    window.resizable(0,0)

    bouttonfold = tk.Button(window, text="Fold",font="Helvetica 15 bold",bg = "#a80602",fg = "white", borderwidth=2, command=lambda: boutonfonction(-1))
    bouttonfold.place(x=670, y=700)
    bouttonfold.lift()
    bouttoncall = tk.Button(window, text="Call",font="Helvetica 15 bold",bg = "#a80602",fg = "white", borderwidth=2, command=lambda: boutonfonction(0))
    bouttoncall.place(x=745, y=700)
    bouttoncall.lift()

    entreebet = tk.Entry(window, font="Helvetica 15 bold",width=4)
    entreebet.place(x=870, y=705)
    entreebet.lift()
    bouttonbet = tk.Button(window, text="Bet",font="Helvetica 15 bold",bg = "#a80602",fg = "white", borderwidth=2, command=lambda: boutonfonction(entreebet.get()))
    bouttonbet.place(x=815, y=700)
    bouttonbet.lift()

    update_interface()
    window.mainloop()

def boutonfonction(a):
    global actionbouton
    try:
        a = int(a)
    except ValueError:
        pass
    if type(a) == int:
        actionbouton = a

#FONCTION POUR DONNER DES CARTES ALEATOIREMENT

def cartealea():
    global Lcarte
    cartealea = carte[randint(0,51)]
    while cartealea in Lcarte:
        cartealea = carte[randint(0,51)]
    Lcarte.append(cartealea)
    return cartealea

def cartejp(nbjoueur):
    global Lcarte
    carteplateau = []
    Lcarte = []
    cartejoueur = []
    blufflist = []
    for i in range(nbjoueur):
        cartejoueur.append((cartealea(),cartealea()))
        blufflist.append(rd.random())
    for i in range(5):
        carteplateau.append(cartealea())
    return cartejoueur,carteplateau, blufflist

#FONCTION DES MISES

def misej(i,nbjoueur,premierj,affichagev):
    global jetonsjoueur, actionbouton, variables_bluff_par_joueur
    actionbouton = -2
    njoueuralgo1 = 1
    carteplateauv = []
    if partieavancementv==1:
        o = 0
    elif partieavancementv==2:
        o=3
    elif partieavancementv==3:
        o=4
    elif partieavancementv==4:
        o=5
    for m in range(o):
        carteplateauv.append(carteplateau[m])

    print(nbjoueur,jetonsjoueur[(premierj+i)%nbjoueur],max(mise),cartejoueur[(premierj+i)%nbjoueur],carteplateauv)

    if not ((premierj+i)%nbjoueur) == 0 : #njoueuralgo1
        print("joueur",((premierj+i)%nbjoueur) + 1)

        c = algoproba1(nbjoueur,jetonsjoueur[(premierj+i)%nbjoueur],max(mise)-mise[(premierj+i)%nbjoueur],cartejoueur[(premierj+i)%nbjoueur],carteplateauv,blufflist[(premierj+i)%nbjoueur],variables_bluff_par_joueur[(premierj+i)%nbjoueur], variables_surete_par_joueur[(premierj+i)%nbjoueur],(premierj+i)%nbjoueur)
        if c[0] == 0:
            misejoueur = "fold"
        elif c[0] == 1:
            misejoueur = "call"
        elif c[0] == 2:
            misejoueur = "bet"
        print(misejoueur)

    elif affichagev == True:
        while actionbouton == -2:
            time.sleep(0.1)
            try:
                if not window.winfo_exists():
                    sys.exit()
            except:
                pass
        if actionbouton == -1:
            misejoueur = "fold"
        elif actionbouton == 0:
            misejoueur = "call"
        else:
            misejoueur = "bet"

    else:
        misejoueur = input("fold, call ou bet")

    if misejoueur == "fold":
        misejoueur = 0
        quijoue[(premierj+i)%nbjoueur] = 0

    if misejoueur == "call":
        if mise[(premierj+i)%nbjoueur] == max(mise):
            if mise[((premierj+i)%nbjoueur)] == max(mise):
                misejoueur = 0
            else:
                if (max(mise)-mise[((premierj+i)%nbjoueur)]) > jetonsjoueur[((premierj+i)%nbjoueur)]:
                    misejoueur = int(jetonsjoueur[((premierj+i)%nbjoueur)])
                else:
                    misejoueur = int(max(mise)-mise[((premierj+i)%nbjoueur)])
        else:
            if (max(mise)-mise[((premierj+i)%nbjoueur)]) > jetonsjoueur[((premierj+i)%nbjoueur)]:
                misejoueur = int(jetonsjoueur[((premierj+i)%nbjoueur)])
            else:
                misejoueur = int(max(mise)-mise[((premierj+i)%nbjoueur)])

    if misejoueur == "bet":
        if not ((premierj+i)%nbjoueur) == 0 :
            misejoueur = int(c[1])
        elif affichagev == True:
            misejoueur = actionbouton
        else:
            misejoueur = input("valeur du bet")
        misejoueur = int(misejoueur)
        if misejoueur < max(mise)-mise[(premierj+i)%nbjoueur]:
            if mise[(premierj+i)%nbjoueur] != max(mise):
                misejoueur += int(max(mise) - mise[(premierj+i)%nbjoueur])
        
        if misejoueur > jetonsjoueur[((premierj+i)%nbjoueur)]:
            misejoueur = jetonsjoueur[((premierj+i)%nbjoueur)]

    jetonsjoueur[(premierj+i)%nbjoueur] = int(jetonsjoueur[(premierj+i)%nbjoueur] - misejoueur)
    actionbouton = -2
    return misejoueur

#FONCTION POUR DETERMINER SI TOUT LE MONDE A BIEN MISE/CALL/FOLD

def quijouef(quijoue,mise):
    a=True
    for i in range(len(mise)):
        if quijoue[i] == 1:
            if mise[i] == max(mise) or jetonsjoueur[i] == 0:
                a = True
            else:
                a = False
        if a == False:
            return False
    return True

def verif(quijoue,jetonsjoueurs,v):

    a = 0
    for k in range(len(quijoue)):
        if quijoue[k] == 1:
            if jetonsjoueurs[k] == 0:
                a+=1
    
    if quijoue.count(1) == a+1 and v == 1:
        return True

    if quijoue.count(1) == a:
        return True
    else:
        return False

def misemax(misemax,max):
    pot1 = 0
    for i in range(len(misemax)):
        if max >= misemax[i]:
            pot1+= misemax[i]
            misemax[i]=0
        else:
            pot1+= max
            misemax[i] -= max
    return pot1,misemax

#FONCTION POUR UNE PARTIE

def partie(nbjoueur,potjoueur,bb,affichagev):
    global mise, pot, quijoue, jetonsjoueur, cartejoueur, carteplateau, partieavancementv, vinterfaffichage, blufflist

    jetonsjoueur = potjoueur

    pot = 0
    mise = []
    for i in range(nbjoueur):
        mise.append(0)
    cartejoueur,carteplateau, blufflist = cartejp(nbjoueur)
    
    quijoue = []
    for i in range(nbjoueur):
        quijoue.append(1)
    

    premierj = randint(0,nbjoueur-1)

    partieavancementv=1

    jetonsgagner = []

    if affichagev == True:
        vinterfaffichage = [1,cartejoueur,carteplateau,quijoue,pot,mise,jetonsjoueur,jetonsgagner,0,quijouepartie] #avancement de la partie , carte des joueurs , cartes plateau , quijoue , pot , mise , jetons des joueur , jetonsgagner , joueur qui gagne

    print(jetonsjoueur)
    if jetonsjoueur[premierj] >= bb:
        mise[premierj] = bb
        jetonsjoueur[premierj] = jetonsjoueur[premierj] - bb
        pot += int(bb)
    else :
        mise[premierj] = jetonsjoueur[premierj]
        pot += int(jetonsjoueur[premierj])
        jetonsjoueur[premierj] = 0

    if premierj == 0:
        if jetonsjoueur[nbjoueur-1] >= int(bb/2):
            mise[nbjoueur-1] = int(bb/2)
            pot += int(bb/2)
            jetonsjoueur[nbjoueur-1] = int(jetonsjoueur[nbjoueur-1] - int(bb/2))
        else:
            mise[nbjoueur-1] = int(jetonsjoueur[nbjoueur-1])
            pot += int(jetonsjoueur[nbjoueur-1])
            jetonsjoueur[nbjoueur-1] = 0
    else:
        if jetonsjoueur[(premierj-1)%nbjoueur] >= int(bb/2):
            mise[(premierj-1)%nbjoueur] = int(bb/2)
            pot += int(bb/2)
            jetonsjoueur[(premierj-1)%nbjoueur] = int(jetonsjoueur[(premierj-1)%nbjoueur] - int(bb/2))
        else:
            mise[(premierj-1)%nbjoueur] = int(jetonsjoueur[(premierj-1)%nbjoueur])
            pot += int(jetonsjoueur[nbjoueur-1])
            jetonsjoueur[(premierj-1)%nbjoueur] = 0

    for i in range(nbjoueur):
        print(cartejoueur[i])

    if affichagev == True:
        vinterfaffichage = [1,cartejoueur,carteplateau,quijoue,pot,mise,jetonsjoueur,jetonsgagner,0,quijouepartie]

    i=1
    while (quijouef(quijoue,mise) == False or i<=nbjoueur) and verif(quijoue,jetonsjoueur,i) == False:
        if quijoue[(premierj+i)%nbjoueur] == 1 and jetonsjoueur[(premierj+i)%nbjoueur] != 0:
            print(mise)
            if affichagev == True:
                vinterfaffichage = [1,cartejoueur,carteplateau,quijoue,pot,mise,jetonsjoueur,jetonsgagner,0,quijouepartie]
            k = misej(i,nbjoueur,premierj,affichagev)
            mise[((premierj+i)%nbjoueur)] += int(k)
            pot += k
        i += 1
    
    if quijoue.count(1) == 1:
        if affichagev == True:
            vinterfaffichage = [1,cartejoueur,carteplateau,quijoue,pot,mise,jetonsjoueur,jetonsgagner,quijoue.index(1),quijouepartie]
        time.sleep(5)
        if affichagev == True:
            vinterfaffichage = [0,cartejoueur,carteplateau,quijoue,pot,mise,jetonsjoueur,jetonsgagner,quijoue.index(1),quijouepartie]
        return (quijoue.index(1)),pot


    if affichagev == True:
        vinterfaffichage = [2,cartejoueur,carteplateau,quijoue,pot,mise,jetonsjoueur,jetonsgagner,0,quijouepartie]

    print(carteplateau[0],carteplateau[1],carteplateau[2])

    partieavancementv=2

    i=1
    while (quijouef(quijoue,mise) == False or i<=nbjoueur) and verif(quijoue,jetonsjoueur,i) == False:
        if quijoue[(premierj+i)%nbjoueur] == 1 and jetonsjoueur[(premierj+i)%nbjoueur] != 0:
            print(mise)
            if affichagev == True:
                vinterfaffichage = [2,cartejoueur,carteplateau,quijoue,pot,mise,jetonsjoueur,jetonsgagner,0,quijouepartie]
            k = int(misej(i,nbjoueur,premierj,affichagev))
            mise[((premierj+i)%nbjoueur)] += k
            pot += k
        i += 1

    if quijoue.count(1) == 1:
        if affichagev == True:
            vinterfaffichage = [2,cartejoueur,carteplateau,quijoue,pot,mise,jetonsjoueur,jetonsgagner,quijoue.index(1),quijouepartie]
        time.sleep(5)
        if affichagev == True:
            vinterfaffichage = [0,cartejoueur,carteplateau,quijoue,pot,mise,jetonsjoueur,jetonsgagner,quijoue.index(1),quijouepartie]
        return (quijoue.index(1)),pot

    if affichagev == True:
        vinterfaffichage = [3,cartejoueur,carteplateau,quijoue,pot,mise,jetonsjoueur,jetonsgagner,0,quijouepartie]

    print(carteplateau[0],carteplateau[1],carteplateau[2],carteplateau[3])

    partieavancementv=3

    i=1
    while (quijouef(quijoue,mise) == False or i<=nbjoueur) and verif(quijoue,jetonsjoueur,i) == False:
        if quijoue[(premierj+i)%nbjoueur] == 1 and jetonsjoueur[(premierj+i)%nbjoueur] != 0:
            print(mise)
            if affichagev == True:
                vinterfaffichage = [3,cartejoueur,carteplateau,quijoue,pot,mise,jetonsjoueur,jetonsgagner,0,quijouepartie]
            k = int(misej(i,nbjoueur,premierj,affichagev))
            mise[((premierj+i)%nbjoueur)] += k
            pot += k
        i += 1

    if quijoue.count(1) == 1:
        if affichagev == True:
            vinterfaffichage = [3,cartejoueur,carteplateau,quijoue,pot,mise,jetonsjoueur,jetonsgagner,quijoue.index(1),quijouepartie]
        time.sleep(5)
        if affichagev == True:
            vinterfaffichage = [0,cartejoueur,carteplateau,quijoue,pot,mise,jetonsjoueur,jetonsgagner,quijoue.index(1),quijouepartie]
        return (quijoue.index(1)),pot

    if affichagev == True:
        vinterfaffichage = [4,cartejoueur,carteplateau,quijoue,pot,mise,jetonsjoueur,jetonsgagner,0,quijouepartie]

    print(carteplateau[0],carteplateau[1],carteplateau[2],carteplateau[3],carteplateau[4])

    partieavancementv=4

    i=1
    while (quijouef(quijoue,mise) == False or i<=nbjoueur) and verif(quijoue,jetonsjoueur,i) == False:
        if quijoue[(premierj+i)%nbjoueur] == 1 and jetonsjoueur[(premierj+i)%nbjoueur] != 0:
            print(mise)
            if affichagev == True:
                vinterfaffichage = [4,cartejoueur,carteplateau,quijoue,pot,mise,jetonsjoueur,jetonsgagner,0,quijouepartie]
            k = int(misej(i,nbjoueur,premierj,affichagev))
            mise[((premierj+i)%nbjoueur)] += k
            pot += k
        i += 1

    if quijoue.count(1) == 1:
        if affichagev == True:
            vinterfaffichage = [4,cartejoueur,carteplateau,quijoue,pot,mise,jetonsjoueur,jetonsgagner,quijoue.index(1),quijouepartie]
        time.sleep(5)
        if affichagev == True:
            vinterfaffichage = [0,cartejoueur,carteplateau,quijoue,pot,mise,jetonsjoueur,jetonsgagner,quijoue.index(1),quijouepartie]
        return (quijoue.index(1)),pot

    for i in range(nbjoueur):
        print(cartejoueur[i])

    cartejoueurrestant = []
    for i in range(len(cartejoueur)):
        if quijoue[i] == 1:
            cartejoueurrestant.append(cartejoueur[i])

    classementdesmains= classement_des_mains(quijoue,carteplateau,cartejoueurrestant)

    jetonsgagner = []
    for i in range(nbjoueur):
        jetonsgagner.append(0)

    mise_1 = mise.copy()

    for i in classementdesmains:
        vprob = 0
        Lprob = []
        if len(i)!=1:
            potegalite= int(pot/len(i))
        for k in i:
            if len(i)!=1:
                if jetonsjoueur[k[1]] != 0:
                    jetonsgagner[k[1]] += potegalite
                    pot -= potegalite
                else:
                    if potegalite > mise[k[1]]*len(i):
                        jetonsgagner[k[1]] += mise[k[1]]*len(i)
                        pot -= mise[k[1]]*len(i)
                        vprob += potegalite-mise[k[1]]*len(i)
                        Lprob.append(k[1])
                        
                    else:
                        jetonsgagner[k[1]] += potegalite
                        pot -= potegalite
            else:
                if jetonsjoueur[k[1]] != 0:
                    jetonsgagner[k[1]] += pot
                    pot = 0
                else:
                    if pot > mise[k[1]]*len(quijoue):
                        pot_1,mise_1 = misemax(mise_1,mise[k[1]])
                        jetonsgagner[k[1]] += pot_1
                        pot -= pot_1
                    else:
                        jetonsgagner[k[1]] += pot
                        pot = 0
        if vprob != 0:
            vprob = int(vprob/(len(i)-len(Lprob)))
            for d in i:
                if d[1] not in Lprob:
                    jetonsgagner[d[1]] += vprob
                    pot -= vprob
        if pot<= 0:
            break

    for i in range(len(jetonsgagner)):
        jetonsjoueur[i] += jetonsgagner[i]

    if len(classementdesmains) == nbjoueur:
        jquigagne = classementdesmains[0][0][1]
    else:
        jquigagne = -1

    if affichagev == True:
        vinterfaffichage = [5,cartejoueur,carteplateau,quijoue,pot,mise,jetonsjoueur,jetonsgagner,jquigagne,quijouepartie]

    time.sleep(5)
    if affichagev == True:
        vinterfaffichage = [0,cartejoueur,carteplateau,quijoue,pot,mise,jetonsjoueur,jetonsgagner,jquigagne,quijouepartie]
    return (jetonsjoueur,classementdesmains,jetonsgagner)

def game(nbjoueur,jetonsmax,bb,affichage):
    global vinterfaffichage, quijouepartie
    if affichage == True :
        vinterfaffichage = [0]
        affichagethread = threading.Thread(target=affichageinterface)
        affichagethread.start()
    potjoueur = []
    for i in range(nbjoueur):
        potjoueur.append(jetonsmax)

    quijouepartie = []
    for i in range(nbjoueur):
        quijouepartie.append(1)

    bbv = 0

    while nbjoueur != 1 :
        partiev = partie(nbjoueur,potjoueur,bb,affichage)
        if len(partiev) == 2:
            joueurquigagne,jetonsjgagner = partiev
            potjoueur[joueurquigagne] += jetonsjgagner
        else:
            potjoueur,classementdesmains,jetonsgagner = partiev
            potjoueur_2 = potjoueur.copy()
            quijouepartie_2 = quijouepartie.copy()
            c = 0
            for i in range(len(potjoueur_2)):
                if potjoueur_2[i] == 0:
                    potjoueur.pop(i-c)
                    d=0
                    for f in range(len(quijouepartie_2)):
                        if quijouepartie_2[f] == 1:
                            if d == i:
                                quijouepartie[f] = 0
                            d+=1
                    nbjoueur -= 1
                    c+= 1
            print(quijouepartie,potjoueur,classementdesmains,jetonsgagner)

        if bbv%4 == 0:
            bb = bb*2

        bbv+=1

        if quijouepartie[0] == 0 and affichage == True:
            break

    if affichage != True:
        print("Le gagnant de la partie est le joueur "+str(quijouepartie.index(1)+1))
        return quijouepartie.index(1)+1

with open('options.txt', 'r') as file:
    lines = file.readlines()

# Assignation des variables
variables = {}
for line in lines:
    key, value = line.strip().split('=')
    key = key.strip()
    if 'variable de bluff' in key:
        key = 'variables_bluff_pour_chaque_joueur'
    elif 'variable surete' in key:
        key = 'variables_surete_pour_chaque_joueur'
    if key == 'affichage':
        value = True if value.strip() == 'True' else False
    else:
        # Utiliser eval pour traiter les listes flottantes
        value = eval(value.strip())
    variables[key] = value

# Assignation des variables individuelles
nb_joueur = variables['nbjoueur']
variables_bluff_par_joueur = variables['variables_bluff_pour_chaque_joueur']
jetons_par_joueur = variables['jetonparjoueur']
bigblind = variables['bigblind']
affichage = variables['affichage']
variables_surete_par_joueur = variables['variables_surete_pour_chaque_joueur']
if nb_joueur > len(variables_bluff_par_joueur):
    for z in range(nb_joueur-len(variables_bluff_par_joueur)+1):
        variables_bluff_par_joueur.append(0)

if nb_joueur > len(variables_surete_par_joueur):
    for z in range(nb_joueur-len(variables_surete_par_joueur)+1):
        variables_surete_par_joueur.append(1)
# Affichage des variables (juste pour vérification)
print("Nombre de joueurs:", nb_joueur)
print("Variables de bluff par joueur:", variables_bluff_par_joueur)
print("Variables de sureté par joueur:", variables_surete_par_joueur)
print("Jetons par joueur:", jetons_par_joueur)
print("BigBlind:", bigblind)
print("Affichage:", affichage)


print("La partie va commencer")
game(nb_joueur,jetons_par_joueur,bigblind,affichage)
