import GuessBase
import random
import math

class Concrete(GuessBase.Guess):
    def __init__(self,course, title, rowh):
        super(Concrete, self).__init__(course, title, rowh)

    def PAGE(self):
        self.f.write('\\normalsize\n')
        random.seed(self.rnum)
        self.f.write('\\begin{enumerate}\n')
        l=str(random.randint(150,200))
        w=str(random.randint(75,100))        
        shallow=str(random.randint(30,60))
        deep=str(random.randint(130,200))
        t=str(random.randint(3,9))

        
        inner=str(random.randint(7,15))
        highi=random.randint(14,30)
        high=str(highi)
        deep=str(highi-2)
        thick=str(random.randint(4,11))


        v1=math.ceil(3.14*13/12/3*(7*7*7-6*6*6))
        answer='Volume=$'+str(v1)+'ft^3$'
        self.f.write('\\GUESSA{You are building a fountain with an inner radius of 6 feet and 13 inch high walls, with everything 12 inches thick. Estimate the volume of concrete for the wall of the fountain.}{'+answer+'}\n')
        self.f.write('\\GUESS{You are building a fountain with an inner radius of '+inner+' feet and '+high+' inch high walls, with everything '+thick+' inches thick. Estimate the volume of concrete for the wall of the fountain.}\n')


        v2=math.ceil(3.14*7*7*13/12)
        answer='Volume=$'+str(v2)+'ft^3$'
        self.f.write('\\GUESSA{You are building a fountain with an inner radius of 6 feet and 13 inch high walls, with everything 12 inches thick. Estimate the volume of concrete for the floor of the fountain.}{'+answer+'}\n')
        self.f.write('\\GUESS{You are building a fountain with an inner radius of '+inner+' feet and '+high+' inch high walls, with everything '+thick+' inches thick. Estimate the volume of concrete for the floor of the fountain.}\n')
        


        yards=math.ceil((v1+v2)/27)
        trucks=math.ceil(yards/10)
        answer='Yards=$'+str(yards)+'yd^3$     Trucks='+str(trucks)+' trucks'
        self.f.write('\\GUESSA{You are building a fountain with an inner radius of 6 feet and 13 inch high walls, with everything 12 inches thick. Estimate the yards and total truck needed to pour the fountain.}{'+answer+'}\n')
        self.f.write('\\GUESS{You are building a fountain with an inner radius of '+inner+' feet and '+high+' inch high walls, with everything '+thick+' inches thick. Estimate the volume of concrete for the floor of the fountain.}\n')

        v3=math.ceil(3.14*6*6*10/12*7.5)
        answer='Volume Water='+str(v3)+'gallons'
        self.f.write('\\GUESSA{You are building a fountain with an inner radius of 6 feet. If you are going to fill it 10 inches deep, estimate the gallons of water if 1 cubic foot is 7.5 gallons.}{'+answer+'}\n')
        self.f.write('\\GUESS{You are building a fountain with an inner radius of '+inner+' feet.   If you are going to fill it '+deep+' inches deep, estimate the gallons of water if 1 cubic foot is 7.5 gallons.}\n')

        self.f.write('\\end{enumerate}\n')

g=Concrete("Construction Technology","Estimate Fountain", "large")
for x in range(1, 40):
    g.WritePage(x)
