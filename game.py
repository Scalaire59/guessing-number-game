import random


print("                                                                           ,--.
  ,----..                    ,---,.  .--.--.    .--.--.      ,---,       ,--.'|
 /   /   \           ,--,  ,'  .' | /  /    '. /  /    '. ,`--.' |   ,--,:  : |
|   :     :        ,'_ /|,---.'   ||  :  /`. /|  :  /`. / |   :  :,`--.'`|  ' :
.   |  ;. /   .--. |  | :|   |   .';  |  |--` ;  |  |--`  :   |  '|   :  :  | |
.   ; /--`  ,'_ /| :  . |:   :  |-,|  :  ;_   |  :  ;_    |   :  |:   |   \ | :
;   | ;  __ |  ' | |  . .:   |  ;/| \  \    `. \  \    `. '   '  ;|   : '  '; |
|   : |.' .'|  | ' |  | ||   :   .'  `----.   \ `----.   \|   |  |'   ' ;.    ;
.   | '_.' ::  | | :  ' ;|   |  |-,  __ \  \  | __ \  \  |'   :  ;|   | | \   |
'   ; : \  ||  ; ' |  | ''   :  ;/| /  /`--'  //  /`--'  /|   |  ''   : |  ; .'
'   | '/  .':  | : ;  ; ||   |    \'--'.     /'--'.     / '   :  ||   | '`--'  
|   :    /  '  :  `--'   \   :   .'  `--'---'   `--'---'  ;   |.' '   : |      
 \   \ .'   :  ,      .-./   | ,'                         '---'   ;   |.'      
  `---`      `--`----'   `----'                                   '---'        
  ,----..                                                                      
 /   /   \                                                                     
|   :     :                                                                    
.   |  ;. /                                                                    
.   ; /--`                                                                     
;   | ;  __                                                                    
|   : |.' .'                                                                   
.   | '_.' :                                                                   
'   ; : \  |                                                                   
'   | '/  .'                                                                   
|   :    /                                                                     
 \   \ .'                                                                      
  `---`                                                                        ")

INVITE = 'propose un nombre : '

QUITTER = -1
QUIT_TXT = 'q'
QUIT_MSG = 'Merci pour tout !'
QUIT_COMFIRMER = 'Es-tu sur de vouloir quitter (oui/non) ?'

def confirmer_quitter():
    confi = input(QUIT_COMFIRMER)
    return confi.lower() == 'oui'

def jouer_tour():
    nbr_secret = random.randint(1,100)
    nbr_saisies = 0
    while True:
        nbr_joueur = input(INVITE)
        if nbr_joueur == QUIT_TXT:
            if confirmer_quitter():
                return QUITTER
            else:
                continue
        nbr_saisies += 1
        if nbr_secret == int(nbr_joueur):
            print('Correct !')
            return nbr_saisies
        elif nbr_secret > int(nbr_joueur):
            print('Trop Petit')
        else:
            print('Trop Grand')

total_tours = 0
total_saisies = 0

for loop in range(999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
    total_tours += 1
    print('On passe au tour ' + str(total_tours))
    print('En avant pour les devinettes !')
    
    ce_tour = jouer_tour()
    
    if ce_tour == QUITTER:
        total_tours -= 1
        break
    
    total_saisies += ce_tour
    
    if total_tours == 1:
        msg_stat = "1er tour pas fini ! Tu veux recommencer ?"
    else:
        moy = total_saisies / total_tours
        msg_stat = 'Tu as fait ' + str(total_tours) + ' tours. Moyenne de ' + str(moy)
    
        print("Tu as fait " + str(ce_tour) + " saisies.")
        print("Ta moyenne de saisies/tours = " + str(moy))
        print("")
        print(QUIT_MSG)
        print(msg_stat)
