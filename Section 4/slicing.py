name="Harry0123456789"

# slicing ..
print(name[0:2]) # from 0 to 2-1..so 0 to 1..so it will print Ha..
print(name[0:4]) # from 0 to 4-1..so 0 to 3..so it will print Harr..
print(name[2:-1]) # as same as [2:4] from 2 to 5-1..so 2 to 4..so it will print rr..

print(name[0:10:1]) # skip n-1 characters..so it will print Harry0123..
print(name[0:10:2]) # skip n-1 means 2-1 =1  characters..hry13
print(name[0:10:3]) # skip n-1 means 3-1 =2 characters..ho24

print(name[:4]) # replace empty no with 0
print(name[4:]) # replace empty no with last no..so it will print 0123456789..