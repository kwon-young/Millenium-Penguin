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

	def getAngleCameraObject(self, p):
		alpha = self.camera.repere.getAngle()
		posCam = self.camera.repere.o
		posObj = p.repere.o
		omega = math.atan((posObj.x - posCam.x)/(posObj.y - posCam.y))
		return (omega - alpha) * 180 / math.pi

	def getAngleCamera(self):
		angle = self.camera.repere.getAngle()
		return angle * 180.0 / math.pi

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
		self.etat = 0

	def actualiser(self, t, dt):
		if self.objet != None:
			#x = random.random()
			x = 1
			if x < 0.4:
				self.objet.avancer(4.0 * dt)
			elif x < 0.6:
				self.objet.tourner(math.pi / 4.0)
			elif x < 0.8:
				self.objet.tourner(-math.pi / 3.0)
			else:
				pass

	# def comportement(self, objet):
	# 	comportement = random.randrange(0, 3, 1)
	# 	if comportement == 0:
	# 		return 0

	# def effraye(self, p):
	# 	xp = p.repere.o.x
	# 	yp = p.repere.o.y
	# 	x = self.objet.repere.o.x
	# 	y = self.objet.repere.o.y

