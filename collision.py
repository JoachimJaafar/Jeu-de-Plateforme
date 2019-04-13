def collision_rects(r1,r2):
    '''Retourne True si r1 et r2 se superposent et False sinon.
    Arguments:
     r1:list(list(int)).
     r2:list(list(int)).
    Retour:
     bool.
    '''
    a1 = r1[0][0]
    b1 = r1[0][0]
    c1 = r1[0][1]
    d1 = r1[0][1]
    a2 = r2[1][0]
    b2 = r2[1][1]
    c2 = r2[1][0]
    d2 = r2[1][1]
    [[a1,b1],[c1,d1]] = r1 #new
    [[a2,b2],[c2,d2]] = r2 #new
    
    if a2 <= a1 and a1 <= c2:
        if (b1 <= b2 and b2 <= d1) or (b2 <= b1 and b1 <= d2):
            return True
    elif a1 <= a2 and a2 <= c1:
        if (b2 <= b1 and b1 <= d2) or (b1 <= b2 and b2 <= d1):
            return True
    return False
    
            
        

    
    
    
    
