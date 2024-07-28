from ft_filter import ft_filter

"""Tester for ft_filter"""

print('###############################')

print(type(ft_filter(None, [-2, -1, 0, 1, 2])))
print(type(filter(None, [-2, -1, 0, 1, 2])))

print(list(ft_filter(None, [-2, -1, 0, 1, 2])))
print(list(filter(None, [-2, -1, 0, 1, 2])))

print(tuple(ft_filter(None, [-2, -1, 0, 1, 2])))
print(tuple(filter(None, [-2, -1, 0, 1, 2])))

print('###############################')

print(list(ft_filter(lambda n: n > 0, [-2, -1, 0, 1, 2])))
print(list(filter(lambda n: n > 0, [-2, -1, 0, 1, 2])))

print(tuple(ft_filter(lambda n: n > 0, [-2, -1, 0, 1, 2])))
print(tuple(filter(lambda n: n > 0, [-2, -1, 0, 1, 2])))

print(set(ft_filter(lambda n: n > 0, [-2, -1, 0, 1, 2])))
print(set(filter(lambda n: n > 0, [-2, -1, 0, 1, 2])))

print('###############################')


def palindrome(word):
    rev = "".join(reversed(word))
    return word.lower() == rev.lower()


print(list(ft_filter(palindrome, ("Python", "Laval", "RaCecar", "Noel leon"))))
print(list(filter(palindrome, ("Python", "Laval", "RaCecar", "Noel leon"))))
