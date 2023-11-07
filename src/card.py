from product import Product

class Card:
    def __init__(self):
        #J'initialise le panier vide
        self.card = []

    def addProduct(self, product: list):
        #Ajoute un produit au pannier
        self.card.append(product)
    
    def getProducType(self, type: str):
        #AVERTISSEMENT : LES INDEX PEUVENT CHANGER SI JAMAIS UN JAMAIS UN CHANGEMENT EST EFFECTUE
        result = []
        for product in self.card:
            if product[3] == type:
                result.append(product)
        return result
    
    def getProduct(self, index: int):
        try:
            return self.card[index]
        except:
            return None
        
    def getCard(self):
        #Retourne le panier
        return self.card
    
    def getCardLength(self):
        #Retourne la taille du panier
        return len(self.card)
    
    def clearCard(self):
        #Vide le panier
        self.card = []

    def getCardPrice(self):
        #AVERTISSEMENT : LES INDEX PEUVENT CHANGER SI JAMAIS UN JAMAIS UN CHANGEMENT EST EFFECTUE
        #Calcule le prix total du panier
        total = 0
        for product in self.card:
            total += product[1]
        return total