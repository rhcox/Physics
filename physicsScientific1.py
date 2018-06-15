import random
import subprocess
import os

def variable():
    xx=str(random.choice('cdefghjkmnopqrstuvwxyz'))
    return xx
    
def HEAD(f,n):
    nn=str(n)
    f.write('\\documentclass[12pt,twocolumn]{article}\n')
    f.write('\\pdfpagewidth 8.5in\n')
    f.write('\\pdfpageheight 11in\n')
    f.write('\\setlength\\topmargin{0cm}\n')
    f.write('\\setlength\\headheight{20pt}\n')
    f.write('\\setlength\\headsep{.2in}\n')
    f.write('\\setlength\\textheight{8.5in}\n')
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
    f.write('\\rhead{Furr HS-'+nn+'}\n')
    f.write('\\lfoot{ Physics }\n')
    f.write('\\rfoot{Show All Work}\n')
    f.write('\\renewcommand\headrule{\\vspace{-8pt}\dotfill}\n')
    f.write('\\newcommand{\\gridpaper}{\n')
    f.write('\\begin{picture}(50,50)\n')
    f.write('\\put(30,5){\\grid(80,100)(10,10)}\n')
    f.write('\\end{picture}\n')
    f.write('}\n')
    f.write('\\begin{document}\n')
    f.write('\\title{Calculator Scientific Notation Quiz}\n')
    f.write('\\author{RH Cox}\n')
    f.write('\\date{DUE 2015 March 24- NO LATE PAPERS }\n')
    f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

    
def PAGE(f,a):
    random.seed(a)
    f.write('\\begin{enumerate}\n')
 
    f.write('\\item Add the values.')
    
    f.write('\\begin{enumerate}[(a)]\n')
    f.write('\\setlength{\\itemsep}{1.7cm}\n')

    a=str(random.randint(1,9))
    b=str(random.randint(1,9))
    nZero=random.randint(11,19)
    Zeros=str(nZero)
    Zero1s=str(nZero+random.randint(1,9))
    f.write('\\item $'+a+'X10^{'+Zeros+'}+'+b+'X10^{'+Zero1s+'}$\n')

    a=str(random.randint(1,9))
    b=str(random.randint(1,9))
    nZero=random.randint(11,19)
    Zeros=str(nZero)
    Zero1s=str(nZero+random.randint(1,9))
    f.write('\\item $'+a+'X10^{'+Zeros+'}-'+b+'X10^{'+Zero1s+'}$\n')

    a=str(random.randint(1,9))
    b=str(random.randint(1,9))
    c=str(random.randint(1,9))
    nZero=random.randint(11,19)
    Zeros=str(nZero)
    Zero1s=str(nZero+random.randint(1,9))
    f.write('\\item $'+a+'.'+c+'X10^{-'+Zeros+'}+'+b+'X10^{-'+Zero1s+'}$\n')

    a=str(random.randint(1,9))
    b=str(random.randint(1,9))
    c=str(random.randint(1,9))
    nZero=random.randint(11,19)
    Zeros=str(nZero)
    Zero1s=str(nZero+random.randint(1,9))
    f.write('\\item $'+a+'.'+c+'X10^{-'+Zeros+'}-'+b+'X10^{-'+Zero1s+'}$\n')
    
    f.write('\\end{enumerate}\n')
    
    f.write('\\vspace{1cm}.')


    f.write('\\item Multiply the values.')
    
    f.write('\\begin{enumerate}[(a)]\n')
    f.write('\\setlength{\\itemsep}{1.7cm}\n')
    
    a=str(random.randint(1,9))
    b=str(random.randint(1,9))
    nZeroa=random.randint(2,6)
    nZerob=random.randint(8,12)
    Zeroa=str(nZeroa)
    Zerob=str(nZerob)
    f.write('\\item $('+a+'X10^{'+Zeroa+'})('+b+'X10^{'+Zerob+'})$\n')
    
    a=str(random.randint(1,9))
    b=str(random.randint(1,9))
    nZeroa=random.randint(2,6)
    nZerob=random.randint(8,12)
    Zeroa=str(nZeroa)
    Zerob=str(nZerob)
    f.write('\\item $('+a+'X10^{-'+Zeroa+'})('+b+'X10^{'+Zerob+'})$\n')

    a=str(random.randint(1,9))
    b=str(random.randint(1,9))
    c=str(random.randint(1,9))
    nZeroa=random.randint(2,6)
    nZerob=random.randint(8,12)
    Zeroa=str(nZeroa)
    Zerob=str(nZerob)
    Zeros=str(nZero)
    f.write('\\item $('+a+'.'+c+'X10^{'+Zeroa+'})('+b+'X10^{-'+Zerob+'})$\n')


    a=str(random.randint(1,9))
    b=str(random.randint(1,9))
    c=str(random.randint(1,9))
    nZeroa=random.randint(2,6)
    nZerob=random.randint(8,12)
    Zeroa=str(nZeroa)
    Zerob=str(nZerob)
    Zeros=str(nZero)
    f.write('\\item $('+a+'.'+c+'X10^{-'+Zeroa+'})('+b+'X10^{-'+Zerob+'})$\n')


    f.write('\\end{enumerate}\n')


    f.write('\\vspace{1cm}.')
    f.write('\\item Divide the values.')
    
    f.write('\\begin{enumerate}[(a)]\n')
    f.write('\\setlength{\\itemsep}{1.7cm}\n')

    a=str(random.randint(1,9))
    b=str(random.randint(1,9))
    nZeroa=random.randint(2,6)
    nZerob=random.randint(8,12)
    Zeroa=str(nZeroa)
    Zerob=str(nZerob)
    f.write('\\item $ \\frac{'+a+'X10^{'+Zeroa+'}}{'+b+'X10^{'+Zerob+'}}$\n')

    a=str(random.randint(1,9))
    b=str(random.randint(1,9))
    nZeroa=random.randint(2,6)
    nZerob=random.randint(8,12)
    Zeroa=str(nZeroa)
    Zerob=str(nZerob)
    f.write('\\item $ \\frac{'+a+'X10^{-'+Zeroa+'}}{'+b+'X10^{'+Zerob+'}}$\n')

    a=str(random.randint(1,9))
    b=str(random.randint(1,9))
    nZeroa=random.randint(2,6)
    nZerob=random.randint(8,12)
    Zeroa=str(nZeroa)
    Zerob=str(nZerob)
    f.write('\\item $ \\frac{'+a+'X10^{'+Zeroa+'}}{'+b+'X10^{-'+Zerob+'}}$\n')

    a=str(random.randint(1,9))
    b=str(random.randint(1,9))
    c=str(random.randint(1,9))
    d=str(random.randint(1,9))
    nZeroa=random.randint(2,6)
    nZerob=random.randint(8,12)
    Zeroa=str(nZeroa)
    Zerob=str(nZerob)
    f.write('\\item $ \\frac{'+a+'.'+c+'X10^{'+Zeroa+'}}{'+b+'.'+d+'X10^{'+Zerob+'}}$\n')

    f.write('\\end{enumerate}\n')
    f.write('\\vspace{1cm}.')
    f.write('\\item Simplify the expression.')
    
    f.write('\\begin{enumerate}[(a)]\n')
    f.write('\\setlength{\\itemsep}{1.7cm}\n')
    
    a=str(random.randint(1,9))
    b=str(random.randint(2,4))
    nZeros=random.randint(2,6)
    Zeros=str(nZerob)
    f.write('\\item $('+a+'X10^{'+Zeroa+'})^{'+b+'}$\n')
 
    a=str(random.randint(1,9))
    b=str(random.randint(2,4))
    nZeros=random.randint(2,6)
    Zeros=str(nZerob)
    f.write('\\item $('+a+'X10^{-'+Zeroa+'})^{'+b+'}$\n')
    
    a=str(random.randint(1,9))
    b=str(random.randint(2,4))
    nZeros=random.randint(2,6)
    Zeros=str(nZerob)
    f.write('\\item $\\sqrt{'+a+'X10^{-'+Zeroa+'}}$\n')

    f.write('\\end{enumerate}\n')


    f.write('\\vspace{1cm}.')
    f.write('\\item Simplify.')

    f.write('\\begin{enumerate}[(a)]\n')
    f.write('\\setlength{\\itemsep}{3cm}\n')
    
    q1=str(-1*1.6)
    q2=str(2*1.6)
    r=str(random.randint(11,99)/10)
    nZeros=str(random.randint(2,6))
    f.write('\\item $9X10^9\\frac{('+q1+'X10^{-19} )( '+ q2+'X10^{-19})}{('+r+'X10^{-'+nZeros+'})^2}$\n')
 
    a=str(random.randint(11,99)/10)
    nZeros=str(random.randint(2,6))
    nZero1s=str(random.randint(2,6))
    m1=a+'X10^{'+nZeros+'}'
    m2=str(random.randint(1000,9000))
    r=str(random.randint(11,99)/10)
    f.write('\\item $6.7X10^{-11} \\frac{('+m1+' )( '+ m2+')}{('+r+'X10^{'+nZero1s+'})^2}$\n')
    

    q1=str(5*1.6)
    q2=str(-3*1.6)
    r=str(random.randint(11,99)/10)
    nZeros=str(random.randint(2,6))
    f.write('\\item $9X10^9\\frac{('+q1+'X10^{-19} )( '+ q2+'X10^{-19})}{('+r+'X10^{-'+nZeros+'})^2}$\n')
 
    a=str(random.randint(40,90)/10)
    nZeros=str(random.randint(3,7))
    nZero1s=str(random.randint(4,9))
    m1=a+'X10^{'+nZeros+'}'
    m2=str(random.randint(10000,19000))
    r=str(random.randint(11,80)/10)
    f.write('\\item $6.7X10^{-11} \\frac{('+m1+' )( '+ m2+')}{('+r+'X10^{'+nZero1s+'})^2}$\n')

    q1=str(-6*1.6)
    q2=str(-4*1.6)
    r=str(random.randint(20,40)/10)
    nZeros=str(random.randint(5,9))
    f.write('\\item $9X10^9\\frac{('+q1+'X10^{-19} )( '+ q2+'X10^{-19})}{('+r+'X10^{-'+nZeros+'})^2}$\n')
 
    a=str(random.randint(5,50)/10)
    nZeros=str(random.randint(2,9))
    nZero1s=str(random.randint(3,7))
    m1=a+'X10^{'+nZeros+'}'
    m2=str(random.randint(100,500))
    r=str(random.randint(20,60)/10)
    f.write('\\item $6.7X10^{-11} \\frac{('+m1+' )( '+ m2+')}{('+r+'X10^{'+nZero1s+')^2}}$\n')

    q2=str(6*1.6)
    r=str(random.randint(30,70)/10)
    nZeros=str(random.randint(3,6))
    f.write('\\item $9X10^9\\frac{'+ q2+'X10^{-19}}{('+r+'X10^{-'+nZeros+'})^2}$\n')
 
    a=str(random.randint(20,80)/10)
    nZeros=str(random.randint(2,9))
    nZero1s=str(random.randint(4,9))
    m1=a+'X10^{'+nZeros+'}'
    r=str(random.randint(20,60)/10)
    f.write('\\item $6.7X10^{-11} \\frac{'+m1+'}{('+r+'X10^{'+nZero1s+'})^2}$\n')

    q2=str(-4*1.6)
    r=str(random.randint(22,77)/10)
    nZeros=str(random.randint(6,10))
    f.write('\\item $9X10^9\\frac{'+ q2+'X10^{-19}}{('+r+'X10^{-'+nZeros+'})^2}$\n')
 
    a=str(random.randint(50,90)/10)
    nZeros=str(random.randint(2,9))
    nZero1s=str(random.randint(10,20))
    m1=a+'X10^{'+nZeros+'}'
    r=str(random.randint(20,60)/10)
    f.write('\\item $6.7X10^{-11} \\frac{'+m1+'}{('+r+'X10^{'+nZero1s+'})^2}$\n')

    q2=str(5*1.6)
    r=str(random.randint(5,25)/10)
    nZeros=str(random.randint(3,11))
    f.write('\\item $9X10^9\\frac{'+ q2+'X10^{-19}}{('+r+'X10^{-'+nZeros+'})^2}$\n')
 
    f.write('\\end{enumerate}\n')

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
for x in range(1, 25):
	WritePage(home,x)
