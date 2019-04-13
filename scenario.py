# -*- coding: utf-8 -*-

import pygame
import __main__
import avatar
import ennemis
import collision

from couleur import ROUGE,CHAIR,MARRON_FONCE,VERT,JAUNE_FONCE,KAKI,VERT_FONCE,BLEU,NOIR,BLANC,BLEU_CIEL,BEIGE,JAUNE,GRIS,ORANGE,MARRON,ARDOISE

def init(surf):
    '''Initialise le scenario.
    Arguments:
        surf: dict
    Retour:
        dict.
    '''
    att={}
    
    image_fond = pygame.image.load_basic('temple.bmp')
    att['img'] = image_fond
    
    att['surface'] = surf

    rect1 = (130, 580, 170, 10)
    rect2 = (400, 470, 170, 10)
    rect3 = (670, 370, 170, 10)
    rect4 = (940, 270, 170, 10)
    rect5 = (650, 170, 170, 10)
    rect6 = (250, 170, 230, 10)
    plateformes = [rect1,rect2,rect3,rect4,rect5,rect6]
    att['pforms'] = plateformes
    
    triangle1 = ((260,150),(270,132),(280,150))
    triangle2 = ((260,139),(270,157),(280,139))
    objectif_part1 = [triangle1,triangle2]
    rond = ((270,146))
    objectif = objectif_part1 + [rond]
    att['obj'] = objectif

    att['ennemis'] = ennemis.init(5)
    
    pos_x = 50
    pos_y = 615
    pos = [pos_x, pos_y]
    att['avatar'] = avatar.init(pos)

    att['rect_plateformes'] = []
    r_p1 = [[135,580],[295,590]]
    r_p2 = [[405,470],[565,480]]
    r_p3 = [[675,370],[835,380]]
    r_p4 = [[945,270],[1105,280]]
    r_p5 = [[655,170],[815,180]]
    r_p6 = [[255,170],[475,180]]
    r_plateformes = [r_p1,r_p2,r_p3,r_p4,r_p5,r_p6]
    for u in range(len(plateformes)):
        att['rect_plateformes'] += [r_plateformes[u]]

    att['rect_obj'] = []
    r_o = [[260,150],[265,157]]
    att['rect_obj'] += r_o
    

    return att

def dessine(scenario, surface):
    '''Fonction principale du dessin.
    Arguments:
        scenario: dict
        surface: dict
    Retour:
        None
    '''

    dessine_plateformes(surface,scenario['pforms'])

    dessine_objectif(surface,scenario['obj'])

    ennemis.dessine(scenario['ennemis'],surface)

    avatar.dessine(scenario['avatar'],surface)

    
def dessine_une_plateforme(surface, rect1):
    '''Dessine la premiere plateforme.
    Arguments:
        surface: dict
        rect1: list(int)
    Retour:
        None.
    '''
    pygame.draw.rect(surface, ORANGE, rect1)
    

def dessine_plateformes(surface, plateformes):
    '''Dessine les autres plateformes.
    Arguments:
        surface: dict
        plateformes: list(float)
    Retour:
     None.
    '''
    
    for i in plateformes:
        pygame.draw.rect(surface, ORANGE, i)
    
def dessine_objectif(surface,objectif):
    '''Dessine l'objectif.
    Arguments:
        surface: dict
        objectif: list(list((int)).
    Retour:
        None
    '''
    pygame.draw.polygon(surface, GRIS, (objectif[0]))
    pygame.draw.polygon(surface, GRIS, objectif[1])
    pygame.draw.circle(surface, BLANC, objectif[2], 3)
    
def update(scen):
    '''Met a jour le scenario.
    Arguments:
        scen: dict
    Retour:
        None
    '''

    ennemis.update(scen['ennemis'])
    avatar.update(scen['avatar'],scen['ennemis']['col_ennemis'],scen['rect_plateformes'],scen['rect_obj'])

def get_rectangle_pforme(att,i):
    '''Retourne les coordonnées des coins haut gauche et bas droit de la i-ème platforme du scénario.
    Arguments:
     att:dict.
     i:int.
    Retour:
     list(list(int)).
    '''
    return att['rect_plateformes'][i]    

def get_rectangle_obj(att):
    '''Retourne les coordonnées du coin haut gauche et bas droit de l'objectif.
    Arguments:
     att:str.
    Retour:
     list(int).
    '''

    return att['rect_obj']
