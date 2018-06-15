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
	f.write('\\title{AP Physics Exam Six Weeks 3}\n')
	f.write('\\author{RH Cox}\n')
	f.write('\\date{DATE: 2017 Decmber 12 }\n')
	f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

    
def PAGE(f,a):
    random.seed(a)


    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{4cm}\n')
    massrf=float(random.randint(40,99))/100
    massr=str(massrf)
    heightf=float(random.randint(30,80))/100
    height=str(heightf)
    distancef=float(random.randint(110,160))/100
    distance=str(distancef)
    rollf=float(random.randint(50,90))/100
    roll=str(rollf)
    f.write('\\item A '+massr+' kg ball is on a flat table.  The table is '+height+' m above the floor.  The ball accelerates from rest to a maximum speed over a distance of '+roll+' m.  It rolls off the flat table at this speed and hits the floor '+distance+' m away from the edge of the table. Sketch a schematic and a free body diagram each of the ball at rest on the table, the ball accelerating on the table, the ball in free fall, and the ball hitting the ground. \n')
    

    timeB=str(float(random.randint(20,40))/10)
    accel=str(18.0/massrf)
    Y0=str(float(random.randint(5,40))/100)
    f.write('\\item Calculate the time of flight of the ball from the edge of the table to the first contact with the floor.\n')


    f.write('\\item Calculate the horizontal speed of the ball as it rolls off the table.\n')


    f.write('\\newpage \n')


    massS=str(round(massrf/6,2))
    f.write('\\item Calculate the veritcal speed of the ball just before it hits the floor.\n')


    f.write('\\item Calculate the total speed of the ball just after it hits the floor.\n')


 
    f.write('\\item Calculate the angle the ball hits the floor.\n')



    f.write('\\item  Calculate the force needed to accelerate the ball from rest on the table top to the speed that the ball rols off the table.\n')

    bouncef=heightf*.7
    bounce=str(bouncef)

    f.write('\\item  If the ball bounces to a msximum hieght of '+bounce+' m, calculate the speed of the ball just after the bounce.\n')


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
for x in range(1, 40):
	WritePage(home,x)
