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
	f.write('\\title{Pre-Calculus Quiz 8 - Paper}\n')
	f.write('\\author{No credit if work not show or if not turned in at end of class.}\n')
	f.write('\\date{DATE: 2017 January 20  }\n')
	f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

def PROB(f,Expres):
    f.write('\\item For the expression f(x)='+Expres+'\n')
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{5mm}\n')
    f.write('\\item Graph and sketch the function.\n')
    f.write('\\item Identify on graph and list the cordinates here of all extrema.\n')
    f.write('\\item Identify each extrema as local or absolute minimum or maximum.\n')
    f.write('\\item State the domain and range here.\n')
    f.write('\\item Identify all transformations here.\n')
    f.write('\\end{enumerate}\n')
    

def PAGE(f,a,N):
    random.seed(a)

    AA=random.randint(2,10)
    SA=str(AA)
    BB=random.randint(5,19)
    SB=str(BB)
    CC=random.randint(10,20)
    SC=str(CC)
    DD=random.randint(10,30)
    SD=str(DD)
    EE=random.randint(8,20)
    SE=str(EE)
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{25mm}\n')
    Express='$'+SA+'x^2+'+SB+'x+'+SC+'$'
    PROB(f,Express)
    Express='$'+SA+'x^3+'+SB+'x^2+'+SC+'x+'+SD+'$'
    PROB(f,Express)
    Express='$'+SA+'x^4+'+SB+'x^3+'+SC+'x^2+'+SD+'x+'+SE+'$'
    PROB(f,Express)
    Express='$'+SB+'x^4+'+SA+'x^2+'+SE+'x+'+SD+'$'
    PROB(f,Express)
    Express='$'+SA+'x^3+'+SB+'x+'+SE+'$'
    PROB(f,Express)
    f.write('\\newpage\n\n')
    f.write('\\end{enumerate}\n')
    

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
