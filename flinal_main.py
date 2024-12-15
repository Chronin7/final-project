import random #imports
import time
import math
import sys,tty,os,termios
dropmap = [['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', '=', '=', '=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', '=', '=', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', '=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ' ', ' ', ' ', '='],
['=', ' ', ' ', '=', '=', '=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', '=', '=', ' ', ' ', '='],
['=', ' ', ' ', ' ', '=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', '=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', '=', '=', '=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', '=', '=', '=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', '=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', ' ', '='],
['=', '=', ' ', ' ', ' ', '=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', ' ', ' ', ' ', '=', '='],
['=', '=', '=', ' ', ' ', ' ', '=', ' ', ' ', ' ', ' ', ' ', ' ', '=', ' ', ' ', ' ', '=', '=', '='],
['=', ' ', '=', '=', ' ', ' ', ' ', '=', ' ', ' ', ' ', ' ', '=', ' ', ' ', ' ', '=', '=', ' ', '='],
['=', ' ', ' ', '=', '=', ' ', ' ', ' ', '=', ' ', ' ', '=', ' ', ' ', ' ', '=', '=', ' ', ' ', '='],
['=', ' ', ' ', ' ', '=', '=', ' ', ' ', ' ', '=', '=', ' ', ' ', ' ', '=', '=', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', '=', '=', ' ', ' ', ' ', ' ', ' ', ' ', '=', '=', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', '=', '=', ' ', ' ', ' ', ' ', '=', '=', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', '=', '=', ' ', ' ', '=', '=', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', '=', '=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', '=', '=', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', '=', '=', '=', ' ', ' ', ' ', ' ', '=', '=', '=', '=', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', '=', '=', ' ', ' ', '='],
['=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', '=', '=', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', '=', '=', '=', '=', '=', '=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', '=', '=', '=', '=', '=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', '=', '=', '=', '=', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '='],
['=', ' ', ' ', '=', '=', '=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '=', '=', '=', '=', '=', '=', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', ' ', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', ' ', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', ' ', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', ' ', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', ' ', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', ' ', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', ' ', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', '=', '=', ' ', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '=', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', ' ', ' ', '=', '=', '=', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '!', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '!', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'V', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '[', ']', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
['=', '=', '=', '=', '=', '=', '=', '=', '=', '/', '\\', '=', '=', '=', '=', '=', '=', '=', '=', '='],]
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
#declaring vars
exoshtion = 0
gameover = False
rations = 5
monkilled = False
pythonbridge = False
win = False
loot = ["hp+20"]
name = ""
playedmount = 0
health = 100
coller = ""
lootunseen = ["h20"]
monlist = ["skeleton","mummy","giant lizard","dragon","flying snake","killer bunny","wannabe coder"]
movopt = []
damagebuff = 1
rpg=0
len_loot = -1
luck = 0
gunseen = ["cg","","h50","","","l7","l2"]
nunseen = ["","","h10","cd","l1","l2"]
runseen = ["","","h20","","","l3","l4"]
looted = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
monster = [None,None,None,None,True,None,None,None,None,True,None,None,None,True,None,None,True,None,True,True,True,None,True,None]
good = ['holy hand gernade one use insta kill','rpg once per battle 20 damage at begining','heth + 50 potion','Sten MK II tends to misfire sometimes has buletts bounce off of tagert +20% damage','Apache Revolver you can use it like a gun (terible aim) a nife (way to flexible) or a iron fist (the only safe way to use it) +30% damage','pickled lepercon head +1 luck for 7 turns','luck potion +1 luck for 2 turns']
norm = ["nuke (you cant use it cuse it will kill evorything and evoryone including you)","stick + 3% damage",'helth + 10 porion','deodorant (shreck wants it)','luck charm +1 luck for a turn','luck potion +1 luck for 2 turns']
rearer = ['a peace of a lemon','sord + 10% damage','helth + 20 prtion','slingshot +5% damage','a 15 foot long pole','clover +1 luck for 3 turns','luck potion +1 luck for 4 turns']
def getloot(rear):# 1 for norm 2 for rear 3 for good retuns from the lists abuve status: no bugs
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	if luck == 0:
		chr(1234)
	else:
		rear+=1
	len_loot+=1
	if rear == 1:
		rand = random.randint(0,5)
		if rand == 1:
			damagebuff +=.3
		lootunseen.append(nunseen[rand])
		return norm[rand]
	elif rear == 2:
		rand = random.randint(0,6)
		if rand == 1:
			damagebuff +=.10
		if rand == 3:
			damagebuff+=.05
		lootunseen.append(runseen[rand])
		return rearer[rand]
	elif rear == 3:
		rand = random.randint(0,6)
		if rand == 1:
			rpg +=20
		if rand == 3:
			damagebuff+=.20
		if rand == 4:
			damagebuff+=.30
		lootunseen.append(gunseen[rand])
		return good[rand]
	else:
		damagebuff += 1
		health = health*2
		return "spoon +100% damage and heath"
def monbattle(monname):#monster battle status: buggy
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	
	hp = random.randint(1,100)-rpg
	if random.randint(1,20) > 14:
		damage =random.randint(5,20)
		print(f"you took {damage} damage from a {monname}")
		health -= damage
	while True:
		if health < 1:
			print(f"you died from a {monname} puny mortal")
			print("game over")
			return "die"
		while True:
			try:
				print(f"a {monname} apperes and is at {hp} HP")
				print(f"you are at {health} HP")
				inp = int(input("""1 to atack the monster
2 to use a item: """))
				if inp in [1,2]:
					break
				else:
					print("bruh")
			except:
				print("bruh")
		if inp == 1:
			damage = random.randint(3,10)*damagebuff
			print(f"you did {damage} damage")
			hp-=damage
			if hp <1:
				print(f"you killed {monname}")
				loot.append(getloot(2))
				print(f"you got a {loot[len_loot]}")
				return "live"
			else:
				print(f"the {monname} is at {hp} HP")
			damage =random.randint(5,20)
			print(f"you took {damage} damage from the {monname}")
			health -= damage
		if inp == 2:
			itera = 0
			prinitera = 0
			use = []
			user = []
			print("your items you can use")
			print("0 to return")
			for x in lootunseen:
				if "c" in x or "h" in x:
					prinitera += 1
					print(prinitera,end=" to use: ")
					print(loot[itera])
					use.append(loot[itera])
					user.append(itera)
				itera += 1
			while True:
				try:
					inp = int(input("what do you want to use: "))
					print(len(use))
					if inp <= itera and inp >-1:
						break
					else:
						print("nope")
				except:
					print("nope")
			if inp == 0:
				continue
			if "h" in use[inp-1]:
				health += int(use[inp-1][len(use[inp-1]) - 2:])
				loot.pop(use.index(use[inp-1]))
				lootunseen.pop(use.index(use[inp-1]))
				print(f"you are now at {health} HP")
			if "cg" == use[inp-1]:
				loot.pop(use.index(use[inp-1]))
				lootunseen.pop(use.index(use[inp-1]))
				print(f"you killed {monname}")
				loot.append(getloot(2))
				print(f"you got a {loot[len_loot]}")
				return "live"
			if "cd" == use[inp-1] and monname == "shreck":
				loot.pop(use.index(use[inp-1]))
				lootunseen.pop(use.index(use[inp-1]))
				print("shreck thanks you")
				loot.append(getloot(1275043980432759837259743))
				print("you get a spoon")
				return "live"
			elif "cd" == use[inp-1] and monname !="shreck":
				print("the monster eats it and is engraged even more")
				loot.pop(use.index(use[inp-1]))
				lootunseen.pop(use.index(use[inp-1]))
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
def feld1():#hard coded squares status: buggy
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	while True:
		print("you are in a feald")
		while True:
			try:
				if luck > 0:
					luck -=1
				desition = int(input(f"""would you like to 
1 to move
2 to serach for loot
3 to use item: """))
				if desition in [1,2,3]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition == 3:
			itera = 0
			prinitera = 0
			use = []
			user = []
			print("your items you can use")
			print("0 to return")
			for x in lootunseen:
				if "c" in x or "h" in x:
					prinitera += 1
					print(prinitera,end=" to use: ")
					print(loot[itera])
					use.append(loot[itera])
					user.append(itera)
				itera += 1
			while True:
				try:
					inp = int(input("what do you want to use: "))
					print(len(use))
					if inp <= itera and inp >-1:
						break
					else:
						print("nope")
				except:
					print("nope")
				if inp == 0:
					break
			try:
				if "l" in use[inp-1]:
					luck += int(use[inp-1][len(use[inp-1]) - 1:])
					loot.pop(loot[user[inp-1]])
					lootunseen.pop(lootunseen[user[inp-1]])
					print(f"you use the luck potion")
			except:
				print("error 404: item not found")
		if desition == 2:
			if looted[0]==False:
				looted[0]=True
				temp = getloot(1)
				loot.append(temp)
				print(f"you got a {temp}")
			else:
				print("you dont find anything")
		if desition == 1:
			return "fo1"
def feld2():
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	while True:
		print("you find yourself in a feald")
		while True:
			try:
				if luck > 0:
					luck -=1
				desition = int(input(f"""would you like to 
1 to move
2 to serach for loot
3 to use item: """))
				if desition in [1,2,3]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if inp == 3:
			itera = 0
			prinitera = 0
			use = []
			user = []
			print("your items you can use")
			print("0 to return")
			for x in lootunseen:
				if "c" in x or "h" in x:
					prinitera += 1
					print(prinitera,end=" to use: ")
					print(loot[itera])
					use.append(loot[itera])
					user.append(itera)
				itera += 1
			while True:
				try:
					inp = int(input("what do you want to use: "))
					print(len(use))
					if inp <= itera and inp >-1:
						break
					else:
						print("nope")
				except:
					print("nope")
				if inp == 0:
					break
			try:
				if "l" in use[inp-1]:
					luck += int(use[inp-1][len(use[inp-1]) - 1:])
					loot.pop(loot[user[inp-1]])
					lootunseen.pop(lootunseen[user[inp-1]])
					print(f"you use the luck potion")
			except:
				print("error 404: item not found")
		if desition == 2:
			if looted[1]==False:
				looted[1]=True
				temp = getloot(1)
				loot.append(temp)
				print(f"you got a {temp}")
			else:
				print("you dont find anything")
		if desition == 1:
			while True:
				try:
					desition=int(input("""
0 to return
1 to move east
2 to move west
"""))
					if desition in [0,1,2]:
						break
					else:
						inputcorect()
				except:
					inputcorect()
			if desition	== 0:
				return "f2"
			elif desition == 1:
				return "fo1"
			elif desition == 2:
				return "fe3"
def feld3():
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	while True:
		print("you are in a feald")
		while True:
			try:
				if luck > 0:
					luck -=1
				desition = int(input(f"""would you like to 
1 to move
2 to serach for loot
3 to use item: """))
				if desition in [1,2,3]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition == 3:
			itera = 0	
			prinitera = 0
			use = []
			user = []
			print("your items you can use")
			print("0 to return")
			for x in lootunseen:
				if "c" in x or "h" in x:
					prinitera += 1
					print(prinitera,end=" to use: ")
					print(loot[itera])
					use.append(loot[itera])
					user.append(itera)
				itera += 1
			while True:
				try:
					inp = int(input("what do you want to use: "))
					print(len(use))
					if inp <= itera and inp >-1:
						break
					else:
						print("nope")
				except:
					print("nope")
				if inp == 0:
					break
			try:
				if "l" in use[inp-1]:
					luck += int(use[inp-1][len(use[inp-1]) - 1:])
					loot.pop(loot[user[inp-1]])
					lootunseen.pop(lootunseen[user[inp-1]])
					print(f"you use the luck potion")
			except:
				print("error 404: item not found")
		if desition == 2:
			if looted[2]==False:
				looted[2]=True
				temp = getloot(2)
				loot.append(temp)
				print(f"you got a {temp}")
			else:
				print("you dont find anything")
		if desition == 1:
			while True:
				try:
					desition=int(input("""
0 to return
1 to move east
2 to move north
"""))
					if desition in [0,1,2]:
						break
					else:
						inputcorect()
				except:
					inputcorect()
			if desition	== 0:
				return "fe3"
			elif desition == 1:
				return "fe2"
			elif desition == 2:
				return "f"
def feld4():
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	while True:
		print("you are in a feald")
		while True:
			try:
				if luck > 0:
					luck -=1
				desition = int(input(f"""would you like to 
1 to move
2 to serach for loot
3 to use item: """))
				if desition in [1,2,3]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition == 3:
			itera = 0
			prinitera = 0
			use = []
			user = []
			print("your items you can use")
			print("0 to return")
			for x in lootunseen:
				if "c" in x or "h" in x:
					prinitera += 1
					print(prinitera,end=" to use: ")
					print(loot[itera])
					use.append(loot[itera])
					user.append(itera)
				itera += 1
			while True:
				try:
					inp = int(input("what do you want to use: "))
					print(len(use))
					if inp <= itera and inp >-1:
						break
					else:
						print("nope")
				except:
					print("nope")
				if inp == 0:
					break
			try:
				if "l" in use[inp-1]:
					luck += int(use[inp-1][len(use[inp-1]) - 1:])
					loot.pop(loot[user[inp-1]])
					lootunseen.pop(lootunseen[user[inp-1]])
					print(f"you use the luck potion")
			except:
				print("error 404: item not found")
		if desition == 2:
			if looted[3]==False:
				looted[3]=True
				temp = getloot(1)
				loot.append(temp)
				print(f"you got a {temp}")
			else:
				print("you dont find anything")
		if desition == 1:
			while True:
				try:
					desition=int(input("""
0 to return
1 to move west
2 to move south
	"""))
					if desition in [0,1,2]:
						break
					else:
						inputcorect()
				except:
					inputcorect()
			if desition	== 0:
				return "fe4"
			elif desition == 1:
				print('you see a french catle and from inside you hear "hon hon hon" they also hate you so they dont let you in')
				return "fe4"
			elif desition == 2:
				return "f"
def feld5():
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	while True:
		print("you are in a feald")
		if monster[4] == True:
			if monbattle("flying snake") != "live":
				return "dead"
			monster[4] = False
		while True:
			try:
				if luck > 0:
					luck -=1
				print("you are in a feald")
				desition = int(input(f"""would you like to 
1 to move
2 to serach for loot
3 to use item: """))
				if desition in [1,2,3]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition == 3:
			itera = 0
			prinitera = 0
			use = []
			user = []
			print("your items you can use")
			print("0 to return")
			for x in lootunseen:
				if "c" in x or "h" in x:
					prinitera += 1
					print(prinitera,end=" to use: ")
					print(loot[itera])
					use.append(loot[itera])
					user.append(itera)
				itera += 1
			while True:
				try:
					inp = int(input("what do you want to use: "))
					print(len(use))
					if inp <= itera and inp >-1:
						break
					else:
						print("nope")
				except:
					print("nope")
				if inp == 0:
					break
			try:
				if "l" in use[inp-1]:
					luck += int(use[inp-1][len(use[inp-1]) - 1:])
					loot.pop(loot[user[inp-1]])
					lootunseen.pop(lootunseen[user[inp-1]])
					print(f"you use the luck potion")
			except:
				print("error 404: item not found")
		if desition == 2:
			if looted[4]==False:
				looted[4]=True
				temp = getloot(2)
				loot.append(temp)
				print(f"you got a {temp}")
			else:
				print("you dont find anything")
		if desition == 1:
			while True:
				try:
					desition=int(input("""
0 to return
1 to move east
2 to move west
"""))
					if desition in [0,1,2]:
						break
					else:
						inputcorect()
				except:
					inputcorect()
			if desition	== 0:
				return "fe5"
			elif desition == 1:
				return "fe6"
			elif desition == 2:
				return "fo1"
def feld6():
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	while True:
		print("you are in a feald")
		while True:
			try:
				if luck > 0:
					luck -=1
				desition = int(input(f"""would you like to 
1 to move
2 to serach for loot
3 to use item: """))
				if desition in [1,2,3]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition == 3:
			itera = 0
			prinitera = 0
			use = []
			user = []
			print("your items you can use")
			print("0 to return")
			for x in lootunseen:
				if "c" in x or "h" in x:
					prinitera += 1
					print(prinitera,end=" to use: ")
					print(loot[itera])
					use.append(loot[itera])
					user.append(itera)
				itera += 1
			while True:
				try:
					inp = int(input("what do you want to use: "))
					print(len(use))
					if inp <= itera and inp >-1:
						break
					else:
						print("nope")
				except:
					print("nope")
				if inp == 0:
					break
			try:
				if "l" in use[inp-1]:
					luck += int(use[inp-1][len(use[inp-1]) - 1:])
					loot.pop(loot[user[inp-1]])
					lootunseen.pop(lootunseen[user[inp-1]])
					print(f"you use the luck potion")
			except:
				print("error 404: item not found")
		if desition == 2:
			if looted[5]==False:
				looted[5]=True
				temp = getloot(2)
				loot.append(temp)
				print(f"you got a {temp}")
			else:
				print("you dont find anything")
		if desition == 1:
			while True:
				try:
					desition=int(input("""
0 to return
1 to move west
2 to move north
"""))
					if desition in [0,1,2]:
						break
					else:
						inputcorect()
				except:
					inputcorect()
			if desition	== 0:
				return "fe6"
			elif desition == 1:
				return "fe5"
			elif desition == 2:
				return "fo2"
def foothills1():
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	while True:
		while True:
			try:
				if luck > 0:
					luck -=1
				desition = int(input(f"""would you like to 
1 to move
2 to serach for loot
3 to use item: """))
				if desition in [1,2,3]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition == 3:
			itera = 0
			prinitera = 0
			use = []
			user = []
			print("your items you can use")
			print("0 to return")
			for x in lootunseen:
				if "c" in x or "h" in x:
					prinitera += 1
					print(prinitera,end=" to use: ")
					print(loot[itera])
					use.append(loot[itera])
					user.append(itera)
				itera += 1
			while True:
				try:
					inp = int(input("what do you want to use: "))
					print(len(use))
					if inp <= itera and inp >-1:
						break
					else:
						print("nope")
				except:
					print("nope")
				if inp == 0:
					break
			try:
				if "l" in use[inp-1]:
					luck += int(use[inp-1][len(use[inp-1]) - 1:])
					loot.pop(loot[user[inp-1]])
					lootunseen.pop(lootunseen[user[inp-1]])
					print(f"you use the luck potion")
			except:
				print("error 404: item not found")
		if desition == 2:
			if looted[6]==False:
				looted[6]=True
				temp = getloot(3)
				loot.append(temp)
				print(f"you got a {temp}")
			else:
				print("you dont find anything")
		if desition == 1:
			while True:
				try:
					desition=int(input("""
	0 to return
	1 to move north
	2 to move south
	3 to move east
	4 to move west
	"""))
					if desition in [0,1,2,3,4]:
						break
					else:
						inputcorect()
				except:
					inputcorect()
			if desition	== 0:
				return "fo1"
			elif desition == 1:
				return "m1"
			elif desition == 2:
				return "fe1"
			elif desition == 3:
				return "fe5"
			elif desition == 4:
				return "fe2"
def foothills2():
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	while True:
		print("you are in some foothills")
		while True:
			try:
				if luck > 0:
					luck -=1
				desition = int(input(f"""would you like to 
1 to move
2 to serach for loot
3 to use item: """))
				if desition in [1,2,3]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition == 3:
			itera = 0
			prinitera = 0
			use = []
			user = []
			print("your items you can use")
			print("0 to return")
			for x in lootunseen:
				if "c" in x or "h" in x:
					prinitera += 1
					print(prinitera,end=" to use: ")
					print(loot[itera])
					use.append(loot[itera])
					user.append(itera)
				itera += 1
			while True:
				try:
					inp = int(input("what do you want to use: "))
					print(len(use))
					if inp <= itera and inp >-1:
						break
					else:
						print("nope")
				except:
					print("nope")
				if inp == 0:
					break
			try:
				if "l" in use[inp-1]:
					luck += int(use[inp-1][len(use[inp-1]) - 1:])
					loot.pop(loot[user[inp-1]])
					lootunseen.pop(lootunseen[user[inp-1]])
					print(f"you use the luck potion")
			except:
				print("error 404: item not found")
		if desition == 2:
			if looted[7]==False:
				looted[7]=True
				temp = getloot(2)
				loot.append(temp)
				print(f"you got a {temp}")
			else:
				print("you dont find anything")
		if desition == 1:
			while True:
				try:
					desition=int(input("""
0 to return
1 to move south
2 to move east
"""))
					if desition in [0,1,2]:
						break
					else:
						inputcorect()
				except:
					inputcorect()
			if desition	== 0:
				return "fo2"
			elif desition == 1:
				return "fe6"
			elif desition == 2:
				return "fo3"
def foothills3():
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	while True:
		print("you are in some foothills")
		while True:
			try:
				if luck > 0:
					luck -=1
				desition = int(input(f"""would you like to 
1 to move
2 to serach for loot
3 to use item: """))
				if desition in [1,2,3]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition == 3:
			itera = 0
			prinitera = 0
			use = []
			user = []
			print("your items you can use")
			print("0 to return")
			for x in lootunseen:
				if "c" in x or "h" in x:
					prinitera += 1
					print(prinitera,end=" to use: ")
					print(loot[itera])
					use.append(loot[itera])
					user.append(itera)
				itera += 1
			while True:
				try:
					inp = int(input("what do you want to use: "))
					print(len(use))
					if inp <= itera and inp >-1:
						break
					else:
						print("nope")
				except:
					print("nope")
				if inp == 0:
					break
			try:
				if "l" in use[inp-1]:
					luck += int(use[inp-1][len(use[inp-1]) - 1:])
					loot.pop(loot[user[inp-1]])
					lootunseen.pop(lootunseen[user[inp-1]])
					print(f"you use the luck potion")
			except:
				print("error 404: item not found")
		if desition == 2:
			if looted[8]==False:
				looted[8]=True
				temp = getloot(2)
				loot.append(temp)
				print(f"you got a {temp}")
			else:
				print("you dont find anything")
		if desition == 1:
			while True:
				try:
					desition=int(input("""
0 to return
1 to move east
2 to move west
"""))
					if desition in [0,1,2]:
						break
					else:
						inputcorect()
				except:
					inputcorect()
			if desition	== 0:
				return "fo3"
			elif desition == 1:
				return "s1"
			elif desition == 2:
				return "fo2"
def forest():
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	while True:
		print("you are in a forest")
		if monster[9] == True:
			if monbattle("killer bunny") != "live":
				return "dead"
			monster[9] = False
		while True:
			try:
				if luck > 0:
					luck -=1
				print("you are in a forest")
				desition = int(input(f"""would you like to 
1 to move
2 to serach for loot
3 to use item: """))
				if desition in [1,2,3]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition == 3:
			itera = 0
			prinitera = 0
			use = []
			print("your items you can use")
			print("0 to return")
			for x in lootunseen:
				if "c" in x or "h" in x:
					prinitera += 1
					print(prinitera,end=" to use: ")
					print(loot[itera])
					use.append(loot[itera])
					user.append(itera)
				itera += 1
			while True:
				try:
					inp = int(input("what do you want to use: "))
					print(len(use))
					if inp <= itera and inp >-1:
						break
					else:
						print("nope")
				except:
					print("nope")
				if inp == 0:
					break
			try:
				if "l" in use[inp-1]:
					luck += int(use[inp-1][len(use[inp-1]) - 1:])
					loot.pop(loot[user[inp-1]])
					lootunseen.pop(lootunseen[user[inp-1]])
					print(f"you use the luck potion")
			except:
				print("error 404: item not found")
		if desition == 2:
			if looted[9]==False:
				looted[9]=True
				temp = getloot(3)
				loot.append(temp)
				print(f"you got a {temp}")
			else:
				print("you dont find anything")
		if desition == 1:
			while True:
				try:
					desition=int(input("""
0 to return
1 to move north
2 to move south
"""))
					if desition in [0,1,2]:
						break
					else:
						inputcorect()
				except:
					inputcorect()
			if desition	== 0:
				return "f"
			elif desition == 1:
				return "fe4"
			elif desition == 2:
				return "fe3"
def swamp1():
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	while True:
		print("you are in a swamp")
		while True:
			try:
				if luck > 0:
					luck -=1
				desition = int(input(f"""would you like to 
1 to move
2 to serach for loot
3 to use item: """))
				if desition in [1,2,3]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition == 3:
			itera = 0
			prinitera = 0
			use = []
			user = []
			print("your items you can use")
			print("0 to return")
			for x in lootunseen:
				if "c" in x or "h" in x:
					prinitera += 1
					print(prinitera,end=" to use: ")
					print(loot[itera])
					use.append(loot[itera])
					user.append(itera)
				itera += 1
			while True:
				try:
					inp = int(input("what do you want to use: "))
					print(len(use))
					if inp <= itera and inp >-1:
						break
					else:
						print("nope")
				except:
					print("nope")
				if inp == 0:
					break
			try:
				if "l" in use[inp-1]:
					luck += int(use[inp-1][len(use[inp-1]) - 1:])
					loot.pop(loot[user[inp-1]])
					lootunseen.pop(lootunseen[user[inp-1]])
					print(f"you use the luck potion")
			except:
				print("error 404: item not found")
		if desition == 2:
			if looted[10]==False:
				looted[10]=True
				temp = getloot(3)
				loot.append(temp)
				print(f"you got a {temp}")
			else:
				print("you dont find anything")
		if desition == 1:
			while True:
				try:
					desition=int(input("""
0 to return
1 to move north
2 to move west
"""))
					if desition in [0,1,2]:
						break
					else:
						inputcorect()
				except:
					inputcorect()
			if desition	== 0:
				return "s1"
			elif desition == 1:
				return "s3"
			elif desition == 2:
				return "fo3"
def swamp2():
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	while True:
		print("you are in a swamp")
		while True:
			try:
				if luck > 0:
					luck -=1
				desition = int(input(f"""would you like to 
1 to move
2 to serach for loot
3 to use item: """))
				if desition in [1,2,3]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition == 3:
			itera = 0
			prinitera = 0
			use = []
			user = []
			print("your items you can use")
			print("0 to return")
			for x in lootunseen:
				if "c" in x or "h" in x:
					prinitera += 1
					print(prinitera,end=" to use: ")
					print(loot[itera])
					use.append(loot[itera])
					user.append(itera)
				itera += 1
			while True:
				try:
					inp = int(input("what do you want to use: "))
					print(len(use))
					if inp <= itera and inp >-1:
						break
					else:
						print("nope")
				except:
					print("nope")
				if inp == 0:
					break
			try:
				if "l" in use[inp-1]:
					luck += int(use[inp-1][len(use[inp-1]) - 1:])
					loot.pop(loot[user[inp-1]])
					lootunseen.pop(lootunseen[user[inp-1]])
					print(f"you use the luck potion")
			except:
				print("error 404: item not found")
		if desition == 2:
			if looted[11]==False:
				looted[11]=True
				temp = getloot(2)
				loot.append(temp)
				print(f"you got a {temp}")
			else:
				print("you dont find anything")
		if desition == 1:
			while True:
				try:
					desition=int(input("""
0 to return
1 to move south
2 to move west
"""))
					if desition in [0,1,2]:
						break
					else:
						inputcorect()
				except:
					inputcorect()
			if desition	== 0:
				return "s2"
			elif desition == 1:
				return "s3"
			elif desition == 2:
				return "m2"
def swamp3():
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	while True:
		print("you are in a swamp")
		if monster[13]==True:
			monster[13]==False
			if monbattle("shreck") != "live":
				return "dead"
		while True:
			try:
				if luck > 0:
					luck -=1
				print("you are in a swamp")
				desition = int(input(f"""would you like to 
1 to move
2 to serach for loot
3 to use item: """))
				if desition in [1,2,3]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition == 3:
			itera = 0
			prinitera = 0
			use = []
			user = []
			print("your items you can use")
			print("0 to return")
			for x in lootunseen:
				if "c" in x or "h" in x:
					prinitera += 1
					print(prinitera,end=" to use: ")
					print(loot[itera])
					use.append(loot[itera])
					user.append(itera)
				itera += 1
			while True:
				try:
					inp = int(input("what do you want to use: "))
					print(len(use))
					if inp <= itera and inp >-1:
						break
					else:
						print("nope")
				except:
					print("nope")
				if inp == 0:
					break
			try:
				if "l" in use[inp-1]:
					luck += int(use[inp-1][len(use[inp-1]) - 1:])
					loot.pop(loot[user[inp-1]])
					lootunseen.pop(lootunseen[user[inp-1]])
					print(f"you use the luck potion")
			except:
				print("error 404: item not found")
		if desition == 2:
			print("you dont find anything")
		if desition == 1:
			while True:
				try:
					desition=int(input("""
0 to return
1 to move north
2 to move south
"""))
					if desition in [0,1,2]:
						break
					else:
						inputcorect()
				except:
					inputcorect()
			if desition	== 0:
				return "s3"
			elif desition == 1:
				return "s1"
			elif desition == 2:
				return "s2"
def mountan1():
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	while True:
		print("you are in a mouantan")
		while True:
			try:
				if luck > 0:
					luck -=1
				desition = int(input(f"""would you like to 
1 to move
2 to serach for loot
3 to use item: """))
				if desition in [1,2,3]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition == 3:
			itera = 0
			prinitera = 0
			use = []
			user = []
			print("your items you can use")
			print("0 to return")
			for x in lootunseen:
				if "c" in x or "h" in x:
					prinitera += 1
					print(prinitera,end=" to use: ")
					print(loot[itera])
					use.append(loot[itera])
					user.append(itera)
				itera += 1
			while True:
				try:
					inp = int(input("what do you want to use: "))
					print(len(use))
					if inp <= itera and inp >-1:
						break
					else:
						print("nope")
				except:
					print("nope")
				if inp == 0:
					break
			try:
				if "l" in use[inp-1]:
					luck += int(use[inp-1][len(use[inp-1]) - 1:])
					loot.pop(loot[user[inp-1]])
					lootunseen.pop(lootunseen[user[inp-1]])
					print(f"you use the luck potion")
			except:
				print("error 404: item not found")
		if desition == 2:
			if looted[14]==False:
				looted[14]=True
				temp = getloot(3)
				loot.append(temp)
				print(f"you got a {temp}")
			else:
				print("you dont find anything")
		if desition == 1:
			while True:
				try:
					desition=int(input("""
0 to return
1 to move north
2 to move south
"""))
					if desition in [0,1,2]:
						break
					else:
						inputcorect()
				except:
					inputcorect()
			if desition	== 0:
				return "m1"
			elif desition == 1:
				return "bod"
			elif desition == 2:
				return "fo1"
def mountan2():
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	while True:
		print("you are in a mouantan")
		while True:
			try:
				if luck > 0:
					luck -=1
				desition = int(input(f"""would you like to 
	1 to move
	2 to serach for loot
	3 to use item: """))
				if desition in [1,2,3]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition == 3:
			itera = 0
			prinitera = 0
			use = []
			user = []
			print("your items you can use")
			print("0 to return")
			for x in lootunseen:
				if "c" in x or "h" in x:
					prinitera += 1
					print(prinitera,end=" to use: ")
					print(loot[itera])
					use.append(loot[itera])
					user.append(itera)
				itera += 1
			while True:
				try:
					inp = int(input("what do you want to use: "))
					print(len(use))
					if inp <= itera and inp >-1:
						break
					else:
						print("nope")
				except:
					print("nope")
				if inp == 0:
					break
			try:
				if "l" in use[inp-1]:
					luck += int(use[inp-1][len(use[inp-1]) - 1:])
					loot.pop(loot[user[inp-1]])
					lootunseen.pop(lootunseen[user[inp-1]])
					print(f"you use the luck potion")
			except:
				print("error 404: item not found")
		if desition == 2:
			if looted[15]==False:
				looted[15]=True
				temp = getloot(3)
				loot.append(temp)
				print(f"you got a {temp}")
			else:
				print("you dont find anything")
		if desition == 1:
			while True:
				try:
					desition=int(input("""
	0 to return
	1 to move east
	2 to move west
	"""))
					if desition in [0,1,2]:
						break
					else:
						inputcorect()
				except:
					inputcorect()
			if desition	== 0:
				return "m21"
			elif desition == 1:
				return "s2"
			elif desition == 2:
				return "m3"
def mountan3():
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	while True:
		print("you are in a mouantan")
		if monster[16] == True:
			if monbattle("dragon") != "live":
				return "dead"
			monster[16] = False
		while True:
			try:
				if luck > 0:
					luck -=1
				print("you are in a mouantan")
				desition = int(input(f"""would you like to 
1 to move
2 to serach for loot
3 to use item: """))
				if desition in [1,2,3]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition == 3:
			itera = 0
			prinitera = 0
			use = []
			user = []
			print("your items you can use")
			print("0 to return")
			for x in lootunseen:
				if "c" in x or "h" in x:
					prinitera += 1
					print(prinitera,end=" to use: ")
					print(loot[itera])
					use.append(loot[itera])
					user.append(itera)
				itera += 1
			while True:
				try:
					inp = int(input("what do you want to use: "))
					print(len(use))
					if inp <= itera and inp >-1:
						break
					else:
						print("nope")
				except:
					print("nope")
				if inp == 0:
					break
			try:
				if "l" in use[inp-1]:
					luck += int(use[inp-1][len(use[inp-1]) - 1:])
					loot.pop(loot[user[inp-1]])
					lootunseen.pop(lootunseen[user[inp-1]])
					print(f"you use the luck potion")
			except:
				print("error 404: item not found")
		if desition == 2:
			if looted[16]==False:
				looted[16]=True
				temp = getloot(3)
				loot.append(temp)
				print(f"you got a {temp}")
			else:
				print("you dont find anything")
		if desition == 1:
			while True:
				try:
					desition=int(input("""
0 to return
1 to move east
2 to move west
"""))
					if desition in [0,1,2]:
						break
					else:
						inputcorect()
				except:
					inputcorect()
			if desition	== 0:
				return "m3"
			elif desition == 1:
				return "m2"
			elif desition == 2:
				return "m4"
def mountan4():
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	while True:
		print("you are in a mouantan")
		while True:
			try:
				if luck > 0:
					luck -=1
				desition = int(input(f"""would you like to 
	1 to move
	2 to serach for loot
	3 to use item: """))
				if desition in [1,2,3]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition == 3:
			itera = 0
			prinitera = 0
			use = []
			user = []
			print("your items you can use")
			print("0 to return")
			for x in lootunseen:
				if "c" in x or "h" in x:
					prinitera += 1
					print(prinitera,end=" to use: ")
					print(loot[itera])
					use.append(loot[itera])
					user.append(itera)
				itera += 1
			while True:
				try:
					inp = int(input("what do you want to use: "))
					print(len(use))
					if inp <= itera and inp >-1:
						break
					else:
						print("nope")
				except:
					print("nope")
				if inp == 0:
					break
			try:
				if "l" in use[inp-1]:
					luck += int(use[inp-1][len(use[inp-1]) - 1:])
					loot.pop(loot[user[inp-1]])
					lootunseen.pop(lootunseen[user[inp-1]])
					print(f"you use the luck potion")
			except:
				print("error 404: item not found")
		if desition == 2:
			if looted[17]==False:
				looted[17]=True
				temp = getloot(2)
				loot.append(temp)
				print(f"you got a {temp}")
			else:
				print("you dont find anything")
		if desition == 1:
			while True:
				try:
					desition=int(input("""
0 to return
1 to move east
2 to move west
"""))
					if desition in [0,1,2]:
						break
					else:
						inputcorect()
				except:
					inputcorect()
			if desition	== 0:
				return "m4"
			elif desition == 1:
				return "m3"
			elif desition == 2:
				return "m5"
def mountan5():
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	while True:
		print("you are in a mouantan")
		if monster[18] == True:
			if monbattle("robot") != "live":
				return "dead"
			monster[18] = False
		while True:
			try:
				if luck > 0:
					luck -=1
				print("you are in a mouantan")
				desition = int(input(f"""would you like to 
1 to move
2 to serach for loot
3 to use item: """))
				if desition in [1,2,3]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition == 3:
			itera = 0
			prinitera = 0
			use = []
			user = []
			print("your items you can use")
			print("0 to return")
			for x in lootunseen:
				if "c" in x or "h" in x:
					prinitera += 1
					print(prinitera,end=" to use: ")
					print(loot[itera])
					use.append(loot[itera])
					user.append(itera)
				itera += 1
			while True:
				try:
					inp = int(input("what do you want to use: "))
					print(len(use))
					if inp <= itera and inp >-1:
						break
					else:
						print("nope")
				except:
					print("nope")
				if inp == 0:
					break
			try:
				if "l" in use[inp-1]:
					luck += int(use[inp-1][len(use[inp-1]) - 1:])
					loot.pop(loot[user[inp-1]])
					lootunseen.pop(lootunseen[user[inp-1]])
					print(f"you use the luck potion")
			except:
				print("error 404: item not found")
		if desition == 2:
			if looted[18]==False:
				looted[18]=True
				temp = getloot(3)
				loot.append(temp)
				print(f"you got a {temp}")
			else:
				print("you dont find anything")
		if desition == 1:
			while True:
				try:
					desition=int(input("""
0 to return
1 to move east
2 to move west
"""))
					if desition in [0,1,2]:
						break
					else:
						inputcorect()
				except:
					inputcorect()
			if desition	== 0:
				return "m5"
			elif desition == 1:
				return "m4"
			elif desition == 2:
				return "g1"
def glich1():
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	while True:
		print("you take 5 damage from the enviorment you are in a giched planes")
		health-=5
		if monster[19] == True:
			if monbattle("robot") != "live":
				return "dead"
			monster[19] = False
		while True:
			try:
				if luck > 0:
					luck -=1
				print("you are in giched planes")
				desition = int(input(f"""would you like to 
1 to move
2 to serach for loot
3 to use item: """))
				if desition in [1,2,3]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition == 3:
			itera = 0
			prinitera = 0
			use = []
			user = []
			print("your items you can use")
			print("0 to return")
			for x in lootunseen:
				if "c" in x or "h" in x:
					prinitera += 1
					print(prinitera,end=" to use: ")
					print(loot[itera])
					use.append(loot[itera])
					user.append(itera)
				itera += 1
			while True:
				try:
					inp = int(input("what do you want to use: "))
					print(len(use))
					if inp <= itera and inp >-1:
						break
					else:
						print("nope")
				except:
					print("nope")
				if inp == 0:
					break
			if "l" in use[inp-1]:
				luck += int(use[inp-1][len(use[inp-1]) - 1:])
				loot.pop(use.index(use[inp-1]))
				lootunseen.pop(use.index(use[inp-1]))
				print(f"you use the luck potion")
		if inp == 3:
			itera = 0
			prinitera = 0
			use = []
			user = []
			print("your items you can use")
			print("0 to return")
			for x in lootunseen:
				if "c" in x or "h" in x:
					prinitera += 1
					print(prinitera,end=" to use: ")
					print(loot[itera])
					use.append(loot[itera])
					user.append(itera)
				itera += 1
			while True:
				try:
					inp = int(input("what do you want to use: "))
					print(len(use))
					if inp <= itera and inp >-1:
						break
					else:
						print("nope")
				except:
					print("nope")
				if inp == 0:
					break
			try:
				if "l" in use[inp-1]:
					luck += int(use[inp-1][len(use[inp-1]) - 1:])
					loot.pop(loot[user[inp-1]])
					lootunseen.pop(lootunseen[user[inp-1]])
					print(f"you use the luck potion")
			except:
				print("error 404: item not found")
		if desition == 2:
			if looted[19]==False:
				looted[19]=True
				temp = getloot(3)
				loot.append(temp)
				print(f"you got a {temp}")
			else:
				print("you dont find anything")
		if desition == 1:
			while True:
				try:
					desition=int(input("""
0 to return
1 to move north
2 to move east
	"""))
					if desition in [0,1,2]:
						break
					else:
						inputcorect()
				except:
					inputcorect()
			if desition	== 0:
				return "g1"
			elif desition == 1:
				return "g2"
			elif desition == 2:
				return "m5"
def glich2():## end of hard coded squares
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	while True:
		print("you take 5 damage from the enviorment you are in a giched planes")
		health-=5
		if monster[20] == True:
			if monbattle("robot") != "live":
				return "dead"
			monster[20] = False
		while True:
			try:
				if luck > 0:
					luck -=1
				print("you are in giched planes")
				desition = int(input(f"""would you like to 
1 to move
2 to serach for loot
3 to use item: """))
				if desition in [1,2,3]:
					break
				else:
					inputcorect()
			except:
				inputcorect()
		if desition == 3:
			itera = 0
			prinitera = 0
			use = []
			user = []
			print("your items you can use")
			print("0 to return")
			for x in lootunseen:
				if "c" in x or "h" in x:
					prinitera += 1
					print(prinitera,end=" to use: ")
					print(loot[itera])
					use.append(loot[itera])
					user.append(itera)
				itera += 1
			while True:
				try:
					inp = int(input("what do you want to use: "))
					print(len(use))
					if inp <= itera and inp >-1:
						break
					else:
						print("nope")
				except:
					print("nope")
				if inp == 0:
					break
			try:
				if "l" in use[inp-1]:
					luck += int(use[inp-1][len(use[inp-1]) - 1:])
					loot.pop(loot[user[inp-1]])
					lootunseen.pop(lootunseen[user[inp-1]])
					print(f"you use the luck potion")
			except:
				print("error 404: item not found")
		if desition == 2:
			if looted[20]==False:
				looted[20]=True
				temp = getloot(2)
				loot.append(temp)
				print(f"you got a {temp}")
			else:
				print("you dont find anything")
		if desition == 1:
			while True:
				try:
					desition=int(input("""
0 to return
1 to move west
2 to move south
"""))
					if desition in [0,1,2]:
						break
					else:
						inputcorect()
				except:
					inputcorect()
			if desition	== 0:
				return "g2"
			elif desition == 1:
				return "gc"
			elif desition == 2:
				return "g1"
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################
def bod():#no looky status:no bugs
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	nam = input("""you come to a rope bridge spanning a casum and a man stops you and says "Stop. Who would cross the Bridge of Death must answer me these questions three, ere the other side he see. What... is your name: """)
	if nam.lower != name.lower:
		print("wrong *as you are thrown into the casum")
		print("you die and aliens take your body and are diapointed that you cant play poker")
		print("wrong *as you are thrown into the casum*")
		print("you die and aliens take your body and are disappointed that you cant play poker")
		print("game over")
		raise "dead"
	else:
		nam = str(input("What... is your quest: ")).lower
		if nam != "To seek the Holy Grail":
			print("wrong *as you are thrown into the casum*")
			print("you die and are turned into a lemon")
			print("game over")
			return "dead"
		if playedmount >1:
			nam = input("What... is the air-speed velocity of an unladen swallow: ").lower
			if nam == "What do you mean? An African or a European swallow?".lower:
				print(" Huh? I... I don't know that. AUUUUUUUGGGGGGGGGGGHHH!!")
				print("you sucsesfully make it across the bridge")
				print(" Huh? I... I don't know that. AUUUUUUUGGGGGGGGGGGHHH!! *as he is thrown into the casum*")
				print("you successfully make it across the bridge")
				return "m5"
			else:
				print("wrong *as you are thrown into the casum")
				print("you die and joe takes your apendix")
				print("wrong *as you are thrown into the casum*")
				print("you die and a goat gives you a wet willy")
				print("game over")
				return "dead"
		else:
			nam = input("What... is your favourite colour: ").lower
			nam = input("What... is your favorite colour: ").lower
			if nam != coller:
				print("wrong *as you are thrown into the casum*")
				print("you die and billy the bird makes you into a nest")
				print("game over")
				return "dead"
			else:
				print("you may pass")
				print("you make it across the bridge")
				return "m5"
def glichcidicel():#no looky status:no bugs
	print("you see a programer")
	print("the programer says")
	print("so you want the holy grail")
	print("you'll have to go thru me")
	return "final battle"
def finalbattle():#status: not made
	depth = 0
	side = 9
	while True:
		move = 9	
		move = getkey()
		if move == 0:
			side += 1
		if move == 1:
			side -= 1
		depth += 1
		if checkcolison(side,depth) == 'dead':
			break
		elif checkcolison(side,depth) == "grail":
			return checkcolison(side,depth)
	print("game over")
	return "dead"
def getkey():
	tty.setcbreak(sys.stdin.fileno())
	b = os.read(sys.stdin.fileno(),3).decode()
	if len(b) == 3:
		k = ord(b[2])
	else:
		k = ord(b)
	key_mapping = {
		67: 0,
		68: 1
	}
	return key_mapping.get(k, chr(k))
def checkcolison(x,y):
	global dropmap
	prinrow =[]
	iteration = -1
	for z in dropmap[y]:
		iteration+=1
		if iteration == x:
			prinrow.append("█")
		else:
			prinrow.append(z)
	for w in range(100):
		print()
	for a in dropmap[y-2]:
		print(a,end="")
	print()
	for a in dropmap[y-1]:
		print(a,end="")
	print()
	for a in prinrow:
		print(a,end="")
	print()
	for a in dropmap[y+1]:
		print(a,end="")
	print()
	for a in dropmap[y+2]:
		print(a,end="")
	print()
	for a in dropmap[y+3]:
		print(a,end="")
	print()
	for a in dropmap[y+4]:
		print(a,end="")
	print()
	for a in dropmap[y+5]:
		print(a,end="")
	print()
	for a in dropmap[y+6]:
		print(a,end="")
	print()
	if dropmap[y][x] == "=":
		return "dead"
	elif dropmap[y][x] == "]" or dropmap[y][x] == "[]" or dropmap[y][x] == "/" or dropmap[y][x] == "\\" or dropmap[y][x] == "|":
		return "grail"
	else:
		return 
def grail():#status:no bugs
	print("you made it to the grail good job")
	return "win"
def inputcorect():#status: no bugs
	print("thats not a valid input ",end="")
	if random.randint(1,10):
		print("so a troll throws you into lava...")
		time.sleep(1)
		print("just kidding just input a valid input")
	else:
		print()
	return random.randint(1,20) < 14,random.randint(1,20)
def intro():#status:no bugs
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	exoshtion = 0
	rations = 5
	monkilled = False
	pythonbridge = False
	win = False
	loot = [f"hp{20}"]
	gameover = False
	name = ""
	playedmount = 0
	health = 100
	coller = ""
	gointor = 1
	lootunseen = []
	while gointor != 2000:
		for x in range(random.randint(1,gointor)):
			print("  ",end="")
		for x in range(round(gointor/20+1)):
			print([0,1][random.randint(0,1)],end = "")
		print()
		time.sleep(random.uniform(0,3/gointor))
		gointor+=1
	for x in range(300):
			print()
	return questens()
def questens():#status:no bugs
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	name = input("whats your name adventurer (type your name then press enter to continue): ")
	coller = input(f"hello {name} whats your favorite color: ")
	print(f"""hello {name} who likes the color {coller}, your quest is "To seek the Holy Grail" good luck""")
	return "fe4"
def main():#status:no bugs
	global exoshtion
	global gameover
	global rations
	global monkilled
	global pythonbridge
	global win
	global loot
	global name
	global playedmount
	global health
	global coller
	global lootunseen
	global monlist
	global movopt
	global damagebuff
	global rpg
	global len_loot
	global luck
	global gunseen
	global nunseen
	global runseen
	global looted
	global monster
	global good
	global norm
	global rearer
	while input("do you want to play (y/n): ") == "y":
		exoshtion = 0
		gameover = False
		rations = 5
		monkilled = False
		pythonbridge = False
		win = False
		loot = ["hp+20"]
		name = ""
		playedmount = 0
		health = 100
		coller = ""
		lootunseen = ["h20"]
		monlist = ["skeleton","mummy","giant lizard","dragon","flying snake","killer bunny","wannabe coder"]
		movopt = []
		damagebuff = 1
		rpg=0
		len_loot = -1
		luck = 0
		gunseen = ["cg","","h50","","","l7","l2"]
		nunseen = ["","","h10","cd","l1","l2"]
		runseen = ["","","h20","","","l3","l4"]
		looted = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
		monster = [None,None,None,None,True,None,None,None,None,True,None,None,None,True,None,None,True,None,True,True,True,None,True,None]
		good = ['holy hand gernade one use insta kill','rpg once per battle 20 damage at begining','heth + 50 potion','Sten MK II tends to misfire sometimes has buletts bounce off of tagert +20% damage','Apache Revolver you can use it like a gun (terible aim) a nife (way to flexible) or a iron fist (the only safe way to use it) +30% damage','pickled lepercon head +1 luck for 7 turns','luck potion +1 luck for 2 turns']
		norm = ["nuke (you cant use it cuse it will kill evorything and evoryone including you)","stick + 3% damage",'helth + 10 porion','deodorant (shreck wants it)','luck charm +1 luck for a turn','luck potion +1 luck for 2 turns']
		rearer = ['a peace of a lemon','sord + 10% damage','helth + 20 prtion','slingshot +5% damage','a 15 foot long pole','clover +1 luck for 3 turns','luck potion +1 luck for 4 turns']
		go = intro()
		while True:
			if go == "dead":
				break
			if go == "fe1":
				go =feld1()
				continue
			if go == "fe2":
				go =feld2()
				continue
			if go == "fe3":
				go =feld3()
				continue
			if go == "fe4":
				go =feld4()
				continue
			if go == "fe5":
				go =feld5()
				continue
			if go == "fe6":
				go =feld6()
				continue
			if go == "fo1":
				go =foothills1()
				continue
			if go == "fo2":
				go =foothills2()
				continue
			if go == "fo3":
				go =foothills3()
				continue
			if go == "f":
				go =forest()
				continue
			if go == "s1":
				go =swamp1()
				continue
			if go == "s2":
				go =swamp2()
				continue
			if go == "s3":
				go =swamp3()
				continue
			if go == "m1":
				go =mountan1()
				continue
			if go == "m2":
				go =mountan2()
				continue
			if go == "m3":
				go =mountan3()
				continue
			if go == "m4":
				go =mountan4()
				continue
			if go == "m5":
				go =mountan5()
				continue
			if go == "g1":
				go =glich1()
				continue
			if go == "g2":
				go =glich2()
				continue
			if go == "bod":
				go =bod()
				continue
			if go == "grail":
				go =grail()
				continue
			if go == "win":
				break
			if go == "die":
				break
main()
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG
#UUUUUGGGGGGGGGGGGGGG