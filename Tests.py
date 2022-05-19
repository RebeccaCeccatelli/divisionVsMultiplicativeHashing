import unittest

from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from numpy import random
from timeit import default_timer as timer

from HashTable import HashTable
from Element import Element

class MyTestCase(unittest.TestCase):

    def testCompareCollisions(self):
        m = 10000
        nKeys = 8000
        randomKeys = self.generateRandomKeys(nKeys)

        hashTableD = HashTable(m, "division hashing")
        hashTableM = HashTable(m, "multiplicative hashing")

        loadingFactorD = [0]
        collisionsD = [0]
        loadingFactorM = [0]
        collisionsM = [0]

        for key in randomKeys:
            hashTableD.insert(Element(None,key))
            loadingFactorD.append(hashTableD.n/m)
            collisionsD.append(hashTableD.collisions)
            hashTableM.insert(Element(None,key))
            loadingFactorM.append(hashTableM.n/m)
            collisionsM.append(hashTableM.collisions)

        plt.plot(loadingFactorD, collisionsD, 'r', loadingFactorM, collisionsM, 'g')
        plt.title("Comparison of collisions with division hashing and multiplicative hashing")
        plt.xlabel("alpha (loading factor)")
        plt.ylabel("collisions")
        redPatch = mpatches.Patch(color = 'red', label = 'Division hashing')
        greenPatch = mpatches.Patch(color = 'green', label = "Multiplicative hashing")
        plt.legend(handles = [redPatch,greenPatch])
        plt.show()

    def testTimeComplexity(self):
        m = 1000
        nKeys = 1500
        randomKeys = self.generateRandomKeys(nKeys)

        hashTableD = HashTable(m, "division hashing")
        hashTableM = HashTable(m, "multiplicative hashing")

        loadingFactorD = [0]
        complexityD = [0]
        loadingFactorM = [0]
        complexityM = [0]

        for key in randomKeys:
            start1 = timer()
            hashTableD.insert(Element(None,key))
            end1 = timer()
            complexityD.append(end1-start1)
            loadingFactorD.append(hashTableD.n/m)

            start2 = timer()
            hashTableM.insert(Element(None,key))
            end2 = timer()
            complexityM.append(end2-start2)
            loadingFactorM.append(hashTableM.n/m)

        plt.plot(loadingFactorD,complexityD,'r',loadingFactorM,complexityM,'g')
        plt.title("Time complexity of 'insert()' with division hashing and multiplicative hashing")
        plt.xlabel("alpha (loading factor)")
        plt.ylabel("seconds")
        plt.ylim(0,0.00010) #o 0.00025 o 0.000025
        redPatch = mpatches.Patch(color = 'red', label = 'Division hashing')
        greenPatch = mpatches.Patch(color = 'green', label = "Multiplicative hashing")
        plt.legend(handles = [redPatch,greenPatch])
        plt.show()

    def testDivisionHashingWorstCase(self):
        m = 50
        hashTableD = HashTable(m,"division hashing")
        hashTableM = HashTable(m, "multiplicative hashing")

        loadingFactorD = []
        collisionsD = []
        loadingFactorM = []
        collisionsM = []

        for key in range(1,1000,m):
            hashTableD.insert(Element(None,key))
            loadingFactorD.append(hashTableD.n/m)
            collisionsD.append(hashTableD.collisions)
            hashTableM.insert(Element(None,key))
            loadingFactorM.append(hashTableM.n/m)
            collisionsM.append(hashTableM.collisions)

        plt.plot(loadingFactorD,collisionsD,'r',loadingFactorM,collisionsM,'g')
        plt.title("Dealing of multiples of m: Worst case for division hashing")
        plt.xlabel("alpha (loading factor)")
        plt.ylabel("collisions")
        redPatch = mpatches.Patch(color = 'red', label = 'Division hashing')
        greenPatch = mpatches.Patch(color = 'green', label = "Multiplicative hashing")
        plt.legend(handles = [redPatch,greenPatch])
        plt.show()

    def generateRandomKeys(self, n):
        randomKeys = [key * n for key in np.random.random(n)]
        return randomKeys

if __name__ == '__main__':
    unittest.main()
