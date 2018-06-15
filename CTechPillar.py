import GuessBase
import random
import math

class Concrete(GuessBase.Guess):
    def __init__(self,course, title, rowh):
        super(Concrete, self).__init__(course, title, rowh)

    def PAGE(self):
        self.f.write('\\normalsize\n')
        random.seed(self.rnum)
        
        inner=str(random.randint(13,23))
        price=str(random.randint(550,800))
        priceY=str(random.randint(65,90))
        priceE=str(random.randint(11,30))
        
        l=str(random.randint(12,25))
        w=str(random.randint(5,15))        
        t=str(random.randint(21,50))

        self.f.write('\\begin{enumerate}\n')


        v1=math.ceil((4.0/12.0)*(4.0/12.0)*3.14*11.0)
        answer='Volume=$'+str(v1)+'ft^3$'
        self.f.write('\\GUESSA{To build a tall building you support the foundation with cylindrical piles from the bedrock.  Suppose a pile has a radius of 4 inches and a height of 11 feet.Calculate the volume of concrete.}{'+answer+'}\n')
        self.f.write('\\GUESS{To build a tall building you support the foundation with cylindrical piles from the bedrock.  Suppose a pile has a radius of '+w+' inches and a height of '+l+' feet.Calculate the volume of concrete.}\n')


        v2=math.ceil(20.0*float(v1)/27.0)
        trucks=math.ceil(float(v2)/10)
        answer='Volume=$'+str(v2)+'yards^3$'
        self.f.write('\\GUESSA{To build a tall building you support the foundation with cylindrical piles from the bedrock.  Suppose a pile has a radius of 4 inches and a height of 11 feet. Calculate the volume in yards of concrete to pour 20 pillars.}{'+answer+'}\n')

        self.f.write('\\newpage\n')
                
        self.f.write('\\GUESS{To build a tall building you support the foundation with cylindrical piles from the bedrock.  Suppose a pile has a radius of '+w+' inches and a height of '+l+' feet. Calculate the volume in yards of concrete to pour '+t+' pillars.}\n')
        

        c=trucks*500
        answer='Maximum costs \\$'+str(c)
        self.f.write('\\GUESSA{To build a tall building you support the foundation with cylindrical piles from the bedrock.  Suppose a pile has a radius of 4 inches and a height of 11 feet. If you need to pour 20 pillars, calculate cost of concrete if a truck  costs \\$500, or \\$55 a yard with a \\$10 empty truck fee per yard? }{'+answer+'}\n')
        self.f.write('\\GUESS{To build a tall building you support the foundation with cylindrical piles from the bedrock.  Suppose a pile has a radius of '+w+' inches and a height of '+l+' feet. If you are need to pour '+t+' pillars, calculate cost of concrete if a truck costs \\$'+price+', or \\$'+priceY+' a yard with a \\$'+priceE+' empty truck fee per yard?  .}\n')


        self.f.write('\\end{enumerate}\n')

g=Concrete("Construction Technology","Estimate Pillar", "large")
for x in range(1, 30):
    g.WritePage(x)
