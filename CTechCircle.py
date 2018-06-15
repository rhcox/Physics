import GuessBase
import random
import math

class Concrete(GuessBase.Guess):
    def __init__(self,course, title, rowh):
        super(Concrete, self).__init__(course, title, rowh)

    def PAGE(self):
        self.f.write('\\normalsize\n')
        random.seed(self.rnum)

        thick=str(random.randint(8,20))
        radius=str(random.randint(21,60))
        price=str(random.randint(600,900))        
        priceY=str(random.randint(70,100))
        priceE=str(random.randint(20,40))

        
        
        self.f.write('\\begin{enumerate}\n')

        v1=math.ceil(3.14*15.0*15.0*13.0/12.0)
        answer='Volume=$'+str(v1)+'ft^3$'
        self.f.write('\\GUESSA{An arena is to built on a circular foundation with a radius of 15 feet.  The thickness is 13 inches. Calculate the volume in cubic feet of the concrete required for the foundation.}{'+answer+'}\n')
        self.f.write('\\GUESS{An arena is to built on a circular foundation with a radius of '+radius+' feet.  The thickness is '+thick+' inches. Calculate the volume in cubic feet of the concrete required for the foundation.}\n')
        
        v2=math.ceil(v1/27.0)
        answer='Volume=$'+str(v2)+'yards^3$'
        self.f.write('\\GUESSA{An arena is to built on a circular foundation with a radius of 15 feet.  The thickness is 13 inches. Calculate the yards of concrete required for the foundation.}{'+answer+'}\n')
        self.f.write('\\GUESS{An arena is to built on a circular foundation with a radius of '+radius+' feet.  The thickness is '+thick+' inches. Calculate the yards of concrete required for the foundation.}\n')
        
        v3=math.ceil(v2/10.0)
        answer=str(v3)+'trucks'
        self.f.write('\\GUESSA{An arena is to built on a circular foundation with a radius of 15 feet.  The thickness is 13 inches. Calculate the number of trucks needed for the amount of concrete.}{'+answer+'}\n')
        self.f.write('\\GUESS{An arena is to built on a circular foundation with a radius of '+radius+' feet.  The thickness is '+thick+' inches.  Calculate the number of trucks needed for the amount of concrete.}\n')


        cmax=v3*500
        cmin=2*500+9*60+1*15
        answer='CostTrucks=\\$'+str(cmax)+' CostPartial=\\$'+str(cmin)
        self.f.write('\\GUESSA{An arena is to built on a circular foundation with a radius of 15 feet.  The thickness is 13 inches. If a truck is \\$500, a yard is \\$60, and an  ampty yard is \$15, calculate the minimum and maximum cost for the trucks of concrete.}{'+answer+'}\n')
        self.f.write('\\GUESS{An arena is to built on a circular foundation with a radius of '+radius+' feet.  The thickness is '+thick+' inches.  If a truck is \\$'+price+', a yard is \\$'+priceY+', and an  ampty yard is \\$'+priceE+', calculate the minimum and maximum cost for the trucks of concrete.}\n')
        
        self.f.write('\\end{enumerate}\n')

g=Concrete("Construction Technology","Circular Foundation", "large")
for x in range(1, 30):
    g.WritePage(x)
