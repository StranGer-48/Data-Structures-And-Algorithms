# Primitive Types in Python
Python has several built-in types: numeric, sequence, mapping, as well as classes, instances, and exceptions. All instances of these types are objects. Integers in Python3 are unbounded - the maximum integer representable is a function of the available memory. The constant sys.maxsize can be used to find the word-size; specifically, it's the maximum value integer that can be stored in the word, e.g., 2**63 -1 on a 64-bit machine. Bounds on floats are specified in sys.float_info.
1. Be very familiar with the bit-wise operations such as AND, OR, LEFT SHIFT, RIGHT SHIFT, NEGATION, XOR.
2. The key method for numeric type are abs(a,b), math.ceil(a.b), math.floor(a.b), min(a,b), max(a,b), pow(a,b)(alternatively, a**b), and math.sqrt(a).
3. Know how to interconvert integers and string e.g., str(42), int('42'), floats and string e.g., str(3.14) and float('3.14').
4. Unlike integers, floats are not infinite precision, and it's convenient to refer to infinity as a float('inf') and float('-inf'). These values are comparable to integers and can be used to create pseudo-max-int and pseudo-min-int.
5. Comparing floating-point values consider using math.isclose() - it is robust, when comparing very large values, and can handle both absolute and relative differences.
6. The key methods in random are random.randrange(a), random.randint(a,b), random.random(), random.shuffle(A), random.choice(A).

## Note
