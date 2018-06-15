import Base
import random
import math

class CA4(Base.BASE):
    def __init__(self,course, title):
        super(CA4, self).__init__(course, title)

    def PAGE(self):
        self.f.write('\\large\n')
        self.f.write('This Final Exam must be completed independently.  Show all Work.  Turn in any review packet you may have completed prior to taking this exam.\n')

        self.f.write('\\normalsize\n')
        random.seed(self.rnum)
        space="32"

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
        voltf=random.randint(5,20)
        volt=str(voltf)
        R1f=random.randint(200,400)
        R2f=random.randint(500,900)
        R3f=random.randint(50,150)
        R1=str(R1f)
        R2=str(R2f)
        R3=str(R3f)
        current=str(float(voltf)/float(R1f+R2f+R3f))
        
        q1=str(float(random.randint(500,800)/100))
        q2=str(float(random.randint(100,400)/100))
        exp=str(random.randint(5,15))
        exp2=str(random.randint(9,14))
        r=str(random.randint(2,9))
        

        self.f.write('\\begin{enumerate}\n')

 

       

        self.f.write('\\item A $'+mass1+' \KG$ mass traveling a $'+speed1+'\\MPS$ collides with second mass of $'+mass2+'\\KG$ which is at rest.  After the collision, the first mass is a rest, and the second mass is in motion in the same direction.\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item Calculate the initial momentum of the system. (6C)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Calculate the speed of the second mass after the collision. (6C)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')        
        self.f.write('\\end{enumerate}\n')

        self.f.write('\\item A $'+mass1+' \KG$ rock is dropped from a height of  $'+height+'\\MET$. After the rock hits the ground, it bounces up to a height of $'+heightb+'\\MET$.\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item Calculate the initial potential energy of the rock. (6B)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')        
        self.f.write('\\item State the work done by gravity and the kinetic energy just before the rock bounces. (6B)\n\n')
        self.f.write('\\newpage\n\n')        
        self.f.write('\\item Calculate the expected maximum speed ofof the ball just before the bounce. (6A)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Calculate the potential energy of the rock at the maximum height after the bounce. (6B)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Calculate the speed just after the bounce. (6D)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item State the energy lost to heat and defelction during the bounce. (6D)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\end{enumerate}\n')


        self.f.write('\\item Laws of thermodynamics.\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item Write a correct statement and an example or picture  of the Zeroth law of thermodynamics. (6E)\n\n')
        self.f.write('\\newpage\n\n')        
        self.f.write('\\item Write a correct statement and an example or picture  of the First law of thermodynamic.(6E)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Write a correct statement and an example or picture  of the Second law of thermodynamic.(6E)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\end{enumerate}\n')


        
        self.f.write('\\item What is the typical medium and type for each  wave generated in the following examples.\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item A rock dropped in the lake.(7A)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item A person yells from across the room.(7A)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item The sun shines light on the earth.(7A)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\end{enumerate}\n')
        self.f.write('\\newpage\n\n')

        self.f.write('\\item A $'+mass+'\\KG$ ball is thrown against a wall with a constant speed of $'+speed1+'\\MPS$.  It sticks to the wall at a height of $'+height+'\\MET$ then falls to the floor.\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item Calculate the momentum of the ball before it hits the wall.(6D)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Calculate the energy lost in the collision.(6C)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Calculate the potential energy of the ball when it is stuck to the wall(6B).\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Assuming the ball loses half the energy after it bounces on the floor, calculate the maximum height the ball will reach(6D).\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\end{enumerate}\n')
       

        self.f.write('\\item Suppose we have four identical thermally conductive containers.  Container A is at $'+temp1+' \\Kelvin$, container B is at $'+temp2+' \\Kelvin$, container C is at $'+temp3+' \\Kelvin$ and container D is at $'+temp1+' \\Kelvin$.  Draw a picture for each situation, and justify each answer with several sentences.\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item If container A and C are placed in thermal contact. Indicate is the direction of heat flow.(6E)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item If container B and D are placed in thermal contact. Indicate the direction of heat flow.(6E)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item If container A and D are placed in thermal contact. Indicate is the direction of heat flow.(6E)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\end{enumerate}\n')

        
        self.f.write('\\item A wave has a frequency of $'+freq+'\\HZ$ and a wave speed of $'+wavespeed+'\\MPS$. Calculate the wavelength.(7B)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item A wave has a frequency of $'+freq+'\\HZ$ and a wavelength of $'+wavelength+'\\MET$. Calculate the wavespeed(7B).\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item A wave has a wave speed of $'+wavespeed+'\\MPS$ and a wavelength of $'+wavelength+'\\MET$. Calculate the frequency(7B).\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item A wave has a frequency of $'+freq+'\\HZ$. Calculate the period.(7B)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')





        self.f.write('\\item Differentiate reflection, refraction, diffraction. In each case, classify as reflection, refraction, and diffraction.\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item image in a mirror(7D).\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item the image trasmited by eye glasses(7D).\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item a bending of straw in water(7D).\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item a rainbow seen on a surface such as a DVD(7D).\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\end{enumerate}\n')

        

        self.f.write('\\item Consider a circuit built from a $'+volt+' \\VOLTS$ battery and two resistors, $'+R1+' \\OHMS$ and $'+R2+' \\OHMS$ .\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item Draw a circuit in which one of the resistor is connected to the battery to create a closed circuit.  Calculate the current and potential accross the resistor.(5F)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Calculate the power supplied by the batery in this example.(5F)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Draw a circuit in which the resistors are connected to the battery in series.  Draw and calcualte the equivelent circuit.  Calculate the current and potential.(5F)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Calculate the power dissapated by each resisitor.(5F)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Draw a circuit in which the resistors are connected in parallel to the battery.  Draw and calcualte the equivelent circuit.  Calculate the current and potential.(5F)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\end{enumerate}\n')

        

       

        self.f.write('\\item Suppose there are two charges $q_1$ and $q_2$ a distance $r$ apart.\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item If $q_1$ was increased to $7q_1$ what would be the change in the force?(5C)\n\n')
        self.f.write('\\newpage\n\n')
        self.f.write('\\item If the charges were separated by $4r$ instead of $r$, what would be the change in the force?(5C)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item If $r='+r+'X10^{'+exp2+'} \\MET$, and $q_1='+q1+'X10^{'+exp+'} \\COUL$ and and $q_2='+q2+'X10^{'+exp+'} \\COUL$,  calculate the electrical force between the charges.(5C)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\end{enumerate}\n')


        ME=str(float(random.randint(10,99)/10))
        MEexp=str(random.randint(10,25))
        RE=str(float(random.randint(20,90)/10))
        REexp=str(random.randint(-8,8))
        FREQ=str(random.randint(1,9))
        FREQexp=str(random.randint(5,34))
        LE=str(float(random.randint(30,99)/10))
        LEexp=str(random.randint(10,30))
        n1=float(random.randint(2,20))
        n2=float(random.randint(21,40))
        L1=1.602e-19*13.6/(n1*n1)
        L2=1.602e-19*13.6/(n2*n2)
        self.toExp(L1)
        E1=self.v
        self.toExp(L2)
        E2=self.v        
        n4=float(random.randint(25,45))
        n3=float(random.randint(5,22))
        L4=1.602e-19*13.6/(n4*n4)
        L3=1.602e-19*13.6/(n3*n3)
        self.toExp(L4)
        E4=self.v
        self.toExp(L3)
        E3=self.v        

        
        self.f.write('\\item Cacluate the equivalent rest energy for a $'+ME+'X10^{-'+MEexp+'} \\KG$ mass. (8C)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Cacluate the mass for a particle with rest energy of $'+RE+'X10^{'+REexp+'} \\JE$. (8C)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item An electron transitions from an energy of $'+E1+' \\JE$ to  $'+E2+'\\JE$.  Calculate the frequency of emitted photon. (8C)\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')

        
        self.f.write('\\end{enumerate}\n')


g=CA4("Physics 1","Physics Spring Final Exam 2018")
for x in range(1,50):
    g.WritePage(x)
