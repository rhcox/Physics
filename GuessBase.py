import Base

class Guess(Base.BASE):
 
    def __init__(self, course, title, rowh):
        super(Guess, self).__init__(course, title)
        self.rowh=rowh
        
    def PrintAll(self):
        print self.rowh

    def GuessBody(self,answer, formula, constants):
        self.f.write('{\n')
        self.f.write('\\item #1\n\n')
        # self.f.write('\\setlength\extrarowheight{'+self.rowh+' mm}\n')
        self.f.write('\\begin{tabular} {| p{20mm} | p{72mm} | p{73mm} |}\n')
        self.f.write('\\hline\n')
        self.f.write('\\Z  Given		& \\SHAD{read text for known data}	 	&  Picture and Process \\newline '+constants+' \\\\ \n')
        self.f.write('\\hline\n')
        self.f.write('\\Z Unknowns 	& \\SHAD{for what is to be calculated} 	&  \\SHAD{Sketch a picture} \\\\ \n')
        self.f.write('\\cline{1-2}\n')
        self.f.write('\\Z Equation 		&'+formula+' & \\SHAD{Draw a schematic}\\\\ \n')
        self.f.write('\\cline{1-2}\n')
        self.f.write('\\Z Solution 		&'+answer+'&	 \\SHAD{Solve an equation} \\\\ \n')
        self.f.write('\\hline\n')
        self.f.write('\\end{tabular}\n')
        self.f.write('}\n')

        
    def WriteGuess(self, text, answer, formula, constansts):
        self.f.write('\\GUESSAFC{'+text+'}{'+answer+'}{'+formula+'}{'+constant+'}\n')
        self.f.write('\\GUESS{'+text+'}\n')

        
    def HeadGuess(self):
        self.f.write('\\def\\Z{\\vphantom{\\parbox[c]{0mm}{\\'+self.rowh+' temp}}}\n\n')
        self.f.write('\\newcommand{\\SHAD}[1]{{\\large \\color{black!20}#1} }\n\n')
        #print '\\def\\Z{\\vphantom{\\parbox[c]{0mm}{\\'+self.rowh+' temp}}}\n\n'
        
        self.f.write('\\newcommand{\\GUESS}[1]\n')
        self.GuessBody('\\SHAD{state solution with units}','\\SHAD{formulas with variables}','')

        self.f.write('\\newcommand{\\GUESSA}[2]\n')
        self.GuessBody('{\\normalsize #2}','\\SHAD{formulas with variables}','')

        self.f.write('\\newcommand{\\GUESSAF}[3]\n')
        self.GuessBody('{\\normalsize #2}','{\\large #3}','')
        
        self.f.write('\\newcommand{\\GUESSAFC}[4]\n')
        self.GuessBody('{\\normalsize #2}','{\\large #3}','{\\normalsize #4}')


    def HeadEnum(self):
        self.f.write('\\renewcommand\\labelenumi{\\Roman{enumi}.}\n')
        self.f.write('\\renewcommand\\labelenumii{\\Alph{enumii}.}\n')
        self.f.write('\\renewcommand\\labelenumiii{\\arabic{enumiii}.}\n')
        self.f.write('\\renewcommand\\labelenumiv{\\alph{enumiv}.}\n')

 
    def HEAD(self):
        super(Guess,self).HEAD()
        self.HeadGuess()
        self.HeadEnum()
 

        
g1=Guess('Construction Technology', 'Estimate Air Handling', 'Large')
g1.PrintAll()
