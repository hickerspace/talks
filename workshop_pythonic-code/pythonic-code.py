# exponential notation
1e6

# multiply lists, strings
[1] * 5
"foo" * 3

# unpacking
a, b, c = (1, 2, 3)

# string/list slicing
"foo bar baz"[4]
"foo bar baz"[-1]
"foo bar baz"[:4]
"123456789"[::-1]
"123456789"[::-2]

# short if-else
facepalm = True if "m(" in "Was fürn mist m(" else False

# true if all elements are true
all([True, True, False])
all([True, True, True])

# true if at least one element is true
any([True, True, True])
any([True, True, False])

# execute funtion on all elements of iterable
map(str, range(10))

# filter elements for which given funktion returns true
def check(i):
	return i > 0
filter(check, [0, 8, -1, 9, -4])

# incrementing/decrementing etc.
a = 3
a += 1 # a++

# list comprehension
[i*3 for i in range(10)]
[i*3 for i in range(10) if i % 2 == 0]
words = 'The quick brown fox jumps over the lazy dog'.split()
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
{value: key for key, value in {"key1":"val1", "key2":"val2", "key3":"val3"}.items()}

# iterables vs generators vs generators + yield
gen = (x*x for x in range(5))
for x in gen: # works only once
	print x

# generating primes with yield
import sys
for i in range(sys.maxint):
	print i
for i in xrange(sys.maxint):
	print i
def genPrimes():
	for i in range(100):
		if all((True if i % div != 0 else False for div in range(2, i))):
			yield i

# awesome dictionaries with default function
mydict = {1: [86, 11], 2: [25, 67]}
mydict[3]
from collections import defaultdict
cooldict = defaultdict(list)
cooldict[3]
cooldict[9999].append("foo")

# with
with open("foo.txt") as f:
	for line in f:
		print f

# unpacking in positional arguments
def foo(a, b, c):
	print a, b, c
x = ("foo", "bar", "baz")
foo(*x)

# unpacking in named arguments
def foo(b="", a="", c=""):
    print a, b, c
x = {"a": "foo", "b": "bar", "c": "baz"}
foo(**x)

# dynamic function/method calls
def foo:
	print "yeah"
locals()["foo"]()
getattr(obj, "foo", ":(")()

