
import GuessBase
import random
import math

class Waves(GuessBase.Guess):
    
    def __init__(self,course, title, rowh):
        super(Waves, self).__init__(course, title, rowh)

    def PAGE(self):
        self.f.write('\\normalsize\n')
        random.seed(self.rnum)

        v=str(5)
        r=str(20)
        self.f.write('1. Solve for current\n\n\n')
        self.f.write('\\begin{circuitikz}\draw\n')
        self.f.write('(0,0)to[battery=$'+v+'kV$] (0,3)\n')
        self.f.write('(6,3) to [R=$'+r+'G\\Omega$,-*] (6,0)\n')
        self.f.write('(0,0)to[short] (6,0)\n')
        self.f.write('(0,3)to[short] (6,3)\n')
        self.f.write(';\n')
        self.f.write('\\end{circuitikz}\n')
        self.f.write('\\vspace{2cm}\n\n')

        k=random.choice(['k','M','G'])
        v=str(random.randint(3,10))
        r=str(random.randint(21,99))
        self.f.write('2. Solve for current\n\n\n')
        self.f.write('\\begin{circuitikz}\draw\n')
        self.f.write('(0,0)to[battery=$'+v+'v$] (0,3)\n')
        self.f.write('(6,3) to [R=$'+r+k+'\\Omega$,-*] (6,0)\n')
        self.f.write('(0,0)to[short] (6,0)\n')
        self.f.write('(0,3)to[short] (6,3)\n')
        self.f.write(';\n')
        self.f.write('\\end{circuitikz}\n')
        self.f.write('\\vspace{2cm}\n\n')

        v=str(15)
        r1=str(18)
        r2=str(7)
        self.f.write('3. Solve for current\n\n\n')
        self.f.write('\\begin{circuitikz}\draw\n')
        self.f.write('(0,0)to[battery=$'+v+'v$] (0,3)\n')
        self.f.write('(2,0) to [R=$'+r1+'\\Omega$,-*] (5,0)\n')
        self.f.write('(6,3) to [R=$'+r2+'\\Omega$,-*] (6,0)\n')
        self.f.write('(0,0)to[short] (2,0)\n')
        self.f.write('(5,0)to[short] (6,0)\n')
        self.f.write('(0,3)to[short] (6,3)\n')
        self.f.write(';\n')
        self.f.write('\\end{circuitikz}\n')
        self.f.write('\\vspace{2cm}\n\n')

        k=random.choice(['k','M','G'])
        v=str(random.randint(3,10))
        r1=str(random.randint(21,99))
        r2=str(random.randint(100,200))
        self.f.write('4. Solve for current\n\n\n')
        self.f.write('\\begin{circuitikz}\draw\n')
        self.f.write('(0,0)to[battery=$'+v+'v$] (0,3)\n')
        self.f.write('(2,0) to [R=$'+r1+k+'\\Omega$,-*] (5,0)\n')
        self.f.write('(6,3) to [R=$'+r2+k+'\\Omega$,-*] (6,0)\n')
        self.f.write('(0,0)to[short] (2,0)\n')
        self.f.write('(5,0)to[short] (6,0)\n')
        self.f.write('(0,3)to[short] (6,3)\n')
        self.f.write(';\n')
        self.f.write('\\end{circuitikz}\n')
        self.f.write('\\vspace{2cm}\n\n')
        self.f.write('\n\\newpage')

    
        v=str(5)
        r1=str(50)
        r2=str(70)
        self.f.write('5. Solve for equivalent circuit and current\n\n\n')
        self.f.write('\\begin{circuitikz}\draw\n')
        self.f.write('(0,0)to[battery=$'+v+'v$] (0,3)\n')
        self.f.write('(6,3) to [R=$'+r1+'M\\Omega$,-*] (6,0)\n')
        self.f.write('(3,3) to [R=$'+r2+'k\\Omega$,-*] (3,0)\n')
        self.f.write('(0,0)to[short] (6,0)\n')
        self.f.write('(0,3)to[short] (6,3)\n')
        self.f.write(';\n')
        self.f.write('\\end{circuitikz}\n')
        self.f.write('\\vspace{1cm}\n\n')
    

        v=str(random.randint(3,10))
        r=str(random.randint(100,900))
        self.f.write('6. Solve for equivalent circuit and current\n\n\n')
        self.f.write('\\begin{circuitikz}\draw\n')
        self.f.write('(0,0)to[battery=$'+v+'v$] (0,3)\n')
        self.f.write('(6,3) to [R=$'+r+'\\Omega$,-*] (6,0)\n')
        self.f.write('(3,3) to [R=$'+r+'\\Omega$,-*] (3,0)\n')
        self.f.write('(0,0)to[short] (6,0)\n')
        self.f.write('(0,3)to[short] (6,3)\n')
        self.f.write(';\n')
        self.f.write('\\end{circuitikz}\n')
        self.f.write('\\vspace{1cm}\n\n')



        v=str(random.randint(3,10))
        r1=str(random.randint(20,150))
        r2=str(random.randint(200,350))
        r3=str(random.randint(400,450))
        self.f.write('7. Solve for current\n\n\n')
        self.f.write('\\begin{circuitikz}\draw\n')
        self.f.write('(0,0)to[battery=$'+v+'v$] (0,3)\n')
        self.f.write('(6,3) to [R=$'+r1+'M\\Omega$,-*] (6,0)\n')
        self.f.write('(4,3) to [R=$'+r2+'k\\Omega$,-*] (4,0)\n')
        self.f.write('(2,3) to [R=$'+r3+'k\\Omega$,-*] (4,3)\n')
        self.f.write('(0,0)to[short] (6,0)\n')
        self.f.write('(0,3)to[short] (2,3)\n')
        self.f.write('(4,3)to[short] (6,3)\n')
        self.f.write(';\n')
        self.f.write('\\end{circuitikz}\n')
        self.f.write('\\vspace{2cm}\n\n')

        
        v=str(random.randint(10,20))
        r1=str(random.randint(30,250))
        r2=str(random.randint(300,550))
        r3=str(random.randint(600,850))
        r4=str(random.randint(900,999))
        self.f.write('8. Solve for current\n\n\n')
        self.f.write('\\begin{circuitikz}\draw\n')
        self.f.write('(0,0)to[battery=$'+v+'v$] (0,4)\n')
        self.f.write('(6,2) to [R=$'+r1+'\\Omega$,-*] (6,0)\n')
        self.f.write('(6,2) to [R=$'+r4+'\\Omega$,-*] (6,4)\n')
        self.f.write('(4,4) to [R=$'+r2+'\\Omega$,-*] (4,0)\n')
        self.f.write('(2,4) to [R=$'+r3+'\\Omega$,-*] (4,4)\n')
        self.f.write('(0,0)to[short] (6,0)\n')
        self.f.write('(0,4)to[short] (2,4)\n')
        self.f.write('(4,4)to[short] (6,4)\n')
        self.f.write(';\n')
        self.f.write('\\end{circuitikz}\n')

        
g=Waves("Physics 1","Series and Parallel Circuits", "small")
for x in range(1, 80):
    g.WritePage(x)