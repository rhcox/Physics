import GuessBase
import random

class HeatE(GuessBase.Guess):
    def __init__(self,course, title, rowh):
        super(HeatE, self).__init__(course, title, rowh)

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



        
        QHi=random.randint(1000,2000)
        QH=str(QHi)
        W=random.randint(50,200)
        QL=str(QHi-W)
        answer='W=$20\JE$  $\\epsilon=$'+str(20.0/200.0*100.0)+'\%' 
        self.f.write('\\GUESSA{A heat engine has a hot side with $200 \\JE$ of heat and a cold side of $180 \\JE$.  Calculate the maximum work done by and the efficiency of the heat engine.}{'+answer+'}\n')
        self.f.write('\\GUESS{A heat engine has a hot side with $'+QH+'\\JE$ of heat and a cold side of $'+QL+'\\JE$.  Calculate the maximum work done by and the efficiency of the heat engine.}\n')

        CP=str((float(random.randint(50,500))/100.0))
        QH=str(random.randint(800,2000))
        TK=round(5000.0/(4.18*8*1000),2)
        mass=str((float(random.randint(25,70))/10.0))
        answer='$\\Delta T='+str(TK)+'\\Kelvin$'
        self.f.write('\\GUESSA{The specific heat of a substance is $4.18\\Jpg$. If $5000\\JE$ is added to $8\\KG$ of the substance, calculate the change in temperature.}{'+answer+'}\n')
        self.f.write('\\GUESS{The specific heat of a substance is $'+CP+'\\Jpg$. If $'+QH+'\\JE$ is added to $'+mass+'\\KG$ of the substance, calculate the change in temperature.}\n')

        
        TK=str((float(random.randint(10,90))/100.0))
        mc=round(5000.0/(4.18*.6)/1000,2)
        answer='$m='+str(mc)+'\\KG$'
        self.f.write('\\GUESSA{The specific heat of a substance is $4.18\\Jpg$. $5000\\JE$ raises the temperature  $0.6\\Kelvin$, calculate the mass.}{'+answer+'}\n')
        self.f.write('\\GUESS{The specific heat of a substance is $'+CP+'\\Jpg$. $'+QH+'\\JE$ raises the temperature $'+TK+'\\Kelvin$, calculate the mass.}\n')

        CP1=str((float(random.randint(300,600))/100.0))
        CP2=str((float(random.randint(20,150))/100.0))
        TK1=str(random.randint(280,350))
        TK2=str(random.randint(400,500))
        mass1=str((float(random.randint(100,200))/10.0))
        mass2=str((float(random.randint(20,50))/10.0))
        TK=round((2*1000*4.18*300+9*1000*.14*400)/(2*1000*4.18+9*1000*.14),1)
        answer='$ T='+str(TK)+'\\Kelvin$'
        self.f.write('\\GUESSA{Container 1 has $2\\KG$ of a liquid with specific heat $4.18\\Jpg$ at  $300\\Kelvin$.  Container 2 has $9\\KG$ of a liquid with  specific heat $0.14\\Jpg$ at  $400\\Kelvin$. The two cotainers are placed in thermal contact for a long time until thermal equlibrium is reached. Calculate the final tempeature.}{'+answer+'}\n')
        self.f.write('\\GUESSA{Container 1 has $'+mass1+'\\KG$ of a liquid with specific heat $'+CP1+'\\Jpg$ at  $'+TK1+'\\Kelvin$.  Container 2 has $'+mass2+'\\KG$ of a liquid with  specific heat $'+CP2+'\\Jpg$ at  $'+TK2+'\\Kelvin$. The two cotainers are placed in thermal contact for a long time until thermal equlibrium is reached. Calculate the final tempeature.}{'+answer+'}\n')

        self.f.write('\\end{enumerate}\n')

g=HeatE("Physics 1","Thermodynamics", "small")
for x in range(1, 100):
    g.WritePage(x)
