import GuessBase
import random
import math
import re

class Waves(GuessBase.Guess):
    def __init__(self,course, title, rowh):
        super(Waves, self).__init__(course, title, rowh)

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
        U=round(0.5*2*15*15,1)
        maxh=round(U/(2*10),1)


        period=(float(random.randint(20,50))/10.)
        wavelength=(float(random.randint(2,20))/10.)
        frequency=random.randint(30,70)
        mant=str(random.randint(1,9))
        exp=str(random.randint(2,24))
        length=(float(random.randint(30,90))/10.0)


        
        i=float(random.randint(50,99))/10.0
        v=random.randint(9,30)
        R=random.randint(100,200)
        p=2.5*8.0
        answer='$p ='+str(p)+' \\Watt$'
        self.f.write('\\GUESSAF{You measure $2.5 \\AMPS$ through a battery of $8 \\VOLTS$.  Calculate is the power of the circuit.}{'+answer+'}{$p=V \cdot i$}\n')
        self.f.write('\\GUESS{You measure $'+str(i)+' \\AMPS$ through a battery of $'+str(v)+' \\VOLTS$.  Calculate is the power of the circuit. .}\n')

        p=2.5e-6*2.5e-6*float(200e3)
        self.toExp(p)
        answer='$p ='+self.v+' \\Watt$'
        self.f.write('\\GUESSAF{You measure $2.5 \\AMPS[\\mu]$ through a resistor of $200 \\OHMS[k]$.  Calculate is the power of the circuit.}{'+answer+'}{$p=i^2 \cdot R$}\n')
        self.f.write('\\GUESS{You measure $'+str(i)+' \\AMPS$ through a resistor of $'+str(R)+' \\OHMS[k]$..  Calculate is the power of the circuit. .}\n')


        self.f.write('\\newpage\n')

        p=7.0*7.0/float(200e6)
        self.toExp(p)
        answer='$p ='+self.v+' \\Watt$'
        self.f.write('\\GUESSAF{You apply a potential of $7 \\VOLTS$ to a resistor of $200 \\OHMS[M]$.  Calculate is the power of the circuit.}{'+answer+'}{$p=\\frac{V^2}{R}$}\n')
        self.f.write('\\GUESS{You apply a potential of $'+str(v)+' \\VOLTS$  a resistor of $'+str(R)+' \\OHMS[k]$.  Calculate is the power of the circuit. .}\n')



        
        V=random.randint(8,40)
        R1=random.randint(5,29)
        R2=random.randint(30,60)
        Re=5.0+12.0
        p=7.0*7.0/(1/float(1/5.0e3+1/12.0e3))
        self.toExp(p)
        answer='$p ='+self.v+' \\Watt$'
        self.f.write('\\GUESSAF{Two resistors are in parallel with a $7 \\VOLTS$ battery.  The values of the resistors are $5 \\OHMS[k]$ and $12 \\OHMS[k]$. Calculate is the power supplied by the battery.}{'+answer+'}{$p=\\frac{V^2}{R}$ $R_e=(\sum_{i=1}^{i=n} \\frac{1}{R_i})^{-1}$ }\n')
        self.f.write('\\GUESS{Two resistors are in parallel with a $'+str(V)+' \\VOLTS$ battery.  The values of the resistors are $'+str(R1)+' \\OHMS[k]$ and $'+str(R2)+' \\OHMS[M]$.  Calculate is the power supplied by the battery.}\n')


        self.f.write('\\end{enumerate}\n')

g=Waves("Physics 1","Power and Circuits", "small")
for x in range(1, 80):
    g.WritePage(x)
