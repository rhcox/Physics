import random
import subprocess
import os

def HEAD(f,n):
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
	f.write('\\rhead{Pre-Calculus-'+str(n)+'}\n')
	f.write('\\lfoot{Furr HS }\n')
	f.write('\\rfoot{Show All Work}\n')
	f.write('\\renewcommand\headrule{\\vspace{-8pt}\dotfill}\n')

	f.write('\\newcommand{\\gridpaper}{\n')
	f.write('\\begin{picture}(50,50)\n')
	f.write('\\put(30,5){\\grid(80,100)(10,10)}\n')
	f.write('\\end{picture}\n')
	f.write('}\n')
	f.write('\\begin{document}\n')
	f.write('\\title{Pre-Calculus Final Exam}\n')
	f.write('\\author{No Credit if work is not completely and neatly shown.}\n')
	f.write('\\date{DATE: Fall 2016  }\n')
	f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

    
def PAGE(f,a,N):
    random.seed(a)
    UnitI=['\\frac{\\pi}{6}','\\frac{\\pi}{4}','\\frac{\\pi}{3}','\\frac{\\pi}{2}']
    UnitII=['\\frac{2\\pi}{3}','\\frac{3\\pi}{4}','\\frac{5\\pi}{6}','\\pi']
    UnitI_II=UnitI+UnitII
    
    SUnitI=['\\frac{\\sqrt{3}}{2}','\\frac{\\sqrt{2}}{2}','\\frac{1}{2}','0']
    SUnitII=['-\\frac{\\sqrt{3}}{2}','-\\frac{\\sqrt{2}}{2}','-\\frac{1}{2}','0']
    SUnitI_II=SUnitI+SUnitII

    TUnitI=['\\sqrt{3}','1','\\frac{1}{\\sqrt{3}}']
    TUnitII=['-\\sqrt{3}','-1','-\\frac{1}{\\sqrt{3}}','0']
    TUnitI_II=TUnitI+TUnitII
    
    f.write('I. Draw a unit circle using a compass and protractor.  Label all customary angles and the value of sine and cosine.\n')
    f.write('\\newpage\n\n')

    AngA,AngB, AngC=random.sample(UnitI_II,3)
    f.write('II. Calculate each value using the unit circle.\n')
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{10mm}\n')
    f.write('\\item $sin('+AngA+')=$\n')
    f.write('\\item $cos('+AngB+')=$\n')
    f.write('\\item $tan('+AngC+')=$\n')
    f.write('\\end{enumerate}\n')
    f.write('\\setlength{\\itemsep}{5mm}\n')
    

    ValA,ValB=random.sample(SUnitI_II,2)
    ValC=random.choice(TUnitI_II)
    f.write('III. Calculate each value using the unit circle. List all angles in radians.  List all angles where the value is valid.\n')
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{10mm}\n')
    f.write('\\item $sin^{-1}('+ValA+')=$\n')
    f.write('\\item $cos^{-1}('+ValB+')=$\n')
    f.write('\\item $tan^{-1}('+ValC+')=$\n')
    f.write('\\end{enumerate}\n')
    f.write('\\setlength{\\itemsep}{5mm}\n')
    

    xi=float(random.randint(10,40))/10
    Sxi=str(xi)
    yj=float(random.randint(50,90))/10
    Syj=str(yj)    
    f.write('IV. Suppose $\\vec{v}='+Sxi+'\\hat{i}+'+Syj+'\\hat{j}$. Write the vector in polar form\n')
    f.write('\\vspace{3cm}\n\n')

    rad=float(random.randint(20,90))/10
    Srad=str(rad)
    ang=float(random.randint(20,150))/100
    Sang=str(ang)    
    f.write('V. Suppose $\\vec{v}='+Srad+'\\angle'+Sang+'$. Write the vector in retangular form\n')
    f.write('\\newpage\n\n')
    
    xi1=float(random.randint(20,50))/10
    Sxi1=str(xi1)
    yj1=float(random.randint(60,99))/10
    Syj1=str(yj1)    
    xi2=float(random.randint(15,70))/10
    Sxi2=str(xi2)
    yj2=float(random.randint(45,85))/10
    Syj2=str(yj2)
    f.write('VI. Calculate $('+Sxi1+'\\hat{i}+'+Syj1+'\\hat{j}) \\cdot ('+Sxi2+'\\hat{i}+'+Syj2+'\\hat{j})$ \n')
    f.write('\\vspace{3cm}\n\n')
    
    f.write('VII. Calculate $('+Sxi1+'\\hat{i}+'+Syj1+'\\hat{j}) \\times ('+Sxi2+'\\hat{i}+'+Syj2+'\\hat{j})$ \n')
    f.write('\\vspace{3cm}\n\n')
    
    zk1=float(random.randint(30,76))/10
    Szk1=str(zk1)    
    zk2=float(random.randint(10,44))/10
    Szk2=str(zk2)
    f.write('VIII. Calculate $('+Sxi1+'\\hat{i}+'+Syj1+'\\hat{j}+'+Szk1+'\\hat{k}) \\times ('+Sxi2+'\\hat{i}+'+Syj2+'\\hat{j}+'+Szk1+'\\hat{k})$ \n')
    f.write('\\vspace{3cm}\n\n')
    
    Amp=float(random.randint(2,9))
    SAmp=str(Amp)    
    Coef=float(random.randint(2,9))
    SCoef=str(Coef)
    Phas=float(random.randint(20,150))/100
    SPhas=str(Phas)    
    f.write('IX.  Consider the function $'+SAmp+'sin('+SCoef+'\\theta+'+SPhas+')$ \n')
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{20mm}\n')
    f.write('\\item Sketch the function')
    f.write('\\item Label and state the amplitude')
    f.write('\\item Label and state the period')
    f.write('\\item Label and state the equation for the midline')
    f.write('\\item Label and state the phase shift')
    f.write('\\end{enumerate}\n')
    f.write('\\setlength{\\itemsep}{5mm}\n')

    Amp1=float(random.randint(2,9))
    SAmp1=str(Amp1)    
    Coef1=float(random.randint(2,9))
    SCoef1=str(Coef1)
    Phas1=float(random.randint(20,150))/100
    SPhas1=str(Phas1)    
    f.write('X.  Consider the function $'+SAmp1+'cos('+SCoef1+'\\theta+'+SPhas1+')$ \n')
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{20mm}\n')
    f.write('\\item Sketch the function')
    f.write('\\item Label and state the amplitude')
    f.write('\\item Label and state the period')
    f.write('\\item Label and state the equation for the midline')
    f.write('\\item Label and state the phase shift')
    f.write('\\end{enumerate}\n')
    f.write('\\setlength{\\itemsep}{5mm}\n')

    bbb=float(random.randint(2,9))
    Sbbb=str(bbb)
    Ang3=float(random.randint(20,150))/100
    SAng3=str(Ang3)    
    f.write('XI. A wire connected from the ground to the top of a tower is '+Sbbb+' meters long.  The wire makes a '+SAng3+' radians angle with the ground. Sketch the scenarion. Calculate the distance from the tower to the point where the wire is connected to the ground. Make sure the calculator is in radians. Use three decimal place.\n')
    f.write('\\newpage\n\n')

    SideA=float(random.randint(20,90))/10
    SSideA=str(SideA)    
    SideB=float(random.randint(100,200))/10
    SSideB=str(SideB)    
    SideC=float(random.randint(300,400))/10
    SSideC=str(SideC)
    f.write('XII.A triangle has the following sides:\n\n a='+SSideA+'\n\n b='+SSideB+'\n\n c='+SSideC+'\n\n  Sketch the triangle. Solve for angle $\\alpha$ in radians.  Write 4 decimal places') 
    f.write('\\vspace{4cm}\n\n')

    SideA=float(random.randint(20,90))/10
    SSideA=str(SideA)
    AngA=float(random.randint(100,150))/100
    SAngA=str(AngA)    
    AngC=float(random.randint(80,130))/100
    SAngC=str(AngC)    
    f.write('XIII.A triangle has the following values:\n\n a='+SSideA+'\n\n $\\alpha$='+SAngA+' radians\n\n $\\gamma$='+SAngC+' radians\n\n  Sketch the Triangle.  Solve for the lengths of the two missing sides.') 
    f.write('\\vspace{4cm}\n\n')

    SideA=float(random.randint(10,20))/10
    SSideA=str(SideA)    
    SideB=float(random.randint(30,40))/10
    SSideB=str(SideB)    
    f.write('XIV.A triangle has the following sides:\n\n a='+SSideA+'\n\n b='+SSideB+'\n\n  Calculate the hypotenuse') 
    f.write('\\vspace{2cm}\n\n')

    f.write('\\newpage\n\n')
    
    Ang5=random.choice(UnitI)
    Ang6=random.choice(UnitII)
    f.write('XV. Write $\\sin('+ Ang5+')sin('+Ang6+')]$ as a sum.\n')
    f.write('\\vspace{3cm}\n\n')

    Ang5=random.choice(UnitI)
    Ang6=random.choice(UnitII)
    f.write('XVI. Write $\\sin('+ Ang5+') + cos('+Ang6+')]$ as a product.\n')
    f.write('\\vspace{3cm}\n\n')
        
    

def WritePage(home,n):
	output=home+"/temp"
	nn=str(n)
	name=output+"/temp"+nn
	filename=name+".tex"
	logname=output+"/log.out"
	f=open(filename,'w')
	HEAD(f,n)
	PAGE(f,n,"I")
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
import math
home = expanduser("~")
for x in range(1, 30):
	WritePage(home,x)
