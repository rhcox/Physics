import GuessBase
import random
import math

class Concrete(GuessBase.Guess):
    def __init__(self,course, title, rowh):
        super(Concrete, self).__init__(course, title, rowh)

    def PAGE(self):
        self.f.write('\\normalsize\n')
        random.seed(self.rnum)

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

        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item Estimate House Wrap(8I)')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\GUESS{You are estimating how much homewrap you need for your house.  The house outer frame of the house is going to be '+l1+' feet by '+w1+' feet and '+h1+' feet high.  There will be two standard '+wd+' inch by '+hd+' inch doors, a '+wd+' inch by '+wp+' inch patio door and '+nw+ ' ' +ww+' inch by '+hw+' inch windows. Calculate the total total surface area of four sides of the house in square feet.}\n')

        self.f.write('\\GUESS{You are estimating how much homewrap you need for your house.  The house outer frame of the house is going to be '+l1+' feet by '+w1+' feet and '+h1+' feet high.  There will be two standard '+wd+' inch by '+hd+' inch doors, a '+wd+' inch by '+wp+' inch patio door and '+nw+ ' ' +ww+' inch by '+hw+' inch windows. The wrap is supplied in '+wwrap+' feet by '+lwrap+' feet rolls.  Calculate the minimum number of rolls needed to wrap the house.}\n')

        self.f.write('\\GUESS{You are estimating how much homewrap you need for your house.  The house outer frame of the house is going to be '+l1+' feet by '+w1+' feet and '+h1+' feet high.  There will be two standard '+wd+' inch by '+hd+' inch doors, a '+wd+' inch by '+wp+' inch patio door and '+nw+ ' ' +ww+' inch by '+hw+' inch windows.  The cost of each roll is \$'+cost+'. Calculate the total cost for the rolls you need to wrap the house.}\n')      
        self.f.write('\\end{enumerate}\n')



       


        

        
        thick=str(random.randint(8,20))
        

        self.f.write('\\newpage\n\n')




        l1=str(int(random.randint(5,15)))
        w1=str(int(random.randint(5,15)))
        l2=str(int(random.randint(15,25)))
        w2=str(int(random.randint(15,25)))
        l3=str(int(random.randint(25,35)))
        w3=str(int(random.randint(25,35)))
        l4=str(int(random.randint(5,45)))
        w4=str(int(random.randint(5,45)))
        roll=str(int(random.randint(4,25)))
        costr=str(int(random.randint(40,80)))

        self.f.write('\\item Estimate Carpet(7J)')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\GUESS{A house needs carpet in three rooms. The first room is '+l1+' by '+w1+' feet, the second  room is '+l2+' by '+w2+' feet, and the third  room is '+l3+' by '+w3+' feet. Calculate the total area of carpet required.}\n')
        self.f.write('\\GUESS{A house needs carpet in three rooms. The first room is '+l1+' by '+w1+' feet, the second  room is '+l2+' by '+w2+' feet, and the third  room is '+l3+' by '+w3+' feet. Each roll of carpet covers '+roll+' square feet. Calculate the minimum number of rolls required.}\n')
        self.f.write('\\GUESS{A house needs carpet in three rooms. The first room is '+l1+' by '+w1+' feet, the second  room is '+l2+' by '+w2+' feet, and the third  room is '+l3+' by '+w3+' feet. Each roll of carpet costs \$'+costr+'. Calculate the minimum cost to purchase the required rolls.}\n')
        self.f.write('\\end{enumerate}\n')

        self.f.write('\\newpage\n\n')

        l1=str(int(random.randint(40,55)))
        w1=str(int(random.randint(30,45)))
        h1=str(float(random.randint(70,100)/10))
        l2=str(int(random.randint(30,40)))
        w2=str(int(random.randint(20,30)))
        h2=str(float(random.randint(70,90)/10))
        l3=str(int(random.randint(20,30)))
        w3=str(int(random.randint(15,20)))
        h3=str(float(random.randint(60,80)/10))        
        l4=str(int(random.randint(5,45)))
        w4=str(int(random.randint(5,45)))
        factor=str(round(random.random()*3+2,1))
        cost=str(int(random.randint(40,80)))
        
        self.f.write('\\item Estimate Air Handling(1B)')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\GUESS{You are sizing an air conditioning for a house. The first floor is '+l1+' by '+w1+' feet with '+h1+' feet ceilings. The second floor is '+l2+' by '+w2+' feet with '+h2+' feet ceilings. There is a finished atic in the shape of a triangle, '+l3+' by '+w3+' feet with the highest point at '+h3+' feet. Calculate the total volume of the house in cubic feet.}\n')
        self.f.write('\\GUESS{You are sizing an air conditioning for a house. The first floor is '+l1+' by '+w1+' feet with '+h1+' feet ceilings. The second floor is '+l2+' by '+w2+' feet with '+h2+' feet ceilings. There is a finished atic in the shape of a triangle, '+l3+' by '+w3+' feet with the highest point at '+h3+' feet. Determine the required cooling rate by dividing the volume by '+factor+' to calculate BTU/hour.}\n')
        self.f.write('\\GUESS{You are sizing an air conditioning for a house. The first floor is '+l1+' by '+w1+' feet with '+h1+' feet ceilings. The second floor is '+l2+' by '+w2+' feet with '+h2+' feet ceilings. There is a finished atic in the shape of a triangle, '+l3+' by '+w3+' feet with the highest point at '+h3+' feet. Using the cooling rate, divide by 1200 to calcluate the required tonnage.}\n')

        self.f.write('\\end{enumerate}\n')


        self.f.write('\\newpage\n\n')

       



       

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

        self.f.write('\\item Estimate Concrete Deck(10C)')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\GUESS{A square concrete deck is to be built around a circular pond.  The pond has a diameter of '+R+' feet.  The deck is to be '+S+' feet on a side.  Calculate the length of the poly form for the interion of the deck and the wooden form for the outside of the deck.}')
        self.f.write('\\GUESS{A square concrete deck is to be built around a circular pond.  The pond has a diameter of '+R+' feet.  The deck is to be '+S+' feet on a side. If the deck is to be '+lwrap+' inches thick, calculate the volume of concrete needed for the pour.}\n')
        self.f.write('\\GUESS{A square concrete deck is to be built around a circular pond.  The pond has a diameter of '+R+' feet.  The deck is to be '+S+' feet on a side. If the deck is to be '+lwrap+' inches thick,  calculate the cost of the concrete.  Assume that a truck holds 10 yards, that each truck is \$'+price+' or \$'+priceY+' a yard with a \$'+priceE+' per yard empty truck fee.}\n')
        self.f.write('\\end{enumerate}\n')

        self.f.write('\\end{enumerate}\n')


    
g=Concrete("Construction Technology","Construction Technology Final Exam 2018 June 1", "large")
for x in range(1, 30):
    g.WritePage(x)
