import numpy as np
import random
import projeto
from projeto import matriz
import plota as plt

# Número de disciplinas
num_disciplinas = len(matriz)

# Construir o grafo
grafo = [[] for _ in range(num_disciplinas)]
projeto.restricaoSemestre(grafo)
for i in range(num_disciplinas):
    for j in range(i + 1, num_disciplinas):
        # Verificar se as disciplinas i e j são ministradas pelo mesmo professor
        for k in range(len(matriz[0])):
            if matriz[i][k] != 0 and matriz[j][k] != 0:
                # Adicionar uma aresta entre as disciplinas i e j
                grafo[i].append(j)
                grafo[j].append(i)
                break

# ------------------------------------------------------#

def verificaCh(disciplina):
    for i in range(len(matriz[disciplina])):
        if matriz[disciplina][i] > 0:
            CH = matriz[disciplina][i]
    return CH


# Matriz, dicionários e função completaMatriz() omitidos para simplificar
atribuicoes = {}


def verificaRestricao(disciplina, atribuicoes, dia, horario):
    count = 0
    # Itera sobre os valores de dias e horários já atribuidos (se chegou a 6)
    for atribuicao in atribuicoes.values():
        # Se for uma lista, compara com os valores de dia e horário
        if isinstance(atribuicao, list):
            for tupla in atribuicao:
                if tupla[0] == dia and tupla[1] == horario:
                    count += 1
        # Senão, olha para a segunda tupla de dia e horário alocada (a primeira já foi contada anteriormente)
        else:
            if atribuicao[0][0] == dia and atribuicao[0][1] == horario:
                count += 1
    # Caso o valor seja igual a 6 retorna true para gerar outro valor de dia e horário
    if count >= 6:
        return True

    # Aloca todas as disciplinas de uma determinada disciplina
    restricoes = grafo[disciplina]
    for restricao in restricoes:
        # Se a restrição tiver na atribuições, é sinal que já foi alocado dia e horário pra ela então deve-se verificar
        if restricao in atribuicoes:
            atribuicao_restricao = atribuicoes[restricao]
            # Mesma lógica na comparação feita acima (do count <= 6)
            if isinstance(atribuicao_restricao, list):
                for tupla in atribuicao_restricao:
                    if tupla[0] == dia and tupla[1] == horario:
                        return True
            else:
                if atribuicao_restricao[0][0] == dia and atribuicao_restricao[0][1] == horario:
                    return True
    # Caso nenhuma restrição tenha sido encontrada, retorna false indicando que aquele dia e horário podem ser alocados
    return False


# Listas para armazenar os dias de alocação de cada disciplina
dias_disciplinas = [[] for _ in range(num_disciplinas)]


matriz = projeto.completaMatriz(matriz)

dias_semana = list(projeto.semana.keys())

horarios = list(projeto.horarios.keys())

# Foi feito a partição dos horários para melhor compreensão e eficiência do algoritmo
horario_sin = [6, 7]
horarios_cco = [1, 2, 3, 4]
horarios_triplos = [1, 4]  # de cco

for key, disciplina in projeto.disciplinas.items():
    # Hora e dia são 'vazios' no começo de cada iteração
    hora1 = None
    hora2 = None
    dia1 = None
    dia2 = None
    # Indica que a disciplina não é exclusiva do curso de sin, portanto deve ser atribuída para o horário integral (horarios_cco)
    if disciplina[0] != 'S':
        while True:
            # Escolhe dias e horários aleatórios para melhor espalhamento das aulas, e menor concentração
            dia = random.choice(dias_semana)
            hora = random.choice(horarios_cco)
            # Verifica a carga horária da disciplina e faz as devidas atribuições, chamando a função que verifica se aquele dia e horário são permitidos
            # Caso contrário, continua o while para gerar outro dia e horário até que não tenha restrições
            if verificaCh(key) == 2:
                if verificaRestricao(key, atribuicoes, dia, hora):
                    continue
                else:
                    dia1 = dia
                    hora1 = hora
                    break

            elif verificaCh(key) == 3:
                hora = random.choice(horarios_triplos)
                if verificaRestricao(key, atribuicoes, dia, hora):
                    continue
                else:
                    dia1 = dia
                    if hora == 1:
                        hora1 = 0, 1
                        break
                    elif hora == 4:
                        hora1 = hora, 5
                        break

            elif verificaCh(key) == 4:
                if verificaRestricao(key, atribuicoes, dia, hora):
                    continue
                else:
                    if dia1 is None:
                        dia1 = dia
                        hora1 = hora
                        continue
                    if dia2 is None and dia != dia1:
                        dia2 = dia
                        hora2 = hora
                        break
                    else:
                        continue

            elif verificaCh(key) == 5:
                if verificaRestricao(key, atribuicoes, dia, hora):
                    continue
                else:
                    if dia1 is None:
                        dia1 = dia
                        hora1 = hora
                    dia = random.choice(dias_semana)
                    hora = random.choice(horarios_triplos)
                    if verificaRestricao(key, atribuicoes, dia, hora):
                        continue
                    else:
                        if dia1 == dia:
                            continue
                        else:
                            if hora == 1:
                                dia2 = dia
                                hora2 = 0, hora
                            elif hora == 4:
                                hora2 = hora, 5
                                break
    # Indica que a disciplina é exclusiva de sin, portanto deve ser alocada para a noite
    # Mesma lógica empregada para disciplinas integrais
    else:
        while True:
            dia = random.choice(dias_semana)
            hora = random.choice(horario_sin)

            if verificaCh(key) == 2:
                if verificaRestricao(key, atribuicoes, dia, hora):
                    continue
                else:
                    dia1 = dia
                    hora1 = hora
                    break

            elif verificaCh(key) == 3:
                if verificaRestricao(key, atribuicoes, dia, hora):
                    continue
                else:
                    dia1 = dia
                    hora1 = hora
                    break

            elif verificaCh(key) == 4:
                if verificaRestricao(key, atribuicoes, dia, hora):
                    continue
                else:
                    if dia1 is None:
                        dia1 = dia
                        hora1 = hora
                        continue
                    if dia2 is None and dia != dia1:
                        dia2 = dia
                        hora2 = hora
                        break
                    else:
                        continue

            elif verificaCh(key) == 5:
                if verificaRestricao(key, atribuicoes, dia, hora):
                    continue
                else:
                    if dia1 is None:
                        dia1 = dia
                        hora1 = hora
                    dia = random.choice(dias_semana)
                    hora = 7
                    if verificaRestricao(key, atribuicoes, dia, hora):
                        continue
                    else:
                        if dia1 == dia:
                            continue
                        else:
                            dia2 = dia
                            hora2 = hora, 8
                            break
    # Se dia2 for vazio, a disciplina só precisa de um dia e horário, caso contrário, aloca os dois dias e horários para ela
    if dia2 is None:
        atribuicoes[key] = [(dia1, hora1)]
    else:
        atribuicoes[key] = [(dia1, hora1), (dia2, hora2)]

# Impressão das disciplinas e seus horários
for disciplina, horarios in enumerate(atribuicoes):
    print(
        f"Disciplina {projeto.disciplinas[disciplina]}: Horarios: {atribuicoes[horarios]}")

