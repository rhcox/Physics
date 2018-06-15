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
	f.write('\\title{Physics Quiz 4}\n')
	f.write('\\author{RH Cox}\n')
	f.write('\\date{DATE: 2015 October 26}\n')
	f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

    
def PAGE(f,a):
    random.seed(a)
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{7cm}\n')
    
    v=random.choice(['box','book','crate', 'mushroom'])
    w=random.choice(['floor','table','sidewalk','lawn'])
    mass=str(random.randint(10,90))
    f.write('\\item A '+mass+' kg '+v+' is on a '+w+'.  Sketch the weight and normal force for this situation.  Sketch the free body diagram.  Calculate the weight and normal force.\n')
    

    mass=str(random.randint(2,90))
    angle=str(random.randint(5,40))
    f.write('\\item A '+mass+' kg mass is motionless on an inclined plane at an angle of '+angle+'$^0$. Sketch the weight and normal force for this situation.  Sketch the free body diagram.  Calculate the weight and normal force.\n')



    w=random.choice(['dog','cat','ferret','llama'])
    speed=str(random.randint(2,15))
    time=str(random.randint(10,60))
    f.write('\\item A '+w+' is running at '+speed+'$\\frac{m}{s}$.  If it runs for '+time+' seconds in a straight line.  Cacluate the displacement.\n')


    w=random.choice(['car','truck','moped','skateboard'])
    speed=str(random.randint(2,15))
    d=str(random.randint(100,500))
    f.write('\\item A '+w+' is racing down a '+d+'m steet at '+speed+'$\\frac{m}{s}$.  How long does it take to get to the end of the street.\n')

    ww=random.choice(['book','block','eraser','mass'])
    amass=str(random.randint(3,12))
    d=str(random.randint(100,500))
    f.write('\\item Calculate the frictional force and coeffecient of static friction on a '+ww+' resting on an inclined plane at $'+angle+'^0$. The '+ww+' is '+amass+' kg.\n')
    
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
for x in range(1, 100):
	WritePage(home,x)
