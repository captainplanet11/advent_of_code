data = open("input.txt").read().splitlines()


def has_repeated_pair(s):
    pairs = {}
    for i in range(len(s) - 1):
        pair = s[i:i+2]  
        if pair in pairs and pairs[pair] < i - 1:
            return True
        pairs[pair] = i  
    return False

def has_repeating_letter_with_gap(s):
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            return True
    return False

count =  0
for i in data:
    if has_repeated_pair(i) == True and has_repeating_letter_with_gap(i) == True:
        count += 1

print(count)
