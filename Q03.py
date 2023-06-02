s, t = input().split()

lista_tuneis = []
for _ in range(int(t)):
    x, y = input().split()
    lista_tuneis.append((x, y)) #tupla

lista_caminhos = []
p = int(input())
for _ in range(p):
    x = input().split()
    x.remove(x[0])
    lista_caminhos.append(x) #lista

cont = 0

for caminho in lista_caminhos:
    c_valido = True

    for i in range(len(caminho)-1):
        if not (caminho[i], caminho[i+1]) in lista_tuneis and not (caminho[i+1], caminho[i]) in lista_tuneis:
            c_valido = False
            break

    if c_valido:
        cont += 1

print(cont)






# s, t = input().split()

# lista_tuneis = []
# for _ in range(int(t)):
#     x, y = input().split()
#     lista_tuneis.append((int(x), int(y))) #tupla

# lista_caminhos = []
# p = int(input())
# for _ in range(p):
#     x = input().split()
#     x = [int(_) for _ in x]
#     x.remove(x[0])
#     lista_caminhos.append(x) #lista

# cont = 0

# for caminho in lista_caminhos:
#     c_valido = True

#     for i in range(len(caminho)-1):
#         if not (caminho[i], caminho[i+1]) in lista_tuneis and not (caminho[i+1], caminho[i]) in lista_tuneis:
#             c_valido = False
#             break

#     if c_valido:
#         cont += 1

# print(cont)
