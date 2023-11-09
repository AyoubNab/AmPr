from variable import COEFFICIENT_EURO, COEFFICIENT_DOLLAR
from IdGenerator import GenerateId
from product import Product

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


    def __buy__(self, productName: str, quantity: int, product_id):
        for _ in range(quantity):
                self.deleteProductId(product_id)
        stock = {"productName":productName,
                    "productPrice":self.card[product_id]["productPrice"],
                    "productId":product_id,
                    "productQuantity":self.card[product_id]["productQuantity"],
                    "productCategory":self.card[product_id]["productCategory"],
                    "priceType":self.card[product_id]["priceType"],
                    "productDescription":self.card[product_id]["productDescription"]}
        return stock

    def __convertMoney__(self, money, moneyType):
        if moneyType == "EURO":
            money *= COEFFICIENT_EURO
        elif moneyType == "DOLLAR":
            money *= COEFFICIENT_DOLLAR
        return money

    def buyProduct(self, productName: str, quantity: int, currentMoney: float, currentMoneyType: str) -> None:
        #permet de acheter des produits
        #parametres : quantity -> nombre
        #retourne : rien
        #verification du currentMoneyType
        if currentMoneyType != "EURO" and currentMoneyType != "DOLLAR":
            currentMoneyType = "EURO"
        product_id = self.getProductId(productName)
        price = 0
        #verification de la quantité de produits
        if quantity > self.card[product_id]["productQuantity"]:
            print("You cannot take that many items as there are no more left in storage.")
        priceTypeProduct = self.card[product_id]["priceType"]

        if currentMoneyType == priceTypeProduct:
            price = self.card[product_id]["productPrice"]
            price *= quantity
            if price > currentMoney:
                return
            currentMoney -= price
            stock = self.__buy__(productName, quantity, product_id)
            return [currentMoney, stock]
                
        if currentMoneyType :
            price = self.__convertMoney__(self.card[product_id]["productPrice"], priceTypeProduct)
            price *= quantity
            if price > currentMoney:
                return
            currentMoney -= price
            stock = self.__buy__(productName, quantity, product_id)
            return [currentMoney, stock]     

iphone = Product("Iphone 14", 999.99, GenerateId("Iphone 14").id, 10, "Electronics", "DOLLAR", "Iphone 14")
pcgamer = Product("PC Gamer", 999.99, GenerateId("PC Gamer").id, 10, "Electronics", "DOLLAR", "PC Gamer")

card = Card()

card.addProduct(iphone.getProduct())
card.addProduct(pcgamer.getProduct())


print(card.getCard())
print("\n")
money,stock = card.buyProduct("Iphone 14", 1, 1000, "DOLLAR")
print(stock)
print("\n")
print(money)