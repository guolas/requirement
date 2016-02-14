"""
Get the number of variables and the number of requirements
"""
n, m = [int(jj) for jj in input().strip().split(" ")]

"""
Get the requirements
"""
r = []
for ii in range(m):
    x, y = [int(jj) for jj in input().strip().split(" ")]
    r.append([x, y])

count = 0
for ii in range(int(10**n)):
    current_values = list("{:014d}".format(ii))[-n:]
    meet = True
    for jj in range(m):
        if current_values[r[jj][0]] > current_values[r[jj][1]]:
            meet = False
            break
    if meet:
        count += 1

print(str(count%1007))
