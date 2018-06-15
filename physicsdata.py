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
    f.write('\\begin{picture}(300,300)\n')
    f.write('\\put(30,5){\\grid(300,300)(10,10)}\n')
    f.write('\\end{picture}\n')
    f.write('}\n')
    f.write('\\begin{document}\n')
    f.write('\\title{AP Physics Quiz 7}\n')
    f.write('\\author{RH Cox}\n')
    f.write('\\date{DATE: 2015 January 6 }\n')
    f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

    
def PAGE(f,a):
    random.seed(a)
    t1=float(random.randint(15,25))/10
    t2=float(random.randint(35,45))/10
    t3=float(random.randint(55,65))/10
    t4=float(random.randint(75,85))/10
    t5=10
    t6=float(random.randint(103,106))/10

    t1s=str(t1)
    t2s=str(t2)
    t3s=str(t3)
    t4s=str(t4)
    t5s=str(t5)
    t6s=str(t6)

    error=float(random.randint(5,10))/100    
    v=float(random.randint(20,50))/10
    x5=float(random.randint(300,400))/100
    error=float(random.randint(90,110))/100    
    x4=x5+v*(t5-t4)*error
    error=float(random.randint(90,110))/100    
    x3=x4+v*(t4-t3)*error
    error=float(random.randint(90,110))/100    
    x2=x3+v*(t3-t2)*error
    error=float(random.randint(90,110))/100    
    x1=x2+v*(t2-t1)*error
    error=float(random.randint(90,110))/100    
    x0=x1+v*(t1)*error

    x5s=str(round(x5,1))
    x4s=str(round(x4,1))
    x3s=str(round(x3,1))
    x2s=str(round(x2,1))
    x1s=str(round(x1,1))
    x0s=str(round(x0,1))

    mass=float(random.randint(200,400))/10    
    smass=str(round(mass,1))    
        
    f.write('\\begin{tabular} {|p{2cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|} \n')
    f.write('\\hline \n')
    f.write('Time[s] & 0 &'+t1s+'&'+t2s+'&'+t3s+'&'+t4s+'&'+t5s+'&'+t6s+'\\\ \n')
    f.write('\\hline \n')
    f.write('Speed[$\\frac{m}{s}$] &'+x0s+'&'+x1s+'&'+x2s+'&'+x3s+'&'+x4s+'&'+x5s+'& 0  \\\ \n')
    f.write('\\hline \n\n')
    f.write('\\end{tabular} \n')

    f.write('\n A '+smass+'kg cart is traveling down a staight flat track. \n')
    f.write('The speed of the cart for certain times between 0 and 10 seconds are listed, as the cart slows due to friction. \n')
    f.write('At 10 seconds, brakes are applied and the car stops at '+t6s+'s as shown in the table \n')
    f.write('Answer the following question based on the data in the table. \n \n')
    
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{4cm}\n')

    f.write('\\item Draw a free body diagram of the cart on track')

    f.write('\\item On the grid, plot the data from 0-10 seconds, labeling and scaling the axis, as a scatter plot \n')
    
    f.write('\\item Using the slope of the best fit line, calculate the average acceleration of the cart between 0-10 seconds. \n')

    f.write('\\item Using the data in the table, calculate the average aceeleration between 10s and '+t6s+'s. \n')

    f.write('\\item Consider the data on the scatterplot.  Does a data point seem to have more error than the others, or do they all seem to have the same random error? \n')

    f.write('\\item Calculate the momentum of the cart at 10s. \n')

    f.write('\\item Calculate the momentum of the cart at '+t6s+'s. \n')

    f.write('\\item Calculate the impulse of the cart between 10s and '+t6s+'s. \n')

    f.write('\\newpage')
    f.write('\n \\gridpaper \n \n')
    f.write('\\newpage')

    f.write('\\item Calculate the kinetic energy of the cart at 10s. \n')


    f.write('\\item Calculate the energy converted to heat between 10s and '+t6s+'s. \n')

    f.write('\\item Suppose the straight track was attached to a ramp. The car is started at the top of the ramp, from rest, and allowed to accelerate. What would the minimum height of the ramp have to be  to achieve the speed listed in the table at time 0.')

    f.write('\\item Calcuate the distance the car travels between 0 and 10 seconds using the average acceleration calcualted from the graph')

    
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
