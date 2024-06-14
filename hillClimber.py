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
# print(f"The distance between Berlin and Hamburg is {getDistance(1,2)}km.")


def getTotalDistance(path): # Definition von "getTotalDistance"
    TotalDistance = 0 # Die gesamte Distanz wird gleich 0 gesetzt
    for i in range(len(path)-1): # Mit range wird der Bereich definiert, aus welchen Stätdten die Distanz errechnet werden soll, da wir die gesamte Distanz errechnen wollen Benötigen wir auch die gesamte liste von insgesamt 80 Einträgen.
        TotalDistance += getDistance(path[i], path[i+1]) # Durch die Vaariable i können wir alle Positionen nacheinander aufaddieren.
         TotalDistance += getDistance(path[-1], path[0]) # Plus die Distanz von der letzten Stadt zur ersten Stadt, da es eine Rundreise sein soll (Durch -1 wird das letzte Element aus der liste verwendet, durch die 0 das erste)
    return TotalDistance 

InitialPath = list(range(1,81)) #Erstellung einer List mit den 80 Städten aus der Excel Datei 
print(f"Die gesamte Distanz aus der unsorterten Liste beträgt {getTotalDistance( InitialPath)} Km") # Ausgabe der unsortierten gesamten Distanz

def swapCities(path): # Definition der Funktion "swapCities" zum Vertauschen zweier zufälliger Städte im Pfad
    New_path = path.copy() # Erstellung einer Kopie, um den "swap" vorzunehmen, und als neuen Path zu speichern
    City1, City2 = random.sample(range(len(path)), 2) # Auswahl von zwei Städten die getauscht werden sollen
    New_path[City1], New_path[City2] = New_path[City2], New_path[City1] # Tausch der Städte im Pfad
    return New_path # Ausgabe des neuen Pfades

def hillClimber(InitialPath, MaxIterations=10000):
    CurrentPath = InitialPath # Gleichsetzen vom aktuellen Pfad und dem ursprünglichen Pfad
    CurrentDistance = getTotalDistance(CurrentPath) # Ausrechnen von der Gesamtstrecke des unsortieren Pfades
    
    for Iteration in range(MaxIterations):
        NewPath = swapCities(CurrentPath) # Erzeugung eines neuen Pfades, indem Städte vertauscht werden
        NewDistance = getTotalDistance(NewPath) # Berechnung der neuen Distanz
        
        if NewDistance < CurrentDistance: # Wenn die neue Distanz kleiner ist, als die aktuelle wird der aktuelle Pfad mit dem neuen Überschrieben
            CurrentPath = NewPath
            CurrentDistance = NewDistance
            print(f"Strecke der neuen besten Reiseroute: {CurrentDistance}Km") # Output über die neue beste Strecke. So wird sichtbar, dass der Code wirklich am "arbeiten" ist
            
    return CurrentPath, CurrentDistance # Gibt den besten gefundenen Pfad und seine Gesamtdistanz zurück

BestPath, BestDistance = hillClimber(InitialPath) # Ausführung vonm Hill-Climbing-Algorithmus , um die beste Route zu finden
print(f"Die Gesamtstecke für die beste Gefundene Rundreise beläuft sich auf {BestDistance} Km") # Ausgabe der Gesamtdistanz der besten Route
print(f"Die optimierte Route ist lautet wie folgt: {BestPath}") # Ausgabe der besten gefundenen Routen
