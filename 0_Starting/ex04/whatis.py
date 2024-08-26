import sys


try:
    if len(sys.argv) == 1:
        sys.exit(1)
    if len(sys.argv) != 2:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")

    try:
        num = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as e:
    print(f"AssertionError: {e}")
    sys.exit(1)
