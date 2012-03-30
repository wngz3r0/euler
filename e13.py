with open ('e13.txt') as f:
    lines = f.readlines()

lenLine = len(lines[0].strip()) 
columns = [0 for i in range(lenLine)]

# First, convert every character in the line to a number
# Then add that to the previous sum, on a per-character basis
for line in lines:
    nums = map(int, line.strip())
    columns = list(map(sum, zip(nums, columns)))

# Now, columns is a list where each entry is the ith column.
# The sum is now (kn * 10^n) + (k(n-1) * 10 ^ (n-1)) + .... + k1
# Sum this up from the lowest bit, and carry the sum to the next column
columns.reverse()
carry = 0
summation = []
for col in columns:
    col += carry
    remainder = col % 10
    carry = col // 10
    summation.append(remainder)

# After the final column, there could still be left-over carry.
if carry > 0:
    summation.append(carry)

summation.reverse()
answer = ''.join(map(str,summation))
print (answer[:10])
