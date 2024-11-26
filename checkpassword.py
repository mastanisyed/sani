def cp(s,n):
     if n<4:
          return 0
     if s[0].isdigit():
          return 0
     con=0
     num=0
     for i in range(n) :
          if s[i]>='A' and s[i]<='Z':
               con+=1
          if s[i]=='' and s[i]=='/':
               return 0
          elif s[i].isdigit():
               num+=1
     if num>0 and con>0:
          return 1
     else:
          return 0
s=input()
n=len(s)
print(cp(s,n))
