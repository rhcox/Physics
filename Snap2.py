import Base
import random

class Snap2(Base.BASE):
    def __init__(self,course, title):
        super(Snap2, self).__init__(course, title)

    def PAGE(self):
        self.f.write('\\large\n')
        self.f.write('This review is due January 30 no later than 9am.  It is worth bonus points. If turned in late, it is worth no points.\n')

        self.f.write('\\normalsize\n')
        random.seed(self.rnum)
        space="10"

        mass=str(random.randint(8,70))
        force=str(float(random.randint(100,200))/10.0)        
        speed1=str((float(random.randint(16,40))/10.0))
        speed2=str((float(random.randint(60,99))/10.0))
        speed3=str(random.randint(20,40))
        dist=str(random.randint(15,40))
        time=str((float(random.randint(12,29))/10.0))


        self.f.write('\\begin{enumerate}\n')

        self.f.write('\\item A $'+mass+'\\KG$ mass is at rest.  It is push accross a frictionless table with a force of $'+force+'\\NF$.\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item Calculate the acceleration.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Calculate the speed after $'+dist+' \\MET$ of travel.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\end{enumerate}\n')
 
        self.f.write('\\item A $'+mass+'\\KG$ box is pushed so it travels at $'+speed1+'\\MPS$.  It is then accelerated to $'+speed2+'\\MPS$.\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item Calcualte the initial and final kinetic energy.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Calcualte the work done to accelerate the box.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Calculate the initial and final momentum.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Calculate the impulse.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\end{enumerate}\n')

        self.f.write('\\item A $'+mass+' \\KG$ ball falls from rest from the top of a tall building.  It achieves a speed of $54 \\MPS$ just before it hits the ground.\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item Calculate the kinetic energy just prior to hititng the gound.  Explain why kinetic energy is maxiumum at bthis point.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')        
        self.f.write('\\item State the potential energy at the top of thge building.  Explain why the potential energy is maximum at this point.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')        
        self.f.write('\\item Use the potential energy to calculate the height of the building.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Calculate the time of flight.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item The ball bounces to half the height.  Explain how the enrgy is conversed even though the potential energy is reduced.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\end{enumerate}\n')
        
        self.f.write('\\item A $'+mass+'00 \\KG$ rocket is at rest.  It is accelerated to $'+speed3+'\\MPS$. over $3 \\SEC$.\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item Calculate the initial and final momentum.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Calculate the impulse.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Calculate the force.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\end{enumerate}\n')

        self.f.write('\\item A $'+mass+' \KG$ mass traveling a $'+speed2+'\\MPS$ collides and sticks to a second mass which is at rest.  The speed of the two masses after the collision is $'+speed1+'\\MPS$.\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item Calculate the initial momentum of the system.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Set up the equation for the final momentum of the system.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item Calculate the values of the second mass.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        
        self.f.write('\\end{enumerate}\n')

        self.f.write('\\item A mass is pushed from one end to the other of a $'+dist+'\\MET$ table with a force of $'+force+'\\NF$.\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item Calculate the work done.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item If the work was done over $4 \\SEC$ calculate the power.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\item If the power developed was $100\\Watt$, calcualte the time.\n\n')
        self.f.write('\\vspace{'+space+'mm}\n')
        self.f.write('\\end{enumerate}\n')

        
        self.f.write('\\end{enumerate}\n')


g=Snap2("Physics 1","SS2 Review")
for x in range(1, 50):
    g.WritePage(x)
