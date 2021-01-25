###### Molekül Super-Klasse #####
from tracker.core import ElementBase
import json

class Molekuel(ElementBase):
    
    def __init__(self, name, smiles, inchi, konz_wert, konz_einheit):
        super().__init__(name, konz_wert, konz_einheit)
        
        self.smiles = smiles
        self.inchi = inchi
        
    def __str__(self):
        
        return json.dumps( { key:val for key, val in  self.__dict__.items() }, indent=4 )