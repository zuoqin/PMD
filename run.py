import sys
import subprocess
import os

result = subprocess.run(['bin/run.sh', 'pmd', '-d', sys.argv[1], '-f', 'text', '-R', 'cyclical.xml', '-language', 'java'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
out = result.stdout.decode('utf-8')
pos1 = out.find('has a total cyclomatic complexity')
pos1 = out.find('of ', pos1)
pos1 = pos1 + 3
pos2 = out.find('(', pos1)

complexity = out[pos1:pos2-1]
print('Total cyclomatic complexity: ', complexity)
