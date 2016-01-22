# -*- coding: utf-8 -*-
import math
import random
import copy


class Vec3:

    def __init__(self, p):
        x, y, z = p
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "<%f %f %f" % (self.x, self.y, self.z)

    def setCoordonnees(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def getCoordonnees(self):
        return self.x, self.y, self.z

    def soit(self, v):
        self.x = v.x
        self.y = v.y
        self.z = v.z

    def copier(self, v):
        self.x = v.x
        self.y = v.y
        self.z = v.z

    def vers(self, de, a):
        self.x = a.x - de.x
        self.y = a.y - de.y
        self.z = a.z - de.z

    def plus(self, u, v):
        self.x = u.x + v.x
        self.y = u.y + v.y
        self.z = u.z + v.z

    def moins(self, u, v):
        self.x = u.x - v.x
        self.y = u.y - v.y
        self.z = u.z - v.z

    def accumuler(self, k, v):
        self.x += k * v.x
        self.y += k * v.y
        self.z += k * v.z

    def scale(self, k):
        self.x *= k
        self.y *= k
        self.z *= k

    def oppose(self):
        self.x = - self.x
        self.y = - self.y
        self.z = - self.z

    def produitVectoriel(self, u, v):
        self.x = u.y * v.z - u.z * v.y
        self.y = u.z * v.x - u.x * v.z
        self.z = u.x * v.y - u.y * v.x

    def produitScalaire(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z

    def distance(self, v):
        x, y, z = v.getCoordonnees()
        return math.sqrt((self.x - x) * (self.x - x) + (self.y - y) * (self.y - y) + (self.z - z) * (self.z - z))

    def norme(self):
        l = math.sqrt(self.x * self.x +
                      self.y * self.y +
                      self.z * self.z)
        return l

    def normer(self):
        l = self.norme()
        self.scale(1.0 / l)

    def tronquer(self, lmax):
        l = self.norme()
        if l > lmax:
            self.scale(lmax / l)


class Repere:

    def __init__(self):
        self.o = Vec3((0.0, 0.0, 0.0))
        self.u = Vec3((1.0, 0.0, 0.0))
        self.v = Vec3((0.0, 1.0, 0.0))
        self.w = Vec3((0.0, 0.0, 1.0))
        self.angle = 0.0
        self.angleDegre = 0.0
        self.memory = [self.o, self.o, self.o]

    def placer(self, p):
        self.o.copier(p)

    def orienter(self, angle):
        self.angle = angle
        self.angleDegre = angle * 180.0 / math.pi
        self.u.setCoordonnees(x=math.cos(angle), y=math.sin(angle))
        self.v.produitVectoriel(self.w, self.u)

    def store(self, vec1, vec2):
        self.memory.pop()
        vecmoins = Vec3([0, 0, 0])
        vecmoins.moins(vec1, vec2)
        self.memory.insert(0, vecmoins)

    def avancer(self, l):
        self.o.accumuler(l, self.u)

    def gauche(self, l):
        self.o.accumuler(l, self.v)

    def monter(self, l):
        self.o.accumuler(l, self.w)

    def tourner(self, a):
        self.angle += a
        self.angleDegre = self.angle * 180.0 / math.pi
        self.u.setCoordonnees(x=math.cos(self.angle), y=math.sin(self.angle))
        self.v.produitVectoriel(self.w, self.u)
    
    def getDistance(self, repere):
        return self.o.distance(repere.o)

    def getVitesse(self):
        for myvec in self.memory:
            print myvec
        memcopy = copy.deepcopy(self.memory)
        distance = memcopy.pop()
        for i in range(len(memcopy)-2):
            distance.plus(distance, memcopy.pop())
        return distance.norme()
        

