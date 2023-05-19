#Harith Izani 1821037
#Muhammad Hariz Bin Hasnan 1827929
#Mohamad Arif Daniel Bin Muhamaddun 1917027
#Nur Atiqah binti Hasbullah 1920744

#WE ARE FOLLOWING THE SPELLING STANDARDS OF https://www.lexisrex.com/Arabic-Numbers/1-1000

import os
from nltk.nltk_contrib.fst.fst import *

path = os.getcwd()
os.chdir(path)

class myFST(FST):
    def recognize(self, iput, oput):
        self.inp = list(iput)
        self.outp = list(oput)

        if list(oput) == f.transduce(list(iput)):
            return True
        else:
            return False

#Adding state 1-5
f = myFST('example')
for i in range(1,5):
    f.add_state(str(i))

#Initial state
f.initial_state = '1'

#State 1->1 (tens and space and 'and')
f.add_arc('1', '1', ('ashar'), ('ten'))
f.add_arc('1', '1', ('ishrun'), ('twenty'))
f.add_arc('1', '1', ('thalathun'), ('thirty'))
f.add_arc('1', '1', ('arba\'un'), ('forty'))
f.add_arc('1', '1', ('hhamsun'), ('fifty'))
f.add_arc('1', '1', ('sittun'), ('sixty'))
f.add_arc('1', '1', ('sab\'un'), ('seventy'))
f.add_arc('1', '1', ('thamanun'), ('eighty'))
f.add_arc('1', '1', ('tis\'un'), ('ninety'))
f.add_arc('1', '1', (' '), (' '))
f.add_arc('1', '1', ('wa'), ('and'))

#State 1->2 (ones)
f.add_arc('1', '2', ('sifr'), ('zero'))
f.add_arc('1', '2', ('wahid'), ('one'))
f.add_arc('1', '2', ('ahada'), ('one'))
f.add_arc('1', '2', ('ithnan'), ('two'))
f.add_arc('1', '2', ('ithna'), ('two'))
f.add_arc('1', '2', ('thalathah'), ('three'))
f.add_arc('1', '2', ('thalatha'), ('three'))
f.add_arc('1', '2', ('thalath'), ('three'))
f.add_arc('1', '2', ('arba\'a'), ('four'))
f.add_arc('1', '2', ('hhamsa'), ('five'))
f.add_arc('1', '2', ('sitta'), ('six'))
f.add_arc('1', '2', ('sab\'a'), ('seven'))
f.add_arc('1', '2', ('thamaniya'), ('eight'))
f.add_arc('1', '2', ('tis\'a'), ('nine'))
#State 1->2 (hundreds)
f.add_arc('1', '2', ('mi\'a'), ('one-hundred'))
f.add_arc('1', '2', ('mi\'atan'), ('two-hundred'))
f.add_arc('1', '2', ('thalath mi\'a'), ('three-hundred'))
f.add_arc('1', '2', ('arba mi\'a'), ('four-hundred'))
f.add_arc('1', '2', ('hhams mi\'a'), ('five-hundred'))
f.add_arc('1', '2', ('sitt mi\'a'), ('six-hundred'))
f.add_arc('1', '2', ('sab mi\'a'), ('seven-hundred'))
f.add_arc('1', '2', ('thaman mi\'a'), ('eight-hundred'))
f.add_arc('1', '2', ('tis mi\'a'), ('nine-hundred'))
#State 1->2 (thousands)
f.add_arc('1', '2', ('alaaf'), ('thousand'))
f.add_arc('1', '2', ('alf'), ('one-thousand'))
f.add_arc('1', '2', ('alfain'), ('two-thousand'))
f.add_arc('1', '2', ('thalathah alaaf'), ('three-thousand'))
f.add_arc('1', '2', ('arba\'a alaaf'), ('four-thousand'))
f.add_arc('1', '2', ('hhamsa alaaf'), ('five-thousand'))
f.add_arc('1', '2', ('sitta alaaf'), ('six-thousand'))
f.add_arc('1', '2', ('sab\'a alaaf'), ('seven-thousand'))
f.add_arc('1', '2', ('thamaniya alaaf'), ('eight-thousand'))
f.add_arc('1', '2', ('tis\'a alaaf'), ('nine-thousand'))

#State 2->1
f.add_arc('2', '1', (''), (''))

#State 2->3
f.add_arc('2', '3', (' '), (' '))

#State 3->1 (tens and thousandth)
f.add_arc('3', '1', ('ashar'), ('ten'))
f.add_arc('3', '1', ('ishrun'), ('twenty'))
f.add_arc('3', '1', ('thalathun'), ('thirty'))
f.add_arc('3', '1', ('arba\'un'), ('forty'))
f.add_arc('3', '1', ('hhamsun'), ('fifty'))
f.add_arc('3', '1', ('sittun'), ('sixty'))
f.add_arc('3', '1', ('sab\'un'), ('seventy'))
f.add_arc('3', '1', ('thamanun'), ('eighty'))
f.add_arc('3', '1', ('tis\'un'), ('ninety'))
f.add_arc('3', '1', ('wa'), ('and'))
f.add_arc('3', '1', ('alaaf'), ('thousand'))

#Ending All
f.add_arc('1', '4', (''), (''))

#Final state
f.set_final('4')

def testing():   
    inp = input()
    outp = input()

    if f.recognize(inp, outp):
        combined = " ".join([inp,'-->' ,outp, '\n'])
        print(combined)
        print('accepted \n')
        file = open('Arab-Eng-trans.dat',"a")
        file.write(combined)
        file.close()
    else:
        print(inp, end='-->')
        print(outp,'\n')
        print("rejected \n")

    if inp == "exit": return False
    else: return True

loop = True
while loop:
    loop = testing()
    
disp = FSTDisplay(f)
