import GuessBase
import random

class EstWrap(GuessBase.Guess):
    def __init__(self,course, title, rowh):
        super(EstWrap, self).__init__(course, title, rowh)

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
        lwrap=str(random.randint(120,160))
        wwrap=str(random.randint(4,9))
        cost=str(random.randint(100,199))

        self.f.write('\\GUESS{You are estimating how much homewrap you need for your house.  The house outer frame of the house is going to be 60 feet by 38 feet and 12 feet high.  There will be two standard 36 inch by 80 inch doors, a 60 inch by 80 inch patio door and 12 30 inch by 50 inch windows. Calculate the total total surface area of four sides of the house in square feet.}\n')
        self.f.write('\\GUESS{You are estimating how much homewrap you need for your house.  The house outer frame of the house is going to be '+l1+' feet by '+w1+' feet and '+h1+' feet high.  There will be two standard '+wd+' inch by '+hd+' inch doors, a '+wd+' inch by '+wp+' inch patio door and '+nw+ ' ' +ww+' inch by '+hw+' inch windows. Calculate the total total surface area of four sides of the house in square feet.}\n')

        self.f.write('\\GUESS{You are estimating how much homewrap you need for your house.  The house outer frame of the house is going to be 60 feet by 38 feet and 12 feet high.  There will be two standard 36 inch by 80 inch doors, a 60 inch by 80 inch patio door and 12 30 inch by 50 inch windows. The wrap is supplied in 3 feet by 6 feet rolls.  Calculate the minimum number of rolls needed to wrap the house.}\n')
        self.f.write('\\GUESS{You are estimating how much homewrap you need for your house.  The house outer frame of the house is going to be '+l1+' feet by '+w1+' feet and '+h1+' feet high.  There will be two standard '+wd+' inch by '+hd+' inch doors, a '+wd+' inch by '+wp+' inch patio door and '+nw+ ' ' +ww+' inch by '+hw+' inch windows. The wrap is supplied in '+wwrap+' feet by '+lwrap+' feet rolls.  Calculate the minimum number of rolls needed to wrap the house.}\n')

        self.f.write('\\GUESS{You are estimating how much homewrap you need for your house.  The house outer frame of the house is going to be 60 feet by 38 feet and 12 feet high.  There will be two standard 36 inch by 80 inch doors, a 60 inch by 80 inch patio door and 12 30 inch by 50 inch windows. The wrap is supplied in 3 feet by 6 feet rolls.  The cost of each roll is \$66. Calculate the total cost for the rolls you need to wrap the house.}\n')
        self.f.write('\\GUESS{You are estimating how much homewrap you need for your house.  The house outer frame of the house is going to be '+l1+' feet by '+w1+' feet and '+h1+' feet high.  There will be two standard '+wd+' inch by '+hd+' inch doors, a '+wd+' inch by '+wp+' inch patio door and '+nw+ ' ' +ww+' inch by '+hw+' inch windows.  The cost of each roll is \$'+cost+'. Calculate the total cost for the rolls you need to wrap the house.}\n')

        self.f.write('\\end{enumerate}\n')

g=EstWrap("Construction Technology","Estimate Home Wrap", "large")
for x in range(1, 45):
    g.WritePage(x)
