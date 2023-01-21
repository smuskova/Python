class Travel:
    def __init__(self,ID,Destination,Flight,Price):
        self.id=ID
        self.destination=Destination
        self.flight=Flight
        self.price=Price
    def print(self):
        print(self.id,self.destination,self.flight,self.price)
    def Reduce(self):
        if self.price>200:
            self.price=selp.price%10
filename= "trevel.txt"
with open(filename, "r") as f:
    data= f.read()
    print(data)
travel1=Travel(254,'Maldivi', 'flight135', 356)
travel1.print()
travel1.Reduce()
trevel1.print()

