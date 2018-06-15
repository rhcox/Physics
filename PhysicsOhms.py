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
    f.write('\\begin{picture}(200,200)\n')
    f.write('\\put(30,5){\\grid(200,200)(10,10)}\n')
    f.write('\\end{picture}\n')
    f.write('}\n')
    f.write('\\begin{document}\n')
    f.write('\\title{Physics Test Six Weeks 6}\n')
    f.write('\\author{RH Cox}\n')
    f.write('\\date{DATE: 2017 April 28-Test Due at end of class or no credit }\n')
    f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

    
def PAGE(f,a):
    random.seed(a)
    v1=float(random.randint(30,60))/10
    v2=float(random.randint(70,100))/10
    v3=float(random.randint(110,140))/10
    v4=float(random.randint(150,180))/10

    v1s=str(v1)
    v2s=str(v2)
    v3s=str(v3)
    v4s=str(v4)
    
    R=random.randint(20000,50000)
    R1=float(R)   
    Rs=str(R/400)    


    i1=float(v1)/(R1/1000)
    i2=float(v2)/(R1/1000)
    i3=float(v3)/(R1/1000)
    i4=float(v4)/(R1/1000)

    errorA=1+float(random.randint(7,12))/100    
    errorB=1+float(random.randint(2,8))/100    
    errorC=1+float(random.randint(3,12))/100
    errorD=1+float(random.randint(5,8))/100
        
    i1e=str(round(i1*errorA,2))
    i2e=str(round(i2*errorB,2))
    i3e=str(round(i3*errorC,2))
    i4e=str(round(i4*errorC,2))
        
    f.write('\\begin{tabular} {|p{3cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|} \n')
    f.write('\\hline \n')
    f.write('Voltage[v] &'+v1s+'&'+v2s+'&'+v3s+'&'+v4s+'\\\ \n')
    f.write('\\hline \n')
    f.write('Current [mA] &'+i1e+'&'+i2e+'&'+i3e+'&'+i4e+'\\\ \n')
    f.write('\\hline \n\n')
    f.write('\\end{tabular} \n\n\n')
    
    f.write('\\gridpaper \n\n\n')

    f.write('\n You are gven a voltage source that produces 3-20 volts, one resistor, \n')
    f.write('and a meter that measures current.  The voltage source can be adjusted to a certain voltage and will display\n')
    f.write('the voltage on a screen. No other equipment can be used. Your taks is validate Ohms Law. \n')
    f.write('The current meter, resistor, and voltage source are connected in series. You will use the voltage and current \n')
    f.write('measurements to caluate the resistance and compare it to the known value of the resistor \n')
        
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{46mm}\n')
    
    f.write('\\newpage')
 
    f.write('\\item Describe your experimental procedure in enough detail so that another student could perform your experiment. Include what measurements you will take, what values you will use, and how you will use them.[10 pts]\n')
    

    f.write('\\item In a paragraph, write a procedure for use of this aparatus to measure the value of the resistor. Include how these measurement will be made accurately, and how they will be used to calculate the value of the resistor.[10 pts]\n')


    f.write('\\item Describe one assumption you made about the design of your experiment, and explain how it might affect the value obtained for the resistor.[10 pts]\n')
    
    f.write('\\item A student doing this experiment collected the data in the table. Graph the data on a well labeled and orgranized scatter plot in the grid provided.  Use a best line fit to calculate the value of the resistor. Show work on the graph including drawing and calculating the slope of the line fit.  Report the value of the resistor. You will take measurements at multiple voltages.[50 pts]\n')

    f.write('\\end{enumerate}\n')
    f.write(Rs+'\n')

    

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
