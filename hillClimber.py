# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 14:59:48 2023

@author: ThomasKopsch

bearbeitet von Felix Kulow
"""

import pandas as pd


# The task is to implement the hillClimber algorithm.
# Find a 'good' solution to the Travelling salesman
# problem using the hillClimber algorithm.
#
# The distances of 80 large German cities is provided.
# Each city is encoded with a number 1-80.
# You can find a legend in the accompanieng documents.


#########################################################
#########################################################
######### NO NOT CHANGE THE FOLLOWING CODE! #############
#########################################################
#########################################################

def readDistances():
    """
    This method reads the example data and splits
    the data randomly into two sets to create a
    training and test data set.
    """
    
    # Read the example Data from the file.
    return pd.read_csv('distances.csv', sep=',', header=0)
    
distanceTable = readDistances()

def getDistance(cityA, cityB):
    return distanceTable.loc[cityA-1][cityB]


#########################################################
#########################################################
########### NO NOT CHANGE THE FORMER CODE! ##############
#########################################################
#########################################################

# Example: The distance between Berlin (1) and Hamburg (2)
print(f"The distance between Berlin and Hamburg is {getDistance(1,2)}km.")


def getTotalDistance(path): # Definition von "getTotalDistance"
    TotalDistance = 0 # Die gesamte Distanz wird gleich 0 gesetzt
    for i in range(len(path)-1): # Mit range wird der Bereich definiert, aus welchen Stätdten die Distanz errechnet werden soll, da wir die gesamte Distanz errechnen wollen Benötigen wir auch die gesamte liste von insgesamt 80 Einträgen.
        TotalDistance += getDistance(path[i], path[i+1]) # Durch die Vaariable i können wir alle Positionen nacheinander aufaddieren.
    return TotalDistance 

initialPath = list(range(1,81))
print(f"Die gesamte Distanz aus der unsorterten Liste beträgt {getTotalDistance( initialPath)} Km") # Ausgabe der unsortierten gesamten Distanz





