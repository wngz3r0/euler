#!/usr/bin/python 
max = 1000
count = 0
for i in range(1, max):
    if (i % 3 == 0) or (i % 5 == 0):
        count += i
print count

multiples = filter(lambda n: n % 3  == 0 or n % 5 == 0, range(1000))
print reduce(lambda i, j: i + j, multiples)

print (reduce(lambda i, j: i + j, (filter(lambda n: n % 3  == 0 or n % 5 == 0, range(1000)))))

' This should just be syntactic sugar of the previous version'
print sum(filter(lambda n: n % 3  == 0 or n % 5 == 0, range(1000)))

