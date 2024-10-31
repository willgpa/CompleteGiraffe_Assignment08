########################################################################################################################################################################
# Name: Will Padgett, Aryan Patel, Heitor Previatti                                                                                                                    #
# email:  padgetwg@mail.uc.edu, patel7ag@mail.uc.edu, peviahc@mail.uc.edu                                                                                              #
# Assignment Number: Assignment 08                                                                                                                                     #
# Due Date:   10/31/2024                                                                                                                                               # 
# Course #/Section: 4010/001                                                                                                                                           #
# Semester/Year:   1/4                                                                                                                                                 #
# Brief Description of the assignment:collaborate with peers to develop a VS project modeling something in the real world                                              #                                                                                                                                                                  
# Brief Description of what this module does.  This module models a supplier of a product located in a retail store inventory                                          #                                       
#                                                                                                                                                                      #
# Citations:                                                                                                                                                           #
# Anything else that's relevant:                                                                                                                                       #
########################################################################################################################################################################


class Supplier(object):
    """
    Model a supplier of a product for inventory systems.
    """
    def __init__(self, name, category):
        """
        Constructor
        @param name String: the name of the supplier
        @param category String: The category of the products supplied.
        """
        self.__name = name
        self.__category = category

    def get_category(self):
        """
        @return String: The suppliers product category of the current object.
        """
        return self.__category
    
    def set_category(self, category):
        """
        Assign a value to the supplier product category of the current object
        @param category String: The supplier product category to be assigned.
        """
        self.__category = category

    def set_name(self,value):
        """
        Set a new name for the supplier.

        @param value string: The new name to assign to the supplier.
        """
        self.__name = value
        
    def change_category(self, new_category):
        """
        Change the supplier's category and print a confirmation
        @param new_category String: The new category for the supplier.
        """
        self.__category = new_category
        print(f"Supplier '{self.__name}' Category changed to: {self.__category}")
        
    def __str__(self):
        """
        @return String: A human-readable basic representation of the current object. 
        Useful for debugging, documentation, etc.
        """
        return f"Supplier(Name: {self.__name}, Category: {self.__category})"

    def __repr__(self):
        """
        @return String: A string containing code that can be executed to create a copy of the current object
        """
        return f"Supplier('{self.__name}', '{self.__category}')"
