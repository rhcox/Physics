import random
import subprocess
import os
import numpy as np
import scipy as spy

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
    f.write('\\rhead{Furr HS '+str(n)+'}\n')
    f.write('\\lfoot{POE}\n')
    f.write('\\rfoot{KVL'+str(n)+'}\n')
    f.write('\\renewcommand\headrule{\\vspace{-8pt}\dotfill}\n')
    f.write('\\newcommand{\\gridpaper}{\n')
    f.write('\\begin{picture}(50,50)\n')
    f.write('\\put(30,5){\\grid(80,100)(10,10)}\n')
    f.write('\\end{picture}\n')


    f.write('}\n')
    f.write('\\begin{document}\n')
    f.write('\\title{POE Matrix Operations}\n')
    f.write('\\author{RH Cox}\n')
    f.write('\\date{DATE: }\n')
    f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

def WSMatrix(f,a):
    nl='\\'+'\\'
    np.savetxt(f,a, fmt='%d', delimiter='&', newline=nl)

def WriteMatrix(f,a):
    f.write('$ \\left( \\begin{smallmatrix} ')
    WSMatrix(f,a)
    f.write(' \\end{smallmatrix} \\right)$')
    
def WMatrix(f,a,b,op):
    f.write('\\begin{tabular} { p{4cm}  p{1cm}  p{4cm}   p{1cm}  p{4cm} p{4cm} }')
    f.write('\n\n')
    WriteMatrix(f,a)
    f.write(' & '+ op + ' & ')
    WriteMatrix(f,b)
    f.write(' & =	&  &  \\\ ')
    f.write('\n\n')
    f.write('\\end{tabular}')
    f.write('\n\n')



    
def PAGE(f,a):
    f.write('\\Large')
    f.write('\n\n\n')
    random.seed(a)

    n1=random.randint(1,20)
    n2=random.randint(1,40)
    n3=random.randint(1,20)
    n4=random.randint(1,40)
    n5=random.randint(1,60)
    n6=random.randint(1,90)
    n7=random.randint(1,80)
    n8=random.randint(1,99)
    n9=random.randint(1,70)
    n10=random.randint(1,80)
    n11=random.randint(1,50)
    n12=random.randint(1,80)
    n13=random.randint(1,50)
    n14=random.randint(1,99)
    n15=random.randint(1,70)
    n16=random.randint(1,80)
    n17=random.randint(1,50)
    n18=random.randint(1,99)
    n19=random.randint(1,70)
    
    f.write('I.  Add or subtract each matrix.\n\n')
    a=np.mat([[n1,n2], [n3,n4]])
    b=np.mat([[n8,n7], [n6,n5]])
    op='+'
    WMatrix(f,a,b,op)


    a=np.mat([[n1,n2,n9], [n3,n4,n11]])
    b=np.mat([[n8,n7,n10], [n6,n5,n12]])
    op='+'
    WMatrix(f,a,b,op)

    a=np.mat([[n1,n2,n9], [n3,n4,n11], [n13,n16,n17] ] )
    b=np.mat([[n8,n7,n10], [n6,n5,n12], [n14,n15,n18]])
    op='+'
    WMatrix(f,a,b,op)

    a=np.mat([[n1,n2], [n3,n4]])
    b=np.mat([[n8,n7], [n6,n5]])
    op='-'
    WMatrix(f,a,b,op)

    a=np.mat([[n1,n2,n9], [n3,n4,n11]])
    b=np.mat([[n8,n7,n10], [n6,n5,n12]])
    op='-'
    WMatrix(f,a,b,op)

    a=np.mat([[n1,n2,n9], [n3,n4,n11], [n13,n16,n17] ] )
    b=np.mat([[n8,n7,n10], [n6,n5,n12], [n14,n15,n18]])
    op='-'
    WMatrix(f,a,b,op)


    
    f.write('II. multiply by a constant.\n\n')
    a=np.mat([[n1]])
    b=np.mat([[n8,n7,n10], [n6,n5,n12]])
    op='*'
    WMatrix(f,a,b,op)

    a=np.mat([[-1*n2]])
    b=np.mat([[n8,n7,n10], [n6,n5,n12]])
    op='*'
    WMatrix(f,a,b,op)


 


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
for x in range(1, 50):
	WritePage(home,x)
