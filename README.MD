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
    - Logger-vous ensuite avec vos identifiant
    - Page flux Deux bouton création de ticket pour ensuite créer une critique et un autre pour créer un ticket et une critique
    - Page Abonnement Barre de texte entrer le nom d'une personne que auquel vous voulez vous abonnez, possibilitéz de vous désabonnez
    - Page Post Vos post et ticket où vous pouvez les supprimer et modifier 
    

4. Optionnel:
    - Vérifier le code:
        flake8 > flake-8/flake8-html.html
