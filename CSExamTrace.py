import Base
import random
import math

class Trace(Base.BASE):
    def __init__(self,course, title):
        super(Trace, self).__init__(course, title)
        self.sum=float(0.0)
        self.x=[random.randint(10,50),random.randint(15,100),random.randint(1,40),random.randint(20,200),random.randint(50,100),random.randint(25,60),random.randint(1,30)]


    def testp(self):
        self.sum=float(0.0)
        for i in range (0,len(self.x)-1):
            for j in range (i,len(self.x)-1):
                if self.x[j]>self.x[j+1]:
                    self.sum+=float(math.sqrt(float(self.x[j]*self.x[j]-self.x[j+1]*self.x[j+1])))                    
                

    def PAGE(self):

        self.f.write('\\large\n')
        self.f.write('Given this pdsuedo code snippet:\n\n')
        self.f.write('int i,j,len=length.x;\n\n')
        self.f.write('double sum=0;\n\n')
        self.f.write('for(i=0;i $<$ len-1;i++)\n\n')
        self.f.write('\hspace{1cm}for(j=i;j$<$len-1;j++)\n\n')        
        self.f.write('\hspace{2cm}if(x[j]$>$x[j+1])\n\n')
        self.f.write('\hspace{3cm}sum+=DIFF(x[j],x[j+1]);\n\n')
        self.f.write('Where x is an array of ints and DIFF is a method that calculates the square root of the differences of squares \n\n')
        self.f.write('$\\sqrt{a^2-b^2}$\n\n')
        self.f.write('In the table below, trace the output for\n\n x=[')
        for k in range(0,len(self.x)):
            self.f.write(str(self.x[k]))
            if k<len(self.x)-1:
                   self.f.write(', ')
        self.f.write(']\n\n')
                   
                           
        self.f.write('and confirm the resulting sum is '+str(round(self.sum,2))+' \n\n')

        self.f.write('\\small \n')
        self.f.write('\\setlength\\extrarowheight{ .5 cm})\n\n')
        self.f.write('\\begin{tabular} {| p{20mm} | p{5mm} | p{20mm} |p{10mm} |p{10mm} |p{20mm} |p{25mm} |p{10mm} |}\n')
        self.f.write('\\hline\n')
        self.f.write(' $i<len-1$ & $j$	 	&  $j<len-1$ & $j+1$ & $x[j]$ & $x[j+1]$ & $x[j]>x[j+1]$ & $sum$ \\\\ \n')
        self.f.write('\\hline\n')
        self.f.write(' & 	 	&   &  &  & &  \\\\ \n')
        self.f.write('\\hline\n')
        self.f.write(' & 	 	&   &  &  & &  \\\\ \n')
        self.f.write('\\hline\n')
        self.f.write(' & 	 	&   &  &  & &  \\\\ \n')
        self.f.write('\\hline\n')
        self.f.write(' & 	 	&   &  &  & &  \\\\ \n')
        self.f.write('\\hline\n')
        self.f.write(' & 	 	&   &  &  & &  \\\\ \n')
        self.f.write('\\hline\n')
        self.f.write(' & 	 	&   &  &  & &  \\\\ \n')
        self.f.write('\\hline\n')
        self.f.write(' & 	 	&   &  &  & &  \\\\ \n')
        self.f.write('\\hline\n')
        self.f.write(' & 	 	&   &  &  & &  \\\\ \n')
        self.f.write('\\hline\n')
        self.f.write(' & 	 	&   &  &  & &  \\\\ \n')
        self.f.write('\\hline\n')
        self.f.write(' & 	 	&   &  &  & &  \\\\ \n')
        self.f.write('\\hline\n')
        self.f.write(' & 	 	&   &  &  & &  \\\\ \n')
        self.f.write('\\hline\n')
        self.f.write(' & 	 	&   &  &  & &  \\\\ \n')
        self.f.write('\\hline\n')
        self.f.write('\\end{tabular}')
  



g=Trace("AP Computer Science","Trace Exam")
for x in range(1, 30):
    g.testp()
    g.WritePage(x)
