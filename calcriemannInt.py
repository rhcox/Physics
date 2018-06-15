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
	f.write('\\lfoot{ Calculus}\n')
	f.write('\\rfoot{Product Rule}\n')
	f.write('\\renewcommand\headrule{\\vspace{-8pt}\dotfill}\n')

	f.write('\\newcommand{\\gridpaper}{\n')
	f.write('\\begin{picture}(50,50)\n')
	f.write('\\put(30,5){\\grid(80,100)(10,10)}\n')
	f.write('\\end{picture}\n')
	f.write('}\n')
	f.write('\\begin{document}\n')
	f.write('\\title{Calculus Integration Quiz Reimann Sum Addendum}\n')
	f.write('\\author{RH Cox}\n')
	f.write('\\date{DATE: }\n')
	f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

    
def PAGE(f,a):
    random.seed(a)
    
    t1=str(random.randint(10,25))
    t2=str(random.randint(30,45))
    t3=str(random.randint(50,65))
    t4=str(random.randint(70,95))
    t5=str(random.randint(100,115))
    t6=str(random.randint(120,135))
    t7=str(random.randint(140,155))
    t8=str(random.randint(160,175))
    t9=str(random.randint(180,195))

    v1=str((float(random.randint(20,40)))/10)
    v2=str((float(random.randint(60,100)))/10)
    v3=str((float(random.randint(30,50)))/10)
    v4=str((float(random.randint(-30,-10)))/10)
    v5=str((float(random.randint(-70,-50)))/10)
    v6=str((float(random.randint(-40,-10)))/10)
    v7=str((float(random.randint(10,30)))/10)
    v8=str((float(random.randint(40,80)))/10)
    v9=str((float(random.randint(100,120)))/10)


    f.write('\\begin{tabular} {|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}|p{1cm}| } \n')
    f.write('\\hline \n')
    f.write('time[s] & '+t1+' & '+t2+' & '+t3+' & '+t4+' & '+t5+' & '+t6+' & '+t7+' & '+t8+' & '+t9+' \\\ \n')
    f.write('\hline \n')
    f.write ('v [$\\frac{m}{s}$n] &'+v1+'&'+v2+'&'+v3+'&'+v4+'&'+v5+'&'+v6+'&'+v7+'&'+v8+'&'+v9+'\\\ \n')
    f.write('\hline \n')
    f.write('\\end{tabular} \n')

    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{3cm}\n')
    
    f.write('\\item Caculate the right hand Reimann Sum \n')
    
    f.write('\\item Caculate the left hand Reimann Sum \n')

    f.write('\\item Caculate the midpoint Reimann Sum \n')

    f.write('\\item Caculate the trapezoidal Reimann Sum \n')
    


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
for x in range(1, 25):
	WritePage(home,x)
