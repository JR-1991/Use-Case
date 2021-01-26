###### Molekül Super-Klasse #####
from tracker.core import ElementBase
import json

class Molekuel(ElementBase):
    
    def __init__(self, name, smiles, inchi, konz_wert, konz_einheit):
        super().__init__(name, konz_wert, konz_einheit)
        
        self.smiles = smiles
        self.inchi = inchi