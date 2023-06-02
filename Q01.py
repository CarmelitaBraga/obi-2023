def num_contas(v, a, f, p):
    if (a + f + p) <= v:
        return 3
    elif (a + f) <= v:
        return 2
    elif (a + p) <= v:
        return 2
    elif (f + p) <= v:
        return 2
    elif a <= v or f <= v or p <= v:
        return 1
    else:
        return 0
    
v = int(input())
a = int(input())
f = int(input())
p = int(input())

x = num_contas(v, a, f, p)
print(x)
