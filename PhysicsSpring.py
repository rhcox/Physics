import GuessBase
import random

class Waves(GuessBase.Guess):
    def __init__(self,course, title, rowh):
        super(Waves, self).__init__(course, title, rowh)

    def PAGE(self):
        self.f.write('\\normalsize\n')
        random.seed(self.rnum)
        self.f.write('\\begin{enumerate}\n')



        K=str(float(random.randint(10,30))/10.)
        S=str(float(random.randint(10,49))/100.)
        S1=str(float(random.randint(51,90))/100.)
        mass1=str(float(random.randint(30,200))/100.)
        g=str(float(random.randint(110,190))/10.)


        
        mass=round(0.2*1.2/9.8,3)
        answer='$m ='+str(mass)+' \\KG$'
        self.f.write('\\GUESSAF{A spring with a constant of $1.2\\NPM$ is hung freely vertically. It stretches $0.2\\MET$ when an object is attached in the earths gravitational field, calculate the mass.}{'+answer+'}{$f=-k \cdot \Delta X$}\n')
        self.f.write('\\GUESS{A spring with a constant of $'+K+'\\NPM$ is hung freely vertically. It stretches $'+S+'\\MET$ when an object is attached in the earths gravitational field, calculate the mass.}\n')

        dx=round(0.04*10/1.2)
        answer='$dx ='+str(dx)+' \\MET$'
        self.f.write('\\GUESSAF{A spring has a constant of $1.2\\NPM$.  If the spring is allowed to freeely hang vertically has a $0.04\\KG$ attached in the earths gravitational field, calculate the distance the spring will streatch.}{'+answer+'}{$f=-k \cdot \Delta X$}\n')
        self.f.write('\\GUESS{A spring has a constant of $'+K+'\\NPM$.  If the spring is allowed to freeely hang vertically has a $'+mass1+'\\KG$ attached in the earths gravitational field, calculate the distance the spring will streatch.}\n')

        self.f.write('\\newpage\n')

        dx=round(4*0.1/10)
        answer='$dx ='+str(dx)+' \\MET$'
        self.f.write('\\GUESSAF{A mass is hung from a spring on earth and the spring stretches $0.1\\MET$.  How much will the spring stretch on a planet with gravity of $4\\MPS$}{'+answer+'}{$f=-k \cdot \Delta X$}\n')
        self.f.write('\\GUESS{A mass is hung from a spring on earth and the spring stretches $'+S+'\\MET$.  How much will the spring stretch on a planet with gravity of $'+g+'\\MPS$}\n')
 
        dx=round(10*0.07/.1)
        answer='$g ='+str(dx)+' \\MPS$'
        self.f.write('\\GUESSAF{A mass is hung from a spring on earth and the spring stretches $0.1\\MET$. The same mass stretches the spring $0.07\\MET$ on another planet.  What is the local gravity on that planet?}{'+answer+'}{$f=-k \cdot \Delta X$}\n')
        self.f.write('\\GUESS{A mass is hung from a spring on earth and the spring stretches $'+S+'\\MET$. The same mass stretches the spring $'+S1+'\\MET$ on another planet.  What is the local gravity on that planet?}\n')

        self.f.write('\\end{enumerate}\n')

g=Waves("Physics 1","Springs", "small")
for x in range(1, 80):
    g.WritePage(x)
