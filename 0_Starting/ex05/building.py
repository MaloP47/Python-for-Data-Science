"""
This module counts characters type in argv[1]
and prints the results
"""

import sys
import string


def countTypes(s: str) -> list[int]:

    """Function prototypes says it all..."""

    counts = [0, 0, 0, 0, 0]

    for character in s:
        if character.isupper():
            counts[0] += 1
        elif character.islower():
            counts[1] += 1
        elif character in string.punctuation:
            counts[2] += 1
        elif character.isspace():
            counts[3] += 1
        elif character.isdigit():
            counts[4] += 1
    return counts


def printTypes(toPrint: list[int]):

    """Print the stats of the string passed as parameter"""

    print(f"The text contains {sum(toPrint)} characters:\n\
{toPrint[0]} upper letters\n\
{toPrint[1]} lower letters\n\
{toPrint[2]} punctuation marks\n\
{toPrint[3]} spaces\n\
{toPrint[4]} digits")


def main():

    """Main function"""

    try:
        if len(sys.argv) < 2:
            try:
                s = input('What is the text to count?\n')
                s += '\n'
                printTypes(countTypes(s))
            except KeyboardInterrupt:
                print("\nUser interrupted the prompt")
            except EOFError:
                print("Input ended unexpectedly")
        elif len(sys.argv) == 2:
            s = sys.argv[1]
            printTypes(countTypes(s))
        else:
            raise ValueError("Wrong number of arguments")
    except Exception as e:
        print("Error: " + str(e))


if __name__ == "__main__":
    main()

# print(__doc__)
# print(countTypes.__doc__)
# print(printTypes.__doc__)
# print(main.__doc__)
