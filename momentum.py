import GuessBase
import random

class Momentum(GuessBase.Guess):
    def __init__(self,course, title, rowh):
        super(Momentum, self).__init__(course, title, rowh)

    def PAGE(self):
        self.f.write('\\normalsize\n')
        random.seed(self.rnum)
        self.f.write('\\begin{enumerate}\n')

        mass=str((float(random.randint(25,70))/10.))
        heightf=float(random.randint(20,50))/10.0        
        height=str(heightf)
        speed=str((float(random.randint(16,50))/10.0))
        force=str((float(random.randint(30,60))/10.0))
        time=str((float(random.randint(5,29))/10.0))
        len=str(round(heightf/0.8,1))

        
        P=round(2*5)
        answer='P=$'+str(P)+'\\NS$' 
        self.f.write('\\GUESSA{A $2 \\KG$ mass is traveling at $5 \\MPS$.  Calculate the momentum.}{'+answer+'}\n')
        self.f.write('\\GUESS{A $'+mass+' \\KG$ ball mass is traveling at $'+speed+' \\MPS$.  Calculate the momentum.}\n')

        
        mass1f=random.randint(400,900)
        mass1=str(mass1f)
        mass2f=random.randint(30,999)
        mass2=str(mass2f)
        speed1f=random.randint(10,999)
        speed1=str(speed1f)
        v=round(200.0/(200.0+30.0)*15.0,2)
        answer='v=$'+str(v)+'\\MPS$'     
        self.f.write('\\GUESSA{A $200 \\KG$ truck is traveling at constant  $15 \\MPS$ down a straight flat road. A $30 \\KG$ boulder falls in the truck doing no damage. Calculate the speed of the truck immediately after impact.}{'+answer+'}\n')
        self.f.write('\\GUESS{A $'+mass1+' \\KG$ truck is traveling at  $'+speed1+' \\MPS$ down a straight flat road. A $'+mass2+'\\KG$ boulder falls in the truck doing no damage. Calculate the speed of the truck immediately after impact.}\n')

        self.f.write('\n\n\\newpage\n\n')


        mass5=str(random.randint(3000,4000))
        mass6=str(random.randint(400,500))
        speed5=str(random.randint(300,500))
        P=(2500*200)/(2500-350)
        answer='p=$'+str(P)+' \\NS$'        
        self.f.write('\\GUESSA{A $2500 \\KG$ ship is traveling through space at $200\MPS$.  It buns $350 \\KG$ of fuel.  Calculate the speed due to the loss of mass.}{'+answer+'}\n')
        self.f.write('\\GUESS{A $'+mass5+'\\KG$ ship is traveling through space at $'+speed5+' \\MPS$.  It burns $'+mass6+'\\KG$.   of fuel.  Calculate the speed due to the loss of mass.}\n')

        times=str(random.randint(10,40))
        answer='$\\frac{v_2i}{'+times+'}$'
        self.f.write('\\GUESSA{Mass 1 has 2 times the mass as Mass 2. Mass 1 is at rest. Mass 2 has a positive speed. The mases collide. After the collision Mass 2 is a rest and Mass 1 has a positive speed. Calculate the speed of Mass 1 after the collision.}{'+answer+'}\n')
        self.f.write('\\GUESS{Mass 1 has '+times+' times the mass as Mass 2. Mass 1 is at rest.  Mass 2 has a positive speed.  The mases collision. After the collison Mass 2 is a rest and Mass 1 has a positive speed. Calculate the speed of Mass 1 after the collision.}\n')

        self.f.write('\\end{enumerate}\n')

g=Momentum("Physics 1","Momentum and Impulse", "Large")
for x in range(1, 100):
    g.WritePage(x)
