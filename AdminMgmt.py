from Toy import Toy
import os
class Toymanagement:
    def addToy(t):
        with open("Toydata.txt","a") as fp:
            fp.write(str(t))

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

    def showAllToys():
        if(os.path.exists("Toydata.txt")):
            with open("Toydata.txt","r") as fp:
                data = fp.read()
                print("ID|Name|Price|Qty")
                print(data)
        else:
            print("File is not present")

    def deleteToyById(id):
        if(os.path.exists("Toydata.txt")):
            with open("Toydata.txt","r") as fp:
                allToy = []
                found = False
                for Toy in fp:
                    try:
                        Toy.index(str(id),0,4)
                    except:
                        allToy.append(Toy)
                    else:
                        found = True
            if(found):
                with open("Toydata.txt","w") as fp:
                    for Toy in allToy:
                        fp.write(Toy)
            else:
                print("Record not found")
        else:
            print("File is not present")

    def editToyById(id):
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
                        ans = input("Do you wish to change name(y/n)?")
                        if(ans.lower() == 'y'):
                            Toy[1] = input("Enter new name")
                        ans = input("Do you wish to change price(y/n)?")
                        if(ans.lower() == 'y'):
                            Toy[2] = str(float(input("Enter new price")))
                        ans = input("Do you wish to change quantity(y/n)?")
                        if(ans.lower() == 'y'):
                            Toy[3] = int(input("Enter new quantity"))
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
