import re
def isMatch(word, pattern):


    str = "hej"
    test_list = [print(x) for x in str]



    temp_word = list(word)
    temp_pattern = list(pattern)
    for x in range(0,len(pattern)):
        if pattern == '?':
            continue
        elif pattern[x] != '*':
            if pattern[x] != word[x]:
                return False
        else:

            print(1)



if __name__ == "__main__":
    #print(isMatch('aa', 'aa'))
    print(re.search("aa","$**^"))