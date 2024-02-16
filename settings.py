import sys
import time
# This function taken from this source: 
# https://github.com/DebbieBergstrom/Russian-Roulette/blob/main/all_functions.py
# By Debbie Bergstrom, def slow_print() function.
def slowprint(text, delay=0.03):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)
        
