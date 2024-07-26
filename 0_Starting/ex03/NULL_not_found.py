import math

def NULL_not_found(object: any) -> int:
	if object is None:
		print(f'Nothing: None {type(object)}')
	elif isinstance(object, float) and math.isnan(object):
		print(f'Cheese: {object} {type(object)}')
	elif isinstance(object, int) and object is 0:
		print(f'Zero: {object} {type(object)}')
	elif isinstance(object, str) and not len(object):
		print(f'Empty: {object} {type(object)}')
	elif isinstance(object, bool) and object is False:
		print(f'Fake: {object} {type(object)}')
	# else:
	# 	print(f'Anything else: {object} {type(object)}')
	# 	return 1
	else:
		print('Type not found')
		return 1
	return 0
