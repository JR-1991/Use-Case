###### ElementBase Super-Klasse #####
import json
import pandas as pd

class Rohdaten(object):
    
    def __init__(self, molekuel, data, time, type):
        
        self.data = pd.DataFrame( { 
                                   
                                   'time': time,
                                   f'{molekuel.name}_{type}': data,
                                   
                                   } )
        
    def __str__(self):
        return { key:val for key, val in  self.__dict__.items() }
    
    def getInfos(self):
        print(self.data.describe())