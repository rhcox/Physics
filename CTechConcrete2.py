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
        lwrap=str(random.randint(2,7))
        wwrap=str(random.randint(7,10))
        price=str(random.randint(610,800))
        priceY=str(random.randint(70,90))
        priceE=str(random.randint(15,30))
        Ri=random.randint(3,9)
        R=str(Ri)
        S=str(Ri+random.randint(2,8))

        P=4*11
        C=3.14*2*4
        answer='Perimeter=$'+str(P)+'ft  Circumference='+str(C)+' fr$'
        self.f.write('\\GUESSA{A square concrete deck is to be built around a circular pond.  The pond has a diameter of 4 feet.  The deck is to be 11 feet on a side.  Calculate the length of the poly form for the interion of the deck and the wooden form for the outside of the deck.}{'+answer+'}\n')
        self.f.write('\\GUESS{A square concrete deck is to be built around a circular pond.  The pond has a diameter of '+R+' feet.  The deck is to be '+S+' feet on a side.  Calculate the length of the poly form for the interion of the deck and the wooden form for the outside of the deck.}')

        V=11*11-3.14*4*4
        answer='Volume=$'+str(V)+'ft^3$'
        self.f.write('\\GUESSA{A square concrete deck is to be built around a circular pond.  The pond has a diameter of 4 feet.  The deck is to be 11 feet on a side.  If the deck is to be 4 inches thick, calculate the volume of concrete needed for the pour.}{'+answer+'}\n')
        self.f.write('\n\n\\newpage\n\n')
        self.f.write('\\GUESS{A square concrete deck is to be built around a circular pond.  The pond has a diameter of '+R+' feet.  The deck is to be '+S+' feet on a side. If the deck is to be '+lwrap+' inches thick, calculate the volume of concrete needed for the pour.}\n')
        


        V=math.ceil((float(11*11-3.14*4*4)/27.0)/10)
        cost=V*600
        answer='Truckloads='+str(V)+' truck     Cost=\$'+str(cost)
        self.f.write('\\GUESSA{A square concrete deck is to be built around a circular pond.  The pond has a diameter of 4 feet.  The deck is to be 11 feet on a side.  If the deck is to be 4 inches thick, calculate the cost of the concrete.  Assume that a truck holds 10 yards, that each truck is \$600 or \$70 a yard with a \$20 per yard empty truck fee.}{'+answer+'}\n')
        self.f.write('\\GUESS{A square concrete deck is to be built around a circular pond.  The pond has a diameter of '+R+' feet.  The deck is to be '+S+' feet on a side. If the deck is to be '+lwrap+' inches thick,  calculate the cost of the concrete.  Assume that a truck holds 10 yards, that each truck is \$'+price+' or \$'+priceY+' a yard with a \$'+priceE+' per yard empty truck fee.}\n')

        self.f.write('\\end{enumerate}\n')

g=Concrete("Construction Technology","Estimate Pond Deck", "LARGE")
for x in range(1, 20):
    g.WritePage(x)
