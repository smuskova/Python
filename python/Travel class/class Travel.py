class Travel:
    def __init__(self,ID,Destination,Flight,Price):
        self.id=ID
        self.destination=Destination
        self.flight=Flight
        self.price=Price
    def print_info(self):
        print(self.id,self.destination,self.flight,self.price)
    def Reduce(self):
        if self.price>200:
            self.price=self.price*0.1
            
f1=Travel(152,"Maldivi","A2",146)
f2=Travel(326,"Nex York","G4",321)
f1.Reduce()
f1.print_info()
f2.Reduce()
f2.print_info()


    


