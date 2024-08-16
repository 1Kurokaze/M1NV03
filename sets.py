# Criação do set inicial
set_inicial = {11, 12, 13, 14}
print("Conteúdo do set inicial:", set_inicial)

# Adicionando o elemento 15 ao set
set_inicial.add(15)
print("Conteúdo do set após adicionar 15:", set_inicial)

# Atualizando o set com novos elementos
set_inicial.update([1, 2, 3, 4, 5])
print("Conteúdo do set após a atualização:", set_inicial)

# Removendo o elemento 13 do set
set_inicial.discard(13)
print("Conteúdo do set após remover o 13:", set_inicial)

# Criação de um novo set com o método set()
novo_set = set([20, 21, 23, 1, 2])
print("Conteúdo do novo set:", novo_set)

# União dos dois sets
uniao_sets = set_inicial.union(novo_set)
print("União dos dois sets:", uniao_sets)

# Interseção dos dois sets
intersecao_sets = set_inicial.intersection(novo_set)
print("Interseção dos dois sets:", intersecao_sets)

# Diferença entre os dois sets
diferenca_sets = set_inicial.difference(novo_set)
print("Diferença entre os dois sets:", diferenca_sets)

# Diferença simétrica entre os dois sets
diferenca_simetrica_sets = set_inicial.symmetric_difference(novo_set)
print("Diferença simétrica entre os dois sets:", diferenca_simetrica_sets)