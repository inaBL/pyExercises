'''
Numbers to text, Checkio.

All the words in the string must be separated by exactly one space character.
Be careful with spaces -- it's hard to see if you place two spaces instead one.

Input: A number as an integer.
Output: The string representation of the number as a string.

Precondition: 0 < number < 1000
'''

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]


def checkio(number):
    lst = []
    # 1-9
    if number < 10:
        lst.append(FIRST_TEN[number - 1])
    # 10-19
    elif 10 <= number < 20:
        lst.append(SECOND_TEN[int(str(number)[1])])
    # 20-90, full tens
    elif 20 <= number < 100 and str(number)[1] == '0':
        lst.append(OTHER_TENS[int(str(number)[0]) - 2])
    # 21-99, other numbers
    elif 20 <= number < 100 and str(number)[1] != '0':
        lst.append(OTHER_TENS[int(str(number)[0]) - 2])
        lst.append(FIRST_TEN[int(str(number)[1]) - 1])
    else:
        # full hundreds
        if str(number)[1] == '0' and str(number)[2] == '0':
            lst.append(FIRST_TEN[int(str(number)[0]) - 1])
            lst.append('hundred')
        # hundreds and under ten, e.g. 204
        elif str(number)[1] == '0':
            lst.append(FIRST_TEN[int(str(number)[0]) - 1])
            lst.append('hundred')
            lst.append(FIRST_TEN[int(str(number)[2]) - 1])
        # hundreds and tens, e.g. 310
        elif str(number)[1] == '1' and str(number)[2] == '0':
            lst.append(FIRST_TEN[int(str(number)[0]) - 1])
            lst.append('hundred')
            lst.append(SECOND_TEN[0])
        # hundreds and other full tens starting from 20, e.g. 120
        elif int(str(number)[1]) >= 2 and str(number)[2] == '0':
            lst.append(FIRST_TEN[int(str(number)[0]) - 1])
            lst.append('hundred')
            lst.append(OTHER_TENS[int(str(number)[1]) - 2])
        # hundreds and under 20, e.g. 312
        elif str(number)[1] == '1' and str(number)[2] != '0':
            lst.append(FIRST_TEN[int(str(number)[0]) - 1])
            lst.append('hundred')
            lst.append(SECOND_TEN[int(str(number)[2])])
        # hundreds and over 20, e.g. 133
        elif int(str(number)[1]) >= 2 and str(number)[2] != '0':
            lst.append(FIRST_TEN[int(str(number)[0]) - 1])
            lst.append('hundred')
            lst.append(OTHER_TENS[int(str(number)[1]) - 2])
            lst.append(FIRST_TEN[int(str(number)[2]) - 1])

    return ' '.join(lst)


if __name__ == '__main__':

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
