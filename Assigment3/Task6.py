def middle_chars(s):
    length = len(s)
    if length == 0:
        return ""
    mid = length // 2
    if length % 2 == 1:          
        print(s[mid])
    else:                        
        print(s[mid-1:mid+1])

middle_chars(input('give me a string: '))