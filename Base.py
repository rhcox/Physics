import random
import subprocess
import os
import time
import math
import re

class BASE(object):
    def make(self, course, title):
        self.rnum=0
        self.num=-1
        self.f=None
        self.course=course
        self.title=title
        from os.path import expanduser
        self.home = expanduser("~")
        self.v="";

    def PrintAll(self):
        print self.rnum
        print self.num        
        print self.f
        print self.course
        print self.title
        print self.home

    def __init__(self, course, title):
        self.make(course, title)
        
    def PAGE(self):
        pass

    def HeadInclude(self):
        self.f.write('\\documentclass[12pt]{article}\n')
        self.f.write('\\pdfpagewidth 8.5in\n')
        self.f.write('\\pdfpageheight 11in\n')
        self.f.write('\\usepackage{amsmath}\n')
        self.f.write('\\usepackage{amsthm}\n')
        self.f.write('\\usepackage{epsfig}\n')
        self.f.write('\\usepackage{graphicx}\n')
        self.f.write('\\usepackage{color}\n')
        self.f.write('\\usepackage{graphpap}\n')
        self.f.write('\\usepackage{array}\n')
        self.f.write('\\usepackage{epic}\n')
        self.f.write('\\usepackage{fancyhdr}\n')
        self.f.write('\\usepackage{enumerate}\n')
        self.f.write('\\usepackage{pstricks}\n')
        self.f.write('\\usepackage{pst-plot}\n')
        self.f.write('\\usepackage{epstopdf}\n')
        self.f.write('\\usepackage{geometry}\n')
        self.f.write('\\usepackage{xcolor}\n')
        self.f.write('\\usepackage{lastpage}')
        self.f.write('\\usepackage{circuitikz} \n')

        
    def HeadMargins(self):
        self.f.write('\\geometry{letterpaper,textwidth=190mm,textheight=225mm,left=15mm,top=15mm,includehead}\n')
        self.f.write('\\input xy\n')
        self.f.write('\\xyoption{all}\n')

    def HeadTop(self):
        self.f.write('\setcounter{page}{1}\n')
        self.f.write('\pagenumbering{arabic}\n')
        self.f.write('\\large\n')
        self.f.write('\\pagestyle{fancyplain}\n')
        self.f.write('\\lhead{Name:}\n')
        self.f.write('\\chead{Date:}\n')
        self.f.write('\\rhead{Period:       }\n')
        self.f.write('\\lfoot{'+self.course+'- '+self.rnum[-5:]+'}\n')
        self.f.write('\\cfoot{\\thepage\ of \\pageref{LastPage}}\n')
        self.f.write('\\rfoot{RH Cox}\n')

        
    def HeadUnits(self):
        self.f.write('\\newcommand{\\MOM}[1][]{\\, \\frac{kg \\cdot m}{s}}\n')
        self.f.write('\\newcommand{\\MET}[1][]{\\, m}\n')
        self.f.write('\\newcommand{\\MPS}[1][]{\\, \\frac{m}{s}}\n')
        self.f.write('\\newcommand{\\MPSS}[1][]{\\, \\frac{m}{s^2}}\n')
        self.f.write('\\newcommand{\\KG}[1][]{\\, kg}\n')
        self.f.write('\\newcommand{\\NF}[1][]{\\, N}\n')
        self.f.write('\\newcommand{\\SEC}[1][]{\\, s}\n')
        self.f.write('\\newcommand{\\JE}[1][]{\\, J}\n')
        self.f.write('\\newcommand{\\Watt}[1][]{\\, W}\n')
        self.f.write('\\newcommand{\\NS}[1][]{\\, N \\cdot s}\n')
        self.f.write('\\newcommand{\\TQ}[1][]{\\, N \\cdot m}\n')
        self.f.write('\\newcommand{\\Jpg}[1][]{\\, \\frac{J}{g \cdot K}}\n')
        self.f.write('\\newcommand{\\Kelvin}[1][]{\\, K}\n')
        self.f.write('\\newcommand{\\HZ}[1][]{\\, Hz}\n')
        self.f.write('\\newcommand{\\NPM}[1][]{\\, \\frac{N}{m}}\n')
        self.f.write('\\newcommand{\\COUL}[1][]{\\, C}\n')
        self.f.write('\\newcommand{\\NCOUL}[1][]{\\, \\frac{N}{C}}\n')
        self.f.write('\\newcommand{\\OHMS}[1][]{\\, #1 \\Omega}\n')
        self.f.write('\\newcommand{\\VOLTS}[1][]{\\, #1 V}\n')
        self.f.write('\\newcommand{\\AMPS}[1][]{\\, #1 A}\n')
        self.f.write('\\newcommand{\\EV}[1][]{\\, #1 eV}\n')

 


    def HeadGrid(self):
        self.f.write('\\newcommand{\\gridpaper}{\n')
        self.f.write('\\begin{picture}(50,50)\n')
        self.f.write('\\put(30,5){\\grid(80,100)(10,10)}\n')
        self.f.write('\\end{picture}\n')
        self.f.write('}\n')

    def HeadTitle(self):
        self.f.write('\\begin{document}\n')
        self.f.write('\\begin{center}\n')
        self.f.write('\\Large\n')
        self.f.write('\\bfseries\n')
        self.f.write(self.title+'\n')
        self.f.write('\\end{center}\n')


    def HEAD(self):
        self.HeadInclude()
        self.HeadMargins()
        self.HeadTop()
        self.HeadUnits()
        self.HeadGrid()
        self.HeadTitle()

    def ENDMAT(self):
        self.f.write('\\end{document}\n')


    def WritePage(self,n):
        self.num=str(n)
        output=self.home+"/temp"
        name=output+"/temp"+self.num
        filename=name+".tex"
        logname=output+"/log.out"
        self.f=open(filename,'w')
        self.rnum=str(int(time.time()*100))
        self.HEAD()
        self.PAGE()
        self.ENDMAT()
        self.f.close()
        pdfcommand="/Library/TeX/texbin/pdflatex --file-line-error --synctex=1 -output-directory "+output+" "+filename+" >"+logname
        os.system(pdfcommand)
        os.system(pdfcommand)   # run twice for lastpage. 
        rmnamen='rm '+name+'.aux'
        os.system(rmnamen)
        rmnamen='rm '+name+'.log'
        os.system(rmnamen)
        rmnamen='rm '+name+'.synctex.gz'
        os.system(rmnamen)
        rmnamen='rm '+name+'.tex'
        os.system(rmnamen)

    def toExp(self,v):
        m=re.compile('\s*(.*)\s*[eE]\s*([+-])\s*([1-9]*[0-9]*)')
        m1="{0:.2e}".format(v)
        m2=m.match(m1)
        if m2:
            m3=m2.group(1)+'X10^{'
            if m2.group(2)=='-':
                   m3+='-'
            m3+=m2.group(3)+'}'
        else:
            m3=m1
        self.v=m3



        
b1=BASE('Construction Technology', 'Estimate Air Handling')
b1.PrintAll()
