###### ElementBase Super-Klasse #####
import json

class Reaktion(object):
    
    def __init__(self, name, temp, ph):
        
        self.name = name
        self.temp = temp
        self.ph = ph

        self.edukte = []
        self.produkte = []
        self.biokat = []
        
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
        return dict(self.__dict__.items())