# Criação do dicionário meu_dicionario
meu_dicionario = {
    "codigo_1": "Python",
    "codigo_2": "Java",
    "codigo_3": "PHP"
}

# Imprimindo o conteúdo do dicionário
print("Conteúdo do dicionário:", meu_dicionario)

# Imprimindo o tipo de dados do dicionário
print("Tipo de dados do dicionário:", type(meu_dicionario))

# Utilizando o método get para imprimir o valor da chave "linguagem"
linguagem = meu_dicionario.get("codigo_1")
print("Valor da chave 'codigo_1':", linguagem)

# Imprimindo o tamanho do dicionário
print("Tamanho do dicionário:", len(meu_dicionario))

# Criação de um novo dicionário aninhado chamado dicionario_frutas
dicionario_frutas = {
    1: {"nome": "limão", "tipo": "ácida"},
    2: {"nome": "laranja", "tipo": "ácida"},
    3: {"nome": "manga", "tipo": "semiácida"},
    4: {"nome": "maçã", "tipo": "semiácida"},
    5: {"nome": "banana", "tipo": "doce"},
    6: {"nome": "mamão", "tipo": "doce"}
}

# Imprimindo o valor das chaves "nome" e "tipo" da chave 1
print("Chave 1 - Nome:", dicionario_frutas[1]["nome"], "- Tipo:", dicionario_frutas[1]["tipo"])

# Imprimindo o valor das chaves "nome" e "tipo" da chave 2
print("Chave 2 - Nome:", dicionario_frutas[2]["nome"], "- Tipo:", dicionario_frutas[2]["tipo"])

# Iterando no dicionário dicionario_frutas e imprimindo os valores das chaves "nome" e "tipo"
for chave, valor in dicionario_frutas.items():
    print(f"Chave {chave} - Nome: {valor['nome']} - Tipo: {valor['tipo']}")