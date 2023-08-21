import datetime
new = datetime.datetime.today()
class Account :
    def __init__(self , name , bolanca):
        self.name = name 
        self.bolanca = bolanca 
    
    
    def deposit(slef , amount):
        slef.bolanca += amount
        print("Don" , amount , new)
    
    def withdraw(slef , amount):
        if  0 < amount <= slef.bolanca :
            slef.bolanca -= amount
            print("withdrae : " , amount , new )
        else :
            print("لايوجد رصيد ")  
            
    def show_bolanca(self):
        print("Account name : {} , has bolanca: {}".format(self.name , self.bolanca))
        
if __name__ == "__main__":
    Abdullah = Account("Abdullah " , 0)
    Abdullah.show_bolanca()
    Abdullah.deposit(2000)
    Abdullah.show_bolanca()
    Abdullah.withdraw(300)
    Abdullah.show_bolanca()
    Abdullah.withdraw(3050)