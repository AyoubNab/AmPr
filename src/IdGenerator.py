from random import randint

class CreateId:
    def __init__(self, productName:str):
        self.id = ""
        self.id += len(productName)
        self.id += str(randint(0,9))
        self.id += str(int(productName))
        self.id += str(randint(1000,9999))
        
    def __str__(self):
        return self.id

    