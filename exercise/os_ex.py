import os

os.chdir(("c:/"))
dir = os.popen(("dir"))

print(dir)
print(dir.read())