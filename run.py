import sys
import subprocess
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

result = subprocess.run(['bin/run.sh', 'pmd', '-d', sys.argv[1], '-f', 'text', '-R', 'cyclical.xml', '-language', 'java'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
out = result.stdout.decode('utf-8')

pos1 = out.find('PMDException: Error while parsing')
if pos1 >= 0:
    print(f"{bcolors.ERROR}Incorrect input file{bcolors.ENDC}")
else:
    pos1 = out.find('has a total cyclomatic complexity')
    pos1 = out.find('of ', pos1)
    pos1 = pos1 + 3
    pos2 = out.find('(', pos1)

    complexity = int(out[pos1:pos2-1])
    if complexity <= 10:
        print(f"{bcolors.OKGREEN}Total cyclomatic complexity: " + str(complexity) + f"{bcolors.ENDC}")
    else:
        print(f"{bcolors.WARNING}Total cyclomatic complexity: " + str(complexity) + f"{bcolors.ENDC}")
