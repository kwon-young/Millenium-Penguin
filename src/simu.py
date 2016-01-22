# -*- coding: utf-8 -*-

import geo
import visu

import math
import random


class Monde:

    def __init__(self):
        self.horloge = 0.0
        self.camera = visu.Camera()
        self.pinguin = visu.Objet()
        self.decor = []
        self.activites = []
        self.annuaire = {}

    def dessiner(self):
        self.camera.lookAt()
        for x in self.decor:
            x.dessiner()

    def actualiser(self, dt):
        self.horloge += dt
        for x in self.activites:
            x.actualiser(self.horloge, dt)

    def getVitesseCamera(self, dt):
        return self.camera.repere.getVitesse(dt)

    def getAngleCamera(self, p):
        #On récupere la position de p
        pos = geo.Vec3((0.0, 0.0, 0.0))
        pos.copier(p.repere.o)

        #On récupere la position de la caméra
        posCam = geo.Vec3((0.0, 0.0, 0.0))
        posCam.copier(self.camera.repere.o)

        #On calcule p si le repère a juste translater à la caméra
        pos.moins(pos, posCam)
        
        #Soit alpha l'angle de la caméra
        alpha = self.camera.repere.getAngle()

        aPrim = pos.x * math.cos(alpha) - pos.y * math.sin(alpha)
        bPrim = pos.x * math.sin(alpha) + pos.y * math.cos(alpha)
        return math.degrees(math.atan(bPrim/aPrim))

        

    def ajouter(self, decor=None, activite=None):
        if decor != None:
            self.decor.append(decor)
        if activite != None:
            self.activites.append(activite)

    def ajouterObjet(self, objet=None):
        if objet != None:
            self.objet.append(objet)

    def enregistrer(self, nom, obj):
        self.annuaire[nom] = obj


class Activite:

    def __init__(self, id=None, objet=None):
        self.id = id
        self.actif = False
        self.objet = objet

    def start(self):
        self.actif = True

    def stop(self):
        self.actif = False

    def pause(self):
        self.actif = False

    def actualiser(self, t, dt):
        if self.actif:
            print "ACTIVITE : ", t, " - ", dt


class Fou(Activite):

    def __init__(self, id=None, objet=None):
        Activite.__init__(self, id, objet)

    def actualiser(self, t, dt):
        if self.objet != None:
            x = random.random()
            if x < 0.4:
                self.objet.avancer(4.0 * dt)
            elif x < 0.6:
                self.objet.tourner(math.pi / 4.0)
            elif x < 0.8:
                self.objet.tourner(-math.pi / 3.0)
            else:
                pass
