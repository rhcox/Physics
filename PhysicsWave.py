import GuessBase
import random

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
        len=str(round(heightf/0.8,1))
        U=round(0.5*2*15*15,1)
        maxh=round(U/(2*10),1)


        period=(float(random.randint(20,50))/10.)
        wavelength=(float(random.randint(2,20))/10.)
        frequency=random.randint(30,70)
        mant=str(random.randint(1,9))
        exp=str(random.randint(2,24))

        
        freq=round(1/1.5,2)
        answer='$\\nu ='+str(freq)+' \\HZ$'
        self.f.write('\\GUESSAF{A wave has a period of 1.5 s.  Calculate the frequency.}{'+answer+'}{$\\nu=\\frac{1}{T}$}\n')
        self.f.write('\\GUESS{A wave has a period of '+str(period)+' s.  Calculate the frequency.}\n')

        vw=round(.1/1.5,2)
        answer='$v_w ='+str(vw)+' \\MPS$'
        self.f.write('\\GUESSAF{A wave has a period of 1.5 s and a wavelength of 0.1 m.  Calculate the wavespeed.}{'+answer+'}{$v_w=\\frac{\\lambda}{T}$}\n')
        self.f.write('\\GUESS{A wave has a period of '+str(period)+' s and a wavelength of '+str(wavelength)+' m.  Calculate the wavespeed.}\n')

        self.f.write('\\newpage\n')

        vw=20*.1
        answer='$v_w ='+str(vw)+' \\MPS$'
        self.f.write('\\GUESSAF{A wave has a frequency of $20 \\HZ$ and a wavelength of 0.1 m.  Calculate the wavespeed.}{'+answer+'}{$v_w=\\nu \\cdot \\lambda$}\n')
        self.f.write('\\GUESS{A wave has a frequency of $'+str(frequency)+'\\HZ$ and a wavelength of '+str(wavelength)+' m.  Calculate the wavespeed.}\n')

        wave=3e8/1e25
        answer='$\\lambda ='+str(wave)+' \\MET$'
        self.f.write('\\GUESSAF{All light has a speed of $3X10^{8}\\MPS$. $\\gamma$-rRays have a frequency around $1X10^{25}\\HZ$.  Calculate the wavelength.}{'+answer+'}{$v_w=\\nu \\cdot \\lambda$}\n')
        self.f.write('\\GUESS{All light has a speed of $3X10^{8}\\MPS$. A certain electromagnetic wave has a frequency around $'+mant+'X10^{'+exp+'}\\HZ$.  Calculate the wavelength.}\n')

        self.f.write('\\end{enumerate}\n')

g=Waves("Physics 1","Waves", "small")
for x in range(1, 80):
    g.WritePage(x)
