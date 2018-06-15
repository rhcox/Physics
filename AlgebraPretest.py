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
    f.write('\\rhead{Algebra II - '+str(n)+'}\n')
    f.write('\\lfoot{ Furr '+n+'}\n')
    f.write('\\rfoot{Show All Work}\n')
    f.write('\\renewcommand\headrule{\\vspace{-8pt}\dotfill}\n')
    f.write('\\newcommand{\\gridpaper}{\n')
    f.write('\\begin{picture}(150,150)\n')
    f.write('\\put(30,5){\\grid(140,140)(10,10)}\n')
    f.write('\\end{picture}\n')
    f.write('}\n')
    f.write('\\begin{document}\n')
    f.write('\\title{Algebra II Pre Quiz }\n')
    f.write('\\author{RH Cox}\n')
    f.write('\\date{DATE: 2015 August 28 }\n')
    f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

    
def PAGE(f,a):
    random.seed(a)
    m=random.randint(2,9)
    b=random.randint(2,9)
    c=random.randint(2,9)
    d=random.randint(2,9)
    e=random.randint(2,9)
    g=random.randint(2,9)
    k=random.randint(2,9)
    
    ms=str(m)
    bs=str(b)
    cs=str(c)
    ds=str(d)
    es=str(e)
    gs=str(g)
    ks=str(k)

    f.write('\\begin{enumerate}\n')
    
    f.write('\\item For each function, sketch the graph and state the expression and name of the parent function. \n')

    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{6mm}\n')


    f.write('\\item $f(x)='+ms+'x+'+bs+ '$\n\n \\gridpaper \n ')


    f.write('\\item $f(x)=-'+ms+'x^2$ \n\n \\gridpaper \n ')

    f.write('\\newpage\n')

    f.write('\\item $f(x)='+ms+'x^2$ \n\n \\gridpaper \n ')

    f.write('\\item $f(x)=(x+'+bs+')^2$  \n\n \\gridpaper \n ')

    f.write('\\item $f(x)=e^{x}+'+cs+'$  \n\n \\gridpaper \n ')

    f.write('\\newpage\n')

    f.write('\\item $f(x)=\sqrt{x+'+cs+'}$ \n\n \\gridpaper \n ')

    f.write('\\item $f(x)=\sqrt{x-'+cs+'}$  \n\n \\gridpaper \n ')

    f.write('\\end{enumerate}\n')
    
    f.write('\\item For each equation, solve for the variable. Show all work. No credit given if work is not shown.\n')


    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{35mm}\n')
    
    f.write('\\item $'+cs+'x='+ds+'$ \n ')
    
    f.write('\\item $'+ms+'x-'+bs+'='+ds+'$ \n ')


    f.write('\\item $'+ms+'x+'+bs+'='+ds+'$ \n ')

    f.write('\\item $-'+ms+'x^2='+es+'$  \n ')

    f.write('\\item $'+ms+'x^2='+ks+'$ \n ')

    f.write('\\item $(x+'+bs+')^2='+gs+'$ \n ')

    f.write('\\item $\sqrt{x+'+cs+'='+gs+'}$ \n ')

    f.write('\\item $\sqrt{x-'+cs+'}='+gs+'$ \n ')

    f.write('\\end{enumerate}\n\n')

    f.write('\\item Suppose you were aksed to solve the equation $\sqrt{x^2+3x_4}=7$ What would be the first step you would apply to solve for the variable.  Do not solve for the variable, in a sentence only state what you would do.\n ')

    f.write('\\end{enumerate}\n\n')

    

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
for x in range(1, 100):
	WritePage(home,x)
