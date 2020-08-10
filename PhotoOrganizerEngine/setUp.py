import os
import sys

root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
CommonPath = os.path.join(root, 'Common')
sys.path.insert(0, CommonPath)