from variable import COEFFICIENT_EURO, COEFFICIENT_DOLLAR
class Product:
    def __init__(self, productName: str, productPrice: float, productId: str, productQuantity: int, productCategory: str ="ALL", priceType: str ="EURO", productDescription: str = "EMPTY"):
        #creation des variables necessaires pour le produit
        #stockage des donnee dans la variable globalProduct qui sera utilise ulterieurment
        #parametres : productName -> string, productPrice -> nombre a virgule, productId -> string
        #parametres : priceType -> string (EURO / DOLLAR), productDescription -> string
        #parametres : productCategory -> string (ALL / FOOD / DRINK / ELECTRONICS ...)
        #retourne : globalProduct

        #verification de la monnaire utilise si elle n'est pas reconnue automatiquement EURO
        if priceType != "EURO" and priceType != "DOLLAR":
            priceType = "EURO"

        #verification de la taille du nom du produit si elle est trop petite ou grande elle est racourics
        if len(productName) < 4:
            productName = "EMPTY"
        if len(productName) > 20:
            productName = productName[:20]

        #verification de la taille de la description du produit si elle est trop petite ou grande elle est racouric
        if len(productDescription) < 4:
            productDescription = "EMPTY"

        if len(productDescription) > 200:
            productDescription = productDescription[:197]
            productDescription += "..."

        self.productName = productName
        self.productPrice = productPrice
        self.productId = productId
        self.productQuantity = productQuantity
        self.productCategory = productCategory
        self.priceType = priceType
        self.productDescription = productDescription
        
        #AVERTISSEMENT : TOUT CHANGEMENT DU PLACEMENT DE CES VARIABLES DANS LA VARIABLE GLOBAL PRODUCT PEUVENT CAUSER UNE ERREUR
        self.globalProduct = {"productName":self.productName,
                                "productPrice":self.productPrice,
                                  "productId":self.productId,
                                    "productQuantity":self.productQuantity,
                                      "productCategory":self.productCategory,
                                        "priceType":self.priceType,
                                          "productDescription":self.productDescription}
       
    
    def updateGloablProduct(self) -> None:
        #met a jour la variable globalProduct
        #parametres : rien
        #retourne : rien
        #AVERTISSEMENT : TOUT CHANGEMENT DU PLACEMENT DE CES VARIABLES DANS LA VARIABLE GLOBAL PRODUCT PEUVENT CAUSER UNE ERREUR
        self.globalProduct = {"productName":self.productName,
                                "productPrice":self.productPrice,
                                  "productId":self.productId,
                                    "productQuantity":self.productQuantity,
                                      "productCategory":self.productCategory,
                                        "priceType":self.priceType,
                                          "productDescription":self.productDescription}

    def getProduct(self) -> None:
        #retourne la variable globalProduct (qui stocke tout les atribus du produit)
        #parametres : rien
        #retourne : globalProduct
        return self.globalProduct
    
    def modifyDescription(self, newDescription: str) -> None:
        #change la description du produit
        #parametres : newDescription -> string
        #retourne : rien
        self.productDescription = newDescription
        self.updateGloablProduct()


    def getProductName(self) -> str:
        #retourne le nom du produit
        #parametres : rien
        #retourne : productName
        return self.productName

    def getProductPrice(self) -> float:
        #retourne le prix du produit
        #parametres : rien
        #retourne : productPrice
        return self.productPrice
    
    def getProductId(self) -> str:
        #retourne l'id du produit
        #parametres : rien
        #retourne : productId
        return self.productId

    def getProductCategory(self) -> str:
        #retourne le type du produit
        #parametres : rien
        #retourne : productCategory
        return self.productCategory

    def getPriceType(self) -> str:
        #retourne la monnaie utilise
        #parametres : rien
        #retourne : productPrice
        return self.priceType
    
    def getProductDescription(self) -> str:
        #retourne la description du produit
        #parametres : rien
        #retourne : productDescription
        return self.productDescription
    
    
    def changePriceType(self):
        #change la monnaie utilise et convertis la valeur
        #parametres : rien
        #retourne : rien
        if self.priceType == "EURO":
            self.productPrice = self.productPrice * COEFFICIENT_DOLLAR
            self.priceType = "DOLLAR"
        if self.priceType == "DOLLAR":
            self.productPrice = self.productPrice * COEFFICIENT_EURO
            self.priceType = "EURO"
       
    