import re

def reverse(string):

    string = string.split(' ')

    new_string = ""
    for word in string:
        if word.isalnum()  or re.match('^[\w-]+$', word):
            new_string = new_string + word[::-1] + " "
        else:
            temp = ""
            for i in word:
                if not i.isalnum():
                    new_string += temp[::-1] + i
                    temp = ""
                else:
                    temp += i

            new_string = new_string + temp[::-1] + " "

    return new_string


string = raw_input()
print reverse(string)
