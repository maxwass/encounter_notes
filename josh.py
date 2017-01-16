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

#this is how you use comments
word_input = 'josh has a small shmekle'

correct = False
while (correct == False):
    #input patient name
    print('Patient Name')
    Patient_First_Name = raw_input("    Enter Patient First Name: ")
    Patient_Last_Name = raw_input("    Enter Patient Last Name: ")
    Patient_Full_Name = Patient_Last_Name + '_' + Patient_First_Name
    print('    Patient Name: ' + Patient_First_Name + ' ' + Patient_Last_Name)

    correct = raw_input('Correct[y|n]?: ')
    if (correct == 'y') | (correct == ''):
        correct = True
        print('Patient Name: ' + Patient_First_Name + ' ' + Patient_Last_Name)
    else:
        clear_lines_above(5)
        #print('Redo Patient Name.')
        correct = False


#input patient age
Patient_Age = raw_input("Enter Patient Age: ")







now = datetime.datetime.now()
filename = Patient_Full_Name + '_' + str(now.month) + '_' +  str(now.day) + '_' +  str(now.year) + '.txt'
print(filename)
time.sleep(1)
#goes up one line to replace old text
sys.stdout.write("\033[F")
time.sleep(1)
print(filename + 'replaced!!')


f = open(filename, 'a')

f.write('This is a test\n')
