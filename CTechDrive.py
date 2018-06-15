import GuessBase
import random
import math

class Concrete(GuessBase.Guess):
    def __init__(self,course, title, rowh):
        super(Concrete, self).__init__(course, title, rowh)

    def PAGE(self):
        self.f.write('\\normalsize\n')
        random.seed(self.rnum)
        
        l=str(random.randint(21,50))
        w=str(random.randint(10,20))        
        t=str(random.randint(3,7))
        inner=str(random.randint(13,23))
        price=str(random.randint(550,800))
        priceY=str(random.randint(65,90))
        priceE=str(random.randint(11,30))
        
        self.f.write('\\begin{enumerate}\n')


        v1=math.ceil((30*8-(28*11/12))*2)
        answer='Volume=$'+str(v1)+'ft^3$'
        self.f.write('\\GUESSA{A driveway will be 30 feet by 8 feet with a 11 inches of empty space in the middle with one for endcaps.  The driveway will be 2 feet thick.  Calculate the volume of concrete .}{'+answer+'}\n')
        self.f.write('\\GUESS{A driveway will be '+l+' feet by '+w+' feet with a '+inner+' inches of empty space in the middle with one for endcaps.  The driveway will be '+t+' feet thick.  Calculate the volume of concrete .}\n')


        v2=math.ceil(float(v1)/27.0)
        trucks=math.ceil(float(v2)/10)
        answer='Volume=$'+str(v2)+'yards^3$       Trucks='+str(trucks)+' Trucks'
        self.f.write('\\GUESSA{A driveway will be 30 feet by 8 feet with a 11 inches of empty space in the middle with one for endcaps.  The driveway will be 2 feet thick.  Calculate the yards and trucks of concrete required .}{'+answer+'}\n')
        self.f.write('\\GUESS{A driveway will be '+l+' feet by '+w+' feet with a '+inner+' inches of empty space in the middle with one for endcaps.  The driveway will be '+t+' feet thick.  Calculate the volume of concrete .}\n')
        

        c=trucks*500
        answer='Maximum costs \\$'+str(c)
        self.f.write('\\GUESSA{A driveway will be 30 feet by 8 feet with a 11 inches of empty space in the middle with one for endcaps.  The driveway will be 2 feet thick. Calculate cost of concrete if a truck  costs \\$500, or \\$55 a yard with a \\$10 empty truck fee per yard, how much wil the concrete cost? .}{'+answer+'}\n')
        self.f.write('\\GUESS{A driveway will be '+l+' feet by '+w+' feet with a '+inner+' inches of empty space in the middle with one for endcaps.  The driveway will be '+t+' feet thick. Calculate cost of concrete if a truck costs \\$'+price+', or \\$'+priceY+' a yard with a \\$'+priceE+' empty truck fee per yard?  .}\n')

        v3=math.ceil((28*11/12)*2)
        answer='Volume Soil=$'+str(v3)+'ft^3$'
        self.f.write('\\GUESSA{For this driveway, calcuate the soil needed to fill the middle.}{'+answer+'}\n')
        self.f.write('\\GUESS{For your driveway, calcuate the soil needed to fill the middle.}\n')

        self.f.write('\\end{enumerate}\n')

g=Concrete("Construction Technology","Estimate Driveway", "large")
for x in range(1, 40):
    g.WritePage(x)
