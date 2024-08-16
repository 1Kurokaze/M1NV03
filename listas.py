# Criação da lista mesclada
lista_mesclada = [1, 2, 3, "Olá, Python", True, 12.6]
print("Conteúdo da lista:", lista_mesclada)

# Adicionando uma lista aninhada usando o método append
lista_mesclada.append(["Lista aninhada"])
print("Conteúdo da lista após append:", lista_mesclada)

# Inserindo o número 5 na posição 4
lista_mesclada.insert(4, 5)
print("Conteúdo da lista após insert:", lista_mesclada)

# Imprimindo o tamanho atual da lista
print("Tamanho da lista:", len(lista_mesclada))

# Removendo o item da posição 1
lista_mesclada.pop(1)
print("Conteúdo da lista após remover o item da posição 1:", lista_mesclada)

# Criando uma nova lista com os primeiros 4 elementos
nova_lista_mesclada = lista_mesclada[:4]
print("Conteúdo da nova lista mesclada:", nova_lista_mesclada)