
import GuessBase
import random
import math

class Waves(GuessBase.Guess):
    
    def __init__(self,course, title, rowh):
        super(Waves, self).__init__(course, title, rowh)

    def PAGE(self):
        self.f.write('\\large\n')
        self.f.write('Solve each circuit.  Insure that the current through the battery is shown or calcualted. Show or calculate the potential across and the current through each resistor.  If neccesary, calculate and draw the equivlent circuit with the equivelent resistance calculated, and current shown.\n\n')
        self.f.write('\\vspace{1cm}\n\n')
        self.f.write('\\normalsize\n')
        random.seed(self.rnum)

        
        k=random.choice(['m','\\mu','n'])
        v=str(random.randint(11,20))
        i=str(random.randint(100,200))
        self.f.write('1. Solve the circuit\n\n\n')
        self.f.write('\\begin{circuitikz}\draw\n')
        self.f.write('(0,0)to[battery=$'+v+'v$] (0,3)\n')
        self.f.write('(6,3) to [R=,-*] (6,0)\n')
        self.f.write('(0,0)to[short] (6,0)\n')
        self.f.write('(0,3)to[short,i=$'+i+' '+k+' A$] (6,3)\n')
        self.f.write(';\n')
        self.f.write('\\end{circuitikz}\n')
        self.f.write('\\vspace{2cm}\n\n')

        k=random.choice(['k','M','G'])
        v=str(random.randint(3,10))
        r=str(random.randint(21,99))
        self.f.write('2. Solve the circuit\n\n\n')
        self.f.write('\\begin{circuitikz}\draw\n')
        self.f.write('(0,0)to[battery=$'+v+'v$] (0,3)\n')
        self.f.write('(6,3) to [R=$'+r+k+'\\Omega$,-*] (6,0)\n')
        self.f.write('(0,0)to[short] (6,0)\n')
        self.f.write('(0,3)to[short] (6,3)\n')
        self.f.write(';\n')
        self.f.write('\\end{circuitikz}\n')
        self.f.write('\\vspace{2cm}\n\n')

        k1=random.choice(['k','M','G'])
        k2=random.choice(['m','\\mu','n'])
        r=str(random.randint(100,200))
        i=str(random.randint(12,50))
        self.f.write('3. Solve the circuit\n\n\n')
        self.f.write('\\begin{circuitikz}\draw\n')
        self.f.write('(0,0)to[battery=] (0,3)\n')
        self.f.write('(6,3) to [R=$'+r+k1+'\\Omega$,-*] (6,0)\n')
        self.f.write('(0,0)to[short] (6,0)\n')
        self.f.write('(0,3)to[short,i=$'+i+' '+k2+' A$] (6,3)\n')
        self.f.write(';\n')
        self.f.write('\\end{circuitikz}\n')
        self.f.write('\\vspace{2cm}\n\n')

        self.f.write('\\newpage\n\n')

        k=random.choice(['k','M','G'])
        v=str(random.randint(3,10))
        r1=str(random.randint(100,199))
        r2=str(random.randint(200,300))
        self.f.write('4. Solve teh circuit\n\n\n')
        self.f.write('\\begin{circuitikz}\draw\n')
        self.f.write('(0,0)to[battery=$'+v+'v$] (0,3)\n')
        self.f.write('(2,0) to [R=$'+r1+k+'\\Omega$,-*] (5,0)\n')
        self.f.write('(6,3) to [R=$'+r2+k+'\\Omega$,-*] (6,0)\n')
        self.f.write('(0,0)to[short] (2,0)\n')
        self.f.write('(5,0)to[short] (6,0)\n')
        self.f.write('(0,3)to[short] (6,3)\n')
        self.f.write(';\n')
        self.f.write('\\end{circuitikz}\n')
        self.f.write('\\vspace{1cm}\n\n')


        v=str(random.randint(3,10))
        r=str(random.randint(100,900))
        self.f.write('5.  Draw the equivilent circuit, calculate the equivlent resistance, and solve the circuit\n\n\n')
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
        r1=str(random.randint(100,199))
        r2=str(random.randint(200,300))
        self.f.write('6.  Draw the equivilent circuit, calculate the equivlent resistance, and solve the circuit\n\n\n')
        self.f.write('\\begin{circuitikz}\draw\n')
        self.f.write('(0,0)to[battery=$'+v+'v$] (0,3)\n')
        self.f.write('(6,3) to [R=$'+r1+'k\\Omega$,-*] (6,0)\n')
        self.f.write('(3,3) to [R=$'+r2+'G\\Omega$,-*] (3,0)\n')
        self.f.write('(0,0)to[short] (6,0)\n')
        self.f.write('(0,3)to[short] (6,3)\n')
        self.f.write(';\n')
        self.f.write('\\end{circuitikz}\n')
        self.f.write('\\vspace{1cm}\n\n')

        
        self.f.write('7.Draw the equivilent circuit, calculate the equivlent resistance, and solve the circuit\n\n\n')
        self.f.write('\\begin{circuitikz}\draw\n')
        v=str(random.randint(3,10))
        r1=str(random.randint(20,150))
        r2=str(random.randint(200,350))
        r3=str(random.randint(400,450))
        c=random.choice([1,2,3])
        if c==1:
            self.f.write('(0,0)to[battery=$'+v+'v$] (0,3)\n')
            self.f.write('(6,3) to [R=$'+r1+'M\\Omega$,-*] (6,0)\n')
            self.f.write('(4,3) to [R=$'+r2+'k\\Omega$,-*] (4,0)\n')
            self.f.write('(2,3) to [R=$'+r3+'k\\Omega$,-*] (4,3)\n')
            self.f.write('(0,0)to[short] (6,0)\n')
            self.f.write('(0,3)to[short] (2,3)\n')
            self.f.write('(4,3)to[short] (6,3)\n')
        if c==2:        
            self.f.write('(0,0)to[battery=$'+v+'v$] (0,4)\n')
            self.f.write('(6,2) to [R=$'+r1+'\\Omega$,-*] (6,0)\n')
            self.f.write('(6,2) to [R=$'+r3+'\\Omega$,-*] (6,4)\n')
            self.f.write('(4,4) to [R=$'+r2+'\\Omega$,-*] (4,0)\n')
            self.f.write('(0,0)to[short] (6,0)\n')
            self.f.write('(0,4)to[short] (6,4)\n')
        if c==3:        
            self.f.write('(0,0)to[battery=$'+v+'v$] (0,4)\n')
            self.f.write('(6,4) to [R=$'+r1+'\\Omega$,-*] (6,0)\n')
            self.f.write('(4,2) to [R=$'+r3+'\\Omega$,-*] (4,4)\n')
            self.f.write('(4,2) to [R=$'+r2+'\\Omega$,-*] (4,0)\n')
            self.f.write('(0,0)to[short] (6,0)\n')
            self.f.write('(0,4)to[short] (6,4)\n')

        self.f.write(';\n')
        self.f.write('\\end{circuitikz}\n')

        
g=Waves("Physics","Circuit Quiz-Due at End of Class", "small")
for x in range(1, 40):
    g.WritePage(x)
