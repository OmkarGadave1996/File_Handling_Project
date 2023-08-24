from AdminMgmt import Toymanagement
from Toy import Toy
if(__name__=="__main__"):       
    choice = 0
    # Menu Driven Program
    # Encapsulation
    while(choice!=10):
        print("\t\t1.Add new Toy")
        print("\t\t2.Display All Toy")
        print("\t\t3.Search by tid")
        print("\t\t4.Search by name")
        print("\t\t5.Delete by Tid")
        print("\t\t6.Edit by Tid")
        print("\t\t10.Exit")

        choice = int(input("Enter your choice : "))
        if(choice==1):
            id = int(input("Enter Tid : "))
            name = input("Enter name : ")
            price = float(input("Enter Price : "))
            qty = int(input("Enter quantity : "))
            t = Toy(id,name,price,qty)
            Toymanagement.addToy(t)
                
        elif(choice==2):
            Toymanagement.showAllToys()

        elif(choice==3):
            id = int(input("Enter Tid to Search"))
            Toymanagement.searchToyById(id)

        elif(choice==4):
            name = input("Enter name to search")
            Toymanagement.searchToyByName(name)

        elif(choice==5):
            id = int(input("Enter Tid to delete"))
            Toymanagement.deleteToyById(id)

        elif(choice==6):
            id = int(input("Enter Tid to Edit"))
            Toymanagement.editToyById(id)
                
        elif(choice==10):
            print("---------End of Program---------")

        else:
            print("Invalid Input")
            