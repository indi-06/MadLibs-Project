import os
import time


print("MadLibs Final Project")
print("By Indigo Suh")
print()
answer = input("Ready to play? Type yes or no:  ")
if answer == "yes" or answer == "Yes" or answer == "yes." or answer == "yes." or answer == "Yes!" or answer == "yes!" :
  import random
  madlib=random.randint(1, 2)
  if madlib==1:
    import madlib1
  elif madlib==2:
    import madlib2
else:
    print("Okay! Have a nice day.")
    exit()


