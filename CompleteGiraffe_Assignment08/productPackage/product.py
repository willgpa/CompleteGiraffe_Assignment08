# documentation

class Product:
    """
    Model a product in inventory at a retail store.
    """
    def __init__(self, UPC):
        """
        @param UPC: String: Univeral Product Code of the product.
        """
        self.__UPC = UPC

    def get_UPC(self):
        """
        @return String: The UPC of the current product object
        """ 
        return self.__UPC

    def set_UPC(self, UPC):
        """
        Assign a UPC to the current product
        @param UPC: the UPC that is going to be assigned
        """

    def restock_product(self):
        """
        Simulate the restocking of a product
        """
        print(f"Restocking product with UPC:, {self.__UPC}")

    def __str__(self):
        """
        @return String: Representation of the current product object.
        """
        return "UPC: " + self.__UPC

    def __repr__(self):
        """
        @return String: Representing the current product object.
        """
        return f"Product('{self.__UPC}')"
      

