# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define e = Character('Eileen', color="#c8ffc8")
define g = Character('Shawn', color="#0000ff")
define m = Character('Moi', color="#ffff00")

# Le jeu commence ici
label start:

    e "Vous venez de créer un nouveau jeu Ren'Py."

    e "Après avoir ajouté une histoire, des images et de la musique, vous pourrez le présenter au monde entier !"
    
    g "Bonjour je suis Shawn !"

    menu:

        "coucou Shawn !":
            jump reponse1

        "Va te faire !":
            jump reponce2

label reponse1:

    g "tu est dans un label test"
    jump suite

label reponce2:

    g "toi même !"
    jump suite

label suite:

    g "voici la suite ..."

    m "C'est bien gentil."

    return
