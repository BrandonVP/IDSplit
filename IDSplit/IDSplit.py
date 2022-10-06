"""
Splits a ScanTool capture into multiple files by ID
"""

import sys
import os

filename = sys.argv[1]
dirName = filename.split('.')

class message(object):
    def __init__(self, number, time, id, length, d0, d1, d2, d3, d4, d5, d6, d7):
        self.number = number
        self.time = time
        self.id = id
        self.length = length
        self.d0 = d0
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.d4 = d4
        self.d5 = d5
        self.d6 = d6
        self.d7 = d7

m = message(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

try:
    with open(filename) as f:
        if not os.path.exists(dirName[0]):
            os.mkdir(dirName[0])
        else:
            print('Folder already exists, delete or rename before running again')
            quit()
        for line in f:
            m.number, m.time, m.id, m.length, m.d0, m.d1, m.d2, m.d3, m.d4, m.d5, m.d6, m.d7 = line.split()

            m.number = m.number.rjust(5, ' ')
            m.time = m.time.rjust(6, ' ')
            m.id = m.id.rjust(3, ' ')

            temp = dirName[0] + '/' + str(m.id) + '.txt'
            file1 = open(temp, "a") 
            
            temp2 = str(m.number) + "    " + str(m.time) + "    " + str(m.id) + "   " + str(m.length) + "   " + str(m.d0) + "  " + str(m.d1) + "  " + \
            str(m.d2) + "  " + str(m.d3) + "  " + str(m.d4) + "  " + str(m.d5) + "  " + str(m.d6) + "  " + str(m.d7) + '\n'
            

            file1.write(temp2)
            file1.close()
except IOError:
    print("File not found")
    sys.exit(1)


print('Split Complete')
quit()