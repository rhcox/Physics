import random
import subprocess
import os

def HEAD(f,nn):
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

    f.write('\\usepackage{tikz}\n')
    f.write('\\usepackage{circuitikz}\n')

    
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

    f.write('\\input xy\n')
    f.write('\\xyoption{all}\n')
    f.write('\\large\n')
    f.write('\\pagestyle{fancyplain}\n')

    f.write('\\lhead{Name:}\n')
    f.write('\\chead{Period:}\n')
    f.write('\\rhead{Physics-'+nn+'}\n')
    f.write('\\lfoot{ Furr HS }\n')
    f.write('\\rfoot{Show All Work}\n')

    f.write('\\renewcommand\headrule{\\vspace{-8pt}\dotfill}\n')

    f.write('\\newcommand{\\gridpaper}{\n')
    f.write('\\begin{picture}(50,50)\n')
    f.write('\\put(30,5){\\grid(80,100)(10,10)}\n')
    f.write('\\end{picture}\n')
    f.write('}\n')
    f.write('\\begin{document}\n')
    f.write('\\title{Physics Circuit Quiz}\n')
    f.write('\\author{Calculate, Draw and Solve the Equivelent Circuit}\n')
    f.write('\\date{DATE: }\n')
    f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

    
def PAGE(f,a):
    random.seed(a)
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{1cm}\n')
    
    volt=random.randint(10,50)
    volts=str(volt)
    volts=str(volt)

    
    R=random.randint(110,750)
    RS=str(R)

    
    R1=random.randint(1,9)
    R1P=random.choice(['k','M'])
    R1S=str(R1)+R1P

    R2=random.randint(10,50)
    R2P=random.choice(['k','M'])
    R2S=str(R2)+R2P
    
    R3=random.randint(500,999)
    R3S=str(R3)
    
    R4=random.randint(50,90)
    R4P=random.choice(['k','M'])
    R4S=str(R4)+R4P
    
    R5=random.randint(2,9)
    R5S=str(R5)

    R6=random.randint(10,50)
    R6S=str(R2)+'M'
    
    w=random.choice(['floor','table','sidewalk','lawn'])
    mass=str(random.randint(10,90))


    f.write('\\item { \n\n \\begin{circuitikz}\draw\n')
    f.write('(0,0)to[battery=$'+volts+'v$] (0,4)\n')
    f.write('(6,0) to [R=$'+RS+'\ \Omega$,-*] (6,4)\n')
    f.write('(0,0)to[short] (6,0)\n')
    f.write('(0,4)to[short] (6,4)\n')
    f.write(';\n\n \end{circuitikz} \n  }\n')
    
    f.write('\\item { \n\n \\begin{circuitikz}\draw\n')
    f.write('(0,0)to[battery=$'+volts+'v$] (0,4)\n')
    f.write('(6,0) to [R=$'+R1S+'\ \Omega$,-*] (6,4)\n')
    f.write('(0,0)to[short] (6,0)\n')
    f.write('(0,4)to[short] (6,4)\n')
    f.write(';\n\n \end{circuitikz} \n  }\n')

    f.write('\\item { \n\n \\begin{circuitikz}\draw\n')
    f.write('(0,0)to[battery=$'+volts+'v$] (0,4)\n')
    f.write('(0,4) to [R=$'+R1S+'\ \Omega$,-*] (3,4)\n')
    f.write('(6,0) to [R=$'+R2S+'\ \Omega$,-*] (6,4)\n')
    f.write('(0,0)to[short] (6,0)\n')
    f.write('(3,4)to[short] (6,4)\n')
    f.write(';\n\n \end{circuitikz} \n  }\n')

    
    f.write('\\item { \n\n \\begin{circuitikz}\draw\n')
    f.write('(0,0)to[battery=$'+volts+'v$] (0,4)\n')
    f.write('(0,4) to [R=$'+R1S+'\ \Omega$,-*] (3,4)\n')
    f.write('(6,0) to [R=$'+R2S+'\ \Omega$,-*] (6,4)\n')
    f.write('(3,0) to [R=$'+R3S+'\ \Omega$,-*] (6,0)\n')
    f.write('(0,0)to[short] (3,0)\n')
    f.write('(3,4)to[short] (6,4)\n')
    f.write(';\n\n \end{circuitikz} \n  }\n')


    f.write('\\item { \n\n \\begin{circuitikz}\draw\n')
    f.write('(0,0)to[battery=$'+volts+'v$] (0,4)\n')
    f.write('(3,4) to [R=$'+R6S+'\ \Omega$,-*] (3,0)\n')
    f.write('(6,4) to [R=$'+R5S+'\ \Omega$,-*] (6,0)\n')
    f.write('(0,0)to[short] (6,0)\n')
    f.write('(0,4)to[short] (6,4)\n')
    f.write(';\n\n \end{circuitikz} \n  }\n')


    f.write('\\item { \n\n \\begin{circuitikz}\draw\n')
    f.write('(0,0)to[battery=$'+volts+'v$] (0,4)\n')
    f.write('(3,4) to [R=$'+RS+'\ \Omega$,-*] (3,0)\n')
    f.write('(6,4) to [R=$'+RS+'\ \Omega$,-*] (6,0)\n')
    f.write('(0,0)to[short] (6,0)\n')
    f.write('(0,4)to[short] (6,4)\n')
    f.write(';\n\n \end{circuitikz} \n  }\n')
    
    f.write('\\item { \n\n \\begin{circuitikz}\draw\n')
    f.write('(0,0)to[battery=$'+volts+'v$] (0,4)\n')
    f.write('(3,4) to [R=$'+R1S+'\ \Omega$,-*] (3,0)\n')
    f.write('(6,4) to [R=$'+R2S+'\ \Omega$,-*] (6,0)\n')
    f.write('(9,4) to [R=$'+R4S+'\ \Omega$,-*] (9,0)\n')
    f.write('(0,0)to[short] (9,0)\n')
    f.write('(0,4)to[short] (9,4)\n')
    f.write(';\n\n \end{circuitikz} \n  }\n')

    

    f.write('\\end{enumerate}\n')

    

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
for x in range(1, 200):
	WritePage(home,x)
