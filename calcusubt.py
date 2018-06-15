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
	f.write('\\lfoot{ Calculus}\n')
	f.write('\\rfoot{U-Substitution}\n')
	f.write('\\renewcommand\headrule{\\vspace{-8pt}\dotfill}\n')

	f.write('\\newcommand{\\gridpaper}{\n')
	f.write('\\begin{picture}(50,50)\n')
	f.write('\\put(30,5){\\grid(80,100)(10,10)}\n')
	f.write('\\end{picture}\n')
	f.write('}\n')
	f.write('\\begin{document}\n')
	f.write('\\title{Calculus U-substitution Quiz}\n')
	f.write('\\author{RH Cox}\n')
	f.write('\\date{DATE: }\n')
	f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

    
def PAGE(f,a):
    random.seed(a)
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{3cm}\n')
    
    v=random.choice(['6','7','8', '9'])
    ww=random.choice([2,3,4,5])
    w=str(ww)
    wm=str(ww-1)
    c=str(round(random.random()*10,2))	
    f.write('\\item $\\int \\; '+v+'x^{'+wm+'} sin(x^{'+w+'}+'+c+') \\; dx$\n')
    

    v=random.choice(['6','7','8', '9'])
    ww=random.choice([2,3,4,5])
    w=str(ww)
    wm=str(ww-1)
    c=str(round(random.random()*10,2))	
    f.write('\\item $\\int \\; \\frac{'+v+'x^{'+wm+'} }{x^{'+w+'}+'+c+'} \\; dx$\n')


    v=random.choice(['6','7','8', '9'])
    ww=random.choice([2,3,4,5])
    w=str(ww)
    wm=str(ww-1)
    c=str(round(random.random()*10,2))	
    f.write('\\item $\\int \\; '+v+'x^{'+wm+'} e^{x^{'+w+'}+'+c+'} \\; dx$\n')


    v=random.choice(['6','7','8', '9'])
    ww=random.choice([2,3,4,5])
    w=str(ww)
    wm=str(ww-1)
    c=str(round(random.random()*10,2))	
    f.write('\\item $\\int \\; \\frac{'+v+'sin('+w+'x)}{cos('+w+'x)} \\; dx$\n')
    
    f.write('\\newpage')
    
    v=random.choice(['6','7','8', '9'])
    ww=random.choice([2,3,4,5])
    w=str(ww)
    wm=str(ww-1)
    c=str(round(random.random()*10,2))	
    f.write('\\item $\\int \\; \\frac{'+v+'tan('+w+'x)sec'+w+'x)}{sec('+w+'x)} \\; dx$\n')


    v=random.choice(['6','7','8', '9'])
    ww=random.choice([2,3,4,5])
    w=str(ww)
    wm=str(ww-1)
    c=str(round(random.random()*10,2))	
    f.write('\\item $\\int \\; '+w+'cos('+v+'x) e^{sin('+v+'x)} \\; dx$\n')

    v=random.choice(['6','7','8', '9'])
    ww=random.choice([2,3,4,5])
    w=str(ww)
    wm=str(ww-1)
    c=str(round(random.random()*10,2))	
    f.write('\\item $\\int \\; '+w+'cos('+v+'x+'+c+') \\; dx$\n')
    

    v=random.choice(['6','7','8', '9'])
    ww=random.choice([2,3,4,5])
    w=str(ww)
    wm=str(ww-1)
    c=str(round(random.random()*10,2))	
    f.write('\\item $\\int \\; '+v+'x^{'+wm+'}cos('+v+'x^{'+w+'}+'+c+') \\; dx$\n')


    v=random.choice(['6','7','8', '9'])
    ww=random.choice([2,3,4,5])
    w=str(ww)
    wm=str(ww-1)
    c=str(round(random.random()*10,2))	
    f.write('\\item $\\int \\; \\frac{1}{'+v+'x+'+c+'} \\; dx$\n')


    v=random.choice(['6','7','8', '9'])
    ww=random.choice([2,3,4,5])
    w=str(ww)
    wm=str(ww-1)
    c=str(round(random.random()*10,2))	
    f.write('\\item $\\int \\; cot(x) \\; dx$\n')

    
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
for x in range(1, 25):
	WritePage(home,x)