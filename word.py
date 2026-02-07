# function to  check weather
# first ad last character of the word match 
def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            
            ctr += 1
            lst.append(word)

    print("list of first with last and first character same\n", lst)
    return ctr
        
count = match_words(['abc', 'cfc','xyz', '1221'])
print("number of words having first and last character same", count)