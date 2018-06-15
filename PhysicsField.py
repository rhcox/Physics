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
    f.write('\\title{AP Physics Quiz 2}\n')
    f.write('\\author{RH Cox}\n')
    f.write('\\date{DATE: 2015 September 25 }\n')
    f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

    
def PAGE(f,a):
    random.seed(a)
    t1=float(random.randint(15,25))/10
    t2=float(random.randint(35,45))/10
    t3=float(random.randint(55,65))/10
    t4=float(random.randint(75,85))/10
    t5=float(random.randint(95,105))/10
    t6=float(random.randint(115,125))/10

    t1s=str(t1)
    t2s=str(t2)
    t3s=str(t3)
    t4s=str(t4)
    t5s=str(t5)
    t6s=str(t6)

    error=float(random.randint(5,10))/100    
    v=float(random.randint(10,20))/10
    x6=float(random.randint(300,400))/100
    error=float(random.randint(90,110))/100
    x5=x6+v*(t6-t5)*error
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
    dtotal=int(x0)+10

    x6s=str(round(x6 ,1))
    x5s=str(round(x5,1))
    x4s=str(round(x4,1))
    x3s=str(round(x3,1))
    x2s=str(round(x2,1))
    x1s=str(round(x1,1))
    x0s=str(round(x0,1))
    sdtotal=str(dtotal)

    mass=float(random.randint(200,400))/10
    smass=str(round(mass,1))
    
    angle=random.randint(10,30)
    sangle=str(angle)

    f.write('\n Two students, a boy and girl, are standing at one corner of large, flat, empty, rectangular field. \n')
    f.write('The boy walks staight across the field diagonaly, the distance traveled measured every second or so for the first several seconds of his travels, and recorded in the table. \n')
    f.write('His total distance traveled to the opposite corner is, '+sdtotal+' meters diagonal at a $'+sangle+'^o$ angle to the side.\n')
    f.write('At the same time the boys starts, the girl begins to run around edge of the field until she reaches other side of the field at the same time as the boy. Based on this scenario and the data in the table, answer the questions below \n \n')

    
    f.write('\\begin{tabular} {|p{2cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|p{1.5cm}|} \n')
    f.write('\\hline \n')
    f.write('Time[s] &'+t1s+'&'+t2s+'&'+t3s+'&'+t4s+'&'+t5s+'&'+t6s+'\\\ \n')
    f.write('\\hline \n')
    f.write('position[m] &'+x6s+'&'+x5s+'&'+x4s+'&'+x3s+'&'+x2s+'&'+x1s+' \\\ \n')
    f.write('\\hline \n\n')
    f.write('\\end{tabular} \n')

    
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{25mm}\n')

    f.write('\\item Sketch a figure depicting the action in the scenario.. \n')
    
    f.write('\\item On the grid, plot the data for the boys walk as a scatter plot. Label and scale the axis. Draw a best line fit. Calculate the slope, State the meaning of the slope. Write an equation for the best line fit. \n')
    
    
    f.write('\\item Using the equation or the graph or the slope, estimate the time needed for the boy to reach the other side of the field. \n')

    f.write('\\newpage \n')
    
    f.write('\\item Estimate the speed the girl must run to reach the opposite corner at the same time as the boy as she runs around the edge of the field. \n')

    f.write('\\item In a paragraph length response, justify the claim that claim that both will reach the opposite corner of the field at the same time. Your claim is suppoerted by the the boy\'s constant speed, and the distance the girl travels. State how the evidence supports your claim based on the calculations you made.. \n')
    
    f.write('\\end{enumerate}\n')
    
    f.write('\\vspace{5cm}\n')

    f.write('\n \\gridpaper \n \n')
    

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
for x in range(1, 29):
	WritePage(home,x)
