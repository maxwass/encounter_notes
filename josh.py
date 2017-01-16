import sys
import math
import time
import datetime
import Tkinter
import Queue


def clear_lines_above(how_many_lines):
    for i in range(1,how_many_lines+1):
        sys.stdout.write("\033[F") #go up one line in console
        sys.stdout.write("\033[K") # Clear to the end of line

class Patient:
    def _init_(self):
        self._first_name = ''
        self._last_name  = ''
        self._age        = 0

    def _add_name(self):
         correct = False
         while (correct == False):
             print('Patient Name')
             first_name = raw_input("    Enter Patient First Name: ")
             last_name = raw_input("    Enter Patient Last Name: ")
             full_name = last_name + '_' + first_name
             print('    Patient Name: ' + first_name + ' ' + last_name)

             correct = raw_input('Correct[y|n]?: ')
             if (correct == 'y') | (correct == ''):
                 correct = True
                 clear_lines_above(5)
                 print('Patient Name: ' + first_name + ' ' + last_name)
             else:
                 clear_lines_above(5)
                 #print('Redo Patient Name.')
                 correct = False
         self._first_name = first_name
         self._last_name  = last_name



patient = Patient()
patient._add_name()

#input patient age
Patient_Age = raw_input("Enter Patient Age: ")


now = datetime.datetime.now()
filename = patient.last_name + '_' + patient.first_name + '_' + str(now.month) + '_' +  str(now.day) + '_' +  str(now.year) + '.txt'
print(filename)
time.sleep(1)
#goes up one line to replace old text
sys.stdout.write("\033[F")
time.sleep(1)
print(filename + 'replaced!!')


f = open(filename, 'a')

f.write('This is a test\n')
