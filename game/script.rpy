﻿# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define e = Character('Barnes', color="#1fe3d7")
define g = Character('Lux', color="#6eb0c9")
define m = Character('[name!t]', color="#339933")
define l = Character('Shawn', color="#bdb755")
define a = Character('Sara', color="#e77354")
define d = Character('Doc Tanaka', color="#8cc4f4")
define s = Character('Sphinx', color="#612b5a")
define n = Character('Robot', color="#979191")

image movie = Movie(size=(1220, 680), xpos=0, ypos=0, xanchor=0, yanchor=0)

transform droite:
    xalign 0.75
    yalign 0.90

transform left:
    xalign 0.8
    yalign 0.5

transform gauche:
    xalign 0.20
    yalign 0.99

transform middle:
    xalign 0.50
    yalign 0.90

style fiche:
    color '#ed6309'
    bold True

# Le jeu commence ici
label start:

  
    scene black
    with Pause(1)

    play movie "fondanime.ogv" loop
    show movie with dissolve

    show robot off at gauche

    n "Bienvenue sur JobStorie, je suis le robot {=fiche}narrateur{/color}."


    hide movie with dissolve
    stop movie

    show lux gigling at gauche
    
    

    g "Bienvenue sur JobStorie, je suis lux la {=fiche}narratrice{/color}."

    python:
        name = renpy.input(_("Quel est ton nom?"))

        name = name.strip() or __("personne")
 

    g "Bonjour [name!t] ! Je suis la narratrice mais aussi l'un des personnages de cette story !"

    hide screen notif

    menu:

        "Coucou lux !":
            jump reponse1

        "Ou sommes nous !":
            jump reponse2

label reponse1:

    g "Puisque nous en sommes aux présentations, laisse moi t'expliquer ce que tu fais la !"
    jump suite

label reponse2:

    g "Dans une visual novel qui te mènera peut-etre vers ton avenir !"
    jump suite

label suite:


    g "Tu es le personnage principal de cette histoire, tout tes choix influeront sur la fin !"

    menu:

        "Et concretement je dois faire quoi ?":
            jump reponse3

        "J'ai toujours su que j'étais un héros":
            jump reponse4

        "Je veux juste rentrer chez moi !":
            jump reponse5

        "Et sinon, tu finis à quelle heure ?":
            jump reponse6

label reponse3:

    g "Terminer l'histoire en agissant comme tu le sens !"
    jump suite2

label reponse4:

    g "Hum, oui tout à fait !"
    jump suite2


label reponse5:

    g "On a pas ecrit toute une story pour que tu rentre chez toi !"
    jump suite2

label reponse6:     

    g "..."
    jump suite2

label suite2:

<<<<<<< HEAD
    g "Sache aussi que je t'enverrais des informations de temps en temps pour te permettre de comprendre certains termes et technos !"
   
=======
    g "Sache aussi que je t'enverrais des informations de temps en temps."
    g "Pour te permettre de comprendre certains termes et technos."
>>>>>>> develop
    show screen notif(None, None, True)
    g "Enfin bref tu verra bien, il est temps pour toi de commencer l'histoire, à plus !"
    hide screen notif
    jump history

label history:  

    hide lux
    scene bg school
    with dissolve

    l "Reveille toi !"
    
    show geek smiling at droite
    with moveinright

    l "Il est temps de bouger, on a à faire !"

    show friend happy at gauche
   
    with moveinleft

    a "Vous avez entendu parler de cet évenement sur les nouvelles technologies ?"
<<<<<<< HEAD
    show geek bulle at droite
=======
    show geek hitting at droite
>>>>>>> develop
    l "Le doc nous a appellé, il faut y aller !"
    show screen notif(1, None, False)
    a "Et toi, que veut tu faire ?"
    

    menu:

        "Bof, on a mieux à faire !":
            show friend unhappy at gauche
            a "Tant pis"
            jump acte1

        "Si ça te fais plaisir !":
            a "Allons y"
            jump acte1


        

label acte1:  

    hide geek
    hide friend
    
   

    
    with moveinleft

    g "Je me permet une petite ellipse car l'histoire n'est pas encore ecrite, bonne chance !"

    hide lux
    show geek smiling at droite
    with moveinright

    l "Il est buggé ce robot, je ne vois pas quoi en faire !"

    show friend happy at gauche
    with moveinleft
    

    a "Et ne parlons meme pas de son design, c'est une catastrophe !"

    show doc talking at middle
    with moveinleft
    
    d "Le probleme c'est le public, je suis très mauvais communicant"
    show screen notif(4, None, False)
    show geek think at droite


    

    l "Il va bien falloir commencer par quelque chose, qu'en pense tu ?"

    menu:
    

        "Il faut s'occuper des problèmes techniques !":
            l "Bon choix, partons la dessus !"
            $ dev = True 
            jump dev

        "Il faut le rendre présentable et plus ergonomique !":
            a "Bon choix, partons la dessus !"
            $ design = True 
            jump non

        "Il faut commencer par seduire la communauté !":
            d "Bon choix, partons la dessus !"
            $ market = True 
            jump non

    


label non:    

    hide geek
    hide friend
    hide doc
    show lux gigling at gauche
    with moveinleft  

    g "Hum, cette partie de l'histoire ne sera pas ecrite pour la présentation. Mais je vous envoi sur la partie dev ^^ !"
    show screen notif(3, None, False)
    jump dev



label dev:    

    hide lux
    show geek think at droite
    show friend unhappy at gauche
    show doc talking at middle

    a "Excelent, nous allons donc nous attaquer à la techno en premier !"
    d "Mais la encore, nous avons des choix à faire, j'ai fais une liste de ses principaux disfonctionnements"
    show friend reading at gauche
    a "Je vais la lire : - Le modèle NOA a une memoire defectueuse et s'exprime comme un enfant de 5 ans"
    a "- Incapable d'evoluer dans son environnement, il se cogne à tout les meubles"
    a "- L'heure, les coordonnées GPS et satellitaires sont defaillants"

    menu:

        "Il faut commencer par la mémoire !":          
            jump conf

        "Le déplacement me semble primordial !":        
            jump conf

        "L'heure et les coordonnées bien sur !":
            jump conf

label conf: 

    l "Tres bien, mais comment fais on, on y connait rien ?"
    show friend happy at gauche
    a "La conférence !!!"
    l "J'imagine que ca vaut le coup d'essayer "

    hide geek
    hide friend
    scene bg conf
    with dissolve

    l "......"
    a "Euh, ca fait un peu cossu pour une conference sur la technologie !"

    show sphinx asking at middle
    with moveintop
    s "De quoi parlez vous,il n'y a rien d'anormal ici !"
    l "Si vous, pour commencer ! c'est du cosplay ? "
    s "Non, je suis le sphinx, et vous devez répondre à ma question pour passer"
    s "Vous allez devoir choisir une des trois conférences"

    menu:

        "La conference sur les bases de données (memoire) !":  
            a "Allons y"      
            jump retour_memoire

        "La conference sur les divers language de programmation (deplacement) !":     
            a "Allons y"
            jump retour_deplacement


label retour_memoire:           
  

    scene bg laboratory
    with dissolve 
    hide sphinx
    show geek smiling at droite
    show friend unhappy at gauche
    show doc talking at middle
    l "Bon, nous sommes de retour, montrez nous le probleme de BDD !"
    d "Comme vous le voyez , notre robot à un 'léger' soucis de communication avec l'espèce humaine."    
    d "Je ne comprends pas ce qu'il se passe au niveau de sa base de données... Je pense que vous devriez y jeter un coup d'oeil."
    m "Je me connecte"
    m "Ca ne marche pas ! Je n'ai pas les droits pour me connecter ! "
    d "Tu as mal tapé le mot de passe que je t'ai envoyé ! "
    m "je retape le mot de passe a{w=0.4}z{w=0.4}e{w=0.4}r{w=0.4}t{w=0.4}y{w=0.4}1{w=0.4}2{w=0.4}3{w=0.4}4{w=0.4}5{w=0.4}6"
    n "Access Granted, Welcome Aboard !"
    d "Ah ! Ca y est ça marche !"
    n "Bonjour et bienvenue, Je suis N.O.A ."
    a "Il s'exprime mieux la ? "
    d "Ton manque de foi me consterne."
    a "Bon, réglons aussi ce probleme d'horaire dans la foulée, ca pourrait servir !"

    jump retour_date
   

label retour_deplacement:


    scene bg laboratory
    with dissolve
    hide sphinx
    show geek smiling at droite
    show friend unhappy at gauche
    show doc talking at middle  
    l "Bon, nous sommes de retour, montrez nous le probleme de deplacement !"   
    d "les capteurs de N.O.A sont défectueux ! Il ne peut pas se déplacer sans casser tout ou passer à travers un mur !"
    a "Vous êtes sérieux ? Mais qu'est ce que c'est que ce robot ?"
    d "Je crois que j'ai fait une erreur en copiant-codant trouvé sur internet"
    l "Copier illegalement c'est mal !"
    d "Je sais , j'aurais du coder moi même ! "
    m "Je m'y connecte "
    m "Euh ? mais ca a été codé avec les pieds !"
    l "Bon , corrigeons ça, je vais le recoder ! "
    a "Comme l'a dit je sais plus qui : Lève toi ! Et trace ta route ! "
    d "Euh ? Tu es vraiment sûr de ta citation ?"
    m "Bon, essayons maintenant"
    d "Il se déplace correctement, c'est un miracle ! Merci mon dieu ! "
    a "Bon, réglons aussi ce probleme d'horaire dans la foulée, ca pourrait servir !"

    jump retour_date


   

label retour_date:


    scene bg laboratory
    with dissolve
    hide sphinx
    show geek smiling at droite
    show friend unhappy at gauche
    show doc talking at middle 
    l "Bon, voyons cela, N.O.A quelle heure est-il ? "   
    n "Il est 36H66 !"
    a "Hein ? Mais qu'est ce qu'il dit ?"
    d "On dirait bien que la synchronysation avec le serveur n'est pas bonne ! Nous allons régler le soucis rapidement. "
    m "Oui pas de problème !"
    d "Regarde ! Je te l'avais dit ! L'heure locale est différente de l'heure serveur ! Le problème vient de la ! "
    m "Je m'en occupe !"
    menu:

        "Je reconfigure l'heure locale du robot.":
            l "Super, il va nous servir de réveil pour demain !"  
            a "Oui, il ne faudrait pas rater la deuxieme journée de conference, ce robot a encore besoin de nous"        
            jump acte2  

        "Je reconfigure l'heure serveur.":    
            l "Super, il va nous servir de réveil pour demain !"  
            a "Oui, il ne faudrait pas rater la deuxieme journée de conference, ce robot a encore besoin de nous"    
            jump acte2retard    
                  

label acte2retard:


    hide geek
    hide friend
    scene bg conf
    with dissolve
    show sphinx asking at middle
    with moveinleft

    s "Vous etes arrivés en retard. Vous ne pourrez assistez qu'a une conférence !"
    l "C'est terrible, nous n'aurions pas du le configurer sur l'heure serveur, il nous a réveiller en retard"

    scene bg laboratory
    with dissolve
    hide sphinx
    show geek smiling at droite
    show friend unhappy at gauche
    show doc talking at middle 

    d "Alors ces conférences ? Tu as appris de nouvelles choses ? Ou c'était du genre barbant ?"
    l "Vraiment intéressant ! nous avons eu de nouvelles idées pour améliorer N.O.A !"
    a "Alors, que devons nous améliorer ?"
    m "Nous n'avons pu suivre qu'un seule conférence ! nous ne pouvons l'améliorer que dans un seul domaine"

    menu:

        "Il faut améliorer la communication !":
            $ communication = True 
            $ reflexion = True
            $ force = True      
            jump acte2com

        "Il faut améliorer sa réflexion !":
            $ communication = True 
            $ reflexion = True
            $ force = True  
            jump acte2ref

        "Il faut améliorer sa force !":
            $ communication = True 
            $ reflexion = True
            $ force = True 
            jump acte2force



label acte2: 

    hide geek
    hide friend
    scene bg conf
    with dissolve
    show sphinx asking at middle
    with moveinleft

    s "Vous etes revenus, et à l'heure. Vous pourrez assister à toutes les conférences, allez y !"

    scene bg laboratory
    with dissolve
    hide sphinx
    show geek smiling at droite
    show friend unhappy at gauche
    show doc talking at middle 

    d "Alors ces conférences ? Tu as appris de nouvelles choses ? Ou c'était du genre barbant ?"
    l "Vraiment intéressant ! nous avons eu de nouvelles idées pour améliorer N.O.A. !"
    a "Alors, que devons nous améliorer en premier ?"

    menu:

        "Il faut améliorer la communication !":      
            $ communication = True 
            $ reflexion = False
            $ force = False   
            jump acte2com

        "Il faut améliorer sa réflexion !":
            $ communication = False 
            $ reflexion = True
            $ force = False   
            jump acte2ref

        "Il faut améliorer sa force !":
            $ communication = False 
            $ reflexion = False
            $ force = True
            jump acte2force


label acte2com:   

    a "N.O.A est froid !"
    n "Mon CPU est actuellement à 75°C , je ne suis pas froid !"
    a "Froid dans ton approche ! Tu parles comme un robot ! Regarde  : \"C'est une bonne situation robot ?\" "
    n "Mais je suis un robot, je n'ai pas de situation ."
    d "Tu as raison ! Changeons ça , c'est vrai que ta façon de parler n'est pas des plus naturelle ! "
    l "il faut modifier dans la base de données le dictionnaire de mot employé par N.O.A !"
    a "et il sera capable de ressentir les émotions des humains avec qui il évolue !"
    n "Je me sens ... différent !"
    a "C'est normal ! Ca va être un peu déroutant pour toi ! Réponds à ma question : \"C'est une bonne situation robot ?\""
    n "Vous savez, moi je ne crois pas qu’il y ait de bonne ou de mauvaise situation......"
    d "Mon Dieu ! Qu'avons nous fait ? On a pas été un peu trop loin ? "
    l "Non ! c'est juste le temps qu'il s'habitue à ces nouvelles fonctions."
    a "Parfait, pouvons nous l'améliorer encore une fois ?"
    menu:

        "Il faut améliorer sa réflexion !" if reflexion == False : 
            $ reflexion = True       
            jump acte2ref

        "Il faut améliorer sa force !" if force == False :
            $ force = True
            jump acte2force
        
        "Je crois qu'on a fait tout notre possbile !" if force == True & communication == True & reflexion == True :
            jump end



label acte2force:

    l "Développons un peu sa force ! Ce sera un vrai super héros !"
    a "Ah, ca ne m'interesse pas, je reviendrais plus tard !"
    hide friend 
    with moveoutleft
    n "Je serais super N.O.A, je serais le meilleur au tennis ! "
    d "Ca sonne bien ! Tu te battras sans répit ? Tu feras tout pour être le meilleur ? Et tu gagneras les défis , parcourant la terre entière !"
    l "Branchons nous, il faut créer un exosquelette décuplant la force"
    m "Voila c'est fini ! Initialisation en cours ... "
    d "Je crois qu'on devrait l'habiller ! Il est vraiment trop ... Impressionnant !"
    show friend unhappy at gauche
    with moveinleft
    l "Attention , il se réveille ! Sara tu arrives au bon moment ! Le N.O.A. nouveau est arrivé ! "
    n "Sarah connor ?"
    d "Il s'énerve ! rebootez le vite !"
    l "C'est pas passer loin !"
    a "Serieusement ?"
    m "Ca devrait allez cette fois !"
    n "Désolé, un morceau de code de l'ancien propriétaire de cet exosquelette a corrompu mes fichiers !"
    n "Le système est à nouveau opérationnelle à 100/100 . Je pourrais aider le professeur dans ses taches au quotidien désormais."
    a "Parfait, pouvons nous l'améliorer encore une fois ?"
    menu:

        "Il faut améliorer sa communication !" if communication == False :
            $ communication = True        
            jump acte2com

        "Il faut améliorer sa reflexion !" if reflexion == False :
            $ reflexion = True
            jump acte2ref
        
        "Je crois qu'on a fait tout notre possbile !" if force == True & communication == True & reflexion == True :
            jump end


label acte2ref:    

    l "N.O.A n'est pas très malin, il est un peu long à apprendre. On devrait améliorer son système neuronal."   
    d "Il est encore jeune." 
    a "Un petit test s'impose ... N.O.A. ? Qu'est ce qui est petit et marron ?"
    n "Un marron ?"
    d "Il est fort ce robot !"
    l "Il n'est même pas connecté à l'Internet du web.... On doit ne le faire \"grandir\" !"
    n "Je ne suis pas sourd, je vous entends ..."
    m "je me connecte au réseau neuronal de N.O.A, et l'améliore pour qu'il soit plus performant. La vitesse d'apprentissage est décuplé."
    a "C'est fini ! Comment tu te sens ?"
    n "Je note aucune différence ... Ah si , attendez ... Mon cerveau a atteint 100/100 de ses capacités."
    m "Les smartphones se mettent tous à sonner !"
    n "Regardez vos téléphones !"
    d "\"Je suis partout\" .... N.O.A ? Est ce bien toi qui vient de faire ça ?"
    a "Parfait, pouvons nous l'améliorer encore une fois ?"
    menu:

        "Il faut améliorer sa communication !" if communication == False :
            $ communication = True        
            jump acte2com

        "Il faut améliorer sa force !" if force == False :
            $ force = True
            jump acte2force
        
        "Je crois qu'on a fait tout notre possbile !" if force == True & communication == True & reflexion == True :
            jump end


label end:

    hide geek
    hide friend
    hide doc
    show lux gigling at gauche
    with moveinleft
    g "Pas mal !"            
    g "Tes réponses m'ont menées a une conclusion"
    g "Tu devrais t'orienter vers le métiers de {=fiche1}Développeur de base de données{/color}"
 

    return
