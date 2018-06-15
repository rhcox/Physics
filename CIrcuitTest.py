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
    f.write('\\lfoot{Physics}\n')
    f.write('\\rfoot{Circuits Quiz '+str(n)+'}\n')
    f.write('\\renewcommand\headrule{\\vspace{-8pt}\dotfill}\n')
    f.write('\\newcommand{\\gridpaper}{\n')
    f.write('\\begin{picture}(50,50)\n')
    f.write('\\put(30,5){\\grid(80,100)(10,10)}\n')
    f.write('\\end{picture}\n')
    f.write('}\n')
    f.write('\\begin{document}\n')
    f.write('\\title{Circuits Quiz}\n')
    f.write('\\author{RH Cox}\n')
    f.write('\\date{DATE: }\n')
    f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

    
def PAGE(f,a):
    random.seed(a)

    v=str(random.randint(10,50))
    r1=str(random.randint(10,200))
    r2=str(random.randint(100,300))
    r3=str(random.randint(10,100))
    r4=str(random.randint(10,99))
    r5=str(random.randint(10,100))
    r6=str(random.randint(10,99))
    r7=str(random.randint(10,100))
    r8=str(random.randint(10,99))

    
    f.write('1.Calculate potential and current.\n\n')
    f.write('\\begin{circuitikz}\draw\n')
    f.write('(0,0)to[battery=$'+v+'v$] (0,3)\n')
    f.write('(4,0) to [R=$78\ \Omega$,-*] (4,3)\n')
    f.write('(0,0)to[short] (4,0)\n')
    f.write('(0,3)to[short] (4,3)\n')
    f.write(';\n')
    f.write('\\end{circuitikz}\n')
    f.write('\\vspace{3cm}\n\n\n')

    
    v=str(random.randint(10,50))
    f.write('2.Draw equivalent circuit, calculate all currents and voltages.\n\n')
    f.write('\\begin{circuitikz}\draw\n')
    f.write('(0,0)to[battery=$'+v+'v$] (0,3)\n')
    f.write('(0,3) to [R=$'+r1+'\ \Omega$,-*] (6,3)\n')
    f.write('(6,0) to [R=$'+r2+'\ \Omega$,-*] (6,3)\n')
    f.write('(0,0)to[short] (6,0)\n')
    f.write(';\n')
    f.write('\\end{circuitikz}\n')

    f.write('\\newpage \n\n')

    
    f.write('3.Draw equivalent circuit, calculate all currents and voltages.\n\n')
    v=str(random.randint(10,50))
    f.write('\\begin{circuitikz}\draw\n')
    f.write('(0,0)to[battery=$'+v+'v$] (0,4)\n')
    f.write('(4,0) to [R=$'+r3+'\ \Omega$,-*] (4,4)\n')
    f.write('(8,0) to [R=$'+r4+'\ \Omega$,-*] (8,4)\n')
    f.write('(0,0)to[short] (8,0)\n')
    f.write('(0,4)to[short] (8,4)\n')
    f.write(';\n')
    f.write('\\end{circuitikz}\n')
    f.write('\\vspace{4cm}\n\n\n')



    f.write('4.Draw equivalent circuits, calculate all currents and voltages.\n\n')
    v=str(random.randint(10,50))
    f.write('\\begin{circuitikz}\draw\n')
    f.write('(0,0)to[battery=$'+v+'v$] (0,4)\n')
    f.write('(0,4) to [R=$'+r5+'\ \Omega$,-*] (4,4)\n')
    f.write('(4,0) to [R=$'+r6+'\ \Omega$,-*] (4,4)\n')
    f.write('(8,0) to [R=$'+r7+'\ \Omega$,-*] (8,4)\n')
    f.write('(0,0)to[short] (8,0)\n')
    f.write('(4,4)to[short] (8,4)  \n')
    f.write(';\n')
    f.write('\\end{circuitikz}\n')
    f.write('\\vspace{5cm}\n\n\n')

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
for x in range(1,101):
	WritePage(home,x)