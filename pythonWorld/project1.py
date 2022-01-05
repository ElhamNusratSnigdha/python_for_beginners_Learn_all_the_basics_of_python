price_product_1 = float(input("What is the price of product 1?"))
quantity_product_1 = float(input("What will be the quantity of product 1?"))
price_product_2 = float(input("What is the price of product 2?"))
quantity_product_2 = float(input("What will be the quantity of product 2?"))
price_product_3 = float(input("What is the price of product 3?"))
quantity_product_3 = float(input("What will be the quantity of product 3?"))

totalPrice_product1 = price_product_1*quantity_product_1
totalPrice_product2 = price_product_2*quantity_product_2
totalPrice_product3 = price_product_3*quantity_product_3


print("Your total bill: "+str(totalPrice_product1+totalPrice_product2+totalPrice_product3))