#append to an existing file called john.txt..
# add data about his home ..
f=open("John.txt","a") # add the data..

string='''
john live in medinipur , wb ..
'''
f.write(string)

f.close()