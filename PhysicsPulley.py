import random
import subprocess
import os
import math

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
    f.write('\\input xy\n')
    f.write('\\xyoption{all}\n')
    f.write('\\large\n')
    f.write('\\pagestyle{fancyplain}\n')
    f.write('\\lhead{Name:}\n')
    f.write('\\chead{Period:}\n')
    f.write('\\rhead{Physics-'+str(n)+'}\n')
    f.write('\\lfoot{ Furr}\n')
    f.write('\\rfoot{Show All Work}\n')
    f.write('\\renewcommand\headrule{\\vspace{-8pt}\dotfill}\n')
    f.write('\\newcommand{\\gridpaper}{\n')
    f.write('\\begin{picture}(180,180)\n')
    f.write('\\put(30,5){\\grid(180,180)(10,10)}\n')
    f.write('\\end{picture}\n')
    f.write('}\n')
    f.write('\\begin{document}\n')
    f.write('\\title{AP Physics Quiz 5}\n')
    f.write('\\author{RH Cox}\n')
    f.write('\\date{DATE: 2015 November 12 }\n')
    f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

    
def PAGE(f,a):
    random.seed(a)
    
    h=float(random.randint(11,21))/10
    hs=str(h)
    tfall=int(math.sqrt(2*h/9.8)*1000)
    tinc=tfall/20
    
    t1=random.randint(tinc,tinc*3)
    t2=random.randint(tinc*5,tinc*8)
    t3=random.randint(tinc*10,tinc*13)
    t4=random.randint(tinc*15,tinc*18)

    t1s=str(t1)
    t2s=str(t2)
    t3s=str(t3)
    t4s=str(t4)
    
    m1=str(random.randint(100,199))
    m2=str(random.randint(200,299))
    m3=str(random.randint(300,399))
    m4=str(random.randint(400,499))

    h1=0.5*9.8*t1*t1/1000000
    h2=0.5*9.8*t2*t2/1000000
    h3=0.5*9.8*t3*t3/1000000
    h4=0.5*9.8*t4*t4/1000000

    errorAp=1+float(random.randint(7,12))/100    
    errorAm=1-float(random.randint(7,12))/100    
    errorBp=1+float(random.randint(9,18))/100    
    errorBm=1-float(random.randint(9,18))/100    
    errorCp=1+float(random.randint(10,20))/100
    errorCm=1-float(random.randint(10,20))/100
    errorDp=1+float(random.randint(20,30))/100
    errorDm=1-float(random.randint(20,30))/100
        
    h1e=str(round(h1*errorAp,2))
    h2e=str(round(h2*errorAm,2))
    h3e=str(round(h3*errorAm,2))
    h4e=str(round(h4*errorAp,2))
        
    f.write('\\begin{tabular} {|p{3cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|} \n')
    f.write('\\hline \n')
    f.write('Time[ms] &'+t1s+'&'+t2s+'&'+t3s+'&'+t4s+'\\\ \n')
    f.write('\\hline \n')
    f.write(m1+'g Dist[m] &'+h1e+'&'+h2e+'&'+h3e+'&'+h4e+'\\\ \n')
    f.write('\\hline \n\n')
    
    h1e=str(round(h1*errorBm,2))
    h2e=str(round(h2*errorBp,2))
    h3e=str(round(h3*errorBp,2))
    h4e=str(round(h4*errorBm,2))    
    f.write(m2+'g Dist[m] &'+h1e+'&'+h2e+'&'+h3e+'&'+h4e+'\\\ \n')
    f.write('\\hline \n\n')

    h1e=str(round(h1*errorCp,2))
    h2e=str(round(h2*errorCm,2))
    h3e=str(round(h3*errorCp,2))
    h4e=str(round(h4*errorCm,2))    
    f.write(m3+'g Dist[m] &'+h1e+'&'+h2e+'&'+h3e+'&'+h4e+'\\\ \n')
    f.write('\\hline \n\n')
    
    h1e=str(round(h1*errorDm,2))
    h2e=str(round(h2*errorDp,2))
    h3e=str(round(h3*errorDm,2))
    h4e=str(round(h4*errorDp,2))
    f.write(m4+'g Dist[m] &'+h1e+'&'+h2e+'&'+h3e+'&'+h4e+'\\\ \n')
    f.write('\\hline \n\n')
    
    f.write('Average & & & &\\\ \n')
    f.write('\\hline \n\n')
    f.write('$\sigma$ & & & &\\\ \n')
    f.write('\\hline \n\n')
    
    f.write('\\end{tabular} \n\n\n')
    
    f.write('\\gridpaper \n\n\n')

    f.write('\n A student creates an experiment to determine if acceleration due to gravity of a falling object depends on mass. The student, \n')
    f.write('attaches a pully to the edge of table. The table is '+hs+'m above the floor. A string is placed over the pully. Tied to the string is a cup that can freely fall to the floor.\n')
    f.write('On the table tied to the other end of the string is a heavy block.  The bottom of the block and the table are very smooth so there is \n')
    f.write('neglible friction. Assume the pulley has negligle friction and mass. Assume the string has negligible mass. \n')
    f.write('Four different masses, as shown, are placed in the cup and the cup is released from rest and allowed to drop from the level of the table \n')
    f.write('to the floor. At the times show, the distance the block traveled is measured and recorded. \n')
        
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{39mm}\n')
    
    f.write('\\newpage')
 
    f.write('\\item Describe the motion of the block if acceleration due to gravity depended on mass. How would the data for each mass be simialir or different?\n')
    

    f.write('\\item Describe the motion of the block if acceleration due to gravity was independent of mass. How would the data for each mass be simialir or different?.\n')


    f.write('\\item Calculate the average and standard deviations. Record the values in the table .Graph the average using different colors for each mass. Graph the standard deviation as error bars.\n')
    
    f.write('\\item In a paragraph length response, state if the data supports the hypthosis that acceleration depends on mass.  Justify your answer by referencing the averages and standard deviations for distance traveled at each time. \n')

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
