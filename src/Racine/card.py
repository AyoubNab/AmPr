from Racine.variable import COEFFICIENT_EURO, COEFFICIENT_DOLLAR
from Racine.IdGenerator import GenerateId
from Racine.product import Product

class Card:
    def __init__(self):
        #J'initialise le panier vide
        self.card = {}

    def getProductId(self, productName: str):
        for product in self.card:
            if self.card[product]["productName"] == productName:
                return product

    def addProduct(self, product: dict):
        #Ajoute un produit au pannier
        self.card[product["productId"]] = product
    
    def filterProducCategory(self, type: str):
        result = []
        for product in self.card:
            if product["productCategory"] == type:
                result.append(product)
        return result
    

        
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
            
    def buyProduct(self, productName: str, quantity: int, currentMoney: float, currentMoneyType: str) -> None:
        #permet de acheter des produits
        #parametres : quantity -> nombre
        #retourne : rien
        product_id = self.getProductId(productName)
        price = 0
        if quantity > self.card[product_id]["productQuantity"]:
            return
        if currentMoneyType == "EURO":
            if self.card[product_id]["priceType"] == "DOLLAR":
                price = self.card[product_id]["productPrice"] * COEFFICIENT_DOLLAR
                price *= quantity
                if price > currentMoney:
                    return
                else:
                    currentMoney -= price
                    for _ in range(quantity):
                        self.deleteProductId(product_id)
                    stock = {"productName":productName,
                                "productPrice":self.card[product_id]["productPrice"],
                                  "productId":product_id,
                                    "productQuantity":self.card[product_id]["productQuantity"],
                                      "productCategory":self.card[product_id]["productCategory"],
                                        "priceType":self.card[product_id]["priceType"],
                                          "productDescription":self.card[product_id]["productDescription"]}
                    
                    print(f"New stock for {productName} -> {self.card[product_id]}")
                    return [currentMoney, stock]
                
            else:
                price = self.card[product_id]["productPrice"] * quantity
                if price > currentMoney:
                    return
                else:
                    currentMoney -= price
                    for _ in range(quantity):
                        self.deleteProductId(product_id)
                    stock = {"productName":productName,
                                "productPrice":self.card[product_id]["productPrice"],
                                  "productId":product_id,
                                    "productQuantity":quantity,
                                      "productCategory":self.card[product_id]["productCategory"],
                                        "priceType":self.card[product_id]["priceType"],
                                          "productDescription":self.card[product_id]["productDescription"]}
                    
                    print(f"New stock for {productName} -> {self.card[product_id]}")
                    return [currentMoney, stock]

        elif currentMoneyType == "DOLLAR":
            if self.card[product_id]["priceType"] == "EURO":
                price = self.card[product_id]["productPrice"] * COEFFICIENT_EURO
                price *= quantity
                if price > currentMoney:
                    return
                else:
                    currentMoney -= price
                    for _ in range(quantity):
                        self.deleteProductId(product_id)
                    
                    stock = {"productName":productName,
                                "productPrice":self.card[product_id]["productPrice"],
                                  "productId":product_id,
                                    "productQuantity":self.card[product_id]["productQuantity"],
                                      "productCategory":self.card[product_id]["productCategory"],
                                        "priceType":self.card[product_id]["priceType"],
                                          "productDescription":self.card[product_id]["productDescription"]}
                    
                    print(f"New stock for {productName} -> {self.card[product_id]}")
                    return [currentMoney, stock] 
                
            else:
                price = self.card[product_id]["productPrice"] * quantity
                if price > currentMoney:
                    return
                else:
                    currentMoney -= price
                    for _ in range(quantity):
                        self.deleteProductId(product_id)
                    
                    stock = {"productName":productName,
                                "productPrice":self.card[product_id]["productPrice"],
                                  "productId":product_id,
                                    "productQuantity":self.card[product_id]["productQuantity"],
                                      "productCategory":self.card[product_id]["productCategory"],
                                        "priceType":self.card[product_id]["priceType"],
                                          "productDescription":self.card[product_id]["productDescription"]}
                    
                    print(f"New stock for {productName} -> {self.card[product_id]}")
                    return [currentMoney, stock]        

        self.updateGloablProduct()        