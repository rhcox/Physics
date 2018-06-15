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
    f.write('\\title{AP Physics Quiz 8}\n')
    f.write('\\author{RH Cox}\n')
    f.write('\\date{DATE: 2015 March 5 }\n')
    f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

    
def PAGE(f,a):
    random.seed(a)
    f1=float(random.randint(300,400))
    f2=float(random.randint(600,700))
    f3=float(random.randint(800,900))
    f4=float(random.randint(1000,1100))

    f1s=str(f1)
    f2s=str(f2)
    f3s=str(f3)
    f4s=str(f4)
    
    rate=float(random.randint(50,250))/100    
    srate=str(round(rate,1))

    speed=float(random.randint(320,360))    
    sspeed=str(speed)    
    speed1=float(random.randint(361,400))    

    w1=speed1*100/f1/4
    w2=speed1*100/f2/4
    w3=speed1*100/f3/4
    w4=speed1*100/f4/4

    errorA=1+float(random.randint(7,12))/100    
    errorB=1+float(random.randint(2,8))/100    
    errorC=1+float(random.randint(3,12))/100
        
    w1a=str(round(w1*errorA,1))
    w1b=str(round(w1*errorB,1))
    w1c=str(round(w1*errorC,1))

    w2a=str(round(w2*errorA,1))
    w2b=str(round(w2*errorB,1))
    w2c=str(round(w2*errorC,1))

    w3a=str(round(w3*errorA,1))
    w3b=str(round(w3*errorB,1))
    w3c=str(round(w3*errorC,1))

    w4a=str(round(w4*errorA,1))
    w4b=str(round(w4*errorB,1))
    w4c=str(round(w4*errorC,1))

        
    f.write('\\begin{tabular} {|p{3cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|} \n')
    f.write('\\hline \n')
    f.write('Frequncy[Hz] &'+f1s+'&'+f2s+'&'+f3s+'&'+f4s+'\\\ \n')
    f.write('\\hline \n')
    f.write('Length [cm] &'+w1a+'&'+w2a+'&'+w3a+'&'+w4a+'\\\ \n')
    f.write('\\hline \n\n')
    f.write('Length [cm] &'+w1b+'&'+w2b+'&'+w3b+'&'+w4b+'\\\ \n')
    f.write('\\hline \n\n')
    f.write('Length [cm] &'+w1c+'&'+w2c+'&'+w3c+'&'+w4c+'\\\ \n')
    f.write('\\hline \n\n')
    f.write('\\end{tabular} \n\n\n')
    
    f.write('\\gridpaper \n\n\n')

    f.write('\n The speed of sound is to be measured using a glass cylinder filled with water. The tube is graduated \n')
    f.write('in cm, the top marked zero. The top of the cylinder has a holder for a tone generator.\n')
    f.write('The bottom of the cyliner is connected to a hose.  A pump is used to adjust the water level in the cyliner. \n')
    f.write('The pump changes the water level via the hose at '+srate+'mm/s. The water level can rise or fall using the pump. \n')
    f.write('For the experiment a tone of a known frequency is set at the top of the cyliner, and the water \n')
    f.write('level is adjusted until resonance is heard. The distance from the top of the cylinder is recorded.. \n')
    f.write('This is repeated a few times for each frequency. Several frequencies are used\n \n')
        
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{7cm}\n')
    
    f.write('\\newpage')
 
    f.write('\\item Draw this experimental setup. Include sufficient details.\n')
    

    f.write('\\item In a paragraph, write a procedure for use of this aparatus to measure the speed of sound. Include the number of measurements for each frequency you will acquire and how these measurement will be made accurately.\n')


    f.write('\\item In a pragraph, explain how to calculate the speed of sound using the data collected. Include figures and formulas as needed. Do not calculate the speed of sound.\n')
    
    f.write('\\item Suppose that you were to use frequencies of '+f1s+'hz, '+f2s+'hz, '+f3s+'hz, and '+f4s+'hz,as shown in the table, as the dependent variables for your measurement. Suppose the speed of sound is '+sspeed+'$\\frac{m}{s}$. Calculate the lengths from the top of the cylinder that would be expected assuming you were measuring quarter wavelengths. Do not use the length data in the table.\n')


    f.write('\\item Using the data in the table, calcuate and report the average and standard deviation of the lengths measured for each frequency. Graph these on the grid as a scatterplot with error bars.\n')
    
    f.write('\\newpage')

    f.write('\\item Assume for each measurement the cylinder starts completely full. Further assume that the water level is lowered at an even rate without interuption and stopped exactly when resonance is heard. Calculate the time it takes the water to reach the measured level for each frequency. Use the rate supplied in the original problem statement. You should use the average measurement for each frequency to calculate the average time.  .\n')

    f.write('\\item Suppose that instead of sound we used light and each average wavelength calculated above represented a wavelength of light. Using these wavelengths, calculate the corresponding frequency of light. Expresss the results using prefixes(T,k,G, etc), not scientific notion.\n')

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
