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
    f.write('\\title{Algebra II Quiz 5 }\n')
    f.write('\\author{RH Cox}\n')
    f.write('\\date{DATE: 2016 November 4 }\n')
    f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

def FILL(f):
    f.write('\\begin{enumerate}\n')
    f.write('\\item Parent function name and expresion:\n ')
    f.write('\\item Domain and Range:\n ')
    f.write('\\item Transformations:  Translate    Reflection    Shrink/Stretch \n ')
    f.write('\\item Sketch function in grid, show intercepts, vertices, if any: \\gridpaper\n ')
    f.write('\\end{enumerate}\n\n')

    
def PAGE(f,seed):
    random.seed(seed)
    m=random.randint(2,9)
    b=random.randint(2,9)
    c=random.randint(2,9)
    d=random.randint(2,9)
    e=random.randint(2,9)
    g=random.randint(2,9)
    k=random.randint(2,9)
    pm=random.choice(' -')
    v=random.choice('stuvwyz')
    v1=random.choice('ABCDF')
    v2=random.choice('MNPQR')
    axis=random.choice('xy')

    aa=random.randint(1,8)
    bb=random.randint(1,8)
    cc=random.randint(10,18)
    dd=random.randint(10,18)
    ee=random.randint(-9,-1)
    ff=random.randint(1,8)
    gg=random.randint(-18,-10)
    hh=random.randint(10,18)
    ii=random.randint(0,5)
    jj=random.randint(-8,9)
    kk=random.randint(0,9)
    k=random.randint(-18,18)

    saa=str(aa)
    sbb=str(bb)
    scc=str(cc)
    sdd=str(dd)
    see=str(ee)
    sff=str(ff)
    sgg=str(gg)
    shh=str(hh)
    sii=str(hh)
    sjj=str(ee)
    skk=str(ff)
    sll=str(gg)
    
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

    f.write('\\item $f('+v+')='+ms+' |'+v+'|$ \n ')
    FILL(f)

    f.write('\\item $f('+v+')=('+cs+v+'+'+ds+')^2+'+gs+ '$ \n ')
    FILL(f)

    f.write('\\end{enumerate}\n')
    
    f.write('\\newpage\n')

    f.write('\\item Solve for '+v+' graphically.  Sketch the graph, mark and state the solution(s). If no solution,write $\emptyset$ \n ')
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{50mm}\n')

    f.write('\\item $'+ds+v+'^2+'+bs+'x='+gs+'|'+v+'|-'+ks+'$\n ')

    f.write('\\item $\\sqrt{'+bs+v+'}='+ms+v+'-'+cs+'$\n ')

    f.write('\\item $-\\sqrt{'+cs+v+'}='+ds+v+'-'+gs+'$\n ')
    
    f.write('\\item $|'+v+'+'+cs+'|= '+v+'^2-'+gs+'$\n ')

    f.write('\\end{enumerate}\n\n')


    f.write('\\newpage\n')

    f.write('\\item Sketch a graph, calculate the slope, and write a point slope expression for a line that contians the two points show.\n ')
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{30mm}\n')

    f.write('\\item $('+see+','+sbb+'), ('+skk+','+sdd+')$\n ')
    
    f.write('\\item $('+see+','+sjj+'), ('+sgg+','+sll+')$\n ')
    
    f.write('\\end{enumerate}\n\n')

    f.write('\\item Solve for $'+v+'$ algebraically.\n ')
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{40mm}\n')

    f.write('\\item $'+bs+v+'-'+gs+'= '+ks+'$\n ')
    f.write('\\item $'+v+'+'+gs+'= '+ks+'$\n ')
    f.write('\\item $|'+v+'-'+bs+'|= '+gs+'$\n ')
    f.write('\\newpage\n')
    f.write('\\item $'+cs+'|'+v+'+'+gs+'|= '+es+'$\n ')

    f.write('\\end{enumerate}\n\n')

    f.write('\\item Write the following equations in matric form $A \\vec{x} =B$.\n ')
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{30mm}\n')

    f.write('\\item $'+v1+'+'+v2+'= 0$ \n\n $'+v1+'-'+v2+'= '+ks+'$\n')

    f.write('\\item $'+v1+'-'+v2+'= '+gs+'$ \n\n $'+bs +v1+'+'+v2+'= 0$\n')

    f.write('\\item $-'+v1+'+'+gs+v2+'= 0$ \n\n $'+v1+'-'+v2+'= '+bs+'$\n')
    
    f.write('\\item $'+v2+'+'+cs+v1+'= '+gs+'$ \n\n $' +v1+'-'+v2+'= 0$\n')
    f.write('\\end{enumerate}\n\n')
     

    f.write('\\item Write the expression for an absolute value function that is reflected and translated 4 units down the y-axis.\n ')
    
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
for x in range(1,50):
	WritePage(home,x)
