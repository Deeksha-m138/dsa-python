s=input()
x=s.upper()
count1=0
count2=0
for i in range(len(s)):
  if s[i]==x[i]:
    count1+=1
  else:
    count2+=1
print("No.of uppercase letters:",count1)
print("No.of lowercase letters:",count2)