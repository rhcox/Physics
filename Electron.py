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


        evC=str((float(random.randint(8,49))/10.))
        evJ=1.6e-19
        planck=6.6e-34
        n0=str(random.randint(5,25))
        n1=str(random.randint(4,15))
        n2=str(random.randint(16,30))


        
        joules=5.0*evJ
        self.toExp(joules)
        answer='$E_0 =' +self.v+' \\JE$'
        self.f.write('\\GUESSAF{Calculate the energy in joules if the energy is $5\\EV$.}{'+answer+'}{$1 \\EV= 1.6X10^{-19} \\JE$ \n}')
        self.f.write('\\GUESS{Calculate the energy in joules if the energy is $'+evC+'\\EV$.}\n')

        evN=13.6/9.0
        joules=13.6/9.0*evJ
        self.toExp(joules)
        answer='$E_0 =' +self.v+' \\JE$=' +str(round(evN,2))+'\\EV'
        self.f.write('\\GUESSAF{Calculate the ionization energy in $\\EV$ and joules of an electron in an hydrogen atom excited to a state n=3.}{'+answer+'}{$E= \\frac{13.6}{n^2} \\EV$ \n}')
        self.f.write('\\GUESS{Calculate the ionization energy in $\\EV$ and joules of an electron in an hydrogen atom excited to a state n='+n0+'.}\n')

        self.f.write('\\newpage\n')

         freq=(13.6/1.0-13.6/16.0)*evJ/planck
        self.toExp(freq)
        answer='$E_0 =' +self.v+' \\HZ$'
        self.toExp(planck)
        self.f.write('\\GUESSAF{Calculate the frequency of the emitted photon if an electron in a hydrogen atom transtion from n=4 to n=1.}{'+answer+'}{$E=h \\cdot \\nu$,    $h='+self.v+'\\frac{m^2 \\cdot kg}{s}$ \n}')
        self.f.write('\\GUESS{Calculate the frequency of the emitted photon if an electron in a hydrogen atom transtion from n='+n2+' n=1.}\n')

        freq=(13.6/49-13.6/9)*evJ/planck
        self.toExp(freq)
        answer='$E_0 =' +self.v+' \\HZ$'
        self.toExp(planck)
        self.f.write('\\GUESSAF{Calculate the frequency of the absorbed photon needed to exicte an electron in a hydrogen atom  from n=3 to n=7.}{'+answer+'}{$E=h \\cdot \\nu$,    $h='+self.v+'\\frac{m^2 \\cdot kg}{s}$ \n}')
        self.f.write('\\GUESS{Calculate the frequency of the absorbed photon needed to exicte an electron in a hydrogen atom  from n='+n1+' n='+n2+'.}\n')

        self.f.write('\\end{enumerate}\n')

g=Waves("Physics 1","Electron Levels", "small")
for x in range(1, 40):
    g.WritePage(x)
