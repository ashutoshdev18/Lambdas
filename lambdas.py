print("Lambda expressions are simply another way to create functions")

print("Syntax:", end=" ")
print(' lambda [parameter list]: expression')

print("Examples")

sq_func = lambda x: x ** 2

add_func = lambda x,y: x + y

hello_func = lambda: "hello"

reverse_str = lambda s: s[::-1]

print("lambdas are not closures")

print(sq_func(2))
print(add_func(10, 12))
print(hello_func())
print(reverse_str("Virat Kohli"))

print("Lambdas also can be as argument to another functions")


def apply_lambda_func(x, cube_fn):
    return cube_fn(x)

print(apply_lambda_func(3, lambda x: x ** 3))

print("Disadvantages of Lambda")
print("No assignments, No annotations, Single line expression")


l = [1, 90, 4, 2, 6, -1, 0]
sorted(l)
#sorted() -> doesn't mean inplace sorting
print(l)


# map(func, *iterables) -> applies function func to the iterables

l = [2, 3, 5]

def sq(x):
    return x * x

res = list(map(sq, l))
print(res)


def add(x, y):
    return x + y
l1 = [2, 5, 7]
l2 = [4, 6, 9]
res = list(map(add, l1, l2))
print(res)


# filter(func, iterable) -> returns the element if true else False

def is_even(n):
    return n % 2 == 0
l = [2, 4, 6, 9, 10, 11, 15, 16]
res = list(filter(is_even, l))
print(res)


#zip function takes multiple iterables and return single iterable

# [1, 2, 3, 4] [10, 20, 30, 40] -> (1, 10), (2, 20), (3, 30), (4, 40)

# [1, 2, 3, 4, 5]
# [10, 20, 30] -> ends when the shortest list ends at (3, 30)


l1 = range(100)
l2 = 'abcd'

print(list(zip(l1, l2)))

l3 = [65, 66, 67, 68, 69, 70, 71, 72, 73]
l4 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
l5 = 'python course'
print(list(zip(l3, l4, l5)))

print("LIST COMPREHENSIONS")
l = [1, 2, 3, 4, 5]
print([x ** 2 for x in l])

l = [1, 2, 3, 4, 5]
l1 = [6, 7, 8, 9, 10]

print([x + y for x, y in zip(l, l1)])

print("[<expression> for <varname> in <iterable> if <expression>]")
