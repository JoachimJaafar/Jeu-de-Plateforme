# -*- coding: utf-8 -*-

import pygame
import scenario
import ennemis
import avatar
import collision

from scenario import update
from couleur import ROUGE,CHAIR,VERT,JAUNE_FONCE,KAKI,VERT_FONCE,BLEU,MARRON_FONCE,NOIR,BLANC,BLEU_CIEL,BEIGE,JAUNE,GRIS,ORANGE,MARRON,ARDOISE,VIOLET,ROUGE,OR,PRUNE,ROSE,PUCE,ROUX,SABLE,GRIS,GRIS_ACIER,LIME,MENTHE,NOISETTE,ROUGE_SANG,SAFRE,TURQUOISE

def traite_evt(att):
    '''Traite des évenements.
    Arguments:
     att:dict.
    Retour:
     bool.
    '''
    for event in pygame.event.get() :
        if event.type == pygame.QUIT: 
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
            elif event.key == pygame.K_LEFT:
                att['avatar']['vit'][0] = -5
            elif event.key == pygame.K_RIGHT:
                att['avatar']['vit'][0] = 5        
            elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                posi = att['avatar']['pos'][1]
                if posi == 615 or posi == 495 or posi == 385 or posi ==  285 or posi == 185 or posi == 85:
                    att['avatar']['vit'][1] = -20
                    pygame.mixer.music.load('saut.wav')
                    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
                    pygame.mixer.music.play()
                else:
                    k = 0
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and att['avatar']['vit'][0] < 0:
                att['avatar']['vit'][0] = 0
            if event.key == pygame.K_RIGHT and att['avatar']['vit'][0] > 0:
                att['avatar']['vit'][0] = 0

        if att['avatar']['play'] == False:
            return False
        
    return True



def main():
    '''Fonction principale.
    Arguments:
        None
    Retour:
        None
    '''
    
    pygame.init()
    horloge=pygame.time.Clock()
    L = 1200
    H = 700
    surface = pygame.display.set_mode((L,H))
    scen=scenario.init(surface)
    image_fond = pygame.image.load_basic('temple.bmp')
    image_fond.convert
    pygame.display.set_caption('Sutikku Man No Bōken') 
    terminer = False
    while not terminer :
        if traite_evt(scen) == False:
            terminer = True
        surface.blit(image_fond,[0,0])
        scenario.update(scen)
        scenario.dessine(scen,surface)
        pygame.display.update()
        horloge.tick(100)
    pygame.quit()
    
if __name__=='__main__':
    main()
