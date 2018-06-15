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
	f.write('\\title{Physics Final Exam}\n')
	f.write('\\author{No Credit if work is not completely and neatly shown.}\n')
	f.write('\\date{DATE: Fall 2016  }\n')
	f.write('\\maketitle\n')

    
def ENDMAT(f):
	f.write('\\end{document}\n')

    
def PAGE(f,a,N):
    random.seed(a)
    
    f.write('I. Three identical masses are dropped from the same height above a floor. Air resistance and friction is negligible.\n')
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{4mm}\n')
    f.write('\\item Mass A is dropped from rest so it falls straight down.\n')
    f.write('\\item Mass B is rolled off a table so that it has no vertical velocity and is allowed to fall to the floor.\n')
    f.write('\\item Mass C is slid down frictionaless inclined plane to the floor.\n')
    f.write('\\end{enumerate}\n')
    f.write('Rank the time elapsed, from longest to shortest, for the masses to reach the floor. Justify your answer in a complete sentence.\n')
    f.write('\\vspace{5cm}\n\n')


    f.write('II. Three identical masses are dropped from the same height above a floor. Air resistance and friction is negligible.\n')
    f.write('\\begin{enumerate}\n')
    f.write('\\item Mass A is dropped from rest so it falls straight down.\n')
    f.write('\\item Mass B is rolled off a table so that it has no vertical velocity and is allowed to fall to the floor.\n')
    f.write('\\item Mass C is slid down frictionaless inclined plane to the floor.\n')
    f.write('\\end{enumerate}\n')
    f.write('Rank the speed, from longest to shorted, for the masses as they reach the floor. Justify your answer in a complete sentence.\n')
    f.write('\\vspace{4cm}\n\n')

    f.write('III. A small box is being carried in the back of a truck.  The box is in the center of the truck bed. The back of the truck is smooth and is covered with oil from previous trip so any friction is negligible. The truck makes a right turn and the box moves. Draw a free body diagram of the forces on the box as the truck is turning.  State the direction the box will move, and explain, using physics words, why the box moves in the stated direction.\n')
    f.write('\\vspace{4cm}\n\n')

    f.write('IV.  A set of triplets are at the park.  The children have equal mass and are wearing the same clothes. They are on the top of three slides, a red slide, a blue slide, and  green slide.  The top of the slides are at equal height, and the bottoms are equal distance from the ground.  The friction and air resistance are negligible. The children start at the top, and slide to the bottom. Rank the speed of each child when exiting at the bottom of the slide. Explain in a sentence why the you rank the speeds in that order.\n')
    f.write('\\vspace{4cm}\n\n')

    f.write('V.  A set of triplets are at the park.  The children have equal mass and are wearing the same clothes. They are on the top of three slides, a red slide, a blue slide, and  green slide.  The top of the red slide is 2 m high, the top of the blue slide is 1.5 m high, and the top of the green slide is 1 m high.  Rank the weight of each child when at the top of each slide. Explain in a sentence why the you rank the speeds in that order.\n')
    f.write('\\vspace{4cm}\n\n')

    f.write('VI. A ball is tossed up in air, through a distance, until it lands on the ground some distance away.  Draw and clearly label a free body diagram of the ball as it leave the hand after being tossed, as it is at its highest pisition, and just before it lands on the ground.  For each postition, state the reletive horizontal and vertical speeds. Justify your diagrams and speed in a few complete sentences.\n')
    f.write('\\vspace{4cm}\n\n')

    Dis=float(random.randint(80,180))/100
    SDis=str(Dis)
    Time=float(random.randint(20,60))/100
    STime=str(Time)
    f.write('VII.  A students starts at the beginning of track from rest and sprint '+SDis+'m in '+STime+' seconds. Calculate the average acceleration. Show All WorkInclude units\n')
    f.write('\\vspace{4cm}\n\n')

    Dis1=float(random.randint(500,900))/100
    SDis1=str(Dis1)
    Dis2=float(random.randint(100,180))/100
    SDis2=str(Dis2)
    f.write('VIII. A ball is dropped straight down  from a height of '+SDis1+'m from rest.  It is allowed to fall under the acceleration of gravity. How fast is the ball traveling at '+SDis2+'m. Include units. Show All Work.\n')
    f.write('\\vspace{4cm}\n\n')

    Dis=float(random.randint(200,400))/100
    SDis=str(Dis)
    Time=float(random.randint(50,150))/100
    STime=str(Time)
    f.write('IX. A ball rolls horizontally off a table.  It lands '+ SDis +'m from the table in '+ STime +' s.  What is the horizontal speed of the ball when it left the table.  Air resistance and friction are negligible. Show All Work. Include units\n')
    f.write('\\vspace{4cm}\n\n')

    
    loss=float(random.randint(40,80))/100
    SLoss=str(loss)
    MassCar=float(random.randint(20,120))/100
    SMassCar=str(MassCar)
    AccCar=float(random.randint(10,90))/100
    SAccCar=str(AccCar)
    TCar=float(random.randint(50,120))/100
    STCar=str(TCar)
    HeightTrack=float(random.randint(100,300))/100
    SHeightTrack=str(HeightTrack)
    HeightTable=float(random.randint(200,400))/100
    SHeightTable=str(HeightTable)
    HeightTable=float(random.randint(200,400))/100
    SHeightTable=str(HeightTable)
    PosFloor=round(math.sqrt(2*HeightTrack*HeightTable)*loss,2)
    SPosFloor=str(PosFloor)
    f.write('X. A table is $'+SHeightTable+'m$ above the ground.  A toy car with a mass of $'+SMassCar+'kg$ is at rest on the table. For this scenario use $g=10\\frac{m}{s^2}$. \n')
    
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{5mm}\n')

    f.write(' \\item For the car at rest on the table.\n')
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{40mm}\n')
    f.write(' \\item Sketch this scenario with all values shown.\n')
    f.write(' \\item Draw a free body diagram of the car at rest on the table.\n')
    f.write(' \\item Calculate the weight and normal force.\n')
    f.write('\\end{enumerate}\n')
    f.write('\\setlength{\\itemsep}{5mm}\n')
   
    f.write(' \\item  The car is then accelerated constantly at $'+SAccCar+'\\frac{m}{s^2}$ for $'+STCar+'s$. \n')
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{40mm}\n')
    f.write(' \\item  Draw the free body diagram as the car is accelerated, neglecting friction. \n')    
    f.write(' \\item  Calculate the force on the car. \n')
    f.write(' \\item Calcualte the distance traveled by the car. \n')
    f.write(' \\item Calculate the final velocity of the car. \n')
    f.write('\\end{enumerate}\n')
    f.write('\\setlength{\\itemsep}{5mm}\n')

    f.write(' \\item At the end of the time stated above, the car is at the edge of the table and falls to the ground. \n')
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{40mm}\n')
    f.write(' \\item Draw a free body diagram as the car is in the air. \n')
    f.write(' \\item Calculate the time that the car falls to the ground. \n')
    f.write(' \\item Calculate the distance the car lands from the table. \n')
    f.write(' \\item Calculate the verticle speed of the car. \n')    
    f.write('\\end{enumerate}\n')
    f.write('\\setlength{\\itemsep}{5mm}\n')

    f.write(' \\item The  car lands on the ground perfectly on the wheels with no loss of horizontal speed. It tavels until it enters a track with a loop  The top of the loop is $'+SHeightTrack+'m$ above the floor. \n')
    f.write('\\begin{enumerate}\n')
    f.write('\\setlength{\\itemsep}{40mm}\n')
    f.write(' \\item Draw the free body diagram of the car at the top of the loop. \n')
    f.write(' \\item Assuming the car has lost no speed, calculate the linear and angular velocity of the car as it travels the loop. \n')
    f.write(' \\item Calculate the time the car takes to complete the loop. \n')
    f.write('\\end{enumerate}\n')
    f.write('\\setlength{\\itemsep}{40mm}\n')

    
    f.write(' \\item After the car completes the loop, it enters a rough area where it begins to lose speed. The car slows to rest in $'+SLoss+'s$. Calculate the force on the car.\n')


    f.write('\\end{enumerate}\n')
    

    

def WritePage(home,n):
	output=home+"/temp"
	nn=str(n)
	name=output+"/temp"+nn
	filename=name+".tex"
	logname=output+"/log.out"
	f=open(filename,'w')
	HEAD(f,n)
	PAGE(f,n,"I")
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
import math
home = expanduser("~")
for x in range(1, 7):
	WritePage(home,x)
