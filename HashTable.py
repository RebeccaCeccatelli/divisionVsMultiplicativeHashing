import numpy as np
from numpy import random

class HashTable:
    def __init__(self, m, hashFunction):
        self.m = m
        self.n = 0
        self.collisions = 0
        self.hashFunction = hashFunction
        self.chainedList = [[] for i in range(m)]     #lista di m liste

    def insert(self, element):
        hk = self.computeHK(element.key)

        if self.chainedList[hk]:    #se la lista non è vuota
            self.collisions +=1

        self.chainedList[hk].insert(0, element)
        self.n +=1

    def search(self, k):
        hk = self.computeHK(k)
        x = None
        for element in self.chainedList[hk]:
            if element.key == k:
                x = element
                break
        return x,hk

    def delete(self, element):
        x,hk = self.search(element.key)
        if x is not None:
            self.chainedList[hk].remove(x)

    def computeHK(self, k):
        hk = None
        if self.hashFunction == "division hashing":
            hk = self.exploreByDivisionHashing(k)
        elif self.hashFunction == "multiplicative hashing":
            hk = self.exploreByMultiplicativeHashing(k)
        return hk

    def exploreByDivisionHashing(self, k):
        return int(k%self.m)

    def exploreByMultiplicativeHashing(self, k):
        A = random.rand()
        floatingDigit = self.m * ((k*A)%1)

        return int(floatingDigit)
