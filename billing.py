class product:
    
        def __init__(self):
            self.name=""
            self.cost=0
            self.quantity=0
            
        def input_product(self):
            self.name=input("Enter The Name of The Product: ")
            self.cost=int(input("Enter The Cost: "))
            self.quantity=int(input("Enter the Quantity in kgs: "))
class bill(product):
    def print_bill(self):
        print("\nBILL DETAILS")
        print("\nName of The Product: ",self.name)
        print("\nPrice: ",self.cost)
        print("\nQuantity: ",self.quantity)
        print("\nTotal Price: ",self.cost*self.quantity)
no=int(input("Enter The No of Grocery Items: "))
for i in range(no):
    i=bill()
    i.input_product()


            
            
