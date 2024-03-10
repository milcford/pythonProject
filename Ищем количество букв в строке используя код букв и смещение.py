s = 'asdfas dlkjba;skjdfn ;jklha;sdjfh kjh;kjH:JBH:KJJKHB:LJNH&68765765$^%$*&(*&)(*&)'
letters = [0] * 26
for i in s.lower():
    if i >= 'a' and i <= 'z':
        nomer = ord(i) - 97
        letters[nomer] += 1

for i in range(26):
    if letters[i] > 0:
        print(chr(i + 97), letters[i])
