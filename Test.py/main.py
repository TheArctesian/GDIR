#import os
#print("Path at terminal when executing this file")
#print(os.getcwd() + "\n")
from pathlib import Path
import os

for root, dirs, files in os.walk("../", topdown=False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))
