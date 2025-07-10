# write to a file john .txt

f=open("John.txt","w")

string='''
john is a gd guy . he like ml very much ..
'''
f.write(string)

f.close()