from collections import OrderedDict

'''
Input: String, special characters allowed.
Output: Most common letter (special characters ir whitespace not counted). In case of multiple same frequencies, returns
letter first in alphabet.


Task (from Checkio):
You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a".
Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet.
'''


def checkio(str):
    ord_dict = OrderedDict([('a', 0), ('b', 0), ('c', 0), ('d', 0), ('e', 0), ('f', 0), ('g', 0), ('h', 0), ('i', 0),
                            ('j', 0), ('k', 0), ('l', 0), ('m', 0), ('n', 0), ('o', 0), ('p', 0), ('q', 0), ('r', 0),
                            ('s', 0), ('t', 0), ('u', 0), ('v', 0), ('w', 0), ('x', 0), ('y', 0), ('z', 0)])

    for character in str.lower():
        if character.isalpha():
            ord_dict[character] = str.lower().count(character)

    return max(ord_dict, key=lambda key: ord_dict[key])


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
