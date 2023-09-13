def to_jaden_case(string):
    lst = string.split()
    lst1 = []
    for word in lst:
        lst1.append(word.capitalize())
    return " ".join(lst1)


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))


# https://www.codewars.com/kata/54ff3102c1bad923760001f3/solutions/python
def getCount(inputStr):
    num_vowels = 0
    for char in inputStr:
        if char in "aeiouAEIOU":
            num_vowels = num_vowels + 1
    return num_vowels


# https://www.codewars.com/kata/54ff3102c1bad923760001f3/solutions/python
inputStr = "inputStr"
print(len(list(filter(lambda x: x in 'aeiouAEIOU', inputStr))))


def encode(string):
    new_string = ""
    for x in string.lower():
        if x.isalpha():
            new_string += str(ord(x) - 96)
        else:
            new_string += x
    return new_string


print(encode('ABCD'))

last = 'Knowles'
first = 'Beyonce'
print(f'Greetings, master {last[:3].capitalize() + first[:2].capitalize()}')
