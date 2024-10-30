class supplier(object):
    """
    Model a supplier of a product for inventory systems.
    """
    def __init__(self, category):
        """
        Constructor
        @param category String: The category of the products supplied
        """
        self.__category = category

    def get_category(self):
        """
        @return String: The suppliers product category of the current object
        """
        return self.__category
    
    def set_category(self, category):
        """
        Assign a value to the supplier product category of the current object
        @param category String: The supplier product category to be assigned.
        """
        self.__category = category
        
    def change_category(self, new_category):
        """
        Change the supplier's category and print a confirmation
        @param new_category String: The new category for the supplier.
        """
        self.__category = new_category
        print(f"Category changed to: {self.__category}")
        
    def __str__(self):
        """
        @return String: A human-readable basic representation of the current object. 
        Useful for debugging, documentation, etc.
        """
        return "category: " + self.__category

    def __repr__(self):
        """
        @return String: A string containing code that can be executed to create a copy of the current object
        """
        return f"supplier('{self.__category}')"
