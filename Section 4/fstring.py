template="Dear {} , you are awesome . Take {} $ dollar"

a="Harry"
a1=10000
b="Sg"
b1=20000
c="Ss"
c1=30000

s1=template.format(a,a1)
print(s1) # Output: Dear Harry , you are awesome . Take 10000 $ dollar
s2=template.format(b,b1)
s3=template.format(c,c1)

print(f"{a} you are awesome.Take this{a1} $ dollar bag.")