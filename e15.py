def arr_print(rows):
    print ("\n".join(["\t".join(map(str, row)) for row in rows]))
    return 0

n = 20
rows = [[0] * n for _ in range(n)]
# This was my incorrect first attempt: rows = [[[0] * n] * n]. 
# The outer lists are just a reference to the same inner list!

for i in range(len(rows)):
    for j in range(len(rows[0])):
        # This is a bit of a hack. It uses the fact that 
        # lst[-n] = lst[-n + len(lst)]. lst[-1] == lst[len(-1)]
        # Therefore, when accessing the items on the edge of a row or column,
        # it actually accesses the last array entry (i.e. i or j == 0). Since
        # this is initialised to 0, and the for loop is increasing, 
        # this evaluates to 0, and the max function sets it to 1
        rows[i][j] = max(1, rows[i - 1][j] + rows[i][j - 1])

arr_print(rows)
print (rows[-1][-1])
