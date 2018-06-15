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

        
        wavespeed=150000*0.002
        answer='$\\nu ='+str(wavespeed)+' \\MPS$'
        self.f.write('\\GUESSAF{A wave has a frequency of 150 KHz amd a wavelength of 0.002 m.  Calculate the wave speed.}{'+answer+'}{$v=\\nu \cdot \\lambda\n$}')
        self.f.write('\\GUESS{If a light wave has a frequency of '+str(frequency)+' MHz amd all light travels at $3X10^8\\MPS$, Calculate the wavelength.}\n')

        per=round(2.0*3.14*math.sqrt(3.0/10.0),2)
        answer='$period ='+str(per)+' sec$'
        self.f.write('\\GUESSAF{A pedulum has a length of 3 m.  Calculate the period on Earth.}{'+answer+'}{$T=2 \\cdot \\pi \\sqrt{\\frac{\\ell}{g}}$}\n')
        self.f.write('\\GUESS{A pedulum has a length of '+str(length)+' m.  Calculate the period on Earth.}\n')

        self.f.write('\\newpage\n')

        leng=round(math.pow(6.1/(2.0*3.14),2)*10.0,2)
        answer='$length ='+str(leng)+' \\MET$'
        self.f.write('\\GUESSAF{A pedulum has a period of 6.1 seconds. Calculate the length of the pendulum on Earth.}{'+answer+'}{$T=2 \\cdot \\pi \\sqrt{\\frac{\\ell}{g}}$}\n')
        self.f.write('\\GUESS{A pedulum has a period of '+str(period)+' seconds. Calculate the length of the pendulum on Earth.}\n')

        grav=round(3.4/math.pow(6.1/(2.0*3.14),2),2)
        answer='$g_0 ='+str(grav)+' \\MPSS$'
        self.f.write('\\GUESSAF{A pedulum has a period of 6.1 seconds and a legnth of 3.4 meters. Calculate the local gravity.}{'+answer+'}{$T=2 \\cdot \\pi \\sqrt{\\frac{\\ell}{g}}$}\n')
        self.f.write('\\GUESS{A pedulum has a period of '+str(period)+' seconds and a legnth of '+str(length)+' meters. Calculate the local gravity.}\n')

        self.f.write('\\end{enumerate}\n')

g=Waves("Physics 1","Oscillatory Motion", "small")
for x in range(1, 80):
    g.WritePage(x)
