#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Nom et prénom : GUILLAUME Benjamin

import pyxel
import random
from math import *
from queue import PriorityQueue
from PIL import Image
# On définit la taille dans une "constante" qui ne changera pas
TAILLE = 64
# Vitesse de déplacement normale du joueur



#le fond d'ecran

# Initialisation de pyxel
pyxel.init(TAILLE, TAILLE, fps=30,title="ValoPYX")
pyxel.load("projet_eleve.pyxres")



### Fonctions pour faire fonctionner le jeu
def deplacement(x, y, xm,ym):
    """ x et y sont les coordonnées du joueur. 
    Renvoie les nouvelles coordonnées du joueur en tenant 
    compte des touches appuyées.  
    Le joueur ne peut pas sortir de l'écran"""
    global is_dashing
    global bullet_x,bullet_y
    if not is_dashing:
        if pyxel.btn(pyxel.KEY_D) and not is_white_pixel_or_Black(x + 1,y): # on incrémente la bonne coordonée du joueur de 1 pour le déplacer si il n'est pas bloqué , on incrémente aussi le décalage de la "camera" pour qu'elle suive le joueur et enfin, on décrémente les coordonées de la balle tirée par le joueur car sinon elle resterait en face de lui
                x += 1
                xm +=1
                bullet_x -= 1
        if pyxel.btn(pyxel.KEY_Q) and not is_white_pixel_or_Black(x - 1, y):
                x -= 1
                xm -=1
                bullet_x += 1
        if pyxel.btn(pyxel.KEY_S) and not is_white_pixel_or_Black(x, y + 1):
                y += 1
                ym +=1
                bullet_y -= 1
        if pyxel.btn(pyxel.KEY_Z) and not is_white_pixel_or_Black(x, y - 1):
                y -= 1
                ym -=1
                bullet_y += 1
            
    return x, y, xm, ym

#competences 
def dash():
    global x 
    global y
    global xm
    global ym
    global is_dashing
    global dash_cooldown
    tempo = 0
    if pyxel.btn(pyxel.KEY_E)  and dash_cooldown == 0:
        is_dashing =True
        if  pyxel.btn(pyxel.KEY_D):
            while tempo <= 10 and not is_white_pixel_or_Black(x+1,y): #si le joueur peut effectuer son dash sans rentre dans un mur , alors on incrémente les coordonées tant que elles n'ont pas augmenté de 10 et ensuite on met que le joueur ne dash plus
                x += 1
                xm +=1
                tempo+=1
            is_dashing = False
            dash_cooldown = 300
        if  pyxel.btn(pyxel.KEY_Q):
            while tempo <= 10 and not is_white_pixel_or_Black(x-1,y):
                x -= 1
                xm -=1
                tempo+=1
            is_dashing = False 
            dash_cooldown = 300
        if  pyxel.btn(pyxel.KEY_Z):
            while tempo <= 10 and not is_white_pixel_or_Black(x,y-1):
                y -= 1
                ym -=1
                tempo+=1
            is_dashing = False
            dash_cooldown = 300
        if  pyxel.btn(pyxel.KEY_S):
            while tempo <= 10 and not is_white_pixel_or_Black(x,y+1):
                y += 1
                ym +=1
                tempo+=1
            is_dashing = False
            dash_cooldown = 300
    else : 
         is_dashing= False
    return x ,y ,xm , ym

def detectSite(): #on détecte si les coordonées du joueurs sont comprisent dans les coordonées d'entrée dans le site A ou B
    global x, y
    global goToASite, goToBSITE
    if (x >= 38 and x  <= 50) and (y==93):
          goToASite = False
          goToBSITE = True
          

    elif (x >= 187 and x <= 195) and (y==119):
          goToASite = True
          goToBSITE = False
          
    return  goToASite, goToBSITE
        


    
            


def create_enemy(): #cette fonction crée les enemis
    global enemy
    global possibleSpawnPointsA
    global possibleSpawnPointsB
    global possibleSpawnPointsMid

    
    hp = 100 #le nombre de points de vie de l'enemi
    for i in range (5): #on en crée 5
        a = random.choice(["A","B","Mid"]) #on choisi sa zone de la carte
        if a == "A":
            if len(possibleSpawnPointsA) >1:
                sp = possibleSpawnPointsA[random.randint(0,len(possibleSpawnPointsA)-1)] #son point de spawn 
                enemy_bullet_x_y = sp[:] #les coordonées initiales des balles qu'il tire
                current_coordinates = sp[:] #les coordonées qui peuvent augmenter ou diminuer
                
                possibleSpawnPointsA.remove(sp) #on retire le point de spawn por que 2 enemis n'aparaissent pas au meme endroit
                Site = "A" #on dit a quelle zone il apartient
                BrotatePoint = [random.randint(0,79) ,random.randint(28,75)] # on définit sa destination de rotation si le joueur ne vas pas sur son site
                while is_white_pixel_or_Black(BrotatePoint[0],BrotatePoint[1] ): #on regarde si le point de rotation n'est pas endehors de la map
                    BrotatePoint = [random.randint(0,79) ,random.randint(28,75)]

                ArotatePoint = [random.randint(216,247) ,random.randint(46,94)]
                while is_white_pixel_or_Black(ArotatePoint[0],ArotatePoint[1]):
                    ArotatePoint = [random.randint(216,247) ,random.randint(46,94)]
                
                path = astar(sp, BrotatePoint, create_grid())  # on définit son chemin vers son point de rotation grace a l'algorithme a*
                
                enemy_shoot_down = False #on initaialise ses variables de tir
                enemy_shoot_up = False
                enemy_shoot_left = False
                enemy_shoot_right = False
            else:
                a = random.choice(["A","B","Mid"])
            
        elif a =="B": #idem
            if len(possibleSpawnPointsB) >1:
                sp = possibleSpawnPointsB[random.randint(0,len(possibleSpawnPointsB)-1)]
                enemy_bullet_x_y = sp[:]
                current_coordinates = sp[:]

                possibleSpawnPointsB.remove(sp)
                Site = "B"
                BrotatePoint = [random.randint(0,79) ,random.randint(28,75)]
                while is_white_pixel_or_Black(BrotatePoint[0],BrotatePoint[1]):
                    BrotatePoint = [random.randint(0,79) ,random.randint(28,75)]

                ArotatePoint = [random.randint(216,247) ,random.randint(46,94)]
                while is_white_pixel_or_Black(ArotatePoint[0],ArotatePoint[1]):
                    ArotatePoint = [random.randint(216,247) ,random.randint(46,94)]
                
                path = astar(sp, ArotatePoint, create_grid())
                
                enemy_shoot_down = False
                enemy_shoot_up = False
                enemy_shoot_left = False
                enemy_shoot_right = False
            else:
                a = random.choice(["A","B","Mid"])
            
        else : 
            if len(possibleSpawnPointsMid) >1:#idem
                sp = possibleSpawnPointsMid[random.randint(0,len(possibleSpawnPointsMid)-1)]
                enemy_bullet_x_y = sp[:]
                current_coordinates = sp[:]
                
                possibleSpawnPointsMid.remove(sp)
                Site = "Mid"
                BrotatePoint = [random.randint(0,79) ,random.randint(28,75)]
                while is_white_pixel_or_Black(BrotatePoint[0],BrotatePoint[1]):
                    BrotatePoint = [random.randint(0,79) ,random.randint(28,75)]

                ArotatePoint = [random.randint(216,247) ,random.randint(46,94)]
                while is_white_pixel_or_Black(ArotatePoint[0],ArotatePoint[1]):
                    ArotatePoint = [random.randint(216,247) ,random.randint(46,94)]

                pathB = astar(sp, BrotatePoint, create_grid())
                
                pathA = astar(sp, ArotatePoint, create_grid())
                
                enemy_shoot_down = False
                enemy_shoot_up = False
                enemy_shoot_left = False
                enemy_shoot_right = False
            else:
                a = random.choice(["A","B","Mid"])
            
            
        if Site != "Mid":#on compile les données de chaque enemi dans un dictionaire(si l'enemi fait parti du milieu, alors il poura aller vers le a et b , c'est pour ça que l'on lui atribut les 2 chemins)
            enemy[f"enemi {i+1}"] =  [sp, hp, False,enemy_bullet_x_y , current_coordinates, Site,BrotatePoint,ArotatePoint, enemy_shoot_down,enemy_shoot_up,enemy_shoot_left,enemy_shoot_right,path] 
            
        else :
            enemy[f"enemi {i+1}"] =  [sp, hp, False,enemy_bullet_x_y , current_coordinates, Site,BrotatePoint,ArotatePoint,  enemy_shoot_down,enemy_shoot_up,enemy_shoot_left,enemy_shoot_right,  pathB, pathA ]
            
            



def enemies_display(enemies): #cete fonction afiche les enemis

    global xm,ym
    global enemy    

    pyxel.pset(enemy[enemies][4][0] - xm, enemy[enemies][4][1] - ym, 8)

        


def is_white_pixel_or_Black(x, y): 
    # Vérifie si le pixel à la position (x, y) est blanc
    color = pyxel.images[0].pget(x, y)
    return (color == 7 )or (color == 0) or (color == 8)

def is_path_clear(player_x, player_y, enemy_x, enemy_y):
    # Utilise l'algorithme de Bresenham pour vérifier s'il y a un pixel blanc entre le joueur et l'ennemi
    dx = abs(enemy_x - player_x)
    dy = abs(enemy_y - player_y)
    sx = 1 if player_x < enemy_x else -1
    sy = 1 if player_y < enemy_y else -1
    err = dx - dy

    while True:
        if is_white_pixel_or_Black(player_x, player_y):
            return False  # Il y a un pixel blanc sur la ligne, donc le chemin n'est pas clair
        if player_x == enemy_x and player_y == enemy_y:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            player_x += sx
        if e2 < dx:
            err += dx
            player_y += sy

    return True  # Aucun pixel blanc trouvé sur la ligne, donc le chemin est clair
    
def shooting_direction(): #cette fonction dit si le joueur tir en haut, a droite ,a gauche ou en bas par rapport a la position de la souris sur l'ecran
    mx = x-xm - pyxel.mouse_x
    my = y -ym -pyxel.mouse_y
    if mx < 0:
        if my < 0:
            if -mx > -my:
                return "droite"
            elif -mx <= -my:
                return "bas"
        elif my > 0:
            if -mx < my:
                return "haut"
            else:
                return "droite"
        else:
            return "droite"
    else:
        if my < 0:
            if mx < -my:
                return "bas"
            elif mx > -y:
                return "gauche"
            else:
                return "gauche"
        else:
            if mx < my:
                return "haut"
            else:
                return "gauche"

def bullet_display(bullet_x, bullet_y):#affiche la balle
    pyxel.pset(bullet_x, bullet_y, 4)

def shoot():#fonction de tir
    global direct
    global is_shooting
    global bullet_x, bullet_y
    global x, y, ym, xm
    
    # Si la souris est cliquée et le tir n'est pas en cours
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and not is_shooting:
        direct = shooting_direction()
        # Position initiale du projectile
        bullet_x = x - xm
        bullet_y = y - ym

        # Démarrer le tir
        is_shooting = True

    # Si le tir est en cours
    if is_shooting:
        
        # Avancer d'un pixel dans la bonne direction
        if direct == "gauche":
            bullet_x -= 1
            
        elif direct == "droite":
            bullet_x += 1
            
        elif direct == "haut":

            bullet_y -= 1
            
        elif direct == "bas":
            bullet_y += 1
            
        # Vérifier si la balle est hors de l'écran

        # Si la balle rencontre un obstacle
        if is_white_pixel_or_Black(bullet_x+xm, bullet_y+ym ):
            # Arrêter le tir
            is_shooting = False
            
        elif pyxel.pget(bullet_x , bullet_y) == 8 :
            is_shooting = False
            
            for name in enemy :
                if (enemy[name][0][0]-xm) ==   bullet_x  and (enemy[name][0][1]-ym == bullet_y):
                    enemy[name][1] -=50
                    

        else:
            # Dessiner la balle à sa nouvelle position
            bullet_display(bullet_x, bullet_y)

def check_right(enemies):#l'enemi regare si il voit le joueur sans obstacles les séparant
    global enemy
    global xm, ym
    

    enemy_x = enemy[enemies][4][0]
    enemy_y = enemy[enemies][4][1]
    a = 1
    while not is_white_pixel_or_Black(enemy_x + a, enemy_y):
        if pyxel.pget(enemy_x + a-xm, enemy_y-ym) == 1:
            return True
        else:
            a += 1
    return False

def check_left(enemies):#l'enemi regare si il voit le joueur sans obstacles les séparant
    global enemy
    global xm, ym
    

    enemy_x = enemy[enemies][4][0]
    enemy_y = enemy[enemies][4][1]
    a = 1
    while not is_white_pixel_or_Black(enemy_x - a, enemy_y):
        if pyxel.pget(enemy_x - a-xm, enemy_y-ym) == 1:
            return True
        else:
            a += 1
    return False

def check_up(enemies):#l'enemi regare si il voit le joueur sans obstacles les séparant
    global enemy
    global xm, ym
     

    enemy_x = enemy[enemies][4][0]
    enemy_y = enemy[enemies][4][1]
    a = 1
    while not is_white_pixel_or_Black(enemy_x, enemy_y - a):
        if pyxel.pget(enemy_x-xm, enemy_y - a-ym) == 1:
            return True
        else:
            a += 1
        
    return False

def check_down(enemies):#l'enemi regare si il voit le joueur sans obstacles les séparant
    global enemy
    global xm, ym
    
    
    enemy_x = enemy[enemies][4][0]
    enemy_y = enemy[enemies][4][1]
    a = 1
    while not is_white_pixel_or_Black(enemy_x, enemy_y + a):
        if pyxel.pget(enemy_x-xm, enemy_y + a-ym) == 1:
            return True
        else:
            a += 1
    return False
        


def shoot_at_player():#fonction qui permet a l'enemi de tirer vers le joueur
    global x, y,xm,ym
    global enemy
    global player
    global shootCooldown

    if shootCooldown > 0:#regarde si cooldown entre chaque tir enemi est fini
        shootCooldown -= 1 #le diminue de 1
    for enemies in enemy:
        if enemyAlive(enemies):
            enemy_bullet_x , enemy_bullet_y =  enemy[enemies][3][0]-xm,enemy[enemies][3][1]-ym 
            enemy_x, enemy_y = enemy[enemies][4]

            if shootCooldown == 0:
                if enemy[enemies][2] == False:
                    
                    enemy[enemies][3][0] , enemy[enemies][3][1] = enemy_x, enemy_y  #si le cooldown est égal a 0 est que le tir n'est pas en cour on réinitialise la balle
                
                


            # Vérifier les différentes directions
            if check_down(enemies)  : #on vérifie la direction du tir
                enemy[enemies][8 ] = True
                

            elif check_up(enemies) :
                enemy[enemies][9 ] = True
                
            elif check_right(enemies) :
                enemy[enemies][11 ] = True
                
            elif check_left(enemies) :
                enemy[enemies][10 ] = True
                
            else:
                enemy[enemies][2] = False
            
            if enemy[enemies][8 ]  : #on fait avancer la balle dans la bonne direction
                enemy_bullet_y += 1
                enemy[enemies][2] = True         
                enemy[enemies][3][1] +=1


            if enemy[enemies][9 ]  :
                enemy_bullet_y -= 1
                enemy[enemies][2] = True
                enemy[enemies][3][1] -=1   



            if enemy[enemies][10 ]  :
                enemy_bullet_x -= 1
                enemy[enemies][2] = True
                enemy[enemies][3][0] -=1


            if enemy[enemies][11 ]  :
                enemy_bullet_x += 1
                enemy[enemies][2] = True
                enemy[enemies][3][0] +=1
            


            if enemy[enemies][2] == True:
                
                if is_white_pixel_or_Black(enemy_bullet_x + xm, enemy_bullet_y + ym): #si la  balle est bloqué
                    
                    # Arrêter le tir
                    
                    enemy[enemies][8 ] =False
                    enemy[enemies][9 ] =False
                    enemy[enemies][10 ] =False
                    enemy[enemies][11] =False
                    enemy[enemies][2] = False
                elif pyxel.pget(enemy_bullet_x, enemy_bullet_y) == 1:
                    player[2] -=100
                    enemy[enemies][2] = False
                else:
                    # Dessiner la balle à sa nouvelle position
                    bullet_display(enemy_bullet_x, enemy_bullet_y)
                    shootCooldown = 45 #remettre le cooldown a sa valeur initiale


def create_grid(): #on crée une liste contenant les mur de la carte 
    # Charger l'image de la carte
    map_image = Image.open("fond2.png")  

    # Convertir l'image en mode "1" (noir et blanc) pour faciliter le traitement
    map_bw = map_image.convert("1")

    # Créer une grille à partir de l'image
    grid = []
    width, height = map_image.size  # Obtenir les dimensions de l'image
    for y in range(height):
        row = [1 if map_bw.getpixel((x, y)) < 255 else 0 for x in range(width)]
        grid.append(row)

    return grid

def heuristic(point1, point2):
    
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def astar(start, end, grid):
    # Initialiser les structures de données
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[tuple(start)] = None
    cost_so_far[tuple(start)] = 0

    while not frontier.empty():
        current = frontier.get()
        current = tuple(current)

        if current == end:
            break

        for next in neighbors(current, grid):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(end, next)
                frontier.put(next, priority)
                came_from[tuple(next)] = tuple(current)

    # Reconstruire le chemin à partir de came_from
    current = end
    current = tuple(current)
    path = []
    while current != tuple(start):
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()

    return path

def neighbors(cell, grid):
    x, y = cell
    width, height = len(grid[0]), len(grid)
    neighbors = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] == 0:
            neighbors.append((nx, ny))
    return neighbors






      
        
def rotate():#fonction qui fait avancer les enmi juqu'a leur point de rotation
    global enemy
    global xm, ym
    global goToBSITE,goToASite  
    for enemy_name in enemy:
        
        if goToBSITE:
            if enemyAlive(enemy_name):
                
                # Si l'ennemi est au milieu ou à A, trouver un chemin jusqu'au point de rotation B
                if enemy[enemy_name][5] == "Mid" or enemy[enemy_name][5] == "A": 
                    enemy_x, enemy_y = enemy[enemy_name][4]
                    if enemy[enemy_name][5] == "Mid":
                        pathB = enemy[enemy_name][12] 
                    else :
                        pathB = enemy[enemy_name][12] 

                        
                    if len(pathB) > 1:
                        if len(pathB) > 2:
                            next_step = pathB[1]  # Prochaine étape du chemin
                            
                            
                            enemy[enemy_name][4] = (next_step[0], next_step[1])  # Met à jour les coordonnées de l'ennemi

                        # Supprime la première étape du chemin sid l'ennemi l'a atteinte
                        if (enemy_x, enemy_y) == pathB[1]:
                            pathB.pop(1)
        
        if goToASite:
            if enemyAlive(enemy_name):
                
                # Si l'ennemi est au milieu ou à A, trouver un chemin jusqu'au point de rotation B
                if enemy[enemy_name][5] == "Mid" or enemy[enemy_name][5] == "B": 
                    enemy_x, enemy_y = enemy[enemy_name][4]
                    if len(enemy[enemy_name]) == 13:
                        path = enemy[enemy_name][12]  # Chemin de cet ennemi
                    else :
                        path = enemy[enemy_name][13]
                    if len(path) > 1:
                        if len(path) > 2:
                            next_step = path[1]  # Prochaine étape du chemin
                            
                            
                            enemy[enemy_name][4] = (next_step[0], next_step[1])  # Met à jour les coordonnées de l'ennemi

                        # Supprime la première étape du chemin sid l'ennemi l'a atteinte
                        if (enemy_x, enemy_y) == path[1]:
                            path.pop(1)

    

        
        
             
                


def buttonPressed(x_min,y_min, x_max, y_max)       : #fonction qui permet de savoir si le joueur a cliqué dans une certaine partie de l'ecran
    mouse_x = pyxel.mouse_x
    mouse_y = pyxel.mouse_y
    if (x_min < mouse_x < x_max) and  (y_min < mouse_y < y_max) and pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) :
        return True
 

                
        
            
def enemyAlive(enemies):#défini si l'enemi est en vie
    global enemy
    if enemy[enemies][1]  > 0 :
            return True
    else : 
        
        return False
            

def is_spike_carried(): #fonction qui permet de ramasser le spike si on est a coté et que l'on presse G
    global x,y
    global spike_x , spike_y
    global spike_display
    if (abs(spike_x -x) <= 3 ) and (abs(spike_y -y) <= 3 ):
        
        if pyxel.btnp(pyxel.KEY_G):
            spike_display = False
            return spike_display

def spike_plant():#fonction qui permet de planter le spike si on est dans la zone de plant d'un des site et que l'on apui sur r
    global x,y 
    global spike_x,spike_y
    global B_plant,A_plant
    global is_spike_planted
    if ((B_plant[0][0] < x < B_plant[1][0]) and (B_plant[0][1] < y < B_plant[1][1])) or ((A_plant[0][0] < x < A_plant[1][0]) and (A_plant[0][1] < y < A_plant[1][1])):
        if pyxel.btnp(pyxel.KEY_R):
            spike_x , spike_y  = x+1,y
            is_spike_planted = True
    

def spike_timing(): #timer jusqu'a l'explosion du spike
    global spikeTiming
    global is_spike_planted
    global win
    if is_spike_planted :
        if spikeTiming > 0:
            if spikeTiming > 300:
                if spikeTiming%30 == 0 :
                    pyxel.sound(0).speed = 11
                    pyxel.play(0, 0)
                    
            elif   spikeTiming > 153 :
                if spikeTiming%15 == 0 :
                    pyxel.sound(0).speed = 11
                    pyxel.play(0, 0)
                    
            elif spikeTiming >0:
                if spikeTiming%8 == 0 :
                    pyxel.sound(0).speed = 11
                    pyxel.play(0, 0)
                    
            spikeTiming -=1
        

        if spikeTiming == 0 :
            
            win = True #on gagne si il explose
            pyxel.sound(1).speed = 11
            pyxel.play(0, 1)
    
def spikeDefuse(): #fonction qui permet qu enemi de désamorcer le spike
    global defuseTimer 
    global GameOVER
    defuseTimer -=1
    if defuseTimer <=0:
        GameOVER = True
def chooseEnemy(): #choisi un enemi pour désamorcer le spike
    global enemyChoosen
    global isEnemyChoosen
    global spike_x,spike_y
    global enemy
    global defusePath
    enemyChoosen = random.randint(1,5)
    defusePath = astar(enemy[f"enemi {enemyChoosen}"][4], [spike_x,spike_y-1 ], create_grid()) #choisi le chemin que l'enemi va prendre
    
    isEnemyChoosen = True

def defend(): #fonction qui envoi l'enemi désamorcer si le spike est planté
    global enemy
    global is_spike_planted
    global isEnemyChoosen , enemyChoosen
    global defusePath
    global defuseTimer 
    if is_spike_planted and not isEnemyChoosen:
        chooseEnemy()
    if isEnemyChoosen :
        if enemy[f"enemi {enemyChoosen}"][1] <= 0: #on rechoisi si l'enemi est tué
            chooseEnemy()
            defuseTimer == 150
        if is_spike_planted :
                if len (defusePath  )>0:
                    enemy[f"enemi {enemyChoosen}"][4] = defusePath[0]
                    defusePath.pop(0)
                else:
                    spikeDefuse()
                    pyxel.sound(2).speed = 11
                    pyxel.play(0, 2)

def AllEnemyDead():#regarde si tout les énemis sont mort pour nous atribuer la victoire
    global enemy
    global GameOVER
    dead = []
    for enemies in enemy :
        if not enemyAlive(enemies):
            dead.append(enemies)
    if len(dead) == 5:
        win = True


### Initialisation du jeu

spikeTiming = 600 #définit le temps que met le spike a exploser
win = False #la victiore est fausse au lancement 
B_plant = [(16,28),(52,65)] #les coordonées des zones plant
A_plant = [(206,46),(247,71)]
spike_display = True #affiche ou non le spie
is_spike_planted = False #si le spike est planté ou non
spike_x  = 96 #coordonées du spike
spike_y =  224
x = 88 #coordonées du joueur
y =240
hp = 100 #pdv du joueur
player = [x,y,hp] #informations du joueur
xm = x- TAILLE//2 #déca lages de l'afichage pour que la "camera" suive le joueur
ym = y- TAILLE//2           


bullet_x = x-xm #coordonées de la balle
bullet_y = y-ym
gameLaunched = False #si le jeux est lancé ou non
GameOVER = False #si la partie est perdu
is_dashing = False #si le joueur dash
dash_cooldown = 0 #cooldown du dash
is_shooting = False #si le joeur tir
direct = "none" #direction du tir


goToBSITE = False #si le joueur va en a ou en B
goToASite = False

possibleSpawnPointsA = [[240,39],[188,87],[229,106],[232,88]] #points de spawn possible

possibleSpawnPointsB = [[33,71],[86,52],[73,22]]

possibleSpawnPointsMid = [[148,105],[130,99],[127,59]]


enemy = {} #dictionaire des info des enemis
a =1  #variable quelquonque utilisé pour conter a un endroit
enemy_shoot_down = False #est ce que l'enemi tire
defuseTimer = 150 #temps pour désamorcer
enemyChoosen = None #quel entmi est choisi
isEnemyChoosen = False#est ce que l'enemi est choisi
defusePath = None #chemin de désamorçage
shootCooldown = 45 #cooldown du tir enemis
create_enemy()#crée les enemi a l'initialisation

def load():#fonction qui recharge le jeux pour quand on relance la partie
    global bullet_x,bullet_y ,  gameLaunched, GameOVER, is_dashing, dash_cooldown, is_shooting, direct ,hp, goToASite, goToBSITE,possibleSpawnPointsA,  possibleSpawnPointsB, possibleSpawnPointsMid, enemy , a,spikeTiming,win,A_plant, B_plant,spike_x,spike_y, spike_display,is_spike_planted,player, x,y,xm,ym, enemy_shoot_down, defuseTimer, enemyChoosen,isEnemyChoosen, defusePath,shootCooldown
    ### Décrire ici vos règles du jeu
    spikeTiming = 600
    win = False
    B_plant = [(16,28),(52,65)]
    A_plant = [(206,46),(247,71)]
    spike_display = True
    is_spike_planted = False
    spike_x  = 96
    spike_y =  224
    x = 88
    y =240
    hp = 100
    player = [x,y,hp]
    xm = x- TAILLE//2
    ym = y- TAILLE//2
    
    
    bullet_x = x-xm
    bullet_y = y-ym

    gameLaunched = False
    GameOVER = False
    is_dashing = False
    dash_cooldown = 0
    is_shooting = False
    direct = "none"
    

    goToBSITE = False
    goToASite = False

    possibleSpawnPointsA = [[240,39],[188,87],[229,106],[232,88]]

    possibleSpawnPointsB = [[33,71],[86,52],[73,22]]

    possibleSpawnPointsMid = [[148,105],[130,99],[127,59]]

    enemy = {}
    a =1 
    enemy_shoot_down = False
    defuseTimer = 150
    enemyChoosen = None
    isEnemyChoosen = False
    defusePath = None
    shootCooldown = 45
    create_enemy()




def update():
    """ fonction qui est exécutée à chaque "frame" et qui
    doit contenir tout ce qui se met à jour à chaque "instant".
    Elle a des variables globales, autant qu'il vous en faut."""
    global gameLaunched
    global GameOVER
    global win
    global enemy_shoot_down
    global enemy
    global x, y,xm,ym,dash_cooldown
    if gameLaunched  and not GameOVER and not win: #quand la partie est lancée
        # déplacement du joueur
        
        x, y, xm , ym  = deplacement(x, y,xm ,ym)
        #décrément le cooldown du dash
        if dash_cooldown >0:
            dash_cooldown-=1
        x,y,xm,ym = dash()

        #fonctions utiles
        detectSite()
        rotate()
        is_spike_carried()
        spike_plant()
        spike_timing()
        defend()
        AllEnemyDead()
        

    elif not gameLaunched and not GameOVER and not win: #menu de base
        
        if buttonPressed(16,24,47,39):
            gameLaunched = True
            
    elif GameOVER and not win :  #si on perd
        gameLaunched = False
        if pyxel.btnp(pyxel.KEY_SPACE) :
            GameOVER = False
            load()
    
    elif win :  #si on gagne
        gameLaunched = False
        if pyxel.btnp(pyxel.KEY_SPACE) :
            win = False
            load()
        

            




    
 
    
def draw():
    global GameOVER

    """ fonction qui contient tout ce qui est affichage du jeu.
    Elle est exécutée à chaque frame aussi."""
    
    global enemy
    global player
    global dash_cooldown

    global xm, ym,x,y 
    global spike_display
    global win
    if gameLaunched and not GameOVER and not win: 
        pyxel.cls(0)
        

        #met la map 
        
        pyxel.blt(0, 0, 0, xm, ym, pyxel.width, pyxel.height)


        # dessine le joueur aux coordonnées x, y si il est en vie
        if player[2] > 0:
            pyxel.pset(x-xm , y-ym,1)
        else:
            GameOVER = True
            
        #dessine les enemi
        for enemies in enemy:
            
            if is_path_clear(x, y, enemy[enemies][4][0], enemy[enemies][4][1]) and enemyAlive(enemies):

                enemies_display(enemies)
                

        #dessine le tir
        shoot()
        # dessine le spike 
        if spike_display  or is_spike_planted:
            pyxel.pset(spike_x-xm, spike_y -ym ,10 )
            
            
        
            

            
        #dessine le curseur
        pyxel.mouse(True)
        
        #dessine le tir enemi
        shoot_at_player()
        #dessine l'icone du dash 
        if  dash_cooldown == 0 :
            pyxel.blt(25,48,1,0,0,16,16,colkey=0)
        else :
            pyxel.blt(25,48,1,16,0,32,16,colkey=0)

        

    elif not gameLaunched and not GameOVER  and not win: #ecran de base
        pyxel.blt(0,0,2,0,0,64,64)
        pyxel.mouse(True)
    elif GameOVER and not win :#ecran de mort
        
        
        pyxel.blt(0,0,2,64,0,128,64)
        pyxel.text(16, 30, "GAME OVER", 7)
    elif  win :#ecran de victoire
         
        pyxel.blt(0,0,2,64,0,128,64)
        pyxel.text(27, 30, "WIN", 7)
     
        

    






    
    
### Lancement du jeu

pyxel.run(update, draw)