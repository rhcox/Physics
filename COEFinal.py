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
    f.write('\\usepackage{tikz} \n')
    f.write('\\usepackage{circuitikz} \n')
    f.write('\\large\n')
    f.write('\\pagestyle{fancyplain}\n')
    f.write('\\lhead{Name:}\n')
    f.write('\\chead{Period:}\n')
    f.write('\\rhead{Furr HS}\n')
    f.write('\\lfoot{POE}\n')
    f.write('\\rfoot{COE Final '+str(n)+'}\n')
    f.write('\\renewcommand\headrule{\\vspace{-8pt}\dotfill}\n')
    f.write('\\newcommand{\\gridpaper}{\n')
    f.write('\\begin{picture}(50,50)\n')
    f.write('\\put(30,5){\\grid(80,100)(10,10)}\n')
    f.write('\\end{picture}\n')
    f.write('}\n')
    f.write('\\begin{document}\n')
    f.write('\\title{COE Final}\n')
    f.write('\\author{RH Cox}\n')
    f.write('\\date{DATE: }\n')
    f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

def EquivCirc(f):
    v=str(random.randint(4,15))
    r=str(random.randint(40,99))
    f.write('\\begin{circuitikz}\draw\n')
    f.write('(0,0)to[battery=$'+v+'v$] (0,3)\n')
    f.write('(6,3) to [R=$'+r+'\\Omega$,-*] (6,0)\n')
    f.write('(0,0)to[short] (6,0)\n')
    f.write('(0,3)to[short] (6,3)\n')
    f.write(';\n')
    f.write('\\end{circuitikz}\n')

def Series2(f):
    v=str(random.randint(3,10))
    r1=str(random.randint(200,500))
    r2=str(random.randint(600,999))
    f.write('\\begin{circuitikz}\draw\n')
    f.write('(0,0)to[battery=$'+v+'v$] (0,3)\n')
    f.write('(6,3) to [R=$'+r1+'\\Omega$,-*] (6,0)\n')
    f.write('(0,0)to[short] (2,0)\n')
    f.write('(2,0) to [R=$'+r2+'\\Omega$,-*] (6,0)\n')
    f.write('(0,3)to[short] (6,3)\n')
    f.write(';\n')
    f.write('\\end{circuitikz}\n')


def Series3(f):
    v=str(random.randint(3,10))
    r1=str(random.randint(200,500))
    r2=str(random.randint(600,999))
    r3=str(random.randint(1000,5000))
    f.write('\\begin{circuitikz}\draw\n')
    f.write('(0,0)to[battery=$'+v+'v$] (0,3)\n')
    f.write('(0,3) to [R=$'+r1+'\\Omega$,-*] (6,3)\n')
    f.write('(6,3) to [R=$'+r2+'\\Omega$,-*] (6,0)\n')
    f.write('(0,0) to [R=$'+r3+'\ \Omega$,-*] (6,0)')
    f.write(';\n')
    f.write('\\end{circuitikz}\n')

def Par2eq(f):
    v=str(random.randint(3,10))
    r1=str(random.randint(100,1000))
    f.write('\\begin{circuitikz}\draw\n')
    f.write('(0,0)to[battery=$'+v+'v$] (0,3)\n')
    f.write('(6,3) to [R=$'+r1+'\\Omega$,-*] (6,0)\n')
    f.write('(3,3) to [R=$'+r1+'\\Omega$,-*] (3,0)\n')
    f.write('(0,0)to[short] (6,0)\n')
    f.write('(0,3)to[short] (6,3)\n')
    f.write(';\n')
    f.write('\\end{circuitikz}\n')
    f.write('\\vspace{.5in}\n\n\n')

def Par2ne(f):
    v=str(random.randint(3,10))
    r1=str(random.randint(200,500))
    r2=str(random.randint(600,999))
    f.write('\\begin{circuitikz}\draw\n')
    f.write('(0,0)to[battery=$'+v+'v$] (0,3)\n')
    f.write('(6,3) to [R=$'+r1+'\\Omega$,-*] (6,0)\n')
    f.write('(3,3) to [R=$'+r2+'\\Omega$,-*] (3,0)\n')
    f.write('(0,0)to[short] (6,0)\n')
    f.write('(0,3)to[short] (6,3)\n')
    f.write(';\n')
    f.write('\\end{circuitikz}\n')
    f.write('\\vspace{.5in}\n\n\n')

def Par3eq(f):
    v=str(random.randint(3,10))
    r1=str(random.randint(100,1000))
    f.write('\\begin{circuitikz}\draw\n')
    f.write('(0,0)to[battery=$'+v+'v$] (0,3)\n')
    f.write('(6,3) to [R=$'+r1+'\\Omega$,-*] (6,0)\n')
    f.write('(4,3) to [R=$'+r1+'\\Omega$,-*] (4,0)\n')
    f.write('(2,3) to [R=$'+r1+'\\Omega$,-*] (2,0)\n')
    f.write('(0,0)to[short] (6,0)\n')
    f.write('(0,3)to[short] (6,3)\n')
    f.write(';\n')
    f.write('\\end{circuitikz}\n')


    
    
                   
def PAGE(f,a):

    f.write('I. Determine if the circuit is series or parallel, indicate.(1pt)\n\n')
    f.write('II. Draw schematic for equivalent circuit, label value for battery.(4pt)\n\n')
    f.write('III. State rule to calculate the equivalent resistance, substute, state equivalent resistance.(3pt)\n\n')
    f.write('IV. Write the equivalent resistor in the equivalent circuit.(3pt)\n\n')
    f.write('V. State rule used to calculate current, substitute, state current.(2pt)\n\n')
    f.write('VI. Write the current into both schematics.(2pt)\n\n')

    random.seed(a)

    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{2cm}\n')
    
    f.write('\\item ')
    EquivCirc(f)

    f.write('\\item ')
    Series2(f)

    f.write('\\item ')
    Par2eq(f)

    f.write('\\item ')
    Par3eq(f)

    f.write('\\item ')
    Series3(f)

    f.write('\\item ')
    Par2ne(f)


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
for x in range(1, 100):
	WritePage(home,x)
