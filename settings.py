import sys
import time
# This function taken from this source: https://www.grepper.com/answers/51377/python+slow+print
def slowprint(text):
    for letter in text + "\n":
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(1./10)
        
