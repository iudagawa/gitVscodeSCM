import sys
import logging
import contextlib

#x = input('enter')
#print(x)

sys.stdin.flush()
sys.stdout.write('input >')
x = sys.stdin.readline()
print(x)

#for line in sys.stdin:
#    # print(line)
#    sys.stdout.write(line)
#    logging.error(line)
    
with open('stdout.log','w') as f:
    with contextlib.redirect_stdout(f): 
        print('Hello!')
