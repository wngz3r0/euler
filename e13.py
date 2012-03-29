f = open ('e13.txt')
lines = f.readlines()
lenLine = len(lines[0]) - 1 # Don't count the newline
columns = [0 for i in range(lenLine)]
for line in lines:
    for i, c in enumerate(line):
        if c != '\n':
            columns[i] += int(c)

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
answer = ''
for i, val in enumerate(summation):
    strVal = str(val)
    answer += strVal
    i += len(strVal) # This coud be greater than 1 for the carry number
    if i >= 10:
        break

print (answer)
