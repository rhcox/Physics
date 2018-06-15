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
        c=3e8
        n0=str(random.randint(5,25))
        n1=str(random.randint(4,15))
        n2=str(random.randint(16,30))
        mass=str((float(random.randint(18,70))/100.))
        speed=str(random.randint(8,30))
        speedc=str((float(random.randint(20,49))/100.))
        speedcf=str((float(random.randint(800,990))/1000.))
        masse=str((float(random.randint(10,89))/10.))


        
        wavelength=planck/(0.14*7.0)
        self.toExp(wavelength)
        answer='$\\lambda =' +self.v+' \\MET$'
        wavelength=wavelength/1.0e-10
        self.toExp(wavelength)
        answer+='$ =' +self.v+' \\AA$'
        self.toExp(planck)
        self.f.write('\\GUESSAFC{Calculate the de broglie wavelength of a $0.14 \\KG$ ball  traveling at $7 \\MPS$.}{'+answer+'}{$\\lambda= \\frac{h}{p}$, $p=mv$ }{$h='+self.v+'\\frac{m^2 \\cdot kg}{s}$}\n')
        self.f.write('\\GUESS{Calculate the de broglie wavelength of a $'+mass+'\\KG$ ball traveling at $'+speed+'\\MPS$.}\n')

        wavelength=planck/(0.14*.5*c)
        self.toExp(wavelength)
        answer='$\\lambda =' +self.v+' \\MET$'
        wavelength=wavelength/1.0e-10
        self.toExp(wavelength)
        answer+='$ =' +self.v+' \\AA$'
        self.toExp(c)
        self.Guessself.f.write('\\GUESSAFC{Calculate the de broglie wavelength of a $0.14 \\KG$ ball  traveling at $0.5c$.}{'+answer+'}{$\\lambda= \\frac{h}{p}$, $p=mv$}{$c='+self.v+'\\frac{m}{s}$}\n')
        self.f.write('\\GUESS{Calculate the de broglie wavelength of a $'+mass+'\\KG$ ball traveling at $'+speedc+'c$.}\n')

        self.f.write('\\newpage\n')

        p=0.14*.999*c/math.sqrt(1-(.999*.999))
        wavelength=planck/p
        self.toExp(wavelength)
        answer='$\\lambda =' +self.v+' \\MET$'
        wavelength=wavelength/1.0e-10
        self.toExp(wavelength)
        answer+='$ =' +self.v+' \\AA$'
        self.toExp(c)
        self.f.write('\\GUESSAF{Calculate the de broglie wavelength of a $0.14 \\KG$ ball  traveling at $0.999c$.}{'+answer+'}{$\\lambda= \\frac{h}{p}$, $p=\\frac{m_0 \\cdot v}{\\sqrt{1-\\frac{v^2}{c^2}}}$ \n}')
        self.f.write('\\GUESS{Calculate the de broglie wavelength of a $'+mass+'\\KG$ ball traveling at $'+speedcf+'c$.}\n')

        p=9e-31*.05*c/math.sqrt(1-(.05*.05))
        wavelength=planck/p
        self.toExp(wavelength)
        answer='$\\lambda =' +self.v+' \\MET$'
        wavelength=wavelength/1.0e-10
        answer+='$ =' +str(round(wavelength,2))+' \\AA$'
        self.toExp(c)
        self.f.write('\\GUESSAF{Calculate the de broglie wavelength of a $9X10^{-31} \\KG$ particle traveling at $0.01c$.}{'+answer+'}{$\\lambda= \\frac{h}{p}$, $p=\\frac{m_0 \\cdot v}{\\sqrt{1-\\frac{v^2}{c^2}}}$ \n}')
        self.f.write('\\GUESS{Calculate the de broglie wavelength of a $'+masse+'X10^{-31}\\KG$ ball traveling at $'+speedc+'c$.}\n')

        self.f.write('\\end{enumerate}\n')

g=Waves("Physics 1","Matter Wave", "small")
for x in range(1, 2):
    g.WritePage(x)
