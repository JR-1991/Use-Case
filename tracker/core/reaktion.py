###### ElementBase Super-Klasse #####
import json

class Reaktion(object):
    
    def __init__(self, name, temp, ph):
        
        self.name = name
        self.temp = temp
        self.ph = ph
        
        self.edukte = list()
        self.produkte = list()
        self.biokat = list()
        
    def __addElement(self, element, stoechometrie, liste):
        liste.append( (element, stoechometrie) )
        
    def addEdukt(self, element, stoechometrie):
        self.__addElement(element, stoechometrie, self.edukte)
        
    def addProdukt(self, element, stoechometrie):
        self.__addElement(element, stoechometrie, self.produkte)
        
    def addBiokat(self, element, stoechometrie):
        self.__addElement(element, stoechometrie, self.biokat)
        
    def addRohdaten(self, data):
        self.data = data
        
    def __str__(self):
        return { key:val for key, val in  self.__dict__.items() }