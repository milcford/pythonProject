text = 'ConvertToInt32'

for i in text:
    if i == i.upper():
        if i not in '1234567890':
            print(type(i))
            text = text.replace(i, '_' + i.lower())
print(text)