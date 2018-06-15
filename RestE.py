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

        massg=str((float(random.randint(411,788))/100000.))
        E0=str((float(random.randint(20,80))/10.))
        E0exp=str(random.randint(10,25))

        F=str((float(random.randint(10,60))/10.))
        Fexp=str(random.randint(10,25))

        EP=str((float(random.randint(10,99))/10.))
        EPexp=str(random.randint(5,24))

        
        re=0.000004*(3.0e8)*(3.0e8)
        self.toExp(re)
        answer='$E_0 =' +self.v+' \\JE$'
        self.f.write('\\GUESSAF{Calculate the rest energy of 0.004 grams of sodium.}{'+answer+'}{$E_0=m_0 \\cdot c^2$ \n}')
        self.f.write('\\GUESS{Calculate the rest energy of '+E0+' grams of sodium.}\n')

        m=(2.0e8)/((3.0e8)*(3.0e8))
        self.toExp(m)
        answer='$M_0 =' +self.v+' \\KG$'
        self.f.write('\\GUESSAF{Calculate the mass of a particle if the rest energy is $2X10^{8} \\JE$.}{'+answer+'}{$E_0=m_0 \\cdot c^2$ }\n')
        self.f.write('\\GUESS{Calculate the mass of a particle if the rest energy is $'+E0+'X10^{'+E0exp+'} \\JE$.}\n')

        self.f.write('\\newpage\n')

        eng=(6.6e-34)*(3.0e5)
        self.toExp(eng)
        answer='$E =' +self.v+' \\JE$'
        self.f.write('\\GUESSAF{Calculate the energy of a photon with a frequency of $3X10^{5} \\HZ$.}{'+answer+'}{$E=h \\cdot \\nu$ }\n')
        self.f.write('\\GUESS{Calculate the energy of a photon with a frequency of $'+F+'X10^{'+Fexp+'} \\HZ$.}\n')

        freq=(3.0e-25)/(6.6e-34)
        self.toExp(freq)
        answer='$\\nu =' +self.v+' \\HZ$'
        self.f.write('\\GUESSAF{Calculate the frequency of a photon with an energy of $3X10^{-25} \\JE$.}{'+answer+'}{$E=h \\cdot \\nu$ }\n')
        self.f.write('\\GUESS{Calculate the frequency of a photon with an energy of $'+EP+'X10^{-'+EPexp+'} \\HZ$.}\n')

        self.f.write('\\end{enumerate}\n')

g=Waves("Physics 1","Rest energy", "small")
for x in range(1, 40):
    g.WritePage(x)
