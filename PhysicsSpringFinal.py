import random
import subprocess
import os

def HEAD(f):
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
	f.write('\\usepackage{pstricks}\n')
	f.write('\\usepackage{pst-plot}\n')
	f.write('\\usepackage{epstopdf}\n')
	f.write('\\input xy\n')
	f.write('\\xyoption{all}\n')
	f.write('\\large\n')
	f.write('\\pagestyle{fancyplain}\n')
	f.write('\\lhead{Name:}\n')
	f.write('\\chead{Period:}\n')
	f.write('\\rhead{Furr HS}\n')
	f.write('\\lfoot{ Physics}\n')
	f.write('\\rfoot{Show All Work}\n')
	f.write('\\renewcommand\headrule{\\vspace{-8pt}\dotfill}\n')

	f.write('\\newcommand{\\gridpaper}{\n')
	f.write('\\begin{picture}(50,50)\n')
	f.write('\\put(30,5){\\grid(80,100)(10,10)}\n')
	f.write('\\end{picture}\n')
	f.write('}\n')
	f.write('\\begin{document}\n')
	f.write('\\title{Senior Spring Final 2014}\n')
	f.write('\\author{Physics}\n')
	f.write('\\date{DATE: }\n')
	f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

    
def PAGE(f,a):
    random.seed(a)
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{7cm}\n')


    speed1=str(random.randint(5,10))
    time1=str(random.randint(2,8))
    speed2=str(random.randint(11,20))
    time2=str(random.randint(3,9))
    time2a=str(random.randint(8,15))
    time3=str(random.randint(16,25))
    f.write('\\item A wagon is traveling at $'+speed1+'m/s$ from the origin for $'+time1+'s$. It then stops for $'+time2+'s$, after which it accelerates to $'+speed2+'m/s$ over $'+time2a+'s$, a speed that it maintains for the next $'+time3+'s$.\n')
    f.write('\\begin{enumerate}\n')
    f.write('\\item Sketch a position time graph of this motion.\n')
    f.write('\\item Sketch a velocity time graph of this motion.\n')
    f.write('\\end{enumerate}\n')

    f.write('\\newpage\n')

    massn=random.randint(15,40)
    mass=str(massn)
    h1n=random.randint(60,75)
    h1=str(h1n)
    h2n=random.randint(5,15)
    h2=str(h2n)
    PE=massn*9.8*(h1n-h2n)
    PLoss=float(random.randint(3,7))/100
    Lossn=int(PE*PLoss)
    Loss=str(Lossn)
    Loss2n=Lossn*2.3
    Loss2=str(Loss2n)
    f.write('\\item On a roller coaster, a $'+mass+'kg$ car it hoisted $'+h1+'m$ above the ground to the top of a track where it is briefly at rest. The car is then allowed to roll down the track until it reaches the bottom of the track $'+h2+'m$ above the ground. On the way down the track, $'+Loss+'J$ of energy to lost to heat.\n')
    f.write('\\begin{enumerate}\n')
    f.write('\\item Calculate the potential energy of the car at the top of the track?\n')
    f.write('\\item Calculate the potential energy of the car at the bottom of the track?\n')
    f.write('\\item Calculate the Kinetic energy of the car at the bottom  of the track?\n')
    f.write('\\item If $'+Loss2+'J$ of energy is lost as the car goes up the next hill on the track, what is the highest point the car could reach?\n')
    f.write('\\item If no energy is lost going down the track, or going up the next hill, what is the highest point the car could reach?\n')
    f.write('\\end{enumerate}\n')

    
    MassLn=random.randint(20,45)
    MassL=str(MassLn)
    MassPn=float(random.randint(10,30)/10)
    MassP=str(MassPn)
    speed=str(random.randint(65,99))
    f.write('\\item A $'+MassL+'kg$ launcher and projectile are initially at rest.  The launcher propels the $'+MassP+'kg$ projectile in a straight line away from the launcher at $'+speed+'m/s$.  Calculate the speed of the launcher immidately after launch.\n')

    f.write('\\newpage\n')

    
    Massbn=random.randint(2,19)
    Massb=str(Massbn)
    Disn=random.randint(10,50)
    Dis=str(random.randint(10,50))
    EnergyN=Massbn*Disn    
    Energy=str(EnergyN)
    f.write('\\item A $'+Massb+'kg$ box is pushed along a smooth floor in a straight line.  To push the box a certain distance, $'+Energy+'J$ of work is expended.\n')
    f.write('\\begin{enumerate}\n')
    f.write('\\item State the minimum energy need to push the box this distance.\n')
    f.write('\\item Calculate the expected distance the box is pushed with this amount of work.\n')
    f.write('\\item Calculate the work that must be done if the mass of the box is doubled?\n')
    f.write('\\item If the mass of the box were double, what value would have to be adjusted to maintain the same amount of original work?\n')
    f.write('\\end{enumerate}\n')


    Masswn=random.randint(2,9)
    Massw=str(Masswn)
    Temp1n=random.randint(350,450)
    Temp1=str(Temp1n)
    Massw2=str(2*Masswn)
    f.write('\\item A pot with $'+Massw+'kg$ of water is heated to $'+Temp1+'k$.  A similar pot with $'+Massw2+'kg$ of water is also heated to $'+Temp1+'K$.  What is the relation between the heat in the first pot to the heat in the second pot?\n')

    
    f.write('\\item Violet light has twice the frequency of red light.  What is the relationship between their wavelengths?\n')
    
    
    f.write('\\item In a paragraph, describe the difference between and give an example of longitudinal and transverse wave.\n')

    
    R1n=random.randint(20,40)*10
    R1=str(R1n)
    R2n=random.randint(50,70)
    R2=str(R2n)
    Num=random.randint(2,4)
    REn=int(R1n/Num)+R2n
    RE=str(REn)
    Temp1n=random.randint(350,450)
    Temp1=str(Temp1n)
    Massw2=str(2*Masswn)
    f.write('\\item A tool box has resistors of $'+R1+' \Omega$ and $'+R2+' \Omega$.  Draw a picture of how the resistors can be combined so that a resistor of $'+RE+' \Omega$ can be achieved.\n')


    f.write('\\end{enumerate}\n')

    

def WritePage(home,n):
    output=home+"/temp"
    nn=str(n)
    name=output+"/temp"+nn
    filename=name+".tex"
    logname=output+"/log.out"
    f=open(filename,'w')
    HEAD(f)
    PAGE(f,n)
    ENDMAT(f)
    f.close()

    pdfcommand="/Library/TeX/texbin/pdflatex --file-line-error --synctex=1 -output-directory "+output+" "+filename+" >"+logname
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
for x in range(1, 2):
	WritePage(home,x)
