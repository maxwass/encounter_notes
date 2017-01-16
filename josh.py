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
        self.first_name = ''
        self.last_name  = ''
        self.age        = 0

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
                 self.first_name = first_name
                 self.last_name  = last_name

             else:
                 clear_lines_above(5)
                 #print('Redo Patient Name.')
                 correct = False



    def _add_age(self):
        correct = False
        while (correct == False):
            print('Patient Age')
            age = raw_input("    Enter Patient Age: ")
            print('Patient Age: ' + age)

            correct = raw_input('Correct[y|n]?: ')
            if (correct == 'y') | (correct == ''):
                 correct = True
                 clear_lines_above(4)
                 print('Patient Age: ' + age)
                 self.age = age
            else:
                 clear_lines_above(4)
                 #print('Redo Patient Name.')
                 correct = False




patient = Patient()
patient._add_name()
patient._add_age()

#input patient age
#Patient_Age = raw_input("Enter Patient Age: ")


now = datetime.datetime.now()
filename = patient.last_name + '_' + patient.first_name + '_' + str(now.month) + '_' +  str(now.day) + '_' +  str(now.year) + '.txt'
print(filename)


f = open(filename, 'a')

f.write('This is a test\n')
