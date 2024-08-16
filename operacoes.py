def calcular_media(notas):
    """
    Calcula a média das notas recebidas.
    :param notas: Lista com as notas dos 4 bimestres.
    :return: Média das notas.
    """
    return sum(notas) / len(notas)

def verificar_reprovacao(media):
    """
    Verifica se o aluno foi reprovado com base na média.
    :param media: Média das notas do aluno.
    :return: True se a média for inferior a 6 (reprovado), False caso contrário.
    """
    return media < 6

def alunos_reprovados(dados_alunos, matriculas_reprovados):
    """
    Retorna a lista de alunos reprovados.
    :param dados_alunos: Dicionário com os dados dos alunos.
    :param matriculas_reprovados: Lista com as matrículas dos alunos reprovados.
    :return: Mensagem com os alunos reprovados.
    """
    for matricula in matriculas_reprovados:
        aluno = dados_alunos[matricula]
        media = calcular_media(aluno["notas"])
        print(f'Aluno Reprovado: {aluno["nome"]} – Matrícula: {matricula} – Média Final: {media:.2f}')