import Base
import random

class CA4(Base.BASE):
    def __init__(self,course, title):
        super(CA4, self).__init__(course, title)

    def PAGE(self):
        self.f.write('\\large\n')
        self.f.write('This review is due February 13 at begining of your class.  It is worth bonus points. If turned in late, it is worth no points.\n')

        self.f.write('\\normalsize\n')
        random.seed(self.rnum)
        space="10"

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


        self.f.write('\\begin{enumerate}\n')

        self.f.write('\\item Convert the following units.\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item '+mass+' pounds to kg if 1 pound is 16 ounces and 1 ounce is 20 grams at earths gravity.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item '+dist+' feet to meters if 1 foot is .305 meters.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item '+time+' hours to seconds if 60 seconds is a minute and 60 mintues is an hour.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\end{enumerate}\n')
 
        self.f.write('\\item A $'+mass+'\\KG$ box is on an inclined plane $'+height+'\\MET$ above a surface.  It is allowed to fall from rest to the surface.  Ignore friction and all non conservative forces.\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item Calcualte potenial energy at the starting position assuming the surface is 0 meters.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item State the kinetic energy at the surface.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Calcualte the speed at the surface.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Calculate the momentum at the suface.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item State the work done by gravity.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item If the inclined plane is $'+dist+'\\MET$ long, what is the force required to do this work.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\end{enumerate}\n')

       

        self.f.write('\\item A $'+mass1+' \KG$ mass traveling a $'+speed1+'\\MPS$ collides with second mass of $'+mass2+'\\KG$ which is at rest.  After the collision, the first mass is a rest, and the second mass is in motion in the same direction.\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item Calculate the initial momentum of the system.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Set up the equation for the final momentum of the system.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Calculate the speed of the second mass .\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Calculate the inital and final kinetic energy, state if collision is elastic or inelastic.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        
        self.f.write('\\end{enumerate}\n')

        self.f.write('\\item A $'+mass1+' \KG$ rock is dropped from a height of  $'+height+'\\MET$. The rock bounces up to $'+heightb+'\\MET$.\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item Calculate the initial potential energy of the rock.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item State the work down by gravity, the kinetic energy and calculate the speed just before the bounce.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Calculate the final potential energy of the rock.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item State the kinetic energy and calculate the speed just after the bounce.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item State the energy lost to heat and defelction during the bounce.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\end{enumerate}\n')


        self.f.write('\\item Laws of thermodynamics.\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item Zeroth - if two systems are in thermal equlibrium with a third, the they are in termal equilibrium with each other.\n\n')
        self.f.write('\\item First - Energy is conserved, it cannot be created or destroyed.  For a thermodynamic cycle, the work done is equal to the heat supplied\n\n')
        self.f.write('\\item Second - Entropy, a measure of disorder, always increases.  Perpetual motion is not possible.\n\n')
        self.f.write('\\item Third - As temperature apporaches aboslute zerom, the system mimizes entopy abnd maximizes order.\n\n')
        self.f.write('\\end{enumerate}\n')

    
        
        self.f.write('\\end{enumerate}\n')


g=CA4("Physics 1","CA 4 Review")
for x in range(1, 100):
    g.WritePage(x)
