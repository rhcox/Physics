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
	f.write('\\lfoot{Furr HS }\n')
	f.write('\\rfoot{Show All Work}\n')
	f.write('\\renewcommand\headrule{\\vspace{-8pt}\dotfill}\n')

	f.write('\\newcommand{\\gridpaper}{\n')
	f.write('\\begin{picture}(50,50)\n')
	f.write('\\put(30,5){\\grid(80,100)(10,10)}\n')
	f.write('\\end{picture}\n')
	f.write('}\n')
	f.write('\\begin{document}\n')
	f.write('\\title{AP Physics Final}\n')
	f.write('\\author{RH Cox}\n')
	f.write('\\date{DATE: Fall 2014  }\n')
	f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

    
def PAGE(f,a):
    random.seed(a)
    loss=float(random.randint(40,80))/100
    MassCar=float(random.randint(20,120))/100
    SMassCar=str(MassCar)
    HeightTrack=float(random.randint(100,300))/100
    SHeightTrack=str(HeightTrack)
    HeightTable=float(random.randint(200,400))/100
    SHeightTable=str(HeightTable)
    HeightTable=float(random.randint(200,400))/100
    SHeightTable=str(HeightTable)
    PosFloor=round(math.sqrt(2*HeightTrack*HeightTable)*loss,2)
    SPosFloor=str(PosFloor)
    f.write(' A track is set up so that the top of the track is '+SHeightTrack+'m above a table.  The bottom of the track is at the level of the table.  The top and bottom of the track are horizontal. A '+SMassCar+'kg car is set on the top of track and allowed to accelerate down the track from rest. When the car reaches the end of the track, it rolls horizontally off the track and is allowed to fall freely to the floor, '+SHeightTable+'m below the table. The car hits the floor '+SPosFloor+'m away from the edge of the track. Use $g=10\\frac{m}{s}$. \n')
    
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{5cm}\n')

    f.write(' \\item Sketch this scenario with all values shown. Show the calculations of the weight and normal force assuming the car is resing on a horizontal surface at the top of the track.\n')
   
    f.write(' \\item Assuming friction, draw 4 freebody diagrams indicating the car a rest at the top of the track, the car accelerating down the track, the car off the track falling to the floor,and the car at rest on the floor. Label on the position of each A, B, C, and D on the sketch above. Label all forces with the name and value where appropriate. \n')

    f.write('\\newpage\n\n')

    f.write(' \\item Assuming NO friction, draw a freebody diagram indicating the car a rest at the top of the track, the car accelerating down the track, the car off the track falling to the floor,and the car at rest on the floor. Label on the position of each A, B, C, and D on the sketch above. Label all forces. \n')

    f.write(' \\item Calculate the potential energy of the car at the top of the track relative to the table. \n')

    f.write(' \\item Calculate the potential energy of the car at the top of the track relative to the floor. \n')

    f.write(' \\item Assuming no friction, calculate the expected kinetic of the car as just as it leave the track. \n')

    f.write('\\newpage\n\n')

    f.write(' \\item Assuming no friction, calculate the expected speed of the car as just as it leave the track. \n')

    f.write(' \\item Calculate the work done by gravity as the car moves from the top of the track to the end of the track.\n')

    f.write(' \\item Calculate the work done by gravity as the car moves from the top of the track to the end of the floor.\n')

    f.write(' \\item Calculate the work done against gravity if you were to lift the car from the floor back to the top of the track.\n')


    f.write('\\newpage\n\n')

    f.write(' \\item Assuming no friction, Calculate the momentum of the car as it leaves the track.\n')


    PHeightTrack=round(HeightTrack*(loss/2),1)
    SPHeightTrack=str(PHeightTrack)
    
    f.write(' \\item Assuming no friction, Calculate the kinetic energy of the car when it is '+SPHeightTrack+'m above the bottom of the track. \n')

    f.write(' \\item Calculate the time the car takes to fall from the edge of the track to the floor. \n')

    f.write(' \\item As stated, The car hits the floor '+SPosFloor+'m from the edge of the track.  Using this value, calculate the horizontal speed of the car as it left the track. \n')

    f.write(' \\item Using the speed above, calculate the actual kinetic energy the car has when it just leaves the track. \n')

    f.write(' \\item Using the kinetic energy above, calculate the energy lost to heat as the car traveled down th track. \n')

    f.write(' \\item Assuming that the direction of the car as it leaves the ramp is only horizontal,calculate the vertical speed of the car just before it hit the floor. \n')

    f.write(' \\item Using the horizontal and vertical speed calculated above, and assuming the horizontal speed remains constant, calculate the total speed of the car just before it hits the floor. \n')

    f.write(' \\item Using the total speed calculated above, calculate the total momentum of the car just before it hits the floor. \n')

    NMassCar=round(MassCar*loss,1)
    SNMassCar=str(NMassCar)
    
    f.write(' \\item Suppose the car breaks into two pieces when it hits the floor.  One piece slides horizontally across the floor while the other piece, '+SNMassCar+'kg, bounces straight up vertically in the air. Calculate the speed of the part of the car that bounces into the air . \n')

    NewTime=float(random.randint(40,98))/100
    SNewTime=str(NewTime)

    f.write(' \\item Suppose another student did this experiment on a different table and forgot to measure the height of the table.  The student, however, did use a photogate to determine the time it took the car to travel from the table to the floor as '+SNewTime+'s.  Calculate the height of the table from this data. \n')

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
import math
home = expanduser("~")
for x in range(1, 2):
	WritePage(home,x)
