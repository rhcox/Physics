import Base
import random

class CA4(Base.BASE):
    def __init__(self,course, title):
        super(CA4, self).__init__(course, title)

    def PAGE(self):
        self.f.write('\\large\n')
        self.f.write('This review is due May 2 at beginning of your class.Late work earns 0 points.\n')

        self.f.write('\\normalsize\n')
        random.seed(self.rnum)
        space="12"


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
 
        self.f.write('\\item Differentiate reflection, refraction, diffraction. In each case, classify as reflection, refraction, and diffraction.\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item image in a mirror.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item the image trasmited by eye glasses.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item a bending of straw in water.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item a rainbow seen on a surface such as a DVD.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\end{enumerate}\n')

        

        self.f.write('\\item Consider a circuit built from a $'+volt+' \\VOLTS$ battery and two resistors, $'+R1+' \\OHMS$ and $'+R2+' \\OHMS$ .\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item Draw a circuit in which one of the resistor is connected to the battery to create a closed circuit.  Calculate the current and potential accross the resistor.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Calculate the power supplied by the batery in this example.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Draw a circuit in which the resistors are connected to the battery in series.  Draw and calcualte the equivelent circuit.  Calculate the current and potential.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Calculate the power dissapated by each resisitor.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Suppose a third resistor was added in series to this circuit in series such that  the current throught the batery was  '+current+' A.  Calcualte the value of the thrid resistor.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Draw a circuit in which the resistors are connected in parallel to the battery.  Draw and calcualte the equivelent circuit.  Calculate the current and potential.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Calculate the power dissapated by each resisitor.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Draw a circuit in which the resistors are connected in parallel to the battery.  Draw and calcualte the equivelent circuit.  Calculate the current and potential.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Using the previously calculated value of the third resistor, Draw a circuit in which one resistor is in series with the batter, and then two  resistors are connected in parallel.  Draw and calcualte the equivelent circuit.  Calculate the current and potential.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\end{enumerate}\n')

       

        self.f.write('\\item Suppose there are two charges $q_1$ and $q_2$ a distance $r$ apart.\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item State the electical force between them.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item If $q_1$ was increased to $7q_1$ what would be the change in the force?.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item If the charges were separated by $4r$ instead of $r$, what would be the change in the force?\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item If the charges were separated by $\\frac{r}{6}$ instead of $r$, what would be the change in the force?\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item If the charges were separated by $6r$ instead of $r$, and $q_1$ was increased ot $3q_1$ and and $q_2$ was increased ot $12q_2$, what would be the change in the force?\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item If $r='+r+'X10^{'+exp2+'} \\MET$, and $q_1='+q1+'X10^{'+exp+'} \\COUL$ and and $q_2='+q2+'X10^{'+exp+'} \\COUL$,  calculate the electrical force between the charges.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        
        self.f.write('\\end{enumerate}\n')

  



        
        self.f.write('\\end{enumerate}\n')


g=CA4("Physics 1","CA 6 Review")
for x in range(1, 40):
    g.WritePage(x)
