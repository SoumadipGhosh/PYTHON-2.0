import os

a = os.listdir("dir") # can acess the dir folder ..
print(a) 
print(os.getcwd())
print(os.path.exists("dir")) # true ..
os.remove("sam.txt") # actually delete the txt file ..
os.rmdir("") # only delete non reading file ..