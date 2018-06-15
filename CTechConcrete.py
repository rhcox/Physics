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
        l1=str(random.randint(50,70))
        w1=str(random.randint(35,45))
        l2=str(random.randint(20,30))
        w2=str(random.randint(10,19))
        t1=str(random.randint(3,5))
        t2=str(random.randint(4,6))        
        h1=str(float(random.randint(9,13)/1))
        ww=str(random.randint(25,39))
        hw=str(random.randint(39,55))
        wd=str(random.randint(34,50))
        hd=str(random.randint(30,75))
        wp=str(random.randint(55,85))
        nw=str(random.randint(4,11))
        lwrap=str(random.randint(2,6))
        wwrap=str(random.randint(7,10))
        price=str(random.randint(610,800))

        P=2*52+2*30+2*15+2*10
        Studs=P/8
        answer='Perimeter=$'+str(P)+'ft  '+str(Studs)+' studs$'
        self.f.write('\\GUESSA{You are quoting a concrete pour of two slab.  A foundation for the house is 52 feet by 30 feet and a drive area that is 15 feet by 10 feet.  Both require a frame of 2X4 wood studs.  Calculate the perimeter of each slab and the number of 8 foot studs required to frame the slabs.}{'+answer+'}\n')
        self.f.write('\\GUESS{You are quoting a concrete pour of two slab.  A foundation for the house is '+l1+' feet by '+w1+' feet and a drive area that is '+l2+' feet by '+w2+' feet.  Both require a frame of 2X4 wood studs.  Calculate the perimeter of each slab and the number of 8 foot studs required to frame the slabs.}\n')

        V=52*30*4+15*10*5
        answer='Volume=$'+str(V)+'ft^3$'
        self.f.write('\\GUESSA{You are quoting a concrete pour of two slab.  A foundation for the house is 52 feet by 30 feet and  and 4 inches thick.  The second slab is a drive area that is 15 feet by 10 feet by 5 inches thick to handle larger trucks. Calculate the total volume of both slabs.}{'+answer+'}\n')
        self.f.write('\n\n\\newpage\n\n')
        self.f.write('\\GUESS{You are quoting a concrete pour of two slab.  A foundation for the house is '+l1+' feet by '+w1+' feet and  and '+t1+' inches thick.  The second slab is a drive area that is '+l2+' feet by '+w1+' feet by '+t2+' inches thick to handle larger trucks. Calculate the total volume of both slabs.}\n')
        


        V=math.ceil((float(52*30*4/12+15*10*5/12)/9.0)/10)
        cost=V*600
        answer='Truckloads='+str(V)+' truck     Cost=\$'+str(cost)
        self.f.write('\\GUESSA{You are quoting a concrete pour of two slab.  A foundation for the house is 52 feet by 30 feet and  and 4 inches thick.  The second slab is a drive area that is 15 feet by 10 feet by 5 inches thick to handle larger trucks. If a truck load of concrete is 10 cubic yards, and each truck is costs \$600, how much will it cost for the concrete to pour the slab.}{'+answer+'}\n')
        self.f.write('\\GUESS{You are quoting a concrete pour of two slab.  A foundation for the house is '+l1+' feet by '+w1+' feet and  and '+t1+' inches thick.  The second slab is a drive area that is '+l2+' feet by '+w1+' feet by '+t2+' inches thick to handle larger trucks.If a truck load of concrete is 10 cubic yards, and each truck is costs \$'+price+', how much will it cost for the concrete to pour the slab.}\n')

        self.f.write('\\end{enumerate}\n')

g=Concrete("Construction Technology","Estimate Concrete Pour", "LARGE")
for x in range(1, 50):
    g.WritePage(x)
