import GuessBase
import random
import math

class Rebar(GuessBase.Guess):
    def __init__(self,course, title, rowh):
        super(Rebar, self).__init__(course, title, rowh)

    def PAGE(self):
        self.f.write('\\normalsize\n')
        random.seed(self.rnum)
        self.f.write('\\begin{enumerate}\n')

        l1=str(random.randint(8,16)*2)
        w1=str(random.randint(10,18)*2)       
        prices=str(float(random.randint(200,300))/100)
        P=2*22+2*18
        Studs=P/8
        money=Studs*2.4
        answer='Perimeter='+str(P)+'ft  '+str(Studs)+' studs \$'+str(money)
        self.f.write('\\GUESSA{You are quoting a concrete pour of a slab.  A foundation for the house is 22 feet by 18 feet. Estimate the number of 8 foot 2X6 wood studs for the frame of the slab. If each stud is \$2.40, calculate the total cost}{'+answer+'}\n')
        self.f.write('\\GUESS{You are quoting a concrete pour of a slab.  A foundation for the house is '+l1+' feet by '+w1+' feet.  Estimate the number of 8 foot 2X6 wood studs for the frame of the slab. If each stud is \$'+prices+', calculate the total cost.}\n')

        volume=22*18*5/12
        yards=math.ceil((22.0*18.0*5.0/12.0)/27.0)
        Trucks=float(yards)/10.0
        iTrucks=int(Trucks)
        ptruck=(Trucks-iTrucks)*10
        petruck=10-ptruck
        cost=iTrucks*600+ptruck*60+petruck*20
        tprices=random.randint(500,700)
        tprice=str(tprices)
        pprices=tprices/10+2
        pprice=str(pprices)
        peprice=str(random.randint(15,25))

        answer='Volume='+str(volume)+'$ft^2$  Yards='+str(yards)+'  Trucks='+str(Trucks)+' Cost=\$'+str(cost)
        self.f.write('\\GUESSA{You are quoting a concrete pour of a slab.  A foundation for the house is 22 feet by 18 feet. Estimate the cost of concrete for a 5 inch slab. Round the result to the next yard. The cost for a 10 yard truck is \$600 with a partial truck cost of \$65 per yard and \$20 per yard empty truck fee.}{'+answer+'}\n')
        self.f.write('\\newpage')
        self.f.write('\\GUESS{You are quoting a concrete pour of a slab.  A foundation for the house is '+l1+' feet by '+w1+' feet. Estimate the cost of concrete for a 7 inch slab. Round the result to the next yard. The cost for a 10 yard truck is \$'+tprice+' with a partial truck cost of \$'+pprice+' per yard and \$'+peprice+' per yard empty truck fee .}\n')
        


        rprice=str(float(random.randint(400,500))/100)
        answer=''
        self.f.write('\\GUESSA{You are quoting a concrete pour of a slab.  A foundation for the house is 22 feet by 18 feet. Estimate the cost of rebar if your frame is every 2 feet. Do not reuse rebar. The cost for a 10 foot length is \$3.}{'+answer+'}\n')
        self.f.write('\\GUESS{You are quoting a concrete pour of a slab.  A foundation for the house is '+l1+' feet by '+w1+' feet.Estimate the cost of rebar if your frame is every 2 feet. Do not reuse rebar. The cost for a 10 foot length is \$'+rprice+'.}\n')

        self.f.write('\\end{enumerate}\n')

g=Rebar("Construction Technology","Estimate Slab Cost", "LARGE")
for x in range(1, 40):
    g.WritePage(x)
