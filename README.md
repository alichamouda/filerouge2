# VaporMap

--- 

## Description

VaporMap est une application web permettant de référencer des points GPS dans une base de données. 
Ces points peuvent être affichés sur une carte.

Techniquement, c'est une application écrite en python, qui utilise le framework Django.

>Cette application est une maquette développée rapidement dans un but pédagogique par Tristan Le Toullec.


---


# Installation


## Architecture de l'application

L'application "VaporMap" est constituée de 2 partie
- Le frontend : chargé de l'interface avec l'utilisateur dans le navigateur. Il est composé de fichiers statiques.
- L'API : chargé de gérer les données, via une API REST. Cette partie est développée avec le framework Python Django

L'utilisateur final de l'application interragit avec le fontend.

Le frontend envoie des requetes vers l'API

rem : l'API peut être utilisée sans le frontend.


## Principe de fonctionnement du framework Python Django

Django permet de déployer les applications dans différents environnements techniques.

Pour Vapormap, les modes développement et production ont été configurés :

* En développement, l'application utilise serveur http intégré à Django, et stocke ses données dans une base sqlite.
* En production l'application utilise un serveur web externe (Apache ou Nginx), et stocke ses données dans une base mysql

Une application Django nécessite (entre autre) des tâches d'administration : 

- gestion de la base de données :
    - `migrate` : installation ou mise à jour des schémas de base de données (tables, schema)
- gestion de la partie web
    - `collecstatic` : installation dans un répertoire unique de l'ensemble des ressources statiques (.js, .css, images, ..) nécessaires au fonctionnement de l'application.

L'outil de gestion d'environement python dédié "venv" est utilisé pour configurer les environnements python permettant de lancer l'application.

--- 

## Déploiement

Pour les différents modes opératoires, suivez les guides :

* [Installation en mode développement](./developpement.md)
* [Installation en mode production](./production.md)

---


