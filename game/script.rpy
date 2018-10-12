# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define e = Character('Barnes', color="#1fe3d7")
define g = Character('Lux', color="#6eb0c9")
define m = Character('Moi', color="#ffff00")
define l = Character('Shauwn', color="#bdb755")
define a = Character('Sara', color="#e77354")
define d = Character('Doc', color="#8cc4f4")

transform droite:
    xalign 0.75
    yalign 0.90

transform gauche:
    xalign 0.20
    yalign 0.99

<<<<<<< HEAD
transform center:
    xalign 0.20
    yalign 0.99



=======
style fiche:
    color '#ed6309'
    bold True
>>>>>>> develop

# Le jeu commence ici
label start:

    scene bg street

    show lux gigling at gauche
    with moveinleft

    g "Bienvenue sur ......, je suis lux la {=fiche}speakerine{/color}."

    g "Je suis la narratrice mais aussi l'un des personnages de cette story !"


    menu:

        "coucou lux !":
            jump reponse1

        "Va te faire voir !":
            jump reponse2

label reponse1:

    g "Puisque nous en sommes aux présentations, je vais t'en apprendre un peu plus sur toi !"
    jump suite

label reponse2:

    g "toi d'abord !"
    jump suite

label suite:

    g "Tu es donc le personnage principal de cette histoire, tout tes choix influeront sur la fin !"

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

    g "Sache aussi que je t'enverrais des informations de temps en temps pour te permettre de comprendre certains termes et technos  !"
    g "Enfin bref tu verra bien, il est temps pour toi de commencer l'histoire, à + !"
    jump history

label history:  

    hide lux
    scene bg school
    with dissolve

    l "Reveille toi !"
    
    show geek smiling at droite
    with moveinright

    l "Il est temps de bouger, on a à faire !"

    show friend unhappy at gauche
    with moveinleft

    a "Vous avez entendu parler de cet évenement sur les nouvelles technologies ?"
    l "Oui, mais on n'a pas que ça à faire !"
    a "Et toi, qu'en pense tu ?"

    menu:

        "Bof, on a mieux à faire !":
            jump acte1

        "Si ça te fais plaisir !":
            jump acte1
        

label acte1:  

    hide geek
    hide friend
    scene bg laboratory
    with dissolve
    show lux gigling at gauche
    with moveinleft

    g "Je me permet une petite ellipse car l'histoire n'est pas encore ecrite, bonne chance !"

    hide lux
    show geek smiling at droite
    with moveinright

    l "Il est bugué ce robot, je ne vois pas quoi en faire !"

    show friend unhappy at gauche
    with moveinleft

    a "Et ne parlons meme pas de son design, c'est une catastrophe !"
    d "Le probleme c'est le public, je suis très mauvais communicant"
    l "Il va falloir choisir ou commencer, qu'en pense tu ?"

    menu:

        "Il faut s'occuper des problèmes techniques !":
            l "Bon choix, partons la dessus !"
            jump dev

        "Il faut le rendre présentable et plus ergonomique !":
            l "Bon choix, partons la dessus !"
            jump non

        "Il faut commencer pas seduire la communautée !":
            l "Bon choix, partons la dessus !"
            jump non


label non:    

    hide geek
    hide friend
    show lux gigling at gauche
    with moveinleft  

    g "Hum, cette partie de l'histoire ne sera pas ecrite pour la présentation. Mais je vous envoi sur la partie dev ^^ !"
    jump dev



label dev:    

    a "Excelent, nous allons donc nous attaquer à la techno en premier !"
   





    return
