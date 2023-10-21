# Function to get the XOR of two integers
def getXOR(a, b):
    return a ^ b

# Function to check and return the c'th bit of d
def getBit(c, d):
    return (d >> c) & 1

# Function to set the e'th bit in f if it is not set
def setBit(e, f):
    # Check if the e'th bit is not set (0)
    if (f & (1 << e)) == 0:
        # Set the e'th bit (1)
        f |= (1 << e)
    return f

# Example usage
a = 1
b = 2
c = 1
d = 3
e = 2
f = 3

# Calculate XOR of a and b
xor_result = getXOR(a, b)
print("XOR Result:", xor_result)

# Check if the 2nd bit of d is set
bit_result = getBit(c, d)
print("Bit Result:", bit_result)

# Set the 1st bit in f if not set
setBit_result = setBit(e, f)
print("Set Bit Result:", setBit_result)