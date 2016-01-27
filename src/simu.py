# -*- coding: utf-8 -*-

import geo
import visu

import math
import random


class Monde:

	def __init__(self):
		self.horloge = 0.0
		self.camera = visu.Camera()
		self.pinguin = visu.Pinguin()
		self.decor = []
		self.activites = []
		self.annuaire = {}

	def dessiner(self):
		self.camera.lookAt()
		for x in self.decor:
			x.dessiner()

	def actualiser(self, dt):
		self.horloge += dt
		self.camera.updateVitesse(dt)
		self.camera.updateAngle()
		self.pinguin.updateAngle()
		self.pinguin.activite.actualiser(self.horloge, dt)
		for x in self.activites:
			x.actualiser(self.horloge, dt)

	def getPositionCamera(self):
		return "x ", self.camera.repere.o.x, " y ", self.camera.repere.o.y

	def getPositionObjet(self, p):
		return "x ", p.repere.o.x, " y ", p.repere.o.y

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
		self.state = 0
		self.dt = 0.0

	def actualiser(self, t, dt):
		if self.objet != None:
			self.dt = dt

	def effraye(self, p):
		if self.objet.maillage.url != "../data/avatars/bleu.obj":
			self.objet.maillage.setUrl("../data/avatars/bleu.obj")
		angle = math.pi - math.radians(self.objet.getAngleObject(p))
		self.objet.tourner(angle)
		self.objet.avancer(2.0 * self.dt)

	def curieux(self, p):
		if self.objet.maillage.url != "../data/avatars/vert.obj":
			self.objet.maillage.setUrl("../data/avatars/vert.obj")
		angle = math.pi - math.radians(self.objet.getAngleObject(p) + 180)
		self.objet.tourner(angle)
		if self.objet.getDistance(p) > 4.0 :
			self.objet.avancer(2.0 * self.dt)

	def enerve(self, p):
		if self.objet.maillage.url != "../data/avatars/rouge.obj":
			self.objet.maillage.setUrl("../data/avatars/rouge.obj")
		angle = math.pi - math.radians(self.objet.getAngleObject(p) + 180)
		self.objet.tourner(angle)
		if self.objet.getDistance(p) > 0.1 :
			self.objet.avancer(5.0 * self.dt)

	def neutre(self):
		if self.objet.maillage.url != "../data/avatars/p.obj":
			self.objet.maillage.setUrl("../data/avatars/p.obj")
		x = random.random()
		if x < 0.5:
			self.objet.avancer(2.0 * self.dt)
		elif x < 0.65:
			self.objet.tourner(math.pi / 4.0)
		elif x < 0.8:
			self.objet.tourner(-math.pi / 3.0)
		else:
			pass
		pass
