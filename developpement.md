# Déploiement en mode développement

## Description

En mode developpement, l'application s'appuie sur une base de données locale Sqlite3.

Django propose un serveur http de developpement (runserver) qui permet de vérifier rapidement le fonctionnement du programme. Il permet également de développer sans installer un serveur http sur la machine de développement: 

-  Par défaut, le serveur fonctionne sur le port 8000 à l’adresse IP 127.0.0.1.
-  Vous pouvez lui transmettre explicitement une adresse IP et un numéro de port.
-  Ce serveur utilise l’objet application WSGI désigné par le réglage "WSGI_APPLICATION".
-  Le serveur de développement recharge automatiquement le code Python lors de chaque requête si nécessaire. 
-  N’UTILISEZ PAS CE SERVEUR DANS UN ENVIRONNEMENT DE PRODUCTION. Il n’a pas fait l’objet d’audits de sécurité ni de tests de performance. 

Pour le frontend, le module "http" de python est utilisé.

----


## Préparation du système

* mise à jour du système (optionnel)
``` bash
sudo apt update && sudo apt upgrade -y
```

* Installation des prérequis (optionnel)
```
sudo apt -y install git sudo vim 
```
---

## Initialisation de l'application

### Pré-requis Python

* Vérifier que python3, pip3 et venv sont installés
``` bash
python3 --version
pip3 --version
python3 -m venv -h
```
* Si besoin les installer :
``` bash
sudo apt -y install python3 python3-pip python3-venv
```

### Récupération du projet
```
cd $HOME
git clone https://gitlab.com/vapormap/vapormap-app.git vapormap-dev
cd vapormap-dev
```

###  Création d'un environnement Python virtuel
``` bash
cd $HOME/vapormap-dev
mkdir venv
python3 -m venv ./venv
```
---

## Lancement de l'API

* Initialisation de l'environnement Python
``` bash
cd $HOME/vapormap-dev
source venv/bin/activate
```

* Installation des "requirements" de l'application
```
cd app
pip install -r requirements/development.txt
python manage.py migrate
```

* Lancement de l'application
``` bash
python manage.py runserver 0.0.0.0:8001
---
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```

* Test : 
  * accès à l'API : dans une autre fenêtre de terminal
``` bash
curl http://localhost:8001/api/?format=json
```
   * Réponse
``` bash
{"points":"http://localhost:8001/api/points/?format=json"}
```

* A la fin des tests : 
  * pour arrêter le serveur 
``` bash
CONTROL-C.
```
  * pour sortir du venv
``` bash
deactivate
```

### Lancement du frontend 

* Ouvrir un autre terminal, et initialiser l'environnement python
``` bash
cd $HOME/vapormap-dev
source venv/bin/activate
```

* Configurer l'accès à l'API
``` bash
cd frontend
export VAPORMAP_BACKEND=<PUBLIC_API_ENDPOINT_HOST>
export VAPORMAP_BACKEND_PORT=8001
envsubst '${VAPORMAP_BACKEND},${VAPORMAP_BACKEND_PORT}' < config.json.template > config.json
```
Attention, pour `VAPORMAP_BACKEND` vous devez indiquer une adresse accessible depuis le navigateur. `localhost` ne fonctionne que si vous travaillez sur votre machine locale, sinon il faut indiquer l'adresse IP publique de votre VM, ou de votre instance Cloud.


* Lancer le frontend
``` bash
python -m http.server
```

* Test de l'accès à l'application
  * Depuis un navigateur : [http://localhost:8000](http://localhost:8000)
  * _Rem : si vous ne travaillez pas sur votre machine locale, l'adresse IP publique de votre VM, ou de votre instance Cloud._

* A la fin des tests : 
  * pour arrêter le serveur 
``` bash
CONTROL-C.
```
  * pour sortir du venv
``` bash
deactivate
```
