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
	f.write('\\rfoot{Power Rule}\n')
	f.write('\\renewcommand\headrule{\\vspace{-8pt}\dotfill}\n')

	f.write('\\newcommand{\\gridpaper}{\n')
	f.write('\\begin{picture}(50,50)\n')
	f.write('\\put(30,5){\\grid(80,100)(10,10)}\n')
	f.write('\\end{picture}\n')
	f.write('}\n')
	f.write('\\begin{document}\n')
	f.write('\\title{Calculus Power Rule Quiz}\n')
	f.write('\\author{RH Cox}\n')
	f.write('\\date{DATE: }\n')
	f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

    
def PAGE(f,a):
	random.seed(a)
	f.write('\\begin{enumerate}\n')
	f.write('\\setlength{\\itemsep}{2cm}\n')
	v=random.choice(['2','3','4','5','6','7','8', '9'])
	f.write('\\item $\\frac{d}{dx} \\; x^{'+v+'}$ \n')
	v=random.choice(['2','3','4','5','6','7','8', '9'])
	w=str(round(random.random()*10,2))
	f.write('\\item $\\frac{d}{dx} \\; '+w+'x^{'+v+'}$\n')
	w=str(round(random.random()*10,2))	
	f.write('\\item $\\frac{d}{dx} \\; x^{'+w+'}$\n')
	f.write('\\item $\\frac{d}{dx} \\; x^{'+v+'}$\n')
	v=random.choice(['6','7','8', '9'])
	w=random.choice(['2','3','4','5'])
	c=str(round(random.random()*10,2))	
	f.write('\\item $\\frac{d}{dx} \\; x^{'+v+'}+x^{'+w+'}+'+c+'$\n')
	v=random.choice(['6','7','8', '9'])
	w=random.choice(['2','3','4','5'])
	c=str(round(random.random()*10,2))
	f.write('\\item $\\frac{d}{dx} \\; x^{-'+v+'}+x^{'+w+'}-'+c+'$\n')
	f.write('\\newpage \n')
	w=str(round(random.random()*10,2))	
	f.write('\\item $\\frac{d}{dx} \\; x^{-'+w+'}$\n')    
	v=str(random.randint(2,20))
	f.write('\\item $\\frac{d}{dx} \\; '+v+'\\sqrt{x}$\n')
	v=random.choice(['2','3','4','5','6','7','8', '9'])
	f.write('\\item $\\frac{d}{dx} \\; \\sqrt['+v+']{x}$\n')
	v=random.choice(['5','6','7','8', '9'])
	w=random.choice(['2','3','4'])
	f.write('\\item $\\frac{d}{dx} \\; \\sqrt['+v+']{x^{'+w+'}}$\n')
	f.write('\\item $\\frac{d}{dx} \\; \\frac{1}{x}$\n')
	v=str(random.randint(2,20))
	f.write('\\item $\\frac{d}{dx} \\; \\frac{1}{x^{'+v+'}}+x$\n')
	v=str(random.randint(2,20))
	w=str(round(random.random()*10,2))	
	x=str(random.randint(2,20))
	f.write('\\item $\\frac{d}{dx} \\; \\frac{'+w+'}{x^{'+v+'}}+x^{'+x+'}$\n')
	v=str(random.randint(2,6))
	w=str(round(random.random()*10,2))	
	x=str(random.randint(2,20))
	f.write('\\item $\\frac{d}{dx} \\; \\frac{1}{\\sqrt['+v+']{x}}+'+w+'x^{'+x+'}$\n')
	v=str(random.randint(2,6))
	w=str(round(random.random()*10,2))
	x=str(random.randint(8,15))
	f.write('\\item $\\frac{d}{dx} \\; \\frac{1}{\\sqrt['+v+']{x}} + \\frac{'+w+'}{x^{'+x+'}}$\n')

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
