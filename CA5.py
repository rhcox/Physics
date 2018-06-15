import Base
import random

class CA4(Base.BASE):
    def __init__(self,course, title):
        super(CA4, self).__init__(course, title)

    def PAGE(self):
        self.f.write('\\large\n')
        self.f.write('This review is due April 4 at beginning of your class. Late work earns 0 points.\n')

        self.f.write('\\normalsize\n')
        random.seed(self.rnum)
        space="22"

        mass=str(random.randint(8,70))
        mass1=str(random.randint(10,30))
        mass2=str(random.randint(31,60))
        force=str(float(random.randint(100,200))/10.0)        
        speed1=str((float(random.randint(16,40))/10.0)) 
        speed2=str((float(random.randint(60,99))/10.0))
        speed3=str(random.randint(20,40))
        dist=str(random.randint(15,40))
        heightf=random.randint(4,15)
        height=str(heightf)
        heightb=str(round(float(heightf)*.3,2))
        time=str((float(random.randint(12,29))/10.0))
        temp1=str(random.randint(100,200))
        temp2=str(random.randint(110,300))
        temp3=str(random.randint(310,400))
        freq=str(random.randint(500,900))
        wavelength=str(random.randint(10,90))
        wavespeed=str(random.randint(1400,1900))
        


        self.f.write('\\begin{enumerate}\n')

        self.f.write('\\item Convert the following units.\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item '+mass+' pounds to kg if 1 pound is 16 ounces and 1 ounce is 20 grams at earths gravity.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item '+dist+' feet to meters if 1 foot is .305 meters.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item '+time+' hours to seconds if 60 seconds is a minute and 60 minutes is an hour.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\end{enumerate}\n')
 
        self.f.write('\\item In each case, how to we know that there is less energy available for useful work, i.e. lost to heat.\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item A ball bounces on the ground.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Ball bounce off each other on a Newton\'s Cradle.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item An incandescent lightbulb.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item A person pedaling bicycle.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\end{enumerate}\n')

        self.f.write('\\item What is the typical medium and type for each  wave generated in the following examples.\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item A rock dropped in the lake.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item A person yells from across the room.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item The sun shines light on the earth.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item A standing wave is created in the slinky.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item A waves detected by a seismograph.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\end{enumerate}\n')

        self.f.write('\\item A $'+mass+'\\KG$ ball is thrown against a wall with a speed of $'+speed1+'\\MPS$.  It sticks to the wall at a height of$'+height+'\\MET$ then falls to the floor.\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item Calculate the momentum of the ball just before it hits the wall.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Calculate the energy lost in the generated.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Calculate the potential energy of the ball as it sticks to the wall.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Assuming the ball loses half the energy as it bounces on the floor, calculate the height the ball will reach.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Assuming the ball loses half the energy as it bounces on the floor, calculate the the momentum of the ball just after the bounce.\n\n')
        self.f.write('\\end{enumerate}\n')

       

        self.f.write('\\item Suppose we have four thermally conductive containers.  Container A is at $'+temp1+' \\Kelvin$, container B is at $'+temp2+' \\Kelvin$, container C is at $'+temp3+' \\Kelvin$ and container D is at $'+temp1+' \\Kelvin$\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item If container A and C are placed next to each other, what is the direction of heat flow.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item If container B and D are placed next to each other, what is the direction of heat flow.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item If container A and D are placed next to each other, what is the direction of heat flow.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item If the container contain an identical sparse weakly interacting gas, what can be said about the reletive kinetic energy of gas in the containeers.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Descibe the calculation of the increase in temperature for a certain amount of heat added.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        
        self.f.write('\\end{enumerate}\n')

        self.f.write('\\item Define and give examples of transverse and longitudinal Wave.\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item Draw a representation of a transverse wave on a time axis labeling the ampliotude, and period.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Draw a transverse wave on a distance axis labeling the ampliotude, and wavelegth.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item A wave has a frequency of $'+freq+'\\HZ$ and a wave speed of $'+wavespeed+'\\MPS$. Calculate the wavelength.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item A wave has a frequency of $'+freq+'\\HZ$ and a wavelength of $'+wavelength+'\\MET$. Calculate the wavespeed.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item A wave has a wave speed of $'+wavespeed+'\\MPS$ and a wavelength of $'+wavelength+'\\MET$. Calculate the frequency.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item A wave has a frequency of $'+freq+'\\HZ$. Calculate the period.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Two sound waves has a frequency of $'+freq+'\\HZ$. One wave has an amplitude twice that of the other.  How do we intepret the differnce in amplitude?.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\end{enumerate}\n')



        
        self.f.write('\\end{enumerate}\n')


g=CA4("Physics 1","CA 5 Review")
for x in range(1, 40):
    g.WritePage(x)
