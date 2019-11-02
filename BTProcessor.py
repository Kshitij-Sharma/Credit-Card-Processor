#!/usr/bin/env python3
import sys
from Input import Input

def main():
  if len(sys.argv) == 1:
    # read from stdin
    processor = Input(sys.stdin)
    processor.summary()

    pass
  if len(sys.argv) == 2:
    filename = sys.argv[1]
    # Read from file
    file1 = open(filename,"r+")
    text = file1.readlines()
    processor = Input(text)
    processor.summary()
    
if __name__ == '__main__':
  main()