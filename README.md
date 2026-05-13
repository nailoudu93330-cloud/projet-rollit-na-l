
https://github.com/user-attachments/assets/91c987c9-79af-4023-98d8-753717f5acf6
# projet-rollit-nail
README – Pick Tok
Présentation du projet

Pick Tok est un jeu développé en Python dans le cadre de l’UE Projet 1 en première année de licence informatique à l’Université Gustave Eiffel.
Le jeu est une adaptation informatique d’un jeu de plateau dans lequel le joueur doit capturer des jetons de différentes couleurs afin d’obtenir le meilleur score possible.

Le jeu propose un mode solo et un mode multijoueur, et respecte les règles fournies dans le cadre du projet.

Membres du groupe – TP 8

Naïl : développement du mode multijoueur, rédaction du compte rendu et du README

Rywan : cahier des charges et interface graphique (bibliothèque FLTK)

Sofiane : développement du programme principal et de la logique générale du jeu

Prérequis

Pour exécuter le jeu, il est nécessaire d’avoir :

Python 3 installé sur l’ordinateur

La bibliothèque FLTK (utilisée pour l’interface graphique)

Lancement du jeu

Récupérer l’ensemble des fichiers du projet.

Ouvrir un terminal ou un environnement de développement Python.

Se placer dans le répertoire contenant les fichiers du jeu.

Lancer le programme principal avec la commande :

python main.py


(Le nom du fichier principal peut être adapté selon l’organisation du projet.)

Règles du jeu (résumé)

Le jeu se déroule sur un plateau comportant des jetons de différentes couleurs.

Certains jetons sont capturables, d’autres non.

Le joueur capture un jeton en le plaçant dans le râtelier.

Lorsqu’une triplette de jetons de même couleur est formée dans le râtelier, ceux-ci sont retirés et des points sont attribués.

La partie s’arrête selon les conditions définies par les règles (râtelier plein, plus de jetons capturables, etc.).

Les règles complètes sont disponibles dans le document fourni avec le sujet.

Modes de jeu
Mode solo

Le joueur joue seul et tente d’obtenir le score le plus élevé possible en capturant les jetons du plateau.

Mode multijoueur

Plusieurs joueurs jouent à tour de rôle.
Le score est calculé individuellement et le joueur ayant le score le plus élevé à la fin de la partie remporte la victoire.

Fonctionnalités principales

Gestion du plateau et des jetons

Interface graphique avec FLTK

Mode solo

Mode multijoueur

Gestion du râtelier

Calcul du score

Détection de la fin de partie

Organisation du code

Le programme est structuré autour de :

fonctions d’initialisation du jeu ;

fonctions de gestion des captures ;

fonctions liées à l’interface graphique ;

fonctions de gestion des tours de jeu et des scores.

Cette organisation permet une bonne lisibilité et facilite la maintenance du code.

Améliorations possibles

Plusieurs améliorations pourraient être envisagées :

enrichir l’interface graphique ;

ajouter des options de configuration (nombre de joueurs, difficulté, etc.) ;

optimiser certaines parties de la logique du jeu.

Remarques finales

Le jeu Pick Tok est fonctionnel et conforme aux attentes du projet.
Ce projet nous a permis de mettre en pratique les notions vues en cours, de travailler en équipe et de développer une application complète en Python.













