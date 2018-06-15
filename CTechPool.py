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


        v1=100/12*24/12*10/12+100/12*120/12*10/12
        answer='Volume=$'+str(v1)+'ft^3$'
        self.f.write('\\GUESSA{A pool is 244 inches by 100 inches.  The shallow end is 24 inches and the deep end is 120 inches, with a linear slope. If the wall at the shallow and deep end are 10 inches thick, calculate the volume.}{'+answer+'}\n')
        self.f.write('\\GUESS{A pool is '+l+' inches by '+w+' inches.  The shallow end is '+shallow+' inches and the deep end is '+deep+' inches, with a linear slope. If the wall at the shallow and deep end are '+t+' inches thick, calculate the volume.}\n')


        v2=2*(244/12*((24+120)/2/12)*10/12)
        answer='Volume=$'+str(v2)+'ft^3$'
        self.f.write('\\GUESSA{A pool is 244 inches by 100 inches.  The shallow end is 24 inches and the deep end is 120 inches, with a linear slope. If the long walls are 10 inches thick, calculate the volume.}{'+answer+'}\n')
        self.f.write('\\GUESS{A pool is '+l+' inches by '+w+' inches.  The shallow end is '+shallow+' inches and the deep end is '+deep+' inches, with a linear slope. If the long walls  are '+t+' inches thick, calculate the volume.}\n')
        


        v3=244/12*100/12*10/12
        answer='Volume=$'+str(v3)+'ft^3$'
        self.f.write('\\GUESSA{A pool is 244 inches by 100 inches.  The shallow end is 24 inches and the deep end is 120 inches, with a linear slope. If the floor is 10 inches thick, calculate the volume.}{'+answer+'}\n')
        self.f.write('\\GUESS{A pool is '+l+' inches by '+w+' inches.  The shallow end is '+shallow+' inches and the deep end is '+deep+' inches, with a linear slope. If the floor is '+t+' inches thick, calculate the volume.}\n')

        
        rebar=math.ceil(math.sqrt((120-24)*(120-24)+244*244)/12)
        answer='Total Volume=$'+str(v1+v2+v3)+'ft^3$    long rebar='+str(rebar)+'ft  short rebar='+str(math.ceil(100/12))+'ft'
        self.f.write('\\GUESSA{A pool is 244 inches by 100 inches.  The shallow end is 24 inches and the deep end is 120 inches, with a linear slope. Calculate the total volume, number of trucks, and maximum legnth of rebar.}{'+answer+'}\n')
        self.f.write('\\GUESS{A pool is '+l+' inches by '+w+' inches.  The shallow end is '+shallow+' inches and the deep end is '+deep+' inches, with a linear slope. Calculate the total volume, number of trucks, and maximum legnth of rebar.}\n')
        self.f.write('\\end{enumerate}\n')

g=Concrete("Construction Technology","Estimate Pond Deck", "large")
for x in range(1, 40):
    g.WritePage(x)
