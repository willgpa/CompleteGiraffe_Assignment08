########################################################################################################################################################################
# Name: Will Padgett, Aryan Patel, Heitor Previatti                                                                                                                    #
# email:  padgetwg@mail.uc.edu, patel7ag@mail.uc.edu, peviahc@mail.uc.edu                                                                                              #
# Assignment Number: Assignment 08                                                                                                                                     #
# Due Date:   10/31/2024                                                                                                                                               # 
# Course #/Section: 4010/001                                                                                                                                           #
# Semester/Year:   1/4                                                                                                                                                 #
# Brief Description of the assignment:collaborate with peers to develop a VS project modeling something in the real world                                              #                                                                                                                                                                  
# Brief Description of what this module does.  This module models a product in inventory in a retail store                                                             #                                       
#                                                                                                                                                                      #
# Citations:                                                                                                                                                           #
# Anything else that's relevant:                                                                                                                                       #
########################################################################################################################################################################

class Product:
    """
    Model a product in inventory at a retail store.
    """
    def __init__(self, UPC, name, price, stock=0):
        """
        @param UPC: String: Univeral Product Code of the product.
        @param name: Name of the product.
        @param price: Price of the product.
        @param stock: Stock quantity available (default is 0).
        """
        self.__UPC = UPC
        self.__name = name
        self.__price = price
        self.__stock = stock


    def get_UPC(self):
        """
        @return String: The UPC of the current product object
        """ 
        return self.__UPC

    def UPC(self, value):
        """
        Assign a UPC to the current product
        @param UPC: the UPC that is going to be assigned
        """
        self.UPC = value

    def get_stock(self):
        """
        Get the current stock quantity.
        @return int: The number of units available in stock.
        """
        return self.__stock

    def set_stock(self, value):
        """
        Set the stock quantity of the product.

        @param value int: The new stock quantity to assign.

        @raises ValueError: If the provided stock value is negative.
        """
        if value < 0:
            raise ValueError("Stock cannot be negative")
        self.__stock = value

    def restock_product(self, amount):
        """
        Simulate the restocking of a product
        """
        if amount <=0:
            raise ValueError("Restock amount must be positive")
        self.__stock+= amount
        print(f"Restocking {amount} units of {self.__name}. New stock {self.__stock}")

    def __str__(self):
        """
        @return String: Representation of the current product object.
        """
        return f"Product(Name: {self.__name}, UPC: {self.__UPC}, Price: ${self.__price:.2f}, Stock: {self.__stock})"

    def __repr__(self):
        """
        @return String: Representing the current product object.
        """
        return f"Product('{self.__UPC}', '{self.__name}', {self.__price}, {self.__stock} )"
      

