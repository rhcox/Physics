import random
import subprocess
import os
import time

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
    f.write('\\lfoot{ Furr}\n')
    f.write('\\rfoot{Show All Work}\n')
    f.write('\\renewcommand\headrule{\\vspace{-8pt}\dotfill}\n')
    f.write('\\newcommand{\\gridpaper}{\n')
    f.write('\\begin{picture}(300,300)\n')
    f.write('\\put(30,5){\\grid(300,300)(10,10)}\n')
    f.write('\\end{picture}\n')
    f.write('}\n')
    f.write('\\begin{document}\n')
    f.write('\\title{AP Physics Six Weeks Exam 2}\n')
    f.write('\\author{RH Cox}\n')
    f.write('\\date{DATE: 2017 November 8 }\n')
    f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

    
def PAGE(f,a):
    random.seed(a)
    t1=float(random.randint(5,10))/10
    t2=float(random.randint(11,15))/10
    t3=float(random.randint(16,20))/10
    t4=float(random.randint(21,25))/10
    t5=float(random.randint(26,30))/10
    t6=float(random.randint(31,35))/10

    t1s=str(t1)
    t2s=str(t2)
    t3s=str(t3)
    t4s=str(t4)
    t5s=str(t5)
    t6s=str(t6)

    v=float(random.randint(30,40))/10
    a=-1*float(random.randint(20,60))/100

    x0=float(random.randint(5,10))/10

    error=float(random.randint(90,110))/100
    x1=(x0+v*t1+0.5*a*t1*t1)*error
    
    error=float(random.randint(90,110))/100
    x2=(x0+v*t2+0.5*a*t2*t2)*error

    error=float(random.randint(90,110))/100
    x3=(x0+v*t3+0.5*a*t3*t3)*error

    error=float(random.randint(90,110))/100
    x4=(x0+v*t4+0.5*a*t4*t4)*error

    error=float(random.randint(90,110))/100
    x5=(x0+v*t5+0.5*a*t5*t5)*error


    error=float(random.randint(90,110))/100
    x6=(x0+v*t6+0.5*a*t6*t6)*error

    x6s=str(round(x6 ,1))
    x5s=str(round(x5,1))
    x4s=str(round(x4,1))
    x3s=str(round(x3,1))
    x2s=str(round(x2,1))
    x1s=str(round(x1,1))
    x0s=str(round(x0,1))

    mass=float(random.randint(20,40))/10    
    smass=str(round(mass,1))    
            
    floor=float(random.randint(30,90))/100    
    sfloor=str(round(floor,2))    

    f.write('\\begin{tabular} {|p{2cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|} \n')
    f.write('\\hline \n')
    f.write('Time[s] & 0 &'+t1s+'&'+t2s+'&'+t3s+'&'+t4s+'&'+t5s+'&'+t6s+'\\\ \n')
    f.write('\\hline \n')
    f.write('position[m] &'+x0s+'&'+x1s+'&'+x2s+'&'+x3s+'&'+x4s+'&'+x5s+'& '+x6s+'  \\\ \n')
    f.write('\\hline \n\n')
    f.write('\\end{tabular} \n')

    f.write('\n A '+smass+'kg block is traveling a on track.  Friction is present and accelerating the block. \n')
    f.write('The position of the cart for certain times listed. \n')
    f.write('Immidiately after the final time, the block slides off the track to the floor '+sfloor+' below. \n')
    f.write('Answer the following question based on the data in the table. \n \n')
    
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{27mm}\n')
    

    f.write('\\item Sketch a schematic of the problem.  Label distances and indicates times. \n')

    f.write('\\item Draw three freebody diagrom, one each of the block traveling down the track, as a projectile after it leaves the track, and at rest on the ground. Label each. \n')

    f.write('\\item Fit the data to the quadratic kinetmatic equation.  Write the equation with paramaters.  State the initial speed and accleration form the fit equation\n')

    f.write('\\newpage \n')

    f.write('\\item Using the acceleration from the fit, calculate the frictional force that is accelerating the block.  Calculate the coeefecient of kinetic friction. \n')


    f.write('\\item Using the initial velocity and acceleration from the fit, and the final time in the table, calculate the the speed of the block as it leaves the table.\n')

    f.write('\\item Using the speed of the block as it leaves the table calcualted above, and the height of the table, calcualte the time the block is in the air and the distance the block travels before it hits the floor.\n')

    f.write('\\item Suppose there was no friction between the tack and the table.  State the speed that the block would exit the track under those conditions.  Calculate the time in the air and the distance traveled under those conditions . \n')
    
    f.write('\\item Suppose the mass was doubled.  In a paragraph length repsonse state if this change would effect or not effect the frictional force, distance traveled, or time of flight.  State the physics you know as evidence.Use this evidence to justify your claims. Do not use calculations as evidence.\n')
    

    f.write('\\end{enumerate}\n')
        

def WritePage(home,n):
	output=home+"/temp"
	nn=str(int(n))
	name=output+"/temp"+nn
	filename=name+".tex"
	logname=output+"/log.out"
	f=open(filename,'w')
	HEAD(f,n)
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
for x in range(1, 30):
	WritePage(home,x*(time.clock()*1000))
