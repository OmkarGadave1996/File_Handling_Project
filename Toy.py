# The Abstract Object is created
class Toy:
    def __init__(self,id,name,prize,qty):
        self.id = id
        self.name = name
        self.prize = prize
        self.quantity = qty

    # Converted into string formatt
    def __str__(self):
        return str(self.tid)+","+self.tname+","+str(self.prize)+","+str(self.quantity)+"\n"