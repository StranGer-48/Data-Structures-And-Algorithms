# Primitive Types in Python
Python has several built-in types: numeric, sequence, mapping, as well as classes, instances, and exceptions. All instances of these types are objects. Integers in Python3 are unbounded - the maximum integer representable is a function of the available memory. The constant sys.maxsize can be used to find the word-size; specifically, it's the maximum value integer that can be stored in the word, e.g., 2**63 -1 on a 64-bit machine. Bounds on floats are specified in sys.float_info.
1. Be very familiar with the bit-wise operations such as AND, OR, LEFT SHIFT, RIGHT SHIFT, NEGATION, XOR.
2. The key method for numeric type are abs(a,b), math.ceil(a.b), math.floor(a.b), min(a,b), max(a,b), pow(a,b)(alternatively, a**b), and math.sqrt(a).
3. Know how to interconvert integers and string e.g., str(42), int('42'), floats and string e.g., str(3.14) and float('3.14').
4. Unlike integers, floats are not infinite precision, and it's convenient to refer to infinity as a float('inf') and float('-inf'). These values are comparable to integers and can be used to create pseudo-max-int and pseudo-min-int.
5. Comparing floating-point values consider using math.isclose() - it is robust, when comparing very large values, and can handle both absolute and relative differences.
6. The key methods in random are random.randrange(a), random.randint(a,b), random.random(), random.shuffle(A), random.choice(A).

## Note
* Be very confortable with the bitwise operators, particularly XOR.
* Understand how to use masks and create them in a machine-independent way
* Know the fast way yo clear the loweermost set bit.
* Understand signedness and its implications to shifting.
* Consider using a cache to accelerate operations by using it to brute force algorithm.
* Be aware that commutativity and associativity can be used to perform operations in parallel and reorder operation.

**Q1. How would you compute the parity of a very large number of 64-bit words?**
**Solution:** 
**Brute Force Method:** The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, it is 0. The brute-force algorithm iteratively tests the value of each bit while tracking the number of 1s seen so far. Since we only care about the number of 1s is even or odd, we can store the number mod 2. The parity computation can be done using different algorithms other than the brute-force algorithm.

**Erasing Last Set Bit:** The first improvement is based on erasing the lowest set bit in a word in a single operation, thereby improving performance in the best and average case. Here is a great bit finding trick which=k you should commit to memory: x & (x-1) equal x with its lowest set bit erased. Here '&' is the bitwise operator. for example, if x = 00101100, then x-1 = 00101011, and so x&(x-1) = 00101100 & 00101011 = 00101000. This fact can be used to reduce the time complexity. 
  Let k be the number of bits set to1 in a particular word. Then the time complexity of the above algorithm is O(k).

**Subwords Method:** We now consider a qualitatively different approach. The problem statement refers to computing the parity for a very large number of words. when you have to perform a large number of parity computations, and, more generally, any kind of bit finding computations, two keys to performance are processing multiple bit at a time and caching results in an array-based lookup table. We compute the parity of a 64-bit integer by grouping its bits into four non-overlapping 16-bit subwords, computing the parity of each subword, and then computing the parity of these four sub results. 
   The time complexity is a function of the size of the keys used to index the lookup table, Let L be the width of the words for which we cache the results and n the words size. Since there are n/L terms, the time complexity is O(n/L), assuming word-level operations, such as shifting, take O(1) time.

**XORed Method:** We can improve on the O(n) worst-case time complexity of the previous algorithms by exploiting some simple properties of parity. Specifically, the XOR of two bits is defined to be 0 if both bits are 0 or both bits are 1; otherwise, it is 1. XOR has the property of being associative, i.e., it does not matter how we group bits, as well as commutative. i.e, the order in which we perform the XORs does not change the result. The XOR of a group of bits is its parity.
  We illustrate the approach with an 8-bit word. The parity of 11010111 is the same as the parity of 1101 XORed with 0111, i.e., of 1010. This in turn is the same as the parity of 10 XORed with 10 i.e., 00. The final result is the XOR of 0 with 0 i.e., 0.
  The time complexity is O(log n), where n is the word size. Note that we can combine caching with word-level operations, e.g., by doing a lookup in the XOR-based approach once we get to 16 bits.
