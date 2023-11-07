# AmPr

AmPr est un algorithme Python qui permet de créer des produits, de les ajouter dans un panier, de vérifier le stock, d'en acheter, et qui s'occupe des conversions des prix USD / EUR. D'autres monnaies seront bientôt prises en charge.

## Installation

Pour installer ce projet, vous pouvez cloner ce dépôt en utilisant la commande git suivante :

```bash
git clone <url_du_dépôt>
```

Utilisation
Product.py
Product.py est la base du produit. Il s’agit d’une classe qui a plusieurs attributs :
```

-“productName” : le nom du produit
-“productPrice” : le prix du produit
-“productId” : l’identifiant du produit
-“productQuantity” : la quantité de produits qui sont dans le pack (utilisé dans la fonction card pour les achats)
-“productCategory” : la catégorie du produit
-“priceType” : la monnaie utilisée, soit EURO / DOLLAR
-“productDescription” : la description du produit

```

Voici comment vous pouvez créer un produit :
```python
  from product import Product
- # Créer un produit
  product = Product("Nom du produit", 10.0, "id_du_produit", 100, "Catégorie", "EURO", "Description du produit")
  Vous pouvez également obtenir les informations sur un produit en utilisant les méthodes fournies :

- # Obtenir le nom du produit
  name = product.getProductName()

- # Obtenir le prix du produit
  price = product.getProductPrice()
```
Contribution
Les contributions sont les bienvenues. Pour contribuer, vous pouvez ouvrir une issue ou faire une pull request.

Licence
Ce projet est sous licence MIT.

