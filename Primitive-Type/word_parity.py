def parityBruteForce(x):
    result = 0
    while x:
        result ^=  x & 1
        x >>= 1
    return result
    
    
def parityLastSetBit(x):
    result = 0
    while x:
        result ^=  1
        x &= x-1 # Drops the lowest set of x.
    return result


def paritySubwords(x):
    mask_size = 16
    bit_mask = 0xFFFF
    return (parityLastSetBit(x >> (3*mask_size)) ^
            parityLastSetBit((x >> (2*mask_size)) & bit_mask) ^
            parityLastSetBit((x >> mask_size) & bit_mask) ^
            parityLastSetBit(x >> bit_mask))
            

def parityXORed(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1


if __name__ == '__main__':
    x = 1274849
    print("/nParity of a word using Brute-Force method./n", partityBruteForce(x))
    print("/nParity of a word using Erasing Last Set Bit./n", parityLastSetBit(x))
    print("/nParity of a word using Subwords./n", paritySubwords(x))
    print("/nParity of a word using XORed approach./n", parityXORed(x))
