# Millenium-Penguin

## PRE-RECQUIS

* python 2.7
* pyglet (www.pyglet.org)
* pillow

## LANCEMENT DU PROGRAMME

se placer dans le répertoire src
exécuter la commande :

```
sh Start.sh
```
+------------------------------------+---------------------------------------+
| arrêt du programme                 | ESC                                   |
+====================================+=======================================+
| orientation de la caméra virtuelle | déplacement de la souris en enfonçant |
|                                    | le bouton gauche                      |
+------------------------------------+---------------------------------------+
| déplacements avant, arrière,       | flêches                               |
| gauche, droite                     |                                       |
+------------------------------------+---------------------------------------+

## PROGRAMMATION

Création de la scène : dans le fichier fabrique.py, méthode fabriquer de la classe Fabrique

Comportement des objets : dans le fichier simu.py
Un nouveau comportement est obtenu en créant une sous-classe de la classe Activite.
Le comportement est alors essentiellement codé dans la méthode actualiser(t,dt) de cette sous-classe (voir les sous-classes Fou et Vent).






