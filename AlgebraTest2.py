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
    f.write('\\usepackage{marginnote}\n')
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
    f.write('\\begin{picture}(110,50)\n')
    f.write('\\put(30,5){\\grid(100,100)(10,10)}\n')
    f.write('\\end{picture}\n')
    f.write('}\n')
    f.write('\\begin{document}\n')
    f.write('\\title{Algebra II Quiz 1 }\n')
    f.write('\\author{RH Cox}\n')
    f.write('\\date{DATE: 2015 September 16 }\n')
    f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

def FILL(f):
    f.write('\\begin{enumerate}\n')
    f.write('\\item Parent function name and expresion:\n ')
    f.write('\\item Domain and Range:\n ')
    f.write('\\item Transformations:  Translate    Reflection    Shrink/Stretch \n ')
    f.write('\\item Sketch function in grid, show intecepts, vertices, if any: \\gridpaper\n ')
    f.write('\\end{enumerate}\n\n')

    
def PAGE(f,a):
    random.seed(a)
    m=random.randint(2,9)
    b=random.randint(2,9)
    c=random.randint(2,9)
    d=random.randint(2,9)
    e=random.randint(2,9)
    g=random.randint(2,9)
    k=random.randint(2,9)
    pm=random.choice(' -')
    v=random.choice('stuvwyz')
    axis=random.choice('xy')
    

    ms=str(m)
    bs=str(b)
    cs=str(c)
    ds=str(d)
    es=str(e)
    gs=str(g)
    ks=str(k)

    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{15mm}\n')
    
    f.write('\\item Graph each function. Sketch the graph. State the expression and name of the parent function. State the Domain and Range. Circle the Transformation. \n')

    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{6mm}\n')

    f.write('\\item $f('+v+')='+ms+' |'+v+'|+'+bs+ '$ \n ')
    FILL(f)

    f.write('\\item $f('+v+')='+v+'^2+'+bs+ '$ \n ')
    FILL(f)

    f.write('\\item $f('+v+')='+pm+v+'^2+'+bs+ '$ \n ')
    FILL(f)

    f.write('\\item $f('+v+')=\sqrt{'+v+'+'+bs+'}$ \n ')
    FILL(f)

    f.write('\\end{enumerate}\n')
    
    f.write('\\item Solve for '+v+'.\n ')
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{20mm}\n')

    f.write('\\item $'+bs+v+'='+ms+'$\n ')
    
    f.write('\\item $'+cs+v+'+'+ds+'='+bs+'$\n ')

    f.write('\\item $-'+v+'-'+cs+'='+gs+'$\n ')

    f.write('\\item $'+v+'-'+bs+'= -'+gs+'$\n ')
    f.write('\\end{enumerate}\n\n')
    
    f.write('\\item Suppose $f(x)='+ds+v+'+'+bs+'$. Suppose the domain of $f$ is {'+bs+','+cs+','+ds+','+es+'}, that is these are the values of x that would be input into the function $f$.  What would the resultant range of $f$ be givin this domain?. \n')
    f.write('\\item Write an expression for an absolute value function that is translated '+ms+' units on the '+axis+' axis.\n ')

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
for x in range(1, 100):
	WritePage(home,x)
