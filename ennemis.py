# -*- coding: utf-8 -*-

import pygame
import __main__
import collision
import avatar
from couleur import ROUGE,MARRON_FONCE,VERT,CHAIR,JAUNE_FONCE,KAKI,VERT_FONCE,BLEU,NOIR,BLANC,BLEU_CIEL,BEIGE,JAUNE,GRIS,ORANGE,MARRON,ARDOISE,VIOLET,ROUGE,OR,PRUNE,ROSE,PUCE,ROUX,SABLE,GRIS,GRIS_ACIER,LIME,MENTHE,NOISETTE,ROUGE_SANG,SAFRE,TURQUOISE

def init(nombre):
    '''Initialise un dictionnaire d’attributs des ennemis et le retourne.
    Arguments:
     nombre:int.
    Retour:
     att:dict.
    '''
    att = {}
    
    att['vit'] = -8
    att['lim_x'] = -170

    att['dim_x'] = 0
    att['dim_y'] = 0

    att['objs_1'] = []
    rect1 = [900,660,30,8]
    rect2 = [330,550,30,8]
    rect3 = [622,424,30,8]
    rect4 = [1100,240,30,8]
    rect5 = [460,135,30,8]
    manches = [rect1,rect2,rect3,rect4,rect5]
    for i in range(nombre):
        att['objs_1'] += [manches[i]]

    att['objs_2'] = [] 
    triangle1 = [[900,660],[900,668],[860,664]]
    triangle2 = [[330,550],[330,558],[290,554]]
    triangle3 = [[622,424],[622,432],[582,428]]
    triangle4 = [[1100,240],[1100,248],[1060,244]]
    triangle5 = [[460,135],[460,143],[420,139]]
    lames = [triangle1,triangle2,triangle3,triangle4,triangle5]
    for j in range(nombre):
        att['objs_2'] += [lames[j]]

    att['objs_3'] = []
    start_ligne1 = [901,653]
    end_ligne1 = [901,675]
    start_ligne2 = [330,543]
    end_ligne2 = [330,565]
    start_ligne3 = [623,417]
    end_ligne3 = [623,439]
    start_ligne4 = [1101,233]
    end_ligne4 = [1101,255]
    start_ligne5 = [461,128]
    end_ligne5 = [461,150]
    ligne1 = [start_ligne1,end_ligne1]
    ligne2 = [start_ligne2,end_ligne2]
    ligne3 = [start_ligne3,end_ligne3]
    ligne4 = [start_ligne4,end_ligne4]
    ligne5 = [start_ligne5,end_ligne5]
    lignes = [ligne1,ligne2,ligne3,ligne4,ligne5]
    for k in range(nombre):
        att['objs_3'] += [lignes[k]]

    ennemis = []
    for m in range(5):
        ennemis += [manches[m],lames[m],lignes[m]]

    att['col_ennemis'] = []
    r_e1 = [[860,653],[930,675]]
    r_e2 = [[290,543],[360,565]]
    r_e3 = [[582,417],[652,439]]
    r_e4 = [[1060,233],[1130,255]]
    r_e5 = [[420,128],[490,150]]
    r_e = [r_e1, r_e2, r_e3, r_e4, r_e5]
    for l in range(nombre):
        att['col_ennemis'] += [r_e[l]]
    
    return att


def dessine(att,surface):
    '''Dessine tous les ennemis sur la surface aux positions données par ses attributs.
    Arguments:
     att:dict.
     surface:dict.
    Retour:
     None.
    '''
    for i in att['objs_1']:
        pygame.draw.rect(surface, MARRON_FONCE, i)

    for j in att['objs_2']:
        pygame.draw.polygon(surface, GRIS_ACIER, j)

    for k in att['objs_3']:
        pygame.draw.line(surface, MARRON_FONCE, k[0], k[1], 2)

def update(att):
    '''Met à jour le scénario.
    Arguments:
     att:dict.
    Retour:
     None.
    '''
    for i in range(5):
        att['objs_1'][i][0] += att['vit']
        if att['objs_1'][i][0] < att['lim_x']:
            att['objs_1'][i][0] = 1240
        for j in range(3):
            att['objs_2'][i][j][0] += att['vit']
            if att['objs_2'][i][1][0] < att['lim_x']:
                att['objs_2'][i][0][0] = 1240
                att['objs_2'][i][1][0] = 1240
                att['objs_2'][i][2][0] = 1200 
        for k in range(2):
            att['objs_3'][i][k][0] += att['vit']
            if att['objs_3'][i][k][0] < att['lim_x']:
                att['objs_3'][i][k][0] = 1240
    
        att['col_ennemis'][i][0][0] += att['vit']
        if att['col_ennemis'][i][0][0] < att['lim_x']:
            att['col_ennemis'][i][0][0] = 1240
    
        att['col_ennemis'][i][1][0] += att['vit']
        if att['col_ennemis'][i][1][0] < att['lim_x']:
            att['col_ennemis'][i][1][0] = 1240


    
    
    
    
    
