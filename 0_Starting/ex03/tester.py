from NULL_not_found import NULL_not_found

Nothing = None
Garlic = float("NaN")
bread = float(3.14)
Zero = 0
Empty = ''
Fake = False

print('########################')
print(Garlic)
print(type(Garlic))
print(Garlic == Garlic)
print('########################')

NULL_not_found(Nothing)
NULL_not_found(Garlic)
print(NULL_not_found(bread))
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
