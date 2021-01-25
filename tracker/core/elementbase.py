###### ElementBase Super-Klasse #####
import json

class ElementBase(object):
    

    def __init__(self, name, konz_wert, konz_einheit):
        
      self.name = name
      self.konz_wert = konz_wert
      self.konz_einheit = konz_einheit
      
    def __str__(self):
        return { key:str(val) for key, val in  self.__dict__.items() }
    
    