from product import Product

if __name__ == "__main__":
    product = Product("123456789012")
    print(product)  

    # Test restocking
    product.restock_product()  

    # Test setting a new UPC
    product.set_UPC("987654321098")
    print("Updated Product:", product)

    # Test __repr__
    print(repr(product))  