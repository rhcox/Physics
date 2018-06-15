import GuessBase
import random
import math

class EstRigid(GuessBase.Guess):
    def __init__(self,course, title, rowh):
        super(EstRigid, self).__init__(course, title, rowh)

    def PAGE(self):
        self.f.write('\\normalsize\n')
        random.seed(self.rnum)
        self.f.write('\\begin{enumerate}\n')
        l1=str(random.randint(50,70))
        w1=str(random.randint(35,45))
        h1=str(float(random.randint(9,13)/1))
        ww=str(random.randint(25,39))
        hw=str(random.randint(39,55))
        wd=str(random.randint(34,50))
        hd=str(random.randint(30,75))
        wp=str(random.randint(55,85))
        nw=str(random.randint(4,11))
        lwrap=str(random.randint(2,6))
        wwrap=str(random.randint(7,10))
        price=str(random.randint(18,30))

        SA=60*12*2+38*12*2-36/12*80/12*2-60/12*80/12-30/12*50/12*10
        answer='A=$'+str(SA)+'ft^2$'
        self.f.write('\\GUESSA{You are estimating how 0any sheets of rigid insulation you need for your house.  The house outer frame of the house is going to be 60 feet by 38 feet and 12 feet high.  There will be two standard 36 inch by 80 inch doors, a 60 inch by 80 inch patio door and 10 windows each 30 by 50 inches. Calculate the total total surface area of four sides of the house in square feet.}{'+answer+'}\n')
        self.f.write('\\GUESS{You are estimating how many sheets of rigid insulation you need for your house.  The house outer frame of the house is going to be '+l1+' feet by '+w1+' feet and '+h1+' feet high.  There will be two standard '+wd+' inch by '+hd+' inch doors, a '+wd+' inch by '+wp+' inch patio door and '+nw+ ' windows each ' +ww+' by '+hw+' inches. Calculate the total total surface area of four sides of the house in square feet.}\n')

                
        Sheets=math.ceil(((float)(SA))/(4.*8.))
        answer='S=$'+str((int)(Sheets))+'sheets$'        
        self.f.write('\\GUESSA{You are estimating how many sheets of rigid insulation you need for your house.  The house outer frame of the house is going to be 60 feet by 38 feet and 12 feet high.  There will be two standard 36 inch by 80 inch doors, a 60 inch by 80 inch patio door and 12 30 inch by 50 inch windows. The insulation is supplied in 4 feet by 8 feet rigid sheets.  Calculate the minimum number of sheets needed to wrap the house.}{'+answer+'}\n')

        self.f.write('\n\n\\newpage\n\n')

        self.f.write('\\GUESS{You are estimating how many sheets of rigid insulation you need for your house.  The house outer frame of the house is going to be '+l1+' feet by '+w1+' feet and '+h1+' feet high.  There will be two standard '+wd+' inch by '+hd+' inch doors, a '+wd+' inch by '+wp+' inch patio door and '+nw+ ' ' +ww+' inch by '+hw+' inch windows. The insulation is supplied in '+wwrap+' feet by '+lwrap+' feet rigid sheets.  Calculate the minimum number of sheets needed to wrap the house.}\n')


        Cost=Sheets*17.
        answer='S=$\$'+str(Cost)+'$'        
        self.f.write('\\GUESSA{You are estimating how many sheets of rigid insulation you need for your house.  The house outer frame of the house is going to be 60 feet by 38 feet and 12 feet high.  There will be two standard 36 inch by 80 inch doors, a 60 inch by 80 inch patio door and 12 30 inch by 50 inch windows.  The cost of each sheet is \$17. Calculate the total cost for the sheets you need to insulate the house.}{'+answer+'}\n')
        self.f.write('\\GUESS{You are estimating how many sheets of rigid insulation you need for your house.  The house outer frame of the house is going to be '+l1+' feet by '+w1+' feet and '+h1+' feet high.  There will be two standard '+wd+' inch by '+hd+' inch doors, a '+wd+' inch by '+wp+' inch patio door and '+nw+ ' ' +ww+' inch by '+hw+' inch windows.  The cost of each sheet is \$'+price+'. Calculate the total cost for the sheets you need to insulate the house.}\n')

        self.f.write('\\end{enumerate}\n')

g=EstRigid("Construction Technology","Estimate Rigid Insulaion", "large")
for x in range(1, 2):
    g.WritePage(x)
