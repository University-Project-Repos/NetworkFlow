"""
COSC364 Internet Technologies and Engineering
Assignment #2: Flow
File: test.py
Tests flow.py optimization for Y={3,...,7} as instructed in assignment doc.
Author:
    - Adam Ross
Date: 25 May 2018
"""

from os import system as flow
from time import sleep

X = 7
Z = 7
Y_MIN = 3
Y_MAX = 7


def main():
    [flow("xfce4-terminal --hold -e 'bash -c \"python3 flow.py " + str(X) + " " +
          str(y) + " " + str(Z) + "; exit bash\"'") for y in range(Y_MIN, Y_MAX + 1)
     if sleep(0.5) is None]


if __name__ == '__main__':
    main()
