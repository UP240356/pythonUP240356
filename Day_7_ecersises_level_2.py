A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#ejercicio 1
print(A.union(B))

#ejercicio 2
print(A.intersection(B))

#ejercicio 3
es_subconjunto=A.issubset(B)
if es_subconjunto:
    print('A es subconjunto de B')
else:
    print('A no es subconjunto de B')

#ejercicio 4
son_disjuntos=A.isdisjoint(B)
if son_disjuntos :
    print('A y b son conjuntos disjuntos')
else:
    print('A y B no son conjuntos disconjuntos')

#ejercicio 5
A_con_B= A.update(B)
B_con_A= B.update(A)
print('union de A con B',A_con_B)
print('union de B con A',B_con_A)

#ejercicio 6
diferencia_simetrica=A^B
print(diferencia_simetrica)

#ejercicio 7
del A
del B