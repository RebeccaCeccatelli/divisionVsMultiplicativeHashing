import unittest

from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from numpy import random
from timeit import default_timer as timer

from HashTable import HashTable
from Element import Element

class Ex2TestCase(unittest.TestCase):

    def testCompareCollisions(self):        #calls helper method generateRandomKeys()
        m = 10000
        nKeys = 12000
        randomKeys = self.generateRandomKeys(nKeys)

        hashTableD = HashTable(m, "division hashing")       #hash table dealed with division hashing
        hashTableM = HashTable(m, "multiplicative hashing")     #hash table dealed with multiplicative hashing

        loadingFactorD = [0]
        collisionsD = [0]
        loadingFactorM = [0]
        collisionsM = [0]

        for key in randomKeys:      #collects data for plotting
            hashTableD.insert(Element(None,key))
            loadingFactorD.append(hashTableD.n/m)
            collisionsD.append(hashTableD.collisions)

            hashTableM.insert(Element(None,key))
            loadingFactorM.append(hashTableM.n/m)
            collisionsM.append(hashTableM.collisions)

        plt.plot(loadingFactorD, collisionsD, 'r', loadingFactorM, collisionsM, 'g')        #plotting commands
        plt.title("Comparison of collisions with division hashing and multiplicative hashing")
        plt.xlabel("alpha (loading factor)")
        plt.ylabel("collisions")
        redPatch = mpatches.Patch(color = 'red', label = 'Division hashing')
        greenPatch = mpatches.Patch(color = 'green', label = "Multiplicative hashing")
        plt.legend(handles = [redPatch,greenPatch])
        plt.show()

    def testTimeComplexity(self):       #calls helper method generateRandomKeys()
        m = 10000
        nKeys = 15000
        randomKeys = self.generateRandomKeys(nKeys)

        hashTableD = HashTable(m, "division hashing")       #hash table dealed with division hashing
        hashTableM = HashTable(m, "multiplicative hashing")     #hash table dealed with multiplicative hashing

        loadingFactorD = [0]
        complexityD = [0]
        loadingFactorM = [0]
        complexityM = [0]

        for key in randomKeys:      #collects data for plotting
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

        DmovingAverage = self.computeMovingAverage(complexityD)
        MMovingAverage = self.computeMovingAverage(complexityM)

        plt.plot(loadingFactorD,DmovingAverage,'r',loadingFactorM,MMovingAverage,'g')       #plotting commands
        plt.title("Time complexity of 'insert()' with division hashing and multiplicative hashing")
        plt.xlabel("alpha (loading factor)")
        plt.ylabel("seconds")
        plt.ylim(0,0.00002)
        redPatch = mpatches.Patch(color = 'red', label = 'Division hashing')
        greenPatch = mpatches.Patch(color = 'green', label = "Multiplicative hashing")
        plt.legend(handles = [redPatch,greenPatch])
        plt.show()

    def testDivisionHashingWorstCase(self):
        m = 50
        hashTableD = HashTable(m,"division hashing")        #hash table dealed with division hashing
        hashTableM = HashTable(m, "multiplicative hashing")     #hash table dealed with multiplicative hashing

        loadingFactorD = []
        collisionsD = []
        loadingFactorM = []
        collisionsM = []

        for key in range(1,1000,m):     #collects data for plotting
            hashTableD.insert(Element(None,key))
            loadingFactorD.append(hashTableD.n/m)
            collisionsD.append(hashTableD.collisions)
            hashTableM.insert(Element(None,key))
            loadingFactorM.append(hashTableM.n/m)
            collisionsM.append(hashTableM.collisions)

        plt.plot(loadingFactorD,collisionsD,'r',loadingFactorM,collisionsM,'g')     #plotting commands
        plt.title("Dealing of multiples of m: Worst case for division hashing")
        plt.xlabel("alpha (loading factor)")
        plt.ylabel("collisions")
        redPatch = mpatches.Patch(color = 'red', label = 'Division hashing')
        greenPatch = mpatches.Patch(color = 'green', label = "Multiplicative hashing")
        plt.legend(handles = [redPatch,greenPatch])
        plt.show()

    def generateRandomKeys(self, n):
        randomKeys = [key * n for key in np.random.random(n)]       #generates array of random keys, each in [0,n)
        return randomKeys

    def computeMovingAverage(self, array):
        movingAverages = []
        cumSum = np.cumsum(array)

        i=1
        while i<=len(array):
            windowAverage = round(cumSum[i-1]/i, 200)
            movingAverages.append(windowAverage)
            i +=1
        return movingAverages

if __name__ == '__main__':
    unittest.main()
