from random import randint
import hashlib

class GenerateId:
    def __init__(self, productName:str):
        self.id = ""
        self.id += str(len(productName))
        self.id += str(randint(0,9))
        try:
            self.id += str(int(productName))
        except ValueError:
            #utilise la librairie hashlib pour hasher le nom du produit
            self.id += hashlib.md5(productName.encode()).hexdigest()[:5]
        self.id += str(randint(1000,9999))

    def __str__(self):
        return self.id
