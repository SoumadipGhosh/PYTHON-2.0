a={2,3,4,5}
b={9,8,4,6}

# union .. add both a and b but no dublicates allow..
c=a.union(b) # 4 is dublicate so not print ..
print(c)

# intersection .. print common element ..
d=a.intersection(b) # 4 is only common element ..
print(d)