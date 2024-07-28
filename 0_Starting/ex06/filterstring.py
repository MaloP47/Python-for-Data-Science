import sys
from ft_filter import ft_filter

"""Filterstring program"""


def main():
    """Main function"""
    try:
        ac = len(sys.argv)
        if ac != 3 or (ac == 3 and not sys.argv[2].isdigit()):
            raise AssertionError("the arguments are bad")
        S = sys.argv[1]
        N = int(sys.argv[2])
        if not isinstance(S, str) or not isinstance(N, int):
            raise AssertionError("the arguments are bad")
        print(list(ft_filter(lambda word: len(word) > N, S.split())))
        # print(list(filter(lambda word: len(word) > N, S.split())))
        # print([word for word in S.split() if len(word) > N])
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
