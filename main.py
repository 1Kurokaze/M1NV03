from operacoes import calcular_media, verificar_reprovacao, alunos_reprovados

# Dados dos alunos
dados_alunos = {
    26: {"nome": "Maria", "notas": [8, 7, 5, 9]},
    101: {"nome": "Ana", "notas": [9, 9, 8, 9]},
    13: {"nome": "João", "notas": [6, 5, 5, 5]},
    37: {"nome": "Ágatha", "notas": [8, 6, 7.5, 9]},
    72: {"nome": "Joaquim", "notas": [6, 5.5, 5, 7]},
    5: {"nome": "Félix", "notas": [10, 8, 8, 8]}
}

# Lista de matrículas dos alunos reprovados
matriculas_reprovados = []

# Verificação da média e aprovação/reprovação de cada aluno
for matricula, dados in dados_alunos.items():
    media = calcular_media(dados["notas"])
    if verificar_reprovacao(media):
        matriculas_reprovados.append(matricula)

# Exibição dos alunos reprovados
alunos_reprovados(dados_alunos, matriculas_reprovados)