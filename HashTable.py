from numpy import random

class HashTable:
    def __init__(self, m, hashFunction):
        self.m = m
        self.n = 0
        self.collisions = 0
        self.hashFunction = hashFunction        #hash function selected
        self.chainedList = [[] for i in range(m)]       #list of m lists

    def insert(self, element):      #calls helper method computeHK()
        hk = self.computeHK(element.key)

        if self.chainedList[hk]:    #if list is not empty there is a collision
            self.collisions +=1

        self.chainedList[hk].insert(0, element)
        self.n +=1

    def search(self, k):        #calls helper method computeHK()
        hk = self.computeHK(k)
        x = None
        for element in self.chainedList[hk]:
            if element.key == k:
                x = element
                break
        return x,hk

    def delete(self, element):      #calls method search()
        x,hk = self.search(element.key)
        if x is not None:
            self.chainedList[hk].remove(x)

    def computeHK(self, k):      #calls helper methods exploreByDivisionHashing() and exploreByMulitplicativeHashing()
        hk = None
        if self.hashFunction == "division hashing":
            hk = self.exploreByDivisionHashing(k)
        elif self.hashFunction == "multiplicative hashing":
            hk = self.exploreByMultiplicativeHashing(k)
        return hk

    def exploreByDivisionHashing(self, k):      #computes index in case of division hashing
        return int(k%self.m)

    def exploreByMultiplicativeHashing(self, k):        #computes index in case of multiplicative hashing
        A = random.rand()
        floatingDigit = self.m * ((k*A)%1)

        return int(floatingDigit)
