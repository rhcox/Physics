import GuessBase
import random
import math

class Concrete(GuessBase.Guess):
    def __init__(self,course, title, rowh):
        super(Concrete, self).__init__(course, title, rowh)

    def PAGE(self):
        self.f.write('\\normalsize\n')
        random.seed(self.rnum)
        
        stand=str(random.randint(10,28))
        wall=str(random.randint(11,25))
        thick=str(random.randint(8,20))
        height=str(random.randint(2,7))
        floor=str(random.randint(15,30))
        price=str(random.randint(600,900))        
        priceY=str(random.randint(70,100))
        priceE=str(random.randint(20,40))
        
        self.f.write('\\begin{enumerate}\n')

        v1=math.ceil(pow((10.0/2+6.0/12.0),2)*3.14*14.0/12.0)
        answer='Volume=$'+str(v1)+'ft^3$'
        self.f.write('\\GUESSA{A fountain has a center stand 11 inches in radius and a wall 10 feet inner diameter with 6 inch thick walls, all 1 feet high. The floor is 14 inches thick. Calculate the concrete for the floor.}{'+answer+'}\n')
        self.f.write('\\GUESS{A fountain has a center stand '+stand+' inches in radius and a wall '+wall+' feet inner diameter with '+thick+' inch thick walls, all '+height+' feet high. The floor is '+floor+' inches thick. Calculate the concrete for the floor.}\n')

        v2=math.ceil(pow(11.0/12.0,2)*3.14*1.0)
        answer='Volume=$'+str(v2)+'ft^3$'
        self.f.write('\\GUESSA{A fountain has a center stand 11 inches in radius and a wall 10 feet inner diameter with 6 inch thick walls, all 1 feet high. The floor is 14 inches thick. Calculate the concrete for the stand.}{'+answer+'}\n')
        self.f.write('\\GUESS{A fountain has a center stand '+stand+' inches in radius and a wall '+wall+' feet inner diameter with '+thick+' inch thick walls, all '+height+' feet high. The floor is '+floor+' inches thick. Calculate the concrete for the stand.}\n')

        v3=math.ceil((pow((10.0/2.0+6.0/12.0),2)*3.14-pow(10.0/2.0,2)*3.14)*1.0)
        answer='Volume=$'+str(v3)+'ft^3$'
        self.f.write('\\GUESSA{A fountain has a center stand 11 inches in radius and a wall 10 feet inner diameter with 6 inch thick walls, all 1 feet high. The floor is 14 inches thick. Calculate the concrete for the wall.}{'+answer+'}\n')
        self.f.write('\\GUESS{A fountain has a center stand '+stand+' inches in radius and a wall '+wall+' feet inner diameter with '+thick+' inch thick walls, all '+height+' feet high. The floor is '+floor+' inches thick. Calculate the concrete for the wall.}\n')

        vy=math.ceil((v1+v2+v3)/27.0)
        truck=math.ceil(float(vy)/10.0)
        cmax=truck*500
        cmin=5*60+5*15
        answer='Volume=$'+str(vy)+'yd^3$ Trucks='+str(truck)+'     CostMax='+str(cmax)+' CostMin='+str(cmin)
        self.f.write('\\GUESSA{For this fountain, if a truck is \$500, or \$60 a yard and \$15 empty truck fee, calculate the maximum and minimum cost for the concrete.}{'+answer+'}\n')
        self.f.write('\\GUESS{For this fountain, if a truck is \$'+price+', or \$'+priceY+' a yard and \$'+priceE+' empty truck fee, calculate the maximum and minimum cost for the concrete.}\n')

        
        self.f.write('\\end{enumerate}\n')

g=Concrete("Construction Technology","Circular Pond", "large")
for x in range(1, 30):
    g.WritePage(x)
