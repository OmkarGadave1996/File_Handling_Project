from Toy import Toy
import os
class Toymanagement:
    def showAllToys():
        if(os.path.exists("Toydata.txt")):
            with open("Toydata.txt","r") as fp:
                data = fp.read()
                print("ID|Name|Price|Qty")
                print(data)
        else:
            print("File is not present")

    def showCart():
        if(os.path.exists("CartDetails.txt")):
            with open("CartDetails.txt","r") as fp:
                data = fp.read()
                print("ID|Name|Price|Qty")
                print(data)
        else:
            print("File is not present")

    def searchToyById(id):
        if(os.path.exists("Toydata.txt")):
            with open("Toydata.txt","r") as fp:
                for Toy in fp:
                    try:
                        Toy.index(str(id),0,4)
                    except:
                        pass
                    else:
                        print("ID|Name|Price|Qty")
                        print(Toy)
                        break
                else:
                    print("Record Not Found")
        else:
            print("File is not present")

    def searchToyByName(name):
        if(os.path.exists("Toydata.txt")):
            with open("Toydata.txt","r") as fp:
                for Toy in fp:
                    if(name in Toy):
                        print("ID|Name|Price|Qty")
                        print(Toy)
                        break
                else:
                    print("Record not found")
        else:
            print("File is not present")


    def Add_to_Cart(id,qty):
        if(os.path.exists("Toydata.txt")):
            with open("Toydata.txt","r") as fp:
                allToy = []
                found = False
                for Toy in fp:
                    try:
                        Toy.index(str(id),0,4)
                    except:
                        pass
                    else:
                        try:
                            found = True
                        except:
                            pass            
                        else:
                            Toy = Toy.split(",")
                            if((int(Toy[4])-qty)>0):
                                Toy[3] = int(Toy[3]) - qty
                                Toy[3] = str(Toy[3])+"\n"
                                Toy = ",".join(Toy)
                                Toy1 = Toy.split(",")
                                Toy1[3] = qty
                                Toy1[3] = str(Toy1[3])+"\n"
                                Toy1 = ",".join(Toy1) 
                                with open("CartDetails.txt","a") as fp:
                                    fp.write(Toy1)
                            else:
                                print("Invalid Quantity")
                                Toy = ",".join(Toy)
                    finally:
                        allToy.append(Toy)
            if(found):
                with open("Toydata.txt","w") as fp:
                    for Toy in allToy:
                        fp.write(Toy)
            else:
                print("Record not found")
        else:
            print("File is not present")


    def End_Cart(id,qty,Input):
        if(os.path.exists("CartDetails.txt")):
            with open("CartDetails.txt","r") as fp:
                allToy = []
                found = False
                for Toy in fp:
                    try:
                        Toy.index(str(id),0,4)
                    except:
                        pass
                    else:
                        found = True
                        ans = input("Do you want to change quantity(y/n)?")
                        if(ans.lower() == 'y'):
                            Toy = Toy.split(",")
                            if(Input == '-'):
                                Toy[3]= int(Toy[3]) - qty
                                Toy[3] = str(Toy[3])+"\n"
                            else:
                                Toy[3]= int(Toy[3]) + qty
                                Toy[3] = str(Toy[3])+"\n"
                            Toy = ",".join(Toy)
                    finally:
                        allToy.append(Toy)
            if(found):
                with open("CartDetails.txt","w") as fp:
                    for Toy in allToy:
                        fp.write(Toy)
            else:
                print("Record not found")
        else:
            print("File is not present")
            
    def End_Cartedit(id,qty,Input):
        if(os.path.exists("Toydata.txt")):
            with open("Toydata.txt","r") as fp:
                allToy = []
                found = False
                for Toy in fp:
                    try:
                        Toy.index(str(id),0,4)
                    except:
                        pass
                    else:
                        found = True
                        Toy = Toy.split(",")
                        if(Input == '-'):
                            Toy[3]= int(Toy[3]) + qty
                            Toy[3] = str(Toy[3])+"\n"
                        else:
                            Toy[3]= int(Toy[3]) - qty
                            Toy[3] = str(Toy[3])+"\n"
                        Toy = ",".join(Toy)
                    finally:
                        allToy.append(Toy)
            if(found):
                with open("Toydata.txt","w") as fp:
                    for Toy in allToy:
                        fp.write(Toy)
            else:
                print("Record not found")
        else:
            print("File is not present")

    def Bill_Details():
        with open("Bill_of_Material.txt","w") as fp:
            fp.write("Bill Of Material\n")
            fp.write("----------------\n")
            fp.write("Id  Item name  Price Qty  Subtotal   \n")
            fp.write("--------------------------------------------\n")
        if(os.path.exists("CartDetails.txt")):
            with open("CartDetails.txt","r") as fp:
                Total = 0
                for Toy in fp:
                    Toy = Toy.strip()
                    Toy = Toy.split(",")
                    total = float(Toy[2])*int(Toy[4])
                    Total = Total + total 
                    Toy.append(str(total))
                    Toy = "    ".join(Toy)+"\n"
                    with open("Bill_of_Material.txt","a") as fp:
                        fp.write(Toy)
                with open("Bill_of_Material.txt","a") as fp:
                        fp.write("--------------------------------------------\n")
                        fp.write("                          Total : ")
                        fp.write(str(Total))
                        fp.write("\n                        GST 18% : ")
                        fp.write(str(int(Total*0.18)))
                        fp.write("\n                    Grand Total : ")
                        fp.write(str(Total+(Total*0.18)))
            open("CartDetails.txt","w")
        else:
            print("File is not present")