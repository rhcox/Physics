import GuessBase
import random
import math

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

        i=random.randint(5,24)
        R=random.randint(26,50)
        
        v=float(25)*1e6*float(8)*1e-3
        answer='$v ='+str(v)+' \\VOLTS$'
        self.f.write('\\GUESSAF{A $25 \\OHMS[M]$ resistor is placed in series with a battery.  A current of $8 \\AMPS[m]$ through the resistor is measured.  Calculate the potential of the battery.}{'+answer+'}{$V=i \cdot r$}\n')
        self.f.write('\\GUESS{A $'+str(R)+' \\OHMS[M]$ resistor is placed in series with a battery.  A current of $'+str(i)+' \\AMPS[m]$ through the resistor is measured.  Calculate the potential of the battery.}\n')

        V=random.randint(15,50)
        re=float(14)/(float(8)*1e-3)
        answer='$v ='+str(v)+' \\VOLTS$'
        self.f.write('\\GUESSAF{A resistor is placed in series with a $14 \\VOLTS$ battery.  A current of $8 \\AMPS[m]$ through the resistor is measured.  Calculate the value of the resistor.}{'+answer+'}{$V=i \cdot r$}\n')
        self.f.write('\\GUESS{A resistor is placed in series with a $'+str(V)+' \\VOLTS$ battery.  A current of $'+str(i)+' \\AMPS[m]$ through the resistor is measured. Calculate the value of the resistor.}\n')

        self.f.write('\\newpage\n')
        
        V=random.randint(8,40)
        R1=random.randint(5,29)
        R2=random.randint(30,60)
        Re=5.0+12.0
        I=round(7.0/(float(Re)*1000),5)
        answer='$R_e ='+str(Re)+' \\OHMS[k]$      $i ='+str(I)+' \\AMPS$'
        self.f.write('\\GUESSAF{Two resistors are in series with a $7 \\VOLTS$ battery.  The values of the resistors are $5 \\OHMS[k]$ and $12 \\OHMS[k]$.  Draw the equivalent circuit with the current through the battery shown.}{'+answer+'}{$R_e=\sum_{i=1}^{i=n} R_i$}\n')
        self.f.write('\\GUESS{Two resistors are in series with a $'+str(V)+' \\VOLTS$ battery.  The values of the resistors are $'+str(R1)+' \\OHMS[k]$ and $'+str(R2)+' \\OHMS[k]$.  Draw the equivalent circuit with the current through the battery shown.}\n')


        V=random.randint(10,45)
        R=random.randint(50,120)
        Re=26/2
        I=round(9.0/(float(Re)*1000000),7)
        answer='$R_e ='+str(Re)+' \\OHMS[k]$      $i ='+str(I)+' \\AMPS$'
        self.f.write('\\GUESSAF{Two resistors are in parallel with a $9 \\VOLTS$ battery.  The values of the resistors are both  $26 \\OHMS[M]$.  Draw the equivalent circuit with the current through the battery shown.}{'+answer+'}{$R_e=(\sum_{i=1}^{i=n} \\frac{1}{R_i})^{-1}$}\n')
        self.f.write('\\GUESS{Two resistors are in series with a $'+str(V)+' \\VOLTS$ battery.  The values of the resistors are both $'+str(R)+' \\OHMS[M]$.  Draw the equivalent circuit with the current through the battery shown.}\n')
        


        self.f.write('\\end{enumerate}\n')

g=Waves("Physics 1","Ohms Law", "small")
for x in range(1, 80):
    g.WritePage(x)
