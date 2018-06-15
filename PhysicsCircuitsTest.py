import random
import subprocess
import os
import numpy

def HEAD(f,nn):
    f.write('\\documentclass[12pt]{article}\n')
    f.write('\\pdfpagewidth 8.5in\n')
    f.write('\\pdfpageheight 11in\n')
    f.write('\\setlength\\topmargin{0in}\n')
    f.write('\\setlength\\headheight{20pt}\n')
    f.write('\\setlength\\headsep{.2in}\n')

    f.write('\\setlength\\textheight{9in}\n')
    f.write('\\setlength\\textwidth{6.5in}\n')
    f.write('\\setlength\\oddsidemargin{0in}\n')
    f.write('\\setlength\\evensidemargin{0in}\n')
    f.write('\\setlength\\parindent{0in}\n')
    f.write('\\setlength\\parskip{.2in}\n')

    f.write('\\usepackage{tikz}\n')
    f.write('\\usepackage{circuitikz}\n')

    
    f.write('\\usepackage{amsmath}\n')
    f.write('\\usepackage{amsthm}\n')
    f.write('\\usepackage{epsfig}\n')
    f.write('\\usepackage{graphicx}\n')

    f.write('\\usepackage{color}\n')
    f.write('\\usepackage{graphpap}\n')
    f.write('\\usepackage{array}\n')
    f.write('\\usepackage{epic}\n')
    f.write('\\usepackage{fancyhdr}\n')
    f.write('\\usepackage{enumerate}\n')

    f.write('\\input xy\n')
    f.write('\\xyoption{all}\n')
    f.write('\\large\n')
    f.write('\\pagestyle{fancyplain}\n')

    f.write('\\lhead{Name:}\n')
    f.write('\\chead{Period:}\n')
    f.write('\\rhead{AP Physics-'+nn+'}\n')
    f.write('\\lfoot{ Furr HS }\n')
    f.write('\\rfoot{Show All Work}\n')

    f.write('\\renewcommand\headrule{\\vspace{-8pt}\dotfill}\n')

    f.write('\\newcommand{\\gridpaper}{\n')
    f.write('\\begin{picture}(300,300)\n')
    f.write('\\put(30,5){\\grid(300,300)(10,10)}\n')
    f.write('\\end{picture}\n')
    f.write('}\n')
    f.write('\\begin{document}\n')
    f.write('\\title{Circuit Test}\n')
    f.write('\\author{RH Cox}\n')
    f.write('\\date{DATE: }\n')
    f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

    
def PAGE(f,a):
    random.seed(a)
    
    volt=random.randint(10,50)
    volts=str(volt)
    volts=str(volt)
    
    R1=random.randint(10,49)
    R1S=str(R1)

    R2=random.randint(50,150)
    R2S=str(R2)
    
    R3=random.randint(200,299)
    R3S=str(R3)
    
    R4=random.randint(800,999)
    R4S=str(R4)
    
    R5=random.randint(5,20)
    R5S=str(R4)+'M'

    CN=random.choice([1,2,3,4,5])

    
    w=random.choice(['floor','table','sidewalk','lawn'])
    mass=str(random.randint(10,90))


    if CN==1:
        f.write(' \n\n \\begin{circuitikz}\draw\n')
        f.write('(0,0)to[battery=$'+volts+'v$] (0,6)\n')
        f.write('(0,6) to [R=$'+R1S+'\ \Omega$,-*] (4,6)\n')
        f.write('(4,0) to [R=$'+R2S+'\ \Omega$,-*] (4,6)\n')
        f.write('(8,0) to [R=$'+R3S+'\ \Omega$,-*] (8,6)\n')
        f.write('(4,6) to [R=$'+R4S+'\ \Omega$,-*] (8,6)\n')
        f.write('(0,0)to[short] (8,0)\n')
        f.write('(0,6) to[R, i>^=$i_1$] (4,6)\n')
        f.write('(4,6) to[R, i>^=$i_2$] (8,6)\n')
        f.write(';\n\n \end{circuitikz} \n \n')

    elif CN==2:
        f.write(' \n\n \\begin{circuitikz}\draw\n')
        f.write('(0,0)to[battery=$'+volts+'v$] (0,6)\n')
        f.write('(0,6) to [R=$'+R1S+'\ \Omega$,-*] (4,6)\n')
        f.write('(4,0) to [R=$'+R2S+'\ \Omega$,-*] (4,6)\n')
        f.write('(8,0) to [R=$'+R3S+'\ \Omega$,-*] (8,6)\n')
        f.write('(0,0) to [R=$'+R4S+'\ \Omega$,-*] (4,0)\n')
        f.write('(4,6)to[short] (8,6)\n')
        f.write('(4,0)to[short] (8,0)\n')
        f.write('(0,6) to[R, i>^=$i_1$] (4,6)\n')
        f.write('(4,6) to[short, i>^=$i_2$] (8,6)\n')
        f.write(';\n\n \end{circuitikz} \n \n')

    elif CN==3:
        f.write(' \n\n \\begin{circuitikz}\draw\n')
        f.write('(0,0)to[battery=$'+volts+'v$] (0,6)\n')
        f.write('(4,0) to [R=$'+R1S+'\ \Omega$,-*] (4,3)\n')
        f.write('(4,3) to [R=$'+R2S+'\ \Omega$,-*] (4,6)\n')
        f.write('(8,0) to [R=$'+R3S+'\ \Omega$,-*] (8,6)\n')
        f.write('(4,6) to [R=$'+R4S+'\ \Omega$,-*] (8,6)\n')
        f.write('(0,0)to[short] (8,0)\n')
        f.write('(0,6) to[short, i>^=$i_1$] (4,6)\n')
        f.write('(4,6) to[R, i>^=$i_2$] (8,6)\n')
        f.write(';\n\n \end{circuitikz} \n \n')

    elif CN==4:
        f.write(' \n\n \\begin{circuitikz}\draw\n')
        f.write('(0,0)to[battery=$'+volts+'v$] (0,6)\n')
        f.write('(4,0) to [R=$'+R1S+'\ \Omega$,-*] (4,3)\n')
        f.write('(4,3) to [R=$'+R2S+'\ \Omega$,-*] (4,6)\n')
        f.write('(8,0) to [R=$'+R3S+'\ \Omega$,-*] (8,6)\n')
        f.write('(0,6) to [R=$'+R4S+'\ \Omega$,-*] (4,6)\n')
        f.write('(0,0)to[short] (8,0)\n')
        f.write('(0,6) to[R, i>^=$i_1$] (4,6)\n')
        f.write('(4,6) to[short, i>^=$i_2$] (8,6)\n')
        f.write(';\n\n \end{circuitikz} \n \n')

    elif CN==5:
        f.write(' \n\n \\begin{circuitikz}\draw\n')
        f.write('(0,0)to[battery=$'+volts+'v$] (0,6)\n')
        f.write('(0,6) to [R=$'+R1S+'\ \Omega$,-*] (4,6)\n')
        f.write('(4,0) to [R=$'+R2S+'\ \Omega$,-*] (4,6)\n')
        f.write('(8,0) to [R=$'+R3S+'\ \Omega$,-*] (8,6)\n')
        f.write('(0,0) to [R=$'+R4S+'\ \Omega$,-*] (4,0)\n')
        f.write('(4,0)to[short] (8,0)\n')
        f.write('(0,6) to[R, i>^=$i_1$] (4,6)\n')
        f.write('(4,6) to[short, i>^=$i_2$] (8,6)\n')
        f.write(';\n\n \end{circuitikz} \n \n')
    

    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{4cm}\n')

    f.write('\\item Draw the schematics of the intermediate cicuits that wuld be generated as you reduce this circuit by combing pairs of parallel or series resistors.  Do not perform calculations or label the value of the resistors\n')
    f.write('\\newpage \n')

    f.write('\\item In a paragraph, describe how to would combine pairs of parallel or series resistors to generate an equivelent circuit. Do not perform calculations, but estiamte the value of the combined resistors and the value of the equivelent resistor.\n')

    f.write('\\item Draw two curent loops in the circuit.  Write an equation for each loop.  Simplify the equtions.  Write the eqautions as a matrx.  Do not solve.\n')
    A =numpy.matrix('0 0; 0 0')
    B =numpy.matrix('0 ; 0')
    B[0]=volt
    B[1]=0

    if CN==1:
        A[0,0]=R1+R2
        A[0,1]=-1*R2
        A[1,0]=-1*R2
        A[1,1]=R2+R3+R4

    elif CN==2:
        A[0,0]=R1+R2+R4
        A[0,1]=-1*R2
        A[1,0]=-1*R2
        A[1,1]=R2+R3
        
    elif CN==3:
        A[0,0]=R1+R2
        A[0,1]=-1*(R1+R2)
        A[1,0]=-1*(R1+R2)
        A[1,1]=R1+R2+R3+R4

    elif CN==4:
        A[0,0]=R1+R2+R4
        A[0,1]=-1*(R1+R2)
        A[1,0]=-1*(R1+R2)
        A[1,1]=R1+R2+R3
        
    elif CN==5:
        A[0,0]=R1+R2+R4
        A[0,1]=-1*(R2)
        A[1,0]=-1*(R2)
        A[1,1]=R2+R3

    V=numpy.linalg.solve(A, B)
    i1=V[0,0]
    i1s=str(round(V[0][0],3))    
    i2=V[1,0]
    i2s=str(round(V[1][0],3))

    f.write('\\item Suppose $i_1$='+i1s+'A, and $i_2$='+i2s+'A.  Label the currents in the original circuit.  Calculate the potential across each resistor. Show all work. \n')

    f.write('\\item Show potentials are consered around the current loops and the currents are conservered at a node. Show work and justification. \n')

    f.write('\\newpage \n')

    f.write('\\item Using the values above, calculate the power for each resistor. \n\n\n')

    f.write('\\item If each resistor represented a light bulb, state which would tend to have the greatest brightness, and which would tend to have the lowest brightness.  Justify your answer. \n\n\n')

    f.write('\\item If a $'+R5S+'\Omega$ resister were added in parallel to this circuit, would the current $i_1$ change significant;y. Justify your answer. \n\n\n')

    f.write('\\item If a $'+R5S+'\Omega$ resister were added in parallel to this circuit, would the current $i_2$ change significant;y. Justify your answer. \n\n\n')

    if CN==1:
        R10=R1
        R10S=R1S
        R10I=i1
        R20=R4
        R20S=R4S
        R20I=i2
        R30=R2
        R30S=R2S
        R30I=i1-i2
    elif CN==2:
        R10=R1
        R10S=R1S
        R10I=i1
        R20=R3
        R20S=R3S
        R20I=i2
        R30=R2
        R30S=R2S
        R30I=i1-i2
    elif CN==3:
        R10=R4
        R10S=R4S
        R10I=i2
        R20=R3
        R20S=R3S
        R20I=i2
        R30=R1
        R30S=R1S
        R30I=i1-i2
    elif CN==4:
        R10=R4
        R10S=R4S
        R10I=i1
        R20=R3
        R20S=R3S
        R20I=i2
        R30=R1
        R30S=R1S
        R30I=i1-i2
    elif CN==5:
        R10=R1
        R10S=R1S
        R10I=i1
        R20=R3
        R20S=R3S
        R20I=i2
        R30=R2
        R30S=R2S
        R30I=i1-i2

    P1=R10*R10I*R10I
    error=float(random.randint(900,1100))/1000
    P1a=str(int(P1*error*1000))
    error=float(random.randint(1000,1100))/1000
    P1b=str(int(2*P1*error*1000))
    error=float(random.randint(900,1000))/1000
    P1c=str(int(3*P1*error*1000))
    error=float(random.randint(800,1000))/1000
    P1d=str(int(4*P1*error*1000))
    error=float(random.randint(1000,1000))/1000
    P1e=str(int(5*P1*error*1000))
    P2=R20*R20I*R20I
    error=float(random.randint(900,1000))/1000
    P2a=str(int(P2*error*1000))
    error=float(random.randint(1000,1100))/1000
    P2b=str(int(2*P2*error*1000))
    error=float(random.randint(1000,1200))/1000
    P2c=str(int(3*P2*error*1000))
    error=float(random.randint(800,1000))/1000
    P2d=str(int(4*P2*error*1000))
    error=float(random.randint(900,1100))/1000
    P2e=str(int(5*P2*error*1000))
    P3=R20*R20I*R20I
    error=float(random.randint(900,1100))/1000
    P3a=str(int(P3*error*1000))
    error=float(random.randint(800,1000))/1000
    P3b=str(int(2*P3*error*1000))
    error=float(random.randint(1000,1100))/1000
    P3c=str(int(3*P3*error*1000))
    error=float(random.randint(900,1100))/1000
    P3d=str(int(4*P3*error*1000))
    error=float(random.randint(1000,1200))/1000
    P3e=str(int(5*P3*error*1000))


    f.write('\\newpage \n')
    f.write('\\begin{tabular} {|p{3cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|} \n')
    f.write('\\hline \n')
    f.write('Resistor[$\Omega$] & 1s & 2s & 3s & 4s & 5s\\\ \n')
    f.write('\\hline \n')
    f.write(R10S+' &'+P1a+'mJ &'+P1b+'mJ &'+P1c+'mJ &'+P1d+'mJ &'+P1e+'mJ \\\ \n')
    f.write('\\hline \n\n')
    f.write(R20S+' &'+P2a+'mJ &'+P2b+'mJ &'+P2c+'mJ &'+P2d+'mJ &'+P2e+'mJ \\\ \n')
    f.write('\\hline \n\n')
    f.write(R30S+' &'+P3a+'mJ &'+P3b+'mJ &'+P3c+'mJ &'+P3d+'mJ &'+P3e+'mJ \\\ \n')
    f.write('\\hline \n\n')
    f.write('\\end{tabular} \n\n\n')
    
    f.write('\\item On the Grid Provided \n')
    f.write('\\begin{enumerate}\n')
    f.write('\\item Scale the grid to plot the data in the table below.\n')
    f.write('\\item Plot the energy consumption data for each resistor listed in the table as a scatter plot.\n')
    f.write('\\item Construct a best line fit for the data for each resistor\n')
    f.write('\\item Calculate the power consumption for each resistor using the best line fit.\n')
    f.write('\\end{enumerate}\n')
    f.write('\\gridpaper \n\n')


    f.write('\\end{enumerate}\n')

    

def WritePage(home,n):
	output=home+"/temp"
	nn=str(n)
	name=output+"/temp"+nn
	filename=name+".tex"
	logname=output+"/log.out"
	f=open(filename,'w')
	HEAD(f,nn)
	PAGE(f,n)
	ENDMAT(f)
	f.close()
	pdfcommand="/usr/texbin/pdflatex --file-line-error --synctex=1 -output-directory "+output+" "+filename+" >"+logname
	os.system(pdfcommand)
	rmnamen='rm '+name+'.aux'
	os.system(rmnamen)
	rmnamen='rm '+name+'.log'
	os.system(rmnamen)
	rmnamen='rm '+name+'.synctex.gz'
	os.system(rmnamen)
	rmnamen='rm '+name+'.tex'
	os.system(rmnamen)

    
from os.path import expanduser
home = expanduser("~")
for x in range(1, 150):
	WritePage(home,x)
