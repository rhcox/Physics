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
	f.write('\\rhead{Physics-'+str(n)+'}\n')
	f.write('\\lfoot{Furr HS }\n')
	f.write('\\rfoot{Show All Work}\n')
	f.write('\\renewcommand\headrule{\\vspace{-8pt}\dotfill}\n')

	f.write('\\newcommand{\\gridpaper}{\n')
	f.write('\\begin{picture}(50,50)\n')
	f.write('\\put(30,5){\\grid(80,100)(10,10)}\n')
	f.write('\\end{picture}\n')
	f.write('}\n')
	f.write('\\begin{document}\n')
	f.write('\\title{Physics Final Review Part 2}\n')
	f.write('\\author{Turn in on day of Final}\n')
	f.write('\\date{DATE: Fall 2016  }\n')
	f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

    
def PAGE(f,a,N):
    random.seed(a)
    loss=float(random.randint(40,80))/100
    SLoss=str(loss)
    MassCar=float(random.randint(20,120))/100
    SMassCar=str(MassCar)
    AccCar=float(random.randint(10,90))/100
    SAccCar=str(AccCar)
    TCar=float(random.randint(50,120))/100
    STCar=str(TCar)
    HeightTrack=float(random.randint(100,300))/100
    SHeightTrack=str(HeightTrack)
    HeightTable=float(random.randint(200,400))/100
    SHeightTable=str(HeightTable)
    HeightTable=float(random.randint(200,400))/100
    SHeightTable=str(HeightTable)
    PosFloor=round(math.sqrt(2*HeightTrack*HeightTable)*loss,2)
    SPosFloor=str(PosFloor)
    f.write(N+'. A table is $'+SHeightTable+'m$ above the ground.  A toy car with a mass of $'+SMassCar+'kg$ is at rest on the table. For this scenario use $g=10\\frac{m}{s^2}$. \n')
    
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{5mm}\n')

    f.write(' \\item For the car at rest on the table.\n')
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{40mm}\n')
    f.write(' \\item Sketch this scenario with all values shown.\n')
    f.write(' \\item Draw a free body diagram of the car at rest on the table.\n')
    f.write(' \\item Calculate the weight and normal force.\n')
    f.write('\\end{enumerate}\n')
    f.write('\\setlength{\\itemsep}{5mm}\n')
   
    f.write(' \\item  The car is then accelerated constantly at $'+SAccCar+'\\frac{m}{s^2}$ for $'+STCar+'s$. \n')
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{40mm}\n')
    f.write(' \\item  Draw the free body diagram as the car is accelerated, neglecting friction. \n')    
    f.write(' \\item  Calculate the force on the car. \n')
    f.write(' \\item Calcualte the distance traveled by the car. \n')
    f.write(' \\item Calculate the final velocity of the car. \n')
    f.write('\\end{enumerate}\n')
    f.write('\\setlength{\\itemsep}{5mm}\n')

    f.write(' \\item At the end of the time stated above, the car is at the edge of the table and falls to the ground. \n')
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{40mm}\n')
    f.write(' \\item Draw a free body diagram as the car is in the air. \n')
    f.write(' \\item Calculate the time that the car falls to the ground. \n')
    f.write(' \\item Calculate the distance the car lands from the table. \n')
    f.write(' \\item Calculate the verticle speed of the car. \n')    
    f.write('\\end{enumerate}\n')
    f.write('\\setlength{\\itemsep}{5mm}\n')

    f.write(' \\item The  car lands on the ground perfectly on the wheels with no loss of horizontal speed. It tavels until it enters a track with a loop  The top of the loop is $'+SHeightTrack+'m$ above the floor. \n')
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{40mm}\n')
    f.write(' \\item Draw the free body diagram of the car at the top of the loop. \n')
    f.write(' \\item Assuming the car has lost no speed, calculate the linear and angular velocity of the car as it travels the loop. \n')
    f.write(' \\item Calculate the time the car takes to complete the loop. \n')
    f.write('\\end{enumerate}\n')
    f.write('\\setlength{\\itemsep}{40mm}\n')

    
    f.write(' \\item After the car completes the loop, it enters a rough area where it begins to lose speed. The car slows to rest in $'+SLoss+'s$. Calculate the force on the car.\n')


    f.write('\\end{enumerate}\n')
    f.write('\\vspace{4cm}\n')
    f.write('\\newpage\n')
    

    

def WritePage(home,n):
	output=home+"/temp"
	nn=str(n)
	name=output+"/temp"+nn
	filename=name+".tex"
	logname=output+"/log.out"
	f=open(filename,'w')
	HEAD(f,n)
	PAGE(f,n,"I")
	PAGE(f,n+100,"II")
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
for x in range(1, 3):
	WritePage(home,x)
