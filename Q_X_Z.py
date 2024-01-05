#Which of the letters Q, X, and Z is the least common?

fn = 'sowpods.txt'
fh = open(fn)

# q = 0
# x = 0
# z = 0

# for line in fh:
#     line = line.strip()
#     if 'Q' in line:
#         q += 1
#     if 'X' in line:
#         x += 1
#     if 'Z' in line:
#         z += 1
# if q < x < z:
#     print('Q')
# if x < q < z:
#     print(x)
# if z < q < x:
#     print(z)
# # if q <z<x:
#     # print('Q')

# # print(min(q,x,z))
# print(f' The least common letter is Q {q}')

fn = 'sowpods.txt'
fh = open(fn)

counts = {'Q': 0, 'X': 0, 'Z': 0}

for line in fh:
    line = line.strip()
    for letter in counts:
        counts[letter] += line.count(letter)

least_common_letter = min(counts, key=counts.get)