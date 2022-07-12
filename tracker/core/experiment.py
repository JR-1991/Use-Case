###### Experiment Super-Klasse #####
import json

class Experiment(object):
    
    def __init__(self, name):
        
        self.name = name
        self.biokat = {}
        self.reaktionen = {}
        self.mols = {}
        self.exps = []
    
    def addExp(self, experimentator):
        self.exps += [experimentator]
        
    def addBiocat(self, biocat):
        self.biokat[ biocat.name ] = biocat
        
    def addMol(self, mol):
        self.mols[ mol.name ] = mol
        
    def addReaktion(self, reaktion):
        self.reaktionen[ reaktion.name ] = reaktion
        
    def __str__(self):
        
        return json.dumps( { key:str(val) for key, val in  self.__dict__.items() }, indent=4 )
    