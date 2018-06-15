import GuessBase
import random

class KineticE(GuessBase.Guess):
    def __init__(self,course, title, rowh):
        super(KineticE, self).__init__(course, title, rowh)

    def PAGE(self):
        self.f.write('\\normalsize\n')
        random.seed(self.rnum)
        self.f.write('\\begin{enumerate}\n')

        mass=str((float(random.randint(200,600))/10.))
        height=str((float(random.randint(20,50))/10.0))
        speed=str((float(random.randint(5,30))/10.0))

        self.f.write('\\GUESS{A 20 kg box is held 4m above a table. Calculate the potential energy relative to the table.}\n')
        self.f.write('\\GUESS{A '+mass+' kg box is held '+height+' m above a table. Calculate the potential energy relative to the table.}\n')

        self.f.write('\\GUESS{A 10 kg box is being pushed along a table at 5m/s.  Calculate the kinetic energy of the box.}\n')
        self.f.write('\\GUESS{A '+mass+' kg box is being pushed along a table at '+speed+' m/s.  Calculate the kinetic energy of the box.}\n')

        self.f.write('\\GUESS{A 15 kg box is lifted from the floor to 3 m above the floor. Calculate the work done against gravity.}\n')
        self.f.write('\\GUESS{A '+mass+' kg box is lifted from the floor to '+height+' m above the floor. Calculate the work done against gravity.}\n')

        self.f.write('\\GUESS{A 15 kg box is dropped from rest 3 m above the floor. Calculate the kinetic energy and speed just before the ball hit the floor.  Ignore any drag or friction.}\n')
        self.f.write('\\GUESS{A '+mass+' kg box is dropped from rest '+height+' above the floor. Calculate the kinetic energy and speed just before the ball hit the floor.  Ignore any drag or friction}\n')

        self.f.write('\\end{enumerate}\n')

g=KineticE("Physics 1","Kinetic and Potential Energy", "small")
for x in range(1, 100):
    g.WritePage(x)
