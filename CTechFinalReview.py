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

        self.f.write('\\newpage\n\n')
        self.f.write('\\item Estimate Rigid Insulation(8I)')

        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\GUESS{You are estimating how many sheets of rigid insulation you need for your house.  The house outer frame of the house is going to be '+l1+' feet by '+w1+' feet and '+h1+' feet high.  There will be two standard '+wd+' inch by '+hd+' inch doors, a '+wd+' inch by '+wp+' inch patio door and '+nw+ ' windows each ' +ww+' by '+hw+' inches. Calculate the total total surface area of four sides of the house in square feet.}\n')
        self.f.write('\\GUESS{You are estimating how many sheets of rigid insulation you need for your house.  The house outer frame of the house is going to be '+l1+' feet by '+w1+' feet and '+h1+' feet high.  There will be two standard '+wd+' inch by '+hd+' inch doors, a '+wd+' inch by '+wp+' inch patio door and '+nw+ ' ' +ww+' inch by '+hw+' inch windows. The insulation is supplied in '+wwrap+' feet by '+lwrap+' feet rigid sheets.  Calculate the minimum number of sheets needed to wrap the house.}\n')
        self.f.write('\\GUESS{You are estimating how many sheets of rigid insulation you need for your house.  The house outer frame of the house is going to be '+l1+' feet by '+w1+' feet and '+h1+' feet high.  There will be two standard '+wd+' inch by '+hd+' inch doors, a '+wd+' inch by '+wp+' inch patio door and '+nw+ ' ' +ww+' inch by '+hw+' inch windows.  The cost of each sheet is \$'+price+'. Calculate the total cost for the sheets you need to insulate the house.}\n')

        self.f.write('\\end{enumerate}\n')


        

        
        thick=str(random.randint(8,20))
        radius=str(random.randint(21,60))
        price=str(random.randint(600,900))        
        priceY=str(random.randint(70,100))
        priceE=str(random.randint(20,40))

        
        self.f.write('\\newpage\n\n')
        
        self.f.write('\\item Estimate Circular Foundation(10C)')

        self.f.write('\\begin{enumerate}\n')

        self.f.write('\\GUESS{An arena is to built on a circular foundation with a radius of '+radius+' feet.  The thickness is '+thick+' inches. Calculate the volume in cubic feet of the concrete required for the foundation.}\n')
        
        self.f.write('\\GUESS{An arena is to built on a circular foundation with a radius of '+radius+' feet.  The thickness is '+thick+' inches. Calculate the yards of concrete required for the foundation.}\n')
        
        self.f.write('\\GUESS{An arena is to built on a circular foundation with a radius of '+radius+' feet.  The thickness is '+thick+' inches.  Calculate the number of trucks needed for the amount of concrete.}\n')

        self.f.write('\\GUESS{An arena is to built on a circular foundation with a radius of '+radius+' feet.  The thickness is '+thick+' inches.  If a truck is \\$'+price+', a yard is \\$'+priceY+', and an  ampty yard is \\$'+priceE+', calculate the minimum and maximum cost for the trucks of concrete.}\n')

        self.f.write('\\end{enumerate}\n')

        self.f.write('\\newpage\n\n')

        l1=str(random.randint(8,16)*2)
        w1=str(random.randint(10,18)*2)       
        prices=str(float(random.randint(200,300))/100)
        P=2*22+2*18
        Studs=P/8
        money=Studs*2.4
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
        rprice=str(float(random.randint(400,500))/100)
        
        self.f.write('\\item Estimate Rebar(10C)')

        self.f.write('\\begin{enumerate}\n')

        self.f.write('\\GUESS{You are quoting a concrete pour of a slab.  A foundation for the house is '+l1+' feet by '+w1+' feet.  Estimate the number of 8 foot 2X6 wood studs for the frame of the slab. If each stud is \$'+prices+', calculate the total cost.}\n')
        self.f.write('\\GUESS{You are quoting a concrete pour of a slab.  A foundation for the house is '+l1+' feet by '+w1+' feet. Estimate the cost of concrete for a 7 inch slab. Round the result to the next yard. The cost for a 10 yard truck is \$'+tprice+' with a partial truck cost of \$'+pprice+' per yard and \$'+peprice+' per yard empty truck fee .}\n')
        self.f.write('\\GUESS{You are quoting a concrete pour of a slab.  A foundation for the house is '+l1+' feet by '+w1+' feet.Estimate the cost of rebar if your frame is every 2 feet. Do not reuse rebar. The cost for a 10 foot length is \$'+rprice+'.}\n')

        self.f.write('\\end{enumerate}\n')

        self.f.write('\\newpage\n\n')

        l=str(random.randint(150,200))
        w=str(random.randint(75,100))        
        shallow=str(random.randint(30,60))
        deep=str(random.randint(130,200))
        t=str(random.randint(3,9))

        self.f.write('\\item Estimate Pool(10C)')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\GUESS{A pool is '+l+' inches by '+w+' inches.  The shallow end is '+shallow+' inches and the deep end is '+deep+' inches, with a linear slope. If the wall at the shallow and deep end are '+t+' inches thick, calculate the volume.}\n')
        self.f.write('\\GUESS{A pool is '+l+' inches by '+w+' inches.  The shallow end is '+shallow+' inches and the deep end is '+deep+' inches, with a linear slope. If the long walls  are '+t+' inches thick, calculate the volume.}\n')
        self.f.write('\\GUESS{A pool is '+l+' inches by '+w+' inches.  The shallow end is '+shallow+' inches and the deep end is '+deep+' inches, with a linear slope. If the floor is '+t+' inches thick, calculate the volume.}\n')
        self.f.write('\\GUESS{A pool is '+l+' inches by '+w+' inches.  The shallow end is '+shallow+' inches and the deep end is '+deep+' inches, with a linear slope. Calculate the total volume, number of trucks, and maximum legnth of rebar.}\n')
        self.f.write('\\end{enumerate}\n')

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

        l=str(random.randint(21,50))
        w=str(random.randint(10,20))        
        t=str(random.randint(3,7))
        inner=str(random.randint(13,23))
        price=str(random.randint(550,800))
        priceY=str(random.randint(65,90))
        priceE=str(random.randint(11,30))
 
        self.f.write('\\item Estimate Drive Way')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\GUESS{A driveway will be '+l+' feet by '+w+' feet with a '+inner+' inches of empty space in the middle with one for endcaps.  The driveway will be '+t+' feet thick.  Calculate the volume of concrete .}\n')
        self.f.write('\\GUESS{A driveway will be '+l+' feet by '+w+' feet with a '+inner+' inches of empty space in the middle with one for endcaps.  The driveway will be '+t+' feet thick.  Calculate the volume of concrete .}\n')
        self.f.write('\\GUESS{A driveway will be '+l+' feet by '+w+' feet with a '+inner+' inches of empty space in the middle with one for endcaps.  The driveway will be '+t+' feet thick. Calculate cost of concrete if a truck costs \\$'+price+', or \\$'+priceY+' a yard with a \\$'+priceE+' empty truck fee per yard?  .}\n')
        self.f.write('\\GUESS{For your driveway, calcuate the soil needed to fill the middle.}\n')
        self.f.write('\\end{enumerate}\n')
        self.f.write('\\newpage\n\n')



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
        
        self.f.write('\\item Estimate Circular Pond(10C)')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\GUESS{You are building a fountain with an inner radius of '+inner+' feet and '+high+' inch high walls, with everything '+thick+' inches thick. Estimate the volume of concrete for the wall of the fountain.}\n')
        self.f.write('\\GUESS{You are building a fountain with an inner radius of '+inner+' feet and '+high+' inch high walls, with everything '+thick+' inches thick. Estimate the volume of concrete for the floor of the fountain.}\n')
        self.f.write('\\GUESS{You are building a fountain with an inner radius of '+inner+' feet and '+high+' inch high walls, with everything '+thick+' inches thick. Estimate the volume of concrete for the floor of the fountain.}\n')
        self.f.write('\\GUESS{You are building a fountain with an inner radius of '+inner+' feet.   If you are going to fill it '+deep+' inches deep, estimate the gallons of water if 1 cubic foot is 7.5 gallons.}\n')
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


    
g=Concrete("Construction Technology","Construction Technology Final Review 2018-Turn in on 2018 June 1 between 0800 and 0830", "large")
for x in range(1, 50):
    g.WritePage(x)
