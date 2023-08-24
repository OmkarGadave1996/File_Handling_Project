# Thus abstract class created for Login
class User:
    def __init__(self,name,pwd):
        self.name = name
        self.pwd = pwd

        
    def __str__(self):
        return str(self.name)+","+str(self.pwd)+"\n"