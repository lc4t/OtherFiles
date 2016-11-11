A={}

code = open('code.tt','r').readlines()
for a in code:
    a = a.replace('*','').split()
    for i in range(0,len(a)//2,1):
        A[a[i+26]]=a[i]
# print A
coder = open('coder.tt','r').readlines()
coder = coder[0].split()

for i in coder:
    print (A[i],end='')