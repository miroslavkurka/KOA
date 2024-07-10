from collections import defaultdict, deque

# riesene podla prednasky 4 z KOA

# zapis v tvare
# vrchol povodu : [(koncovy vrchol, skore)]
edges = {

    1: [(2, 5), (3, 4), (4, 5), (5, 6)], 2: [(6, 1), (7, 2)], 3: [(7, 6)], 4: [(7, 5), (8, 5)], 5: [(8, 7), (9, 3)],
    6: [(10, 2), (11, 4)], 7: [(10, 3), (11, 5)], 8: [(11, 2)], 9: [(12, 4)], 10: [(11, 4), (12, 5)], 11: [(12, 1)],
    12: []}

num_nodes = 12
et = [0] * (num_nodes + 1)
lt = [float('inf')] * (num_nodes + 1)
lt[12] = 0

# zlozitost je O(V+E)
for v in range(1, num_nodes + 1):
    for u, length in edges[v]:
        et[u] = max(et[u], et[v] + length)

# najneskorsi cas v ulohe nebolo treba ale chcel som chcecknut cez tf kriticku cestu teda som ho pridal.
# tiez by malo byt v O(V+E)?
for v in range(num_nodes, 0, -1):
    for u, length in edges[v]:
        lt[v] = min(lt[v], lt[u] - length)

# kod dole je len check ci to funguje kedze plati veta:
# Nech D je AOA siet. Orientovana  s t-cesta je kriticka  prave vtedy, ked je to najdlhsia cesta z s do t.

critical_path = []
for v in range(1, num_nodes + 1):
    for u, length in edges[v]:
        # tf (i , j ) = lt (j ) - et (i )  - w(i , j )
        if lt[v] - et[v] - length == 0:
            critical_path.append((v, u, length))

print(f"Najdlhsia trailova trat (co je vlastne tzv. earliest time) : {et}")
print(f"Kriticka cesta: {critical_path}")
