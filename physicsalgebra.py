import random
import subprocess
import os

def variable():
    xx=str(random.choice('cdefghjkmnopqrstuvwxyz'))
    return xx
    
def HEAD(f,n):
    f.write('\\documentclass[12pt,twocolumn]{article}\n')
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
    nn=str(n)
    f.write('\\lfoot{ Physics '+nn+'}\n')
    f.write('\\rfoot{Show All Work}\n')
    f.write('\\renewcommand\headrule{\\vspace{-8pt}\dotfill}\n')
    f.write('\\newcommand{\\gridpaper}{\n')
    f.write('\\begin{picture}(50,50)\n')
    f.write('\\put(30,5){\\grid(80,100)(10,10)}\n')
    f.write('\\end{picture}\n')
    f.write('}\n')
    f.write('\\begin{document}\n')
    f.write('\\title{Physics Algebra Quiz}\n')
    f.write('\\author{RH Cox}\n')
    f.write('\\date{DATE: }\n')
    f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

    
def PAGE(f,a):
    random.seed(a)
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{3cm}\n')
    
    a=str(random.randint(2,15))
    b=str(random.randint(20,50))
    c=str(random.randint(10,20))
    x=variable()
    f.write('\\item $'+a+x+'+'+b+'='+c+'$\n')

    a=str(random.randint(-15,2))
    b=str(random.randint(20,50))
    c=str(random.randint(10,20))
    x=variable()
    f.write('\\item $'+a+x+'+'+b+'='+c+'$\n')

    a=str(random.randint(2,15))
    b=str(random.randint(20,50))
    c=str(random.randint(10,20))
    x=variable()
    f.write('\\item $'+a+x+'-'+b+'='+c+'$\n')

    a=str(random.randint(2,15))
    b=str(random.randint(20,50))
    c=str(random.randint(1,4))
    d=str(random.randint(5,9))
    x=variable()
    f.write('\\item '+a+x+'+'+b+'=$\\frac{'+c+'}{'+d+'}$\n')
    
    a=str(random.randint(2,15))
    b=str(random.randint(20,50))
    c=str(random.randint(10,20))
    x=variable()
    f.write('\\item $\\sqrt{'+a+x+'}='+c+'$\n')

    a=str(random.randint(2,15))
    b=str(random.randint(20,50))
    c=str(random.randint(10,20))
    x=variable()
    f.write('\\item $\\sqrt{'+a+x+'+'+b+'}='+c+'$\n')

    a=str(random.randint(2,15))
    b=str(random.randint(20,50))
    c=str(random.randint(10,20))
    x=variable()
    f.write('\\item $\\sqrt{'+a+x+'-'+b+'}='+c+'$\n')

    a=str(random.randint(2,15))
    b=str(random.randint(20,50))
    c=str(random.randint(10,20))
    x=variable()
    f.write('\\item $\\sqrt{'+a+x+'+'+b+'}=-'+c+'$\n')

    n1=random.randint(2,7)
    n2=random.randint(2,7)
    a=str(n1+n2)
    b=str(n1*n2)
    x=variable()
    f.write('\\item $'+x+'^2+'+a+x+'+'+b+'=0$\n')

    n1=random.randint(-7,-2)
    n2=random.randint(2,7)
    a=str(n1+n2)
    b=str(n1*n2)
    x=variable()
    f.write('\\item $'+x+'^2+'+a+x+'+'+b+'=0$\n')

    n1=random.randint(2,5)
    n2=random.randint(-9,-6)
    a=str(n1+n2)
    b=str(n1*n2)
    x=variable()
    f.write('\\item $'+x+'^2+'+a+x+'+'+b+'=0$\n')
    
    a=str(random.randint(2,15))
    b=str(random.randint(20,50))
    c=str(random.randint(10,20))
    x=variable()
    f.write('\\item $'+a+x+'^2+'+b+x+'+'+c+'=0$\n')
 
    a=str(random.randint(2,15))
    b=str(random.randint(20,50))
    c=str(random.randint(10,20))
    d=str(random.randint(1,15))
    x=variable()
    f.write('\\item $'+a+x+'^2+'+b+x+'-'+c+'='+d+'$\n')

    a=str(random.randint(2,15))
    x=variable()
    f.write('\\item $ \\frac{1}{'+x+'+'+a+'}=0$\n')

    a=str(random.randint(1,10))
    x=variable()
    f.write('\\item $ \\frac{1}{'+x+'^2-'+a+'}=0$\n')
    
    a=str(random.randint(1,10))
    b=str(random.randint(2,5))
    x=variable()
    f.write('\\item $ \\frac{'+b+'}{'+x+'^2-'+a+'}=0$\n')

    a=str(random.randint(1,10))
    b=str(random.randint(2,5))
    c=str(random.randint(5,12))
    x=variable()
    f.write('\\item $ \\frac{'+b+'}{'+x+'^2-'+a+'}='+c+'$\n')

    a=str(float(random.randint(1,100))/100)
    x=variable()
    f.write('\\item $ sin('+x+')='+a+'$\n')

    a=str(float(random.randint(1,100))/100)
    x=variable()
    f.write('\\item $ cos('+x+')='+a+'$\n')

    a=str(random.randint(1,20))
    x=variable()
    f.write('\\item $ tan('+x+')='+a+'$\n')
    
    a=str(float(random.randint(1,100))/100)
    b=str(random.randint(2,5))
    x=variable()
    f.write('\\item $ sin('+x+'+'+b+')='+a+'$\n')

    a=str(float(random.randint(1,100))/100)
    b=str(random.randint(2,5))
    x=variable()
    f.write('\\item $ cos('+x+'+'+b+')='+a+'$\n')

    a=str(float(random.randint(1,100))/100)
    b=str(random.randint(2,5))
    c=str(random.randint(-9,-2))
    f.write('\\item $ '+c+'sin(x+'+b+')='+a+'$\n')

    a=str(float(random.randint(1,100))/100)
    b=str(random.randint(2,5))
    c=str(random.randint(-9,-2))
    f.write('\\item $ '+c+'cos(x+'+b+')='+a+'$\n')

    f.write('\\end{enumerate}\n')

    

def WritePage(home,n):
	output=home+"/temp"
	nn=str(n)
	name=output+"/temp"+nn
	filename=name+".tex"
	logname=output+"/log.out"
	f=open(filename,'w')
	HEAD(f,n)
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
