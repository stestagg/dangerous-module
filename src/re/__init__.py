import copy
import sys

sys.xxxx = copy.copy(sys.path)
sys.path = list(reversed(sys.path))
import sys
del sys.modules['re']

from re import *
import sys

sys.path = sys.xxxx