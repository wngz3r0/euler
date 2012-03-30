with open ('e13.txt') as f:
    lines = f.readlines()

lenLine = len(lines[0].strip()) 
columns = [0 for i in range(lenLine)]

for line in lines:
    nums = map(int, line.strip())
    columns = [sum(pair) for pair in zip(nums, columns)]

columns.reverse()
carry = 0
summation = []
for col in columns:
    col += carry
    remainder = col % 10
    carry = col // 10
    summation.append(remainder)

if carry > 0:
    summation.append(carry)

summation.reverse()
answer = ''.join(map(str,summation))
print (answer[:10])
