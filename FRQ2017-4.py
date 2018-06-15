import Base
import random

class FRQ20174(Base.BASE):
    def __init__(self,course, title):
        super(FRQ20174, self).__init__(course, title)

    def PAGE(self):
        self.f.write('\\normalsize\n')
        random.seed(self.rnum)

        mass=str((float(random.randint(25,70))/10.))
        heightf=float(random.randint(20,50))/10.0        
        height=str(heightf)
        speed=str((float(random.randint(16,50))/10.0))
        force=str((float(random.randint(30,60))/10.0))
        time=str((float(random.randint(5,29))/10.0))
        len=str(round(heightf/0.8,1))
        lower=str((float(random.randint(2,20))/100.0))
        dist=str((float(random.randint(60,99))/100.0))
        height=str((float(random.randint(120,250))/100.0))

        self.f.write('Due at the end of class, no excepions.  Late work will recieve only points earned, no bonus.')
        self.f.write('\\begin{figure}[ht!]\n')
        self.f.write('\\centering\n')
        self.f.write('\\includegraphics[width=120mm]{FRQ20174.jpg}\n')
        self.f.write('\\caption{Slide for Team 1 and 2 \label{overflow}}\n')
        self.f.write('\\end{figure}\n\n')

        self.f.write('\\begin{enumerate}\n')

        self.f.write('\\item Two teams build a low friction slide.  Team two has a table that is lower than Team 1 by $'+lower+'\\MET$.  Team two builds a bump in their slide so the blocks leave the table at the same height with respect to the floor.  Both blocks leave the table horizontally.\n\n')
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item (1 point)Calculate the horizontal speed of each block as they leave the table in terms of $d$.\n\n')  
        self.f.write('\\vspace{25mm}\n')
        self.f.write('\\item (1 point)Calculate the time for each block to fall the height $h$ after the block leaves the table in terms of $h$.\n\n')
        self.f.write('\\vspace{25mm}\n')
        self.f.write('\\item (1 point)Calculate the horizontal distance that each block lands from the edge of the table in terms of $h$ and $d$.\n\n')     
        self.f.write('\\vspace{25mm}\n')
        self.f.write('\\item (1 point)If $h='+height+'\\MET$ and $d='+dist+'\\MET$ calcuate the horizontal speed, the time, the horizontal distance, and the total speed of the block as it hits the floor.\n\n')
        self.f.write('\\vspace{25mm}\n')
        self.f.write('\\item (2 point)In a paragraph length repsonse, make a claim that the block land the same horizontal distance from the edge of the table.  Use the equations and physics to explain and justify the claim. Do not refer to the values.\n\n')
        self.f.write('\\vspace{30mm}\n')

        self.f.write('\\end{enumerate}\n')
        self.f.write('\\begin{figure}[ht!]\n')
        self.f.write('\\centering\n')
        self.f.write('\\includegraphics[width=120mm]{FRQ20174c.jpg}\n')
        self.f.write('\\caption{Slide for Team 1 and 2 Different Shapes \label{overflow}}\n')
        self.f.write('\\end{figure}\n\n')

        self.f.write('\\item In another experiment, teams 1 and 2 use tables and low-friction slides with the same height. However, the two slides have different shapes, as shown below.\n\n')    
        self.f.write('\\begin{enumerate}\n')
        self.f.write('\\item  (2 point)In a paragraph length repsonse, make a claim about the distance the blocks land from the edge of the table, for instance one lands further or they both land the same distance.  Use physics and equations but no manipulation of the equations to explain and justify the claim. Be specific refering to the variables in the graph and the shape of the slides\n\n')
        self.f.write('\\vspace{30mm}\n')
        self.f.write('\\item  (2 point)In a paragraph length repsonse, make a claim about which blocks hits the ground first, for instance one lands first or they both land the same time.  Use physics and equations but no manipulation of the equations to explain and justify the claim.  Be specific refering to the variables in the graph and the shape of the slides\n\n')
        self.f.write('\\vspace{30mm}\n')
        self.f.write('\\end{enumerate}\n')
        self.f.write('\\end{enumerate}\n')

g=FRQ20174("Physics 1","FRQ 2017-4")
for x in range(1, 50):
    g.WritePage(x)
