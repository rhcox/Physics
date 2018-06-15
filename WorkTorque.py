import GuessBase
import random
import math

class WorkTorque(GuessBase.Guess):
    def __init__(self,course, title, rowh):
        super(WorkTorque, self).__init__(course, title, rowh)

    def PAGE(self):
        self.f.write('\\normalsize\n')
        random.seed(self.rnum)
        self.f.write('\\begin{enumerate}\n')

        mass=str((float(random.randint(25,70))/10.))
        mass1=str((float(random.randint(2,9))/10.))
        heightf=float(random.randint(20,50))/10.0        
        height=str(heightf)
        diam=str(float(random.randint(50,90))/100.0)        
        speedi=str((float(random.randint(16,50))/10.0))
        speedf=str((float(random.randint(60,80))/10.0))
        force=str((float(random.randint(40,70))/10.0))
        time=str((float(random.randint(5,29))/10.0))
        len=str(round(heightf/0.8,1))

        
        P=round((1./2.*2.*4.*4.-1./2.*2.*6.*6.)/(-9.),2)
        answer='P=$'+str(P)+'\\Watt$' 
        self.f.write('\\GUESSA{A $2 \\KG$ mass accelerates from $4\\MPS$ to $6\\MPS$ in $9\\SEC$.  Calculate the power.}{'+answer+'}\n')
        self.f.write('\\GUESS{A $'+mass+'\\KG$ ball mass accelerates from $'+speedi+'\MPS$ to $'+speedf+'\\MPS$ in $'+time+'\\SEC$.  Calculate the power.}\n')

        

        p=round((5.*10.*8.)/math.sqrt(2.*5./10.),2)
        answer='P=$'+str(p)+'\\Watt$'     
        self.f.write('\\GUESSA{A $5 \\KG$ ball is dropped from rest $8 \\MET$ above the floor. Caclculate the power developed just before the ball hits the ground.}{'+answer+'}\n')
        self.f.write('\\GUESS{A $'+mass+'\\KG$ ball is dropped from rest $'+height+'\\MET$ above the floor. Caclculate the power developed just before the ball hits the ground..}\n')
        self.f.write('\n\n\\newpage\n\n')



        v=round(math.sqrt(10.*0.75),2)
        answer='v=$'+str(v)+' \\MPS$'    
        self.f.write('\\GUESSA{A $0.5\\KG$ car is traveling around a verticle loop with a radius of $0.75\\MET$.  What is the minimum speed the car must travel at the top of the loop to complete the loop.}{'+answer+'}\n')
        self.f.write('\\GUESS{A $'+mass1+'\\KG$ car is traveling around a verticle loop with a radius of $'+diam+'\\MET$.  What is the minimum speed the car must travel  at the top of the loop to complete the loop.}\n')

        
        t=3.*0.5
        answer='$\\tau='+str(t)+' \\TQ$'
        self.f.write('\\GUESSA{A force of $3\\NF$ is applied perpendicularly to a door $0.5\MET$ from the hinges of a door.  Calculate the torque.}{'+answer+'}\n')
        self.f.write('\\GUESS{A force of $'+force+'\\NF$ is applied perpendicularly to a door $'+diam+'\MET$ from the hinges of a door.  Calculate the torque.}\n')

        self.f.write('\\end{enumerate}\n')

g=WorkTorque("Physics 1","WorkTorque", "Large")
for x in range(1, 90):
    g.WritePage(x)
