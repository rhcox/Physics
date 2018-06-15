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
	f.write('\\title{Six Weeks Exam 6}\n')
	f.write('\\author{Physics}\n')
	f.write('\\date{DATE: }\n')
	f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

    
def PAGE(f,a):
    random.seed(a)
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{3cm}\n')

    
    shape=random.choice(['cocave ','convex '])
    mirror=random.choice(['lens','mirror'])
    outside=random.choice(['outside','inside'])
    f.write('\\item Draw an '+shape+ mirror+'. Draw an object '+outside+' of the focal point.  Sketch two principle rays and indicate the image.\n')

    
    angle=str(random.randint(5,30))
    n2=str(float(random.randint(11,27))/10)
    f.write('\\item A ray of light is incident at $'+angle+'^o$ to a surface.  The light travels from a medium with index of refraction n=1.0 to another medium index of refraction '+n2+'.  Calculate the refracted angle.\n')


    n1=str(float(random.randint(11,33))/10)
    f.write('\\item A ray of light is traveling from a medium with an index of refraction n='+n1+' to a medium index of refraction n=1.  Calculate the incident angle so that there is total internal reflection.\n')

    f.write('\\newpage')
    
    Battery=str(random.randint(5,19))
    R1=str(random.randint(20,100))
    f.write('\\item A resistor, value $'+R1+' \\Omega$ is connected to battery of $'+Battery+'V$.  Draw a sketch demonstrating such a circuit. Calculate the current.  Indicate the current on the circuit.\n')

    R2=str(random.randint(200,700))
    I1=str(float(random.randint(5,40))/100)
    f.write('\\item A resistor, value $'+R2+' \\Omega$ has a current of $'+I1+'A$ flowing through it.  Calculate the voltage across the resistor.\n')

    f.write('\\item Two resistors, value $'+R1+' \\Omega$ and $'+R2+' \Omega$  are in series.  Draw a sketch demonstrating such a circuit. Calculate the equivalent resistance.  Draw the equivalent circuit.\n')

    R3=str(random.randint(150,555))
    f.write('\\item Two resistors, value $'+R3+' \\Omega$ and $'+R3+'\\Omega$  are in parallel.  Draw a sketch demonstrating such a circuit. Calculate the equivalent resistance.  Draw the equivalent circuit.\n')

    REn=random.randint(30,60)
    Mult=random.randint(3,6)
    RE=str(REn)
    R4n=REn*Mult    
    R4=str(R4n)
    R5=str(random.randint(R4n*2,R4n*3))
    f.write('\\item For a circuit you need a resistance of $'+RE+' \Omega$ connected to a $5V$ battery. You only have resistors of $'+R4+' \\Omega$ and $55 \\Omega$, along with a $'+Battery+'V$ battery.  Sketch the circuit that would be equivalent to the desired circuit using only the available resistors.\n')


   

    
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
for x in range(1, 100):
	WritePage(home,x)
