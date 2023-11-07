from Racine.product import Product
from Racine.IdGenerator import GenerateId

class CreateProduct:
    def __init__(self):
        
        print("CREATE A NEW PRODUCT !")
        self.productName = str(input("Enter Product Name: "))
        self.productPrice = float(input("Enter Product Price: "))
        self.priceType = str(input("Enter Price Type (Only EURO / DOLLAR) : "))
        self.productQuantity = int(input("Enter Product Quantity: "))
        self.productDescription = str(input("Enter Product Description: "))
        self.productCategory = str(input("Enter Product Category: "))
        self.productId = GenerateId(self.productName).id
        try:
            tempProduct = Product(self.productName, self.productPrice, self.productId, self.productQuantity, self.productCategory, self.priceType, self.productDescription)
            self.product = tempProduct.getProduct()
        except:
            print("Unable to create a product with the provided parameters.")
            return
    
x = CreateProduct()
print(x.product)