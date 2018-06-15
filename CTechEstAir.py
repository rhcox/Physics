import GuessBase
import random

class EstAir(GuessBase.Guess):
    def __init__(self,course, title, rowh):
        super(EstAir, self).__init__(course, title, rowh)

    def PAGE(self):
        self.f.write('\\normalsize\n')
        random.seed(self.rnum)
        self.f.write('\\begin{enumerate}\n')
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

        self.f.write('\\GUESS{You are sizing an air conditioning for a house. The first floor is 52 by 38 feet with 9 feet ceilings. The second floor is 46 by 30 feet with 8 feet ceilings. There is a finished atic in the shape of a triangle, 25 by 20 feet with the highest point at 7 feet. Calculate the total volume of the house in cubic feet.}\n')
        self.f.write('\\GUESS{You are sizing an air conditioning for a house. The first floor is '+l1+' by '+w1+' feet with '+h1+' feet ceilings. The second floor is '+l2+' by '+w2+' feet with '+h2+' feet ceilings. There is a finished atic in the shape of a triangle, '+l3+' by '+w3+' feet with the highest point at '+h3+' feet. Calculate the total volume of the house in cubic feet.}\n')

        self.f.write('\\GUESS{You are sizing an air conditioning for a house. The first floor is 52 by 38 feet with 9 feet ceilings. The second floor is 46 by 30 feet with 8 feet ceilings. There is a finished atic in the shape of a triangle, 25 by 20 feet with the highest point at 7 feet. Determine the required cooling rate by dividing the volume by 3 to calculate BTU/hour.}\n')
        self.f.write('\\newpage \n')

        self.f.write('\\GUESS{You are sizing an air conditioning for a house. The first floor is '+l1+' by '+w1+' feet with '+h1+' feet ceilings. The second floor is '+l2+' by '+w2+' feet with '+h2+' feet ceilings. There is a finished atic in the shape of a triangle, '+l3+' by '+w3+' feet with the highest point at '+h3+' feet. Determine the required cooling rate by dividing the volume by '+factor+' to calculate BTU/hour.}\n')
        
        self.f.write('\\GUESS{You are sizing an air conditioning for a house. The first floor is 52 by 38 feet with 9 feet ceilings. The second floor is 46 by 30 feet with 8 feet ceilings. There is a finished atic in the shape of a triangle, 25 by 20 feet with the highest point at 7 feet. Using the cooling rate, divde by 1200 to calcluate the required tonnage.}\n')
        
        
        self.f.write('\\GUESS{You are sizing an air conditioning for a house. The first floor is '+l1+' by '+w1+' feet with '+h1+' feet ceilings. The second floor is '+l2+' by '+w2+' feet with '+h2+' feet ceilings. There is a finished atic in the shape of a triangle, '+l3+' by '+w3+' feet with the highest point at '+h3+' feet. Using the cooling rate, divide by 1200 to calcluate the required tonnage.}\n')
        self.f.write('\\end{enumerate}\n')




g=EstAir("Construction Technology","Estimate Air Handling", "large")
for x in range(1, 40):
    g.WritePage(x)
