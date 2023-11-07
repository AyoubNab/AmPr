from variable import COEFFICIENT_DOLLAR

class Card:
    def __init__(self):
        #J'initialise le panier vide
        self.card = {}

    def addProduct(self, product: dict):
        #Ajoute un produit au pannier
        self.card[product["productId"]] = product
    
    def filterProducCategory(self, type: str):
        result = []
        for product in self.card:
            if product["productCategory"] == type:
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
            print(self.card[product]["priceType"])
            if self.card[product]["priceType"] != "EURO":
                total += self.card[product]["productPrice"] * COEFFICIENT_DOLLAR
            elif self.card[product]["priceType"] == "EURO":
                total += self.card[product]["productPrice"]
        return total
    
    def sortCardByLowerPrice(self):
        #AVERTISSEMENT : LES INDEX PEUVENT CHANGER SI JAMAIS UN JAMAIS UN CHANGEMENT EST EFFECTUE
        #Trier le panier par prix decroissant
        result = []
        for product in self.card:
            result.append(self.card[product]["productPrice"])
        return sorted(result)

    def sortCardByHigherPrice(self):
        #AVERTISSEMENT : LES INDEX PEUVENT CHANGER SI JAMAIS UN JAMAIS UN CHANGEMENT EST EFFECTUE
        #Trier le panier par prix croissant
        result = []
        for product in self.card:
            result.append(self.card[product]["productPrice"])
        return sorted(result, reverse=True)
    
    def deleteProductId(self, id: str):
        #Supprime un produit du panier
        if self.card[id]["productQuantity"] == 0:
            del self.card[id]
        else:
            self.card[id]["productQuantity"] -= 1
            
            

#exemple utilisation :
"""
card = Card()
produitG = Product("Pc gamer", 900.00, "900", "asdasdasd", priceType="DOLLAR")
card.addProduct(produitG.getProduct())
produitP = Product("Pizza", 19.99, "20", "Description" )
card.addProduct(produitP.getProduct())
produitG = Product("Pc sad", 10920.00, "10920", "asdasdasd", priceType="DOLLAR")
card.addProduct(produitG.getProduct())

print(card.sortCardByLowerPrice())
card.deleteProductId("10920")
print(card.sortCardByLowerPrice())
"""