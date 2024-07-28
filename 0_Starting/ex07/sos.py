import sys

"""Morse encoder"""


def strToMorse(s: str) -> str:
    """Returns a new string converted in morse from s"""
    NESTED_MORSE = {
        " ": "/ ", "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ",
        "E": ". ", "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ",
        "J": ".--- ", "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ",
        "O": "--- ", "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ",
        "T": "- ", "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ",
        "Y": "-.-- ", "Z": "--.. ", "0": "----- ", "1": ".---- ",
        "2": "..--- ", "3": "...-- ", "4": "....- ", "5": "..... ",
        "6": "-.... ", "7": "--... ", "8": "---.. ", "9": "----. "}

    morse = ""
    for letter in s.upper():
        morse += NESTED_MORSE[letter]
    return morse


def main():
    """Main function"""
    try:
        if len(sys.argv) != 2 or not sys.argv[1]\
                or not sys.argv[1].replace(' ', '').isalnum()\
                or not isinstance(sys.argv[1], str):
            raise AssertionError("the arguments are bad")
        s = sys.argv[1]
        print(strToMorse(s))
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
