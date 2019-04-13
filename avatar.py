# -*- coding: utf-8 -*-

import pygame
import __main__
import ennemis
import collision

from couleur import ROUGE,MARRON_FONCE,CHAIR,VERT,JAUNE_FONCE,KAKI,VERT_FONCE,BLEU,NOIR,BLANC,BLEU_CIEL,BEIGE,JAUNE,GRIS,ORANGE,MARRON,ARDOISE,VIOLET,ROUGE,OR,PRUNE,ROSE,PUCE,ROUX,SABLE,GRIS,GRIS_ACIER,LIME,MENTHE,NOISETTE,ROUGE_SANG,SAFRE,TURQUOISE

def init(pos):
    '''Initialise et retourne les attributs du personnage.
    Arguments:
        pos: dict.
    Retour:
        att: dict.
    '''
    
    pos_x = 50
    pos_y = 615
    pos = [pos_x, pos_y]
    vit_x = 0
    vit_y = 0
    dim_x = 30
    dim_y = 50
    
    img = 0
    
    att = {}
    att['dim'] = [dim_x, dim_y]
    att['vit'] = [vit_x, vit_y]
    att['pos'] = pos
    att['vivant'] = True
    att['play'] = True
    att['img'] = img
    
    att['grav'] = 1

    return att
    
def dessine(att, surface):
    '''Dessine le personnage.
    Arguments:
        att: dict
        surface: dict
    Retour:
        None
    '''
    pos_x = att['pos'][0]
    pos_y = att['pos'][1]
    img = att['img']
    pygame.draw.circle(surface, NOIR, (pos_x, pos_y), 15)
    pygame.draw.line(surface, NOIR, (pos_x, pos_y), (pos_x, pos_y+60))
    pygame.draw.line(surface, NOIR, (pos_x, pos_y+20), (pos_x-20, pos_y+40))
    pygame.draw.line(surface, NOIR, (pos_x, pos_y+20), (pos_x+20, pos_y+40))
    pygame.draw.ellipse(surface, CHAIR, [pos_x-15, pos_y-7, 30, 10])
    pygame.draw.line(surface, NOIR, (pos_x-8, pos_y-3), (pos_x-3, pos_y-1))
    pygame.draw.line(surface, NOIR, (pos_x+8, pos_y-3), (pos_x+3, pos_y-1))
    if img == 0:
        pygame.draw.line(surface, NOIR, (pos_x, pos_y+60), (pos_x-15, pos_y+85))
        pygame.draw.line(surface, NOIR, (pos_x, pos_y+60), (pos_x+15, pos_y+85))
    elif img == 1:
        pygame.draw.line(surface, NOIR, (pos_x, pos_y+60), (pos_x, pos_y+85))

def get_rectangle(att):
    '''Retourne un tuple de couples d'entiers contenant les sommets d'en haut à gauche et d'en bas à droite du rectangle d'approximation de l'avatar.
    Arguments:
     att:dict.
    Retour:
     list(list(int)).
    '''
    pos_x = att['pos'][0]
    pos_y = att['pos'][1]
    r_av = [[pos_x-20,pos_y-15],[pos_x+20,pos_y+85]]
    att['col_avatar'] = r_av
    return att['col_avatar']

    

def update(att,col_ennemis,rect_plateformes,rect_obj):
    '''Met à jour le scénario.
    Arguments:
     att:dict.
     col_ennemis:list(list(int)).
     rect_plateformes:list(list(int)).
     rect_obj:list(int).
    Retour:
     None.
    '''
    att['vit'][1] += att['grav']

    if att['vit'][0] != 0:
        if att['img'] == 0:
            att['img'] += 1
        else:
            att['img'] -= 1
            
    if (att['pos'][0] <= 20 and att['vit'][0] < 0) or (att['pos'][0] >= 1180 and att['vit'][0] > 0):
        att['img'] = 0
        
    att['pos'][0] += att['vit'][0]
    att['pos'][1] += att['vit'][1]

    posi = att['pos'][1]
    if not(att['vit'][1] >= 0 or att['vit'][0] == 0 and (att['vit'][1] >= 0 and posi != 615 and (posi != 495 or posi != 385 or posi !=  285 or posi != 185 or posi != 85))):
        att['img'] = 0
    if att['vit'][0] == 0:
        att['img'] = 0
        
    if att['pos'][1] >= 615:
        att['pos'][1] = 615

    if att['pos'][0] <= 20:
        att['pos'][0] = 20

    if att['pos'][0] >= 1180:
        att['pos'][0] = 1180

    a = 0
    b = 0
    c = 0
    for i in rect_plateformes:
        if collision.collision_rects(get_rectangle(att),i) == True and att['vit'][1] < 0:
            a += att['vit'][1]
            att['pos'][1] -= att['vit'][1]
            
        elif collision.collision_rects(get_rectangle(att),i) == True and att['vit'][1] > 0:
            att['vit'][1] = 0
            att['pos'][1] = i[0][1]-85
            
    b += att['pos'][1]+5
    if (att['pos'][0] > 130-15 and att['pos'][0] < 170-15) and (att['pos'][1] > 495 and att['pos'][1] < 604):
        att['pos'][0] = 130 - 16
        att['pos'][1] = b-15
        
    c += att['pos'][1]+5    
    if (att['pos'][0] < 300+15 and att['pos'][0] > 250+15) and (att['pos'][1] > 495 and att['pos'][1] < 604):
        att['pos'][0] = 300 + 16
        att['pos'][1] = c-15
        
    if (att['pos'][0] > 400-15 and att['pos'][0] < 450-15) and (att['pos'][1] > 385 and att['pos'][1] < 494):
        att['pos'][0] = 400 - 16
        att['pos'][1] = b-15

    if (att['pos'][0] < 570+15 and att['pos'][0] > 520+15) and (att['pos'][1] > 385 and att['pos'][1] < 494):
        att['pos'][0] = 570 + 16
        att['pos'][1] = c-15

    if (att['pos'][0] > 670-15 and att['pos'][0] < 720-15) and (att['pos'][1] > 285 and att['pos'][1] < 394):
        att['pos'][0] = 670 - 16
        att['pos'][1] = b-15

    if (att['pos'][0] < 740+15 and att['pos'][0] > 690+15) and (att['pos'][1] > 285 and att['pos'][1] < 394):
        att['pos'][0] = 740 + 16
        att['pos'][1] = c-15

    if (att['pos'][0] > 940-15 and att['pos'][0] < 990-15) and (att['pos'][1] > 185 and att['pos'][1] < 294):
        att['pos'][0] = 940 - 16
        att['pos'][1] = b-15

    if (att['pos'][0] < 1110+15 and att['pos'][0] > 1060+15) and (att['pos'][1] > 185 and att['pos'][1] < 294):
        att['pos'][0] = 1110 + 16
        att['pos'][1] = c-15

    if (att['pos'][0] > 650-15 and att['pos'][0] < 700-15) and (att['pos'][1] > 85 and att['pos'][1] < 194):
        att['pos'][0] = 650 - 16
        att['pos'][1] = b-15

    if (att['pos'][0] < 820+15 and att['pos'][0] > 780+15) and (att['pos'][1] > 85 and att['pos'][1] < 194):
        att['pos'][0] = 820 + 16
        att['pos'][1] = c-15

    if (att['pos'][0] > 250-15 and att['pos'][0] < 300-15) and (att['pos'][1] > 85 and att['pos'][1] < 194):
        att['pos'][0] = 250 - 16
        att['pos'][1] = b-15

    if (att['pos'][0] < 480+15 and att['pos'][0] > 530+15) and (att['pos'][1] > 85 and att['pos'][1] < 194):
        att['pos'][0] = 480 + 16
        att['pos'][1] = c-15

    if (att['pos'][0] < 290 and att['pos'][0] > 264) and (att['pos'][1] > 0 and att['pos'][1] < 200):
        att['img'] = 0 

    
    for j in col_ennemis:
        if collision.collision_rects(get_rectangle(att),j) == True:
            att['vivant'] = False
            pygame.mixer.music.load('mort.wav')
            pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
            pygame.mixer.music.play()
            att['pos'][0] = 50
            att['pos'][1] = 615

    if collision.collision_rects(get_rectangle(att),rect_obj):
        print('\nFELICITATIONS, vous etes maintenant un maitre ninja !')
        restart = input('Entrez "1" pour recommencer ou un autre chiffre pour quitter (2 fois) : ')
        quitter = False
        while not quitter:
            if restart == '1' or restart == 1:
                att['pos'][0] = 50
                att['pos'][1] = 615
                quitter = True
            else:
                att['play'] = False
                quitter = True
                
            
        
    

    
        
            
        
            
