import timeit

def test1():
	return [2, *(i for i in range(100))]

def test2():
	return [2] + list(i for i in range(100))

print(timeit.timeit("test1()", number=1000000, globals=globals()))
print(timeit.timeit("test2()", number=1000000, globals=globals()))
