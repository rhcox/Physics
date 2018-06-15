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
	f.write('\\title{AP Physics Review Quiz 1}\n')
	f.write('\\author{RH Cox}\n')
	f.write('\\date{DATE: 2015 April 24 }\n')
	f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

    
def PAGE(f,a):
    random.seed(a)


    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{4cm}\n')
    massrf=float(random.randint(40,99))/100
    massr=str(massrf)
    f.write('\\item A '+massr+' kg rocket is on a lanchpad. Sketch the weight and normal force for this situation.  Sketch the free body diagram. \n')
    

    timeB=str(float(random.randint(20,40))/10)
    accel=str(18.0/massrf)
    Y0=str(float(random.randint(5,40))/100)
    f.write('\\item The rocket is launched. Sketch the free body diagram during the thrust phase.\n')


    f.write('\\item The rocket accelerates for '+timeB+' s at '+accel+'$\\frac{m}{s^2}$. Calculate the velocity at the end of this time assuming the initial velocity is zero. Assuming that the rocket is launched from '+Y0+' m, calculate the hieght at the end of this time.\n')


    f.write('\\newpage \n')


    massS=str(round(massrf/6,2))
    f.write('\\item A '+massS+' kg stage seperates from the rocket. Use conservation of momentum to calculate the speed of the rocket after seperation, assuming the speed before separation is as just calculated.\n')


    f.write('\\item  Using the speed and height from the previous problems, calculate the maximum height achieved by the rocket.\n')


 
    f.write('\\item  A parachute opens as the rocket descends.  Draw the free body diagram of the rockets as it falls to the ground.\n')



    f.write('\\item  If the parachute did not open, and the rocket fell freely, use the maximum height to calculate the time it would take for the rocket reaches the ground.\n')



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
for x in range(1, 2):
	WritePage(home,x)
