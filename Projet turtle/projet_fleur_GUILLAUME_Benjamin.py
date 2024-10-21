# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
from datetime import *
from turtle import *
from random import *
"""on dessine BEGU avec la tortue"""  
def signature(): 
    """on trace le B"""  #forward avant et apres les cercle pour élagir le demi cercle sans modifier la hauteur et  égaliser avec la largeur des autres lettres 
    forward(7)
    circle(11,180) #demi cercle du bas
    forward(7)                       
    left(180)
    forward(7)
    circle(11,180) #demi cercle  du haut
    forward(7)
    left(90)
    forward(45) #barre verticale 
    """on déplace la tortue j'usqu'a l'emplacement du E"""
    up() 
    left (90)
    forward(20)
    down()
    """on trace le E"""
    left(90)
    forward(45) #barre verticale
    right(90)
    forward(18) #barre du haut
    right(90)
    up()
    forward(22)
    left(90)
    backward(5)
    down()
    backward(13) #barre du milieu
    right(90)
    forward(22)
    left(90)
    forward(18) #barre du bas
    """On déplace la tortue j'usqu"a l'emplacement du G"""
    up()
    forward(22)
    down()
    """on trace le G"""
    circle (22,-210) #arondi du G
    up()
    circle(22,-150)
    down()
    forward(9)
    left(90)
    forward(18)#barre verticale
    left(90)
    up()
    forward(9)
    down()
    backward(11)
    """On déplace la tortue j'usqu"a l'emplacement du U"""
    up()
    right(90)
    forward(27)
    right(90)
    forward(3)
    down()
    """on trace le U"""
    right(90)
    forward(31) #barre de gauche
    circle(13,180) #demi cercle du bas
    forward(31) #barre de droite
    
"""crée la tige des fleurs"""  
def tige(taille):
    color("green") #met la couleur en vert pour la tige
    down()
    forward(3*taille)#trace la tige
    color("black")#change la couleur pour le contour noir
    
    
"""dessine la fleur 1"""
def fleur1(taille,couleur):
    originefleur = position() #crée une vatiable qui contient la position de depart de la tortue
    orientationbase = heading() #crée une variable qui contient l'orientation de depart de la tortue
    down()
    tige(taille)
    fillcolor(couleur)#met la couleur de remplissage  a la couleur voulue
    begin_fill() 
    right(90)#oriente la tortue pour tracer le cercle le plus grand
    circle(taille) #trace le cerclele plus grand
    end_fill()
    left(90)
    up()
    forward(taille/2) #l.84 , 85 et 86 : place la tortue pour tracer le coeur
    down()
    right(90)
    fillcolor("yellow")#met la couleur du remplissage en jaune pour tracer le coeur
    begin_fill()
    circle(taille/2)#trace le coeur
    end_fill()
    up()
    goto(originefleur) #fait retourner la tortue a la position de départ
    setheading(orientationbase) #oriente la tortue a l'orientation de depart
    
    
    
    
    
    
    """dessine la fleur 2"""
def fleur2 (taille,couleur,nb_coté):
    originefleur = position() #crée une vatiable qui contient la position de depart de la tortue
    orientationbase = heading() #crée une variable qui contient l'orientation de depart de la tortue
    down()
    tige(taille)
    fillcolor(couleur)#met la couleur de remplissage a la  couleur voulue
    left(90-(360/nb_coté)/2)#oriente la tortue au bon angle pour tracer le polygone
    begin_fill()#commence a remplir la fleur
    for i in range(nb_coté): #trace le polygone
        forward(taille)
        right(360/nb_coté)
    end_fill()
    up()#leve le stylo pour retourner a l'ogine sans dessiner sur la fleur;
    goto(originefleur) #fait retourner la tortue a la position de départ
    setheading(orientationbase) #oriente la tortue a l'orientation de depart
    
    
    
    
    
    """dessine la fleur 3"""
    
def fleur3(taille,couleur):
    originefleur = position() #crée une vatiable qui contient la position de depart de la tortue
    orientationbase = heading() #crée une variable qui contient l'orientation de depart de la tortue
    down()
    tige(taille)
    fillcolor(couleur)#met la couleur de remplissage a la  couleur voulue
    up()
    circle(taille,90) #se met a la bonne position pour tracer le demi cercle
    down()
    begin_fill()
    left(90)
    circle(taille,180) #trace le demi cercle
    forward(taille)#trace la bare inférieure entre le demi cercle et le dessus
    #trace le dessus du calice
    for i in range(3): 
        circle(taille/3,-180)
        left(180)
    backward(taille)#trace la bare supérieure entre le demi cercle et le dessus
    end_fill()
    up()#leve le stylo pour retourner a l'ogine sans dessiner sur la fleur;
    goto(originefleur) #fait retourner la tortue a la position de départ
    setheading(orientationbase) #oriente la tortue a l'orientation de depart



    """dessine la fleur 4(qui a la forme du logo python)"""

def fleur4(taille,couleur1,couleur2,contour):
    originefleur = position() #crée une vatiable qui contient la position de depart de la tortue
    orientationbase = heading() #crée une variable qui contient l'orientation de depart de la tortue
    down()
    tige(taille)
    right(45)
    fillcolor(couleur1)
    pensize(4)
    pencolor(contour)
    for i in range(2):#dessine la 1ere moitiée de la fleur puis son symétrique
        begin_fill()
        forward(taille/8)
        circle(taille/8,90)
        forward(taille/8)
        for i in range(2):
            forward(taille/8)
            circle(taille/8,90)
            forward(taille/4)
            circle(taille/8,90)
            forward(taille/8)
            right(90)
            #dessine la "bouche"
            backward(taille/6)
            forward(taille/6)
        right(180)
        forward(taille/8)
        right(180)
        circle(taille/8,-90)
        left(180)
        forward(taille/8)
        end_fill()
        #dessine les yeux
        up()
        left(90)
        forward(taille*(3/8))
        left(90)
        forward(taille/8)
        down()
        fillcolor("white")
        pencolor("white")
        begin_fill()
        circle(taille/32)
        end_fill()
        #remet les bonnes couleurs, position et orientation pour faire le symetrique de la 1ere partie de la fleur
        pencolor(contour)
        up()
        right(180)
        forward(taille/8)
        right(90)
        forward(taille*(3/8))
        right(90)
        fillcolor(couleur2)
        down()
    width(1)
    up()#leve le stylo pour retourner a l'ogine sans dessiner sur la fleur;
    goto(originefleur) #fait retourner la tortue a la position de départ
    setheading(orientationbase) #oriente la tortue a l'orientation de depart
    
"""dessine la fleur5"""
    
    
def fleur5(taille,nbClochettes,couleur):
    originefleur = position() #crée une vatiable qui contient la position de depart de la tortue
    orientationbase = heading() #crée une variable qui contient l'orientation de depart de la tortue
    down()
    tige(taille)
    for i in range(nbClochettes):
        speed(0)
        tige(taille/2.7)
        origineclochette=position()#crée une vatiable qui contient la position de depart de la tortue pour dessiner la clochette
        orientationbaseclochette=heading()#crée une vatiable qui contient ll'orientation de depart de la tortue pour dessiner la clochette
        coté_clochette = choice([left,right])
        pencolor("green")
        fillcolor(couleur)
        if coté_clochette == left : #tourne la tortue a gauche ou a droite suivant le choix
            left(90)
            circle(taille,90) #trace la tige de la clochette
        else :
            right(90)
            circle(-taille,90)#trace la tige de la clochette
        begin_fill()
        right(90)
        circle(taille/2,90) #trace la moitié gauche de la clochette
        for i in range(5): #trace le dessous de la clochette
            circle(taille/20,-180)
            right(180)
            circle(taille/20,180)
            right(180)
        left(180)
        circle(taille/2,90)#trace la moitié droite de la clochette
        end_fill()
        up()
        goto(origineclochette) #reourne a l'origine de la clochette
        setheading(orientationbaseclochette)#reourne a l'orientation de depart de la clochette
        down()      
    up()#leve le stylo pour retourner a l'ogine sans dessiner sur la fleur;
    goto(originefleur) #fait retourner la tortue a la position de départ
    setheading(orientationbase) #oriente la tortue a l'orientation de depart





"""dessine la fleur6"""



      
def fleur6(taille,couleur):#l'affichage de l'heure peut etre "numerique" ou "aiguille"
    originefleur = position() #crée une vatiable qui contient la position de depart de la tortue
    orientationbase = heading() #crée une variable qui contient l'orientation de depart de la tortue
    down()
    tige(taille)
    right(90)
    heure = int(datetime.now().time().strftime("%H"))
    minute = int(datetime.now().time().strftime("%M"))
    pencolor("black")
    fillcolor("white")
    begin_fill()
    width(2)
    circle(taille)
    end_fill()
    up()
    left(90)
    forward(taille)
    down()
    pencolor(couleur)
    #trace l'aiguille des heures
    angle_heure= (heure/12)*360
    right(angle_heure)
    forward(taille/1.5)
    #retourne au centre
    backward(taille/1.5)
    left(angle_heure)
    #trace l'aiguille des minutes
    angle_minute= (minute/60)*360
    right(angle_minute)
    forward(taille/1.1)
    up()#leve le stylo pour retourner a l'ogine sans dessiner sur la fleur;
    goto(originefleur) #fait retourner la tortue a la position de départ
    setheading(orientationbase) #oriente la tortue a l'orientation de depart
    width(1)
   
    
   
    
"""dessine le décor derière le vase"""
def décor():
    speed(0)
    #dessine le cadre
    up()
    begin_fill()
    fillcolor("gold")
    goto(0,-355)
    down()
    goto(250,-355)
    goto(250,350)
    goto(-250,350)
    goto(-250,-355)
    goto(0,-355)
    end_fill()
    #dessine l'herbe
    up()
    goto(230,-333)
    down()
    begin_fill()
    fillcolor("darkgreen")
    goto(230,-80)
    goto(-230,-80)
    goto(-230,-335)
    goto(230,-335)
    end_fill()
    #dessine le ciel
    up()
    goto(230,-80)
    down()
    begin_fill()
    if int(datetime.now().time().strftime("%H")) >= 20 or int(datetime.now().time().strftime("%H"))<= 7 : #change la couleur du ciel si l'heure est comprise entre 20 h et 7h
        fillcolor("navy")
    else :
        fillcolor("cyan")
    goto(230,330)
    goto(-230,330)
    goto(-230,-80)
    goto(230,-80)
    end_fill()
    #dessine les oiseaux
    for i in range(randint(5,20)):
        x= randint(-210,230)
        y = randint(0,330)
        up()
        goto(x,y)
        down()
        setheading(180)
        if int(datetime.now().time().strftime("%H")) >= 20 or int(datetime.now().time().strftime("%H"))<= 7 : #change les oiseaux en étoile si l'heure est comprise entre 20 h et 7h
            fillcolor("white")
            pencolor("white")
            begin_fill()
            circle(2.5)
            end_fill()
        else :
            for i in range(2): 
                circle(10,90)
                left(180)
        pencolor("black")
    #dessine le soleil
    up()
    if int(datetime.now().time().strftime("%H")) >= 20 or int(datetime.now().time().strftime("%H"))<= 7 : #change le soleil en lune si l'heure est comprise entre 20 h et 7h
        fillcolor("aliceblue")
    else :
        fillcolor("yellow")
    goto(180,260)
    begin_fill()
    down()
    circle(30)
    end_fill()
    #dessine la tour
    up()
    goto(-170,-90)
    down()
    fillcolor("antiquewhite2")
    begin_fill()
    goto(-90,-90)
    goto(-90,230)
    goto(-190,230)
    goto(-190,-90)
    end_fill()
    fillcolor("cadetblue4") 
    up()
    goto(-90,230)
    down()
    begin_fill()
    goto(-140,300)
    goto(-190,230)
    end_fill()
    up()
    goto(-140,150)
    down()
    #dessine l'horloge
    heure = int(datetime.now().time().strftime("%H"))
    minute = int(datetime.now().time().strftime("%M"))
    pencolor("black")
    fillcolor("white")
    begin_fill()
    width(2)
    circle(40)
    end_fill()
    up()
    left(90)
    forward(40)
    down()
    pencolor("black")
    setheading(90)
    #trace l'aiguille des heures
    angle_heure= (heure/12)*360
    right(angle_heure)
    forward(25)
    #retourne au centre
    backward(25)
    left(angle_heure)
    #trace l'aiguille des minutes
    angle_minute= (minute/60)*360
    right(angle_minute)
    forward(35)
    width(1)
    setheading(0)

"""dessine la composition aléatoire de fleurs(cette fonction sera ensuite appelé dans vase()"""



def composition(): 
    speed(0)
    nb_fleur = randint(3,7) #choisi aléatoirement le nombre de fleur a dessiner
    setheading(145)   #met la tortue a l'angle voulu
    for i in range (nb_fleur):
        quel_fleur = choice([[fleur1,(randint(30,45),(random(),random(),random()))], #crée la liste qui contient le nom de la fontion fleur1 puis ses argument. cette liste est un des choix du "choice"
                        [fleur2,(randint(25,35),(random(),random(),random()),randint(3,10))],#idem avec fleur2
                        [fleur3,(randint(25,35),(random(),random(),random()))],#idem avec fleur3
                        [fleur4,(randint(40,60),(random(),random(),random()),(random(),random(),random()),(random(),random(),random()))], #idem avec fleur4
                        [fleur5,(randint(20,30),randint(2,5) , (random(),random(),random()))],#idem avec fleur5
                        [fleur6,(randint(30,45),(random(),random(),random()))]])#idem avec fleur6
        quel_fleur[0](*quel_fleur[1])#recompose et apel la fonction quel_fleur avec le nom et les arguments choisis par le choice
        right((110/(nb_fleur-1)))#tourne la tortue pour la prochaine fleur
        

"""dessine le vase avec les fleur et le décor"""
    
def vase():
    reset()
    speed(0)
    décor()# dessine le décor
    #dessine la base
    up()
    goto(0,-300)
    down()
    pencolor("sienna4")
    fillcolor("sienna4")
    begin_fill()
    forward(67)
    right(180)
    circle(13,-90)
    backward(7)
    circle(13,-90)
    backward(133)
    circle(13,-90)
    backward(7)
    circle(13,-90)
    backward(67)
    end_fill()
    #place la tortue pour dessiner l'oval centrale du vase
    up()
    backward(47)
    right(90)
    forward(13)
    setheading(45)
    down()
    
    for i in range(3): #dessine l'oval centrale et met la tortue en haut de l'oval
        begin_fill()
        circle(133,90)
        circle((133)//2,90)
        end_fill()
    setheading(90)
    #dessine le haut du vase
    begin_fill()
    forward(40)
    circle(7,90)
    right(180)
    circle(13,-180)
    backward(107)
    circle(13,-180)
    setheading(180)
    circle(7,90)
    forward(40)
    end_fill()  
    #trace la 1ere hances
    width(4)# augmente l'épaisseur du pinceau pour avoir un trait arondi
    up()
    a=position()#enregistre la position dans la variable a
    backward(33)
    down()
    setheading(-135)
    circle(13,-180)
    goto(a)
    #trace la 2e hance
    up()
    setheading(180)
    forward(93)
    setheading(-90)
    a=position()#enregistre la position dans la variable a
    backward(33)
    down()
    setheading(135)
    circle(13,180)
    goto(a)
    #trace le motif
    width(1)
    color("black")
    setheading(270)
    up()
    forward(2)
    setheading(0)
    backward(2)
    down()
    for i in range(7):#dessine la répétition de motif en haut
        forward(3.2)
        left(90)
        forward(10)
        right(90)
        forward(10)
        right(90)
        forward(7)
        right(90)
        forward(3.2)
        right(90)
        forward(4)
        left(90)
        forward(3.3)
        left(90)
        forward(7)
        left(90)
        forward(6.5)
    forward(4.7)
    a=position()
    up()
    goto(-84,-204)
    down()
    for i in range(13):#dessine la répétition de motif en bas
        forward(3)
        left(90)
        forward(10)
        right(90)
        forward(10)
        right(90)
        forward(7)
        right(90)
        forward(3)
        right(90)
        forward(4)
        left(90)
        forward(3.3)
        left(90)
        forward(7)
        left(90)
        forward(6.3)
    #place la signature
    up()
    goto(-45,-180)
    down()
    signature() #dessine la signature
    #se rend au point de depart des fleurs
    up()
    goto(0,-26)
    #trace les fleur
    composition()

    


    

vase()
exitonclick() 
    