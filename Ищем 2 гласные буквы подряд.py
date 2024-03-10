vowels = 'aeiou'

s = 'aertiooikjoaikl'

n = len(s)

for i in range(n-1):
    if s[i] in vowels and s[i+1] in vowels:
        print(s[i],s[i+1])