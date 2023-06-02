a, b = input().split()
a = int(a)
b = int(b)

sa = input().split()
sb = input().split()

i = 0
while len(sb) > 0 and i < len(sa) and sb[0] in sa:
    if sa[i] == sb[0]:
        sb.remove(sb[0])
    i += 1

if len(sb) == 0:
    print("S")
else:
    print("N")


# a, b = input().split()
# a = int(a)
# b = int(b)

# sa = input().split()
# sb = input().split()
# sa = [int(i) for i in sa]
# sb = [int(i) for i in sb]

# i = 0
# for _ in sa:
#     if len(sb) == 0:
#         break
#     elif _ == sb[0]:
#         sb.remove(sb[0])

# if len(sb) == 0:
#     print("S")
# else:
#     print("N")