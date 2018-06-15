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

def WSMatrix(f,a, flag=0,prec=2):
    nl='\\'+'\\'
    if flag==0:
        np.savetxt(f,a, fmt='%d', delimiter='&', newline=nl)
    elif flag==1:
        np.savetxt(f,a, fmt='%s', delimiter='&', newline=nl)
    elif flag==2:
        s='%,'+str(prec)+'f'
        np.savetxt(f,a, fmt='%s', delimiter='&', newline=nl)
        
def WriteMatrix(f,a,flag=0):
    f.write('$ \\left( \\begin{smallmatrix} ')
    WSMatrix(f,a, flag)
    f.write(' \\end{smallmatrix} \\right)$')
    
def WMatrix(f,a,b,op,flag=0):
    f.write('\\begin{tabular} { p{4cm}  p{.5cm}  p{4cm}   p{.5cm}  p{4cm} p{5cm} }')
    f.write('\n\n')
    WriteMatrix(f,a)
    f.write(' & '+ op + ' & ')
    if flag==2:
        i=np.mat([["i_1"],["i_2"],["i_3"]])
        WriteMatrix(f,i,1)
        f.write(' & =	& ')
        WriteMatrix(f,b)        
        f.write(' &  ')
    else:
        WriteMatrix(f,b)
        f.write(' & =	&  &  ')
    if flag==0:
        f.write('\\\ ')
    elif flag==1:
        if op=='*':
            c=np.dot(a,b)
        elif op=='+':
            c=a+b
        elif op=='-':
            c=a-b
        else: 
            c=a.I
            c=dot(c,a)
        WriteMatrix(f,c)
        f.write(' \\\ ')
    f.write('\n\n')
    f.write('\\end{tabular}')
    f.write('\n\n')



    
def PAGE(f,a):
    f.write('\\Large')
    f.write('\n\n\n')
    random.seed(a)

    n1=random.randint(1,10)
    n2=random.randint(1,10)
    n3=random.randint(1,10)
    n4=random.randint(1,10)
    n5=random.randint(1,10)
    n6=random.randint(1,10)
    n7=random.randint(1,10)
    n8=random.randint(1,10)
    n9=random.randint(1,10)
    n10=random.randint(1,10)
    n11=random.randint(1,10)
    n12=random.randint(1,10)
    n13=random.randint(1,10)
    n14=random.randint(1,10)
    n15=random.randint(1,10)
    n16=random.randint(1,10)
    n17=random.randint(1,10)
    n18=random.randint(1,10)
    n19=random.randint(1,10)
    n20=random.randint(1,20)
    n21=random.randint(1,20)
    n22=random.randint(1,20)
    n23=random.randint(1,20)
    n24=random.randint(1,20)
    n25=random.randint(1,20)
    n26=random.randint(1,20)
    n27=random.randint(1,20)
    n28=random.randint(1,20)
    n29=random.randint(1,20)
    
    i1=float(random.randint(1,99))/100
    i2=float(random.randint(1,99))/100
    i3=float(random.randint(1,99))/100

    f.write('I.  Multiply each matrix by hand.\n\n')
    
    a=np.mat([[n1,n2], [n3,n4]])
    b=np.mat([[n8,n7], [n6,n5]])
    op='*'
    WMatrix(f,a,b,op,1)


    a=np.mat([[n9,n10], [n11,n12]])
    b=np.mat([[n16,n15], [n14,n13]])
    op='*'
    WMatrix(f,a,b,op,1)

    a=np.mat([[n1,n2], [n3,n4]])
    b=np.mat([[n8,n7,n10], [n6,n5,n12]])
    op='*'
    WMatrix(f,a,b,op,1)

    
    f.write('II.  Multiply each matrix by using the calculator.\n\n')

    a=np.mat([[n20,n21], [n23,n24]])
    b=np.mat([[n28,n27], [n26,n25]])
    op='*'
    WMatrix(f,a,b,op,1)

    
    a=np.mat([[n1,n2,n9], [n3,n4,n11], [n13,n16,n17] ] )
    b=np.mat([[n8,n7,n10], [n6,n5,n12], [n14,n15,n18]])
    op='*'
    WMatrix(f,a,b,op,0)


    a=np.mat([[n20,n21,n22], [n23,n24,n25], [n26,n27,n28] ] )
    b=np.mat([[n29,n1,n2], [n6,n5,n12], [n8,n9,n10]])
    op='*'
    WMatrix(f,a,b,op,0)


    a=np.mat([[n1,n2,n23, n27], [n3,n4,n24, n28], [n5,n6,n26, 0] ] )
    b=np.mat([[n29,n11,0, n12,], [n6,0, n5,n12], [0, n8,n9,n10], [0,n17, n18, 0]])
    op='*'
    WMatrix(f,a,b,op,0)
    
    f.write('\\newpage \n\n\n')
    
    f.write('III. solve each matrix.\n\n')
    a=np.mat([[n1,n2,n8], [n2,0,  n10], [0,n10, n11]])
    i=np.mat([[i1],[i2],[i3]])
    b=np.dot(a,i)
    op='*'
    WMatrix(f,a,b,op,2)
    f.write('$\\vec i = $')
    WriteMatrix(f,i,2)

    
    f.write('\\vspace{3cm} \n\n\n')

    a=np.mat([[n10,n20,n18], [n20,0,  n1], [0,n1, n18]])
    b=np.mat([[n12],[n13],[n14]])
    op='*'
    WMatrix(f,a,b,op,2)

    f.write('\\vspace{4cm} \n\n\n')

    a=np.mat([[n15,n20,0], [0,n18,  n15], [n20,n1, 0]])
    b=np.mat([[n12],[n13],[n14]])
    op='*'
    WMatrix(f,a,b,op,2)

 


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
