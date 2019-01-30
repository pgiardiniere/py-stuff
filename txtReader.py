# per PEP8 style guide, imports on seperate lines
import os
import glob

# get pwd (working dir) and print. OS independent method.
# could be useful modules if attempting to search in other dirs or recursive search
pwd = glob.glob(os.getcwd())
print(pwd)


files = []
for file in glob.glob("*.txt"):
    files.append(file)
print(files)

#import fileinput (multiple streams) or use open() with loops to go into the txt files
#  fileinput looks more appropriate
#  need to get filenames and feed into a list for .input(arg).

import fileinput
x = fileinput.input(files)
print("\n# l# filename() isFirstLine")
print("*************************")
for line in x:
    print(x.fileno(), x.filelineno(), x.filename(), x.isfirstline())


#s = input("enter string to query txt files in current director for\n")