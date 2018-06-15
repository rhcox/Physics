import GuessBase
import random

class WorkE(GuessBase.Guess):
    def __init__(self,course, title, rowh):
        super(WorkE, self).__init__(course, title, rowh)

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
        U=round(0.5*2*15*15,1)
        maxh=round(U/(2*10),1)
        answer='U=$'+str(U)+' \\JE$  '+'h=$'+str(maxh)+' \\MET$  '+ 'W=$'+str(U)+'\JE$' 
        self.f.write('\\GUESSA{A $2 \\KG$ ball is tossed up in the air from the ground at a vertical speed of $15 \\MPS$.  Calculate the maximum potential energy, height achieved by the ball, and work done by gravity during the ascent.}{'+answer+'}\n')
        self.f.write('\\GUESS{A $'+mass+' \\KG$ ball is tossed up in the air from the ground at a vertical speed of $'+speed+' \\MPS$.  Calculate the maximum potential energy, height achieved by the ball, and work done by gravity during the ascent.}\n')

        W=5*8
        answer='W=$'+str(W)+'\\JE$'
        self.f.write('\\GUESSA{A mass is pushed with a force of $5 \\NF$ a distance of $8 \\MET$. Calculate the work done on the ball.}{'+answer+'}\n')
        self.f.write('\\GUESS{A mass is pushed with a force of $'+force+' \\NF$ a distance of $'+height+' \\MET$. Calculate the work done on the ball.}\n')

        
        W=2.0*10.0*4.0
        F=round(W/5.0)
        answer='W=$'+str(W)+'\\JE$  F=$'+str(F)+'\\NF$'     
        self.f.write('\\GUESSA{A $2 \\KG$ mass is pushed up an inclined plane with a length of $5 \\MET$ inclined plane so that the mass is $4 \\MET$ high.  Calculate the work done against gravity and the minimum force that was used to push the mass up the inclined plane, assuming no friction.}{'+answer+'}\n')
        self.f.write('\\GUESS{A $'+mass+' \\KG$ mass is pushed up an inclined plane with a length of $'+len+' \\MET$ inclined plane so that the mass is $'+height+'\\MET$ high.  Calculate the work done against gravity and the minimum force that was used to push the mass up the inclined plane, assuming no friction.}\n')

        P=5*4/3
        answer='P=$'+str(P)+' \\Watt$ (watts)'        
        self.f.write('\\GUESSA{A box is pushed with a force of $5\NF$ a distance of $4 \\MET$ in $3 \\SEC$.  Calculate the power.}{'+answer+'}\n')
        self.f.write('\\GUESS{A box is pushed with a force of $'+force+'\\NF$ a distance of $'+height+' \\MET$ in $'+time+'\\SEC$.  Calculate the power.}\n')

        self.f.write('\\end{enumerate}\n')

g=WorkE("Physics 1","Work Energy Theorem and Power", "small")
for x in range(1, 2):
    g.WritePage(x)
