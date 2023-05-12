# P9_Boulahrouf_Ryad

Description du programme:

0. Récupérer le code :
    git clone https://github.com/ryry-shi/P9_Boulahrouf_Ryad.git
    
1. Créer l'environnement virtuel et le lancer:
        
    - Python -m venv venv       (création de l'environnement)
    - venv\scripts\activate     (activation sur windows)
    - source venv/bin/activate (activation sur Unix)
    
2. Installer les dépendances:
    - pip install -r requirements.txt
    - python manage.py runserver(pour lancer le serveur)
    - python manage.py makemigrations(pour lancer les models)

3. Lancer le programme:
    - python main.py (windows)
    - python3 main.py (Unix)
    - python manage.py runserver( Impossible sans le module django dans requirement.Txt)
    - Créer votre compte sur la première page
        - Créer un nom d'utilisateur
        - Choissisez un mot de passe(qui soit au moins de 8 caractère et avec des chiffre ou caractère spéciaux)
    
    - Utilisateurs déja créer: admin mdp: admin
                               Pierre mdp: avalanche84
                               Ryad mdp: Gintama84

    - Logger-vous ensuite avec vos identifiant
    - Page flux
        - Vue sur les tickets et les critiques que les utilisateurs postes sur l'application
        - Créer un ticket, pour pouvoir demander une critique où faire un ticket et une critique en même temps
    - Page Abonnement
        - Barre de texte où vous entrer le nom d'un utilisateurs auquel vous_voulez vous abonnez si le nom taper correspond a aucun utilisateurs rien ne se passe
        - Vue sur vos abonnés et les personnes auquels vous vous êtes abonnez possibilitez de vous désabonnez
    - Page Post
        - Vue sur les tickets, critique d'un utilisateurs
        - Possibilitez de modifier ou supprimer un ticket ou une critique 
    

4. Optionnel:
    - Vérifier le code:
        flake8 > flake-8/flake8-html.html
