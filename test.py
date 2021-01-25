from tracker.core import *

# Initialisiere Dokument
exp = Experiment(name="Test_Reaktion")

# Definiere Anwender
experimentator = Experimentator("Max", "Mustermann", "max@mustermann.de", "IBTB")
exp.addExp(experimentator)

# Definiere Protein
prot = Biokatalysator(
    name="Protein1", 
    gen="ATGGAATTC", 
    organismus="E.coli", 
    konz_wert=10.0, 
    konz_einheit="mmol/l"
    )

# Definiere Substrat und Produkt
substrat = Molekuel(
    name="Substrat", 
    smiles="SMILES1", 
    inchi="InCHI1", 
    konz_wert=10.0, 
    konz_einheit="mmol/l"
    )

produkt = Molekuel(
    name="Produkt", 
    smiles="SMILES2", 
    inchi="InCHI2", 
    konz_wert=10.0, 
    konz_einheit="mmol/l"
    )

# Füge Produkt, Substrat und Protein dem Dokument hinzu
exp.addMol(produkt)
exp.addMol(substrat)
exp.addBiocat(prot)

# Definiere Reaktion
reaktion = Reaktion(name="Reaktion1", temp=37.0, ph=7.0)

reaktion.addBiokat(prot, 1.0)
reaktion.addEdukt(substrat, 1.0)
reaktion.addProdukt(produkt, 1.0)

# Füge Rohdaten hinzu
rohdaten = Rohdaten(
    molekuel=substrat, 
    data=[1.0, 0.76, 0.57, 0.25], 
    time=[0,1,2,3],
    type="conc"
    )

reaktion.addRohdaten( rohdaten )

# Füge Reaktion dem Dokument hinzu
exp.addReaktion(reaktion)

print(exp)