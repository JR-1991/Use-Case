###### Experimentator Klasse #####
import json

class Experimentator(object):
    
    def __init__(self, vorname, nachname, mail, institut):
        
        self.vorname = vorname
        self.nachname = nachname
        self.mail = mail
        self.institut = institut
        
    def __str__(self):
        
        return dict(self.__dict__.items())