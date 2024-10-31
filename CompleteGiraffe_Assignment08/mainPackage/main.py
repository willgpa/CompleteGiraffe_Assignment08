########################################################################################################################################################################
# Name: Will Padgett, Aryan Patel, Heitor Previatti                                                                                                                    #
# email:  padgetwg@mail.uc.edu, patel7ag@mail.uc.edu, peviahc@mail.uc.edu                                                                                              #
# Assignment Number: Assignment 08                                                                                                                                     #
# Due Date:   10/31/2024                                                                                                                                               # 
# Course #/Section: 4010/001                                                                                                                                           #
# Semester/Year:   1/4                                                                                                                                                 #
# Brief Description of the assignment:collaborate with peers to develop a VS project modeling something in the real world                                              #                                                                                                                                                                  
# Brief Description of what this module does.  This module demonstrates funtionality of product and supplier.py                                                        #                                       
#                                                                                                                                                                      #
# Citations:                                                                                                                                                           #
# Anything else that's relevant:                                                                                                                                       #
########################################################################################################################################################################
from productPackage.product import Product
from supplierPackage.supplier import Supplier

if __name__ == "__main__":
   # Create a new product
    product = Product("123456789012", "Laptop", 999.99, 10)

    # Print product details
    print(product)

    # Restock the product
    product.restock_product(5)

    # Set a new stock value using the setter
    product.set_stock(20)
    print(f"Updated stock: {product.get_stock()}")

    # Use __repr__ to create a new product object
    new_product = eval(product.__repr__())
    print("New Product from repr:", new_product)
    print("************************************************************************************************************")
    # Create a supplier instance
    supplier = Supplier("ABC Electronics", "Electronics")

    # Print the supplier using __str__
    print(supplier)  

    # Change the supplier's category
    supplier.change_category("Home Appliances")

    # Update the supplier's name
    supplier.set_name("XYZ Electronics")
    print(f"Updated Supplier Name: {supplier}")

    # Use __repr__ to create a new supplier 
    new_supplier = eval(supplier.__repr__())
    print("New Supplier from repr:", new_supplier)

    # New supplier's category
    print(f"New Supplier's Category: {new_supplier.get_category()}")
