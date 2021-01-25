###### ElementBase Super-Klasse #####
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Rohdaten(object):
    
    def __init__(self, molekuel, data, time, type):
        
        self.data = pd.DataFrame( { 
                                   
                                   'time': time,
                                   f'{molekuel.name}_{type}': data,
                                   
                                   } )
        
        self.type = type
        self.molekuel = molekuel
        self.plotname = f'{molekuel.name}_{type}'
        
    def __str__(self):
        return { key:val for key, val in  self.__dict__.items() }
    
    def getInfos(self, path):
        
        sns.scatterplot(x="time", y=self.plotname, data=self.data)
        plt.savefig(f"{path}.png", format="png")
        
        print(self.data.describe())