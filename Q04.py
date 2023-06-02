m_tipos, n_tamanhos = input().split()
m_tipos, n_tamanhos = int(m_tipos), int(n_tamanhos)
matrix = [[] for _ in range(m_tipos)]
# m linhas com n tamanhos

for i in range(m_tipos):
    descr = input().split()
    descr = [int(_) for _ in descr]
    for j in range(n_tamanhos):
        matrix[i].append(descr[j])

vendas = 0
p = int(input())
for _ in range(p):
    ptipo, ptam = input().split()
    ptipo, ptam = int(ptipo), int(ptam)
    if matrix[ptipo-1][ptam-1] > 0:
        matrix[ptipo-1][ptam-1] = matrix[ptipo-1][ptam-1]-1
        vendas += 1

#print(matrix)
print(vendas)
