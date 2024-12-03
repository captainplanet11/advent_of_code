data = open("input.txt").read().splitlines()


def has_three_vowels(s):
    vowels = 'aeiou'
    count = 0 
    for char in s:
        if char in vowels:
            count += 1
        if count == 3:
            return True
    return False 

def has_double_letters(s):
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            return True
    return False

def doesnot_contain(s):
    a = ['ab','cd','pq','xy']
    for i in a:
        if i in s:
            return False
    return True 

count = 0
for i in data:
    if has_three_vowels(i) == True and has_double_letters(i) == True and doesnot_contain(i) ==True:
        count += 1
    
print(count)