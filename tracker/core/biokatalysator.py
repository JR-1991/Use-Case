###### Biokatalysator Super-Klasse #####
from tracker.core import ElementBase
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio.Seq import Seq
import json

class Biokatalysator(ElementBase):
    
    def __init__(self, name, gen, organismus, konz_wert, konz_einheit):
        super().__init__(name, konz_wert, konz_einheit)
        
        self.gen = Seq(gen)
        self.sequenz = ProteinAnalysis( str(self.gen.translate()) )
        self.organismus = organismus
        
    def getSequence(self):
        return str(self.sequenz)
    
    def getGene(self):
        return str(self.gen)
    
    def getMolWeight(self):
        return self.sequenz.molecular_weight
    
    def getExtinctionCoeff(self):
        return self.sequenz.molar_extinction_coefficient