s=input()
print(len(s)-len(s.strip()))
print("no extra spaces" if s==s.strip() else "Extra spaces")