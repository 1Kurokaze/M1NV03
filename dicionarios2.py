# Criação do dicionário inicial
meu_dicionario = {
    1: {'nome': 'Maria', 'idade': 26, 'nacionalidade': 'brasileira'}
}

# Utilizando o método update para adicionar novos elementos
meu_dicionario.update({
    2: {'nome': 'João', 'idade': 30, 'nacionalidade': 'português'},
    3: {'nome': 'Ana', 'idade': 22, 'nacionalidade': 'espanhola'}
})

# Imprimindo o dicionário atualizado
print("Dicionário atualizado:", meu_dicionario)

# Criando uma cópia do dicionário
copia_dicionario = meu_dicionario.copy()

# Removendo um elemento com pop e imprimindo o conteúdo
elemento_removido = meu_dicionario.pop(2)
print("Elemento removido (chave 2):", elemento_removido)
print("Dicionário após remoção com pop:", meu_dicionario)

# Removendo o último elemento com popitem e imprimindo o conteúdo
elemento_removido_final = meu_dicionario.popitem()
print("Último elemento removido com popitem:", elemento_removido_final)
print("Dicionário após remoção com popitem:", meu_dicionario)

# Removendo todos os elementos dos dicionários
meu_dicionario.clear()
copia_dicionario.clear()
print("Dicionário original após clear:", meu_dicionario)
print("Cópia do dicionário após clear:", copia_dicionario)

# Usando o método fromKeys para criar um novo dicionário
chaves = ['a', 'b', 'c']
novo_dicionario = dict.fromkeys(chaves, 'valor_padrao')

# Imprimindo o conteúdo do novo dicionário usando o método items
print("Conteúdo do novo dicionário (items):", novo_dicionario.items())

# Imprimindo apenas as chaves do novo dicionário usando o método keys
print("Chaves do novo dicionário:", novo_dicionario.keys())

# Imprimindo apenas os valores do novo dicionário usando o método values
print("Valores do novo dicionário:", novo_dicionario.values())