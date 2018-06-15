import random
import subprocess
import os
import time

def HEAD(f,n):
    f.write('\\documentclass[12pt]{article}\n')
    f.write('\\pdfpagewidth 8.5in\n')
    f.write('\\pdfpageheight 11in\n')
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
    f.write('\\usepackage{geometry}\n')
    f.write('\\geometry{letterpaper,textwidth=175mm,textheight=24cm,left=20mm,top=20mm}\n')
    f.write('\\input xy\n')
    f.write('\\xyoption{all}\n')
    f.write('\\large\n')
    f.write('\\pagestyle{fancyplain}\n')
    f.write('\\lhead{Name:}\n')
    f.write('\\chead{Date:}\n')
    f.write('\\rhead{Period}\n')
    f.write('\\lfoot{ Construction Tech-'+n+'}\n')
    f.write('\\rfoot{RH Cox}\n')

    f.write('\\newcommand{\GUESS}[1]\n')
    f.write('{\n')
    f.write('\\item #1\n\n')
    f.write('\\setlength\extrarowheight{ 5 mm}\n')
    f.write('\\begin{tabular} {| p{25mm} | p{6cm} | p{7cm} |}\n')
    f.write('\\hline\n')
    f.write(' Given		&	 	&  Picture and Process \\\\ \n')
    f.write('\\hline\n')
    f.write('Unknowns 	&  	&  \\\\ \n')
    f.write('\\cline{1-2}\n')
    f.write('Equation 		&  	  &\\\\ \n')
    f.write('\\cline{1-2}\n')
    f.write('Solution 		&	  &	  \\\\ \n')
    f.write('\\hline\n')
    f.write('\\end{tabular}\n')
    f.write('}\n')

    f.write('\\newcommand{\\MPS}{\\, \\frac{m}{s}}\n')
    f.write('\\newcommand{\\MPSS}{\\, \\frac{m}{s^2}}\n')
    f.write('\\newcommand{\\kg}{\\, kg}\n')
    f.write('\\newcommand{\\meters}{\\, m}\n')

    f.write('\\newcommand{\\gridpaper}{\n')

    f.write('\\begin{picture}(50,50)\n')
    f.write('\\put(30,5){\\grid(80,100)(10,10)}\n')
    f.write('\\end{picture}\n')
    f.write('}\n')

    f.write('\\begin{document}\n')
    f.write('\\begin{center}\n')
    f.write('\\Large\n')
    f.write('\\bfseries\n')
    f.write('Estimate Cost of Carpet\n')
    f.write('\\end{center}\n')
    f.write('\\renewcommand\\labelenumi{\\Roman{enumi}.}\n')
    f.write('\\renewcommand\\labelenumii{\\Alph{enumii}.}\n')
    f.write('\\renewcommand\\labelenumiii{\\arabic{enumiii}.}\n')
    f.write('\\renewcommand\\labelenumiv{\\alph{enumiv}.}\n')
    f.write('\\normalsize\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

    
def PAGE(f,a):
    random.seed(a)


    f.write('\\begin{enumerate}\n')
    l1=str(int(random.randint(5,15)))
    w1=str(int(random.randint(5,15)))
    l2=str(int(random.randint(15,25)))
    w2=str(int(random.randint(15,25)))
    l3=str(int(random.randint(25,35)))
    w3=str(int(random.randint(25,35)))
    l4=str(int(random.randint(5,45)))
    w4=str(int(random.randint(5,45)))
    roll=str(int(random.randint(4,25)))
    cost=str(int(random.randint(40,80)))

    
    f.write('\\GUESS{A house needs carpet in three rooms. The first room is 10 by 13 feet, the second room is 8 by 11 feet, and the third room is 15 by 21 feet. Calculate the total area of carpet required.}\n')
    f.write('\\GUESS{A house needs carpet in three rooms. The first room is '+l1+' by '+w1+' feet, the second  room is '+l2+' by '+w2+' feet, and the third  room is '+l3+' by '+w3+' feet. Calculate the total area of carpet required.}\n')
    
    f.write('\\GUESS{A house needs carpet in three rooms. The first room is 10 by 13 feet, the second room is 8 by 11 feet, and the third room is 15 by 21 feet. Each roll of carpet covers 9 square feet. Calculate the minimum number of rolls required.}\n')
    f.write('\\GUESS{A house needs carpet in three rooms. The first room is '+l1+' by '+w1+' feet, the second  room is '+l2+' by '+w2+' feet, and the third  room is '+l3+' by '+w3+' feet. Each roll of carpet covers '+roll+' square feet. Calculate the minimum number of rolls required.}\n')

    f.write('\\newpage\n')
    
    f.write('\\GUESS{A house needs carpet in three rooms. The first room is 10 by 13 feet, the second room is 8 by 11 feet, and the third room is 15 by 21 feet. Each roll of carpet costs \$37. Calculate the minimum cost to purchase the required rolls.}\n')
    f.write('\\GUESS{A house needs carpet in three rooms. The first room is '+l1+' by '+w1+' feet, the second  room is '+l2+' by '+w2+' feet, and the third  room is '+l3+' by '+13+' feet. Each roll of carpet costs \$'+cost+'. Calculate the minimum cost to purchase the required rolls.}\n')

    f.write('\\GUESS{A house needs carpet in three rooms. The first room is 10 by 13 feet, the second room is 8 by 11 feet, and the third room is 15 by 21 feet.The client wants to add a fourth room that is 13 by 13 feet.  Using the numbers for this house, calculate new estimate.}\n')
    f.write('\\GUESS{A house needs carpet in three rooms. The first room is '+l1+' by '+w1+' feet, the second  room is '+l2+' by '+w2+' feet, and the third  room is '+l3+' by '+w3+' feet.The client wants to add a fourth room that is '+l4+' by '+w4+' feet.  Using the numbers for this house, calculate new estimate.}\n')

    f.write('\\end{enumerate}\n')

    

def WritePage(home,n):
    output=home+"/temp"
    nn=str(n)
    name=output+"/temp"+nn
    filename=name+".tex"
    logname=output+"/log.out"
    f=open(filename,'w')
    rnum=str(int(time.time()))

    HEAD(f,rnum)
    PAGE(f,rnum)
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
for x in range(1, 45):
	WritePage(home,x)
