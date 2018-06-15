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

        m1=str((float(random.randint(10,90))/10.))
        m1e=str(random.randint(15,30))
        m2=str((float(random.randint(20,99))/10.))
        m2e=str(random.randint(3,13))
        r=str((float(random.randint(20,80))/10.))
        re=str(random.randint(2,9))

        forceg=6.7e-11*1e12*1e6/(2e4*2e4)
        answer='$F_g ='+str(forceg)+' \\NF$'
        self.f.write('\\GUESSAF{Two masses, one of $1X10^{12} \\KG$ the other of  of $1X10^{6} \\KG$ are $2X10^4 \\MET$ apart.  Calculate the gravitational force between them.}{'+answer+'}{$F_g=G \\frac{m_1 \\cdot m_2}{r^2}$}\n')
        self.f.write('\\GUESS{Two masses, one of $'+m1+'X10^{'+m1e+'} \\KG$ the other of  of $'+m2+'X10^{'+m2e+'} \\KG$ are $'+r+'X10^{'+re+'} \\MET$ apart.  Calculate the gravitational force between them.}\n')

        q1=str((float(random.randint(10,90))/10.))
        q1e=str(random.randint(10,18))
        d=str((float(random.randint(20,80))/10.))
        de=str(random.randint(5,10))
        
        forcee=9e9*1e-12*1e-12/(2e-4*2e-4)
        answer='$F_e ='+str(forcee)+' \\NF$'
        self.f.write('\\GUESSAF{Two charges, both of $1X10^{-12} \\COUL$ are $2X10^{-4} \MET$ apart.  Calculate the electric force between them.}{'+answer+'}{$F_e=k \\frac{q_1 \\cdot q_2}{r^2}$}\n')
        self.f.write('\\GUESS{Two charges, both of $'+q1+'X10^{-'+q1e+'} \\COUL$ are $'+d+'X10^{-'+de+'} \MET$ apart.  Calculate the electric force between them.}\n')

        q1=str((float(random.randint(20,80))/10.))
        q1e=str(random.randint(11,18))
        d=str((float(random.randint(20,90))/10.))
        de=str(random.randint(4,10))
        
        forcee=9e9*1e-12*-1e-12/(2e-4*2e-4)
        answer='$F_e ='+str(forcee)+' \\NF$'
        self.f.write('\\GUESSAF{Two opposite charges, one of $1X10^{-12} \\COUL$ the other of $-1X10^{-12} \\COUL$, are $2X10^{-4} \MET$ apart.  Calculate the electric force between them.}{'+answer+'}{$F_e=k \\frac{q_1 \\cdot q_2}{r^2}$}\n')
        self.f.write('\\GUESS{Two opposite charges, one of $'+q1+'X10^{-'+q1e+'} \\COUL$ the other of $-'+q1+'X10^{-'+q1e+'} \\COUL$, are $'+d+'X10^{-'+de+'} \MET$ apart.  Calculate the electric force between them.}\n')
    
        q1=str((float(random.randint(30,99))/10.))
        q1e=str(random.randint(4,15))
        d=str((float(random.randint(10,90))/10.))
        de=str(random.randint(3,11))
        
        fielde=9e9*1e-12/(2e-4*2e-4)
f        answer='$F_e ='+str(fielde)+' \\NCOUL$'
        self.f.write('\\GUESSAF{Calculate the field of single charge of $1X10^{-12} \\COUL$ at a point $2X10^{-4} \MET$ away.}{'+answer+'}{$F_e=k \\frac{q}{r^2}$}\n')
        self.f.write('\\GUESS{Calculate the field of single charge of $'+q1+'X10^{-'+q1e+'} \\COUL$ at a point $'+d+'X10^{-'+de+'} \MET$ away.}\n')

        self.f.write('\\end{enumerate}\n')

g=Waves("Physics 1","Electrical Force", "small")
for x in range(1, 80):
    g.WritePage(x)
