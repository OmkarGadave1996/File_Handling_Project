from UserMgmt import Toymanagement
from Toy import Toy
if(__name__=="__main__"):
    choice = 0
    # Menu Driven Program
    # Here we have intoduce Encasulation    
    while(choice!=10):
        print("\t\t1.Display All Toys")
        print("\t\t2.Search toy  by ID")
        print("\t\t3.Search toy  by Name")
        print("\t\t4.Add to Cart")
        print("\t\t5.Display Cart")
        print("\t\t6.Edit Cart")
        print("\t\t7.Bill Genration")
        print("\t\t10.Exit")

        choice = int(input("Enter your choice : "))
        if(choice==1):
            Toymanagement.showAllToys()
        
        elif(choice==2):
            id = int(input("Enter Tid to Search"))
            Toymanagement.searchToyById(id)

        elif(choice==3):
            name = input("Enter name to search")
            Toymanagement.searchToyByName(name)
        
        elif(choice==4):
            id = int(input("Enter Tid : "))
            qty = int(input("Enter quantity : "))
            Toymanagement.Add_to_Cart(id,qty)

        elif(choice==5):
            print("ID|Name|Price|Qty")
            Toymanagement.showCart()

        elif(choice==6):
            id = int(input("Id to edit quantity : "))
            qty = int(input("Enter quantity : "))
            Input = input("If you want to add use + and for sub use - ")
            Toymanagement.End_Cart(id,qty,Input)
            Toymanagement.End_Cartedit(id,qty,Input)

        elif(choice==7):
            Toymanagement.Bill_Details()

        elif(choice==10):
            print("---------End of Program---------")

        else:
            print("Invalid Input")