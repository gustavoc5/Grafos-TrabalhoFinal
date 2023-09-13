import numpy as np

# Dicionário de dias da semana
semana = {
    2: 'Segunda',
    3: 'Terça',
    4: 'Quarta',
    5: 'Quinta',
    6: 'Sexta'
}

# Dicionário de horários
horarios = {
    0: "7h00 - 7h55",
    1: "7h55 - 9h45",
    2: "10h10 - 12h00",
    3: "13h30 - 15h20",
    4: "15h45 - 17h35",
    5: "17h35 - 18h30",
    6: "19h00 - 20h40",
    7: "21h00 - 22h40",
    8: "22h40 - 23h30"
}

# Define as restrições compreendidas de forma manual


def restricaoSemestre(grafo):
    grafo[0].extend([1, 2, 3, 22])
    grafo[1].extend([0, 2, 3, 22])
    grafo[2].extend([0, 1, 3, 22])
    grafo[3].extend([0, 1, 2, 22])
    grafo[4].extend([5, 6, 7, 8, 9, 25])
    grafo[5].extend([4, 6, 7, 8, 9, 25])
    grafo[6].extend([4, 5, 7, 8, 9, 25])
    grafo[7].extend([4, 5, 6, 8, 9, 25])
    grafo[8].extend([4, 5, 6, 7, 9, 25])
    grafo[9].extend([4, 5, 6, 7, 8, 25])
    grafo[10].extend([11, 12, 13, 14, 15, 16])
    grafo[11].extend([10, 12, 13, 14, 15, 16])
    grafo[12].extend([10, 11, 13, 14, 15, 16])
    grafo[13].extend([10, 11, 12, 14, 15, 16])
    grafo[14].extend([10, 11, 12, 13, 15, 16])
    grafo[15].extend([10, 11, 12, 13, 14, 16])
    grafo[16].extend([10, 11, 12, 13, 14, 15])
    grafo[17].extend([18, 19, 20, 21])
    grafo[18].extend([17, 19, 20, 21])
    grafo[19].extend([17, 18, 20, 21])
    grafo[20].extend([17, 18, 19, 21])
    grafo[21].extend([17, 18, 19, 20])
    grafo[22].extend([0, 1, 2, 3, 23, 24])
    grafo[23].extend([22, 24])
    grafo[24].extend([22, 23])
    grafo[25].extend([4, 5, 6, 7, 8, 9, 26, 27, 28, 29, 30])
    grafo[26].extend([25, 27, 28, 29, 30])
    grafo[27].extend([25, 26, 28, 29, 30])
    grafo[28].extend([25, 26, 27, 29, 30])
    grafo[29].extend([25, 26, 27, 28, 30])
    grafo[30].extend([25, 26, 27, 28, 29])
    grafo[31].extend([32, 33, 34])
    grafo[32].extend([31, 33, 34])
    grafo[33].extend([31, 32, 34])
    grafo[34].extend([31, 32, 33])
    grafo[35].extend([36, 37, 38, 39, 40])
    grafo[36].extend([35, 37, 38, 39, 40])
    grafo[37].extend([35, 36, 38, 39, 40])
    grafo[38].extend([35, 36, 37, 39, 40])
    grafo[39].extend([35, 36, 37, 38, 40])
    grafo[40].extend([35, 36, 37, 38, 39])
    grafo[46].extend([47, 49, 54, 55])
    grafo[47].extend([46, 49, 54, 55])
    grafo[49].extend([46, 47, 54, 55])
    grafo[52].extend([53])
    grafo[53].extend([52])
    grafo[54].extend([46, 47, 49, 55])
    grafo[55].extend([46, 47, 49, 54])
    grafo[56].extend([48])
    return grafo


# Dicionário das disciplinas
disciplinas = {
    0: "XDES01",
    1: "CRSC03",
    2: "XMAC01",
    3: "CAHC04",
    4: "XDES02",
    5: "XDES04",
    6: "CRSC02",
    7: "CTCO02",
    8: "XMAC02",
    9: "CMAC03",
    10: "CIC111",
    11: "CIC132",
    12: "COM211",
    13: "COM221",
    14: "COM230",
    15: "COM240",
    16: "COM311",
    17: "CIC271",
    18: "COM212",
    19: "COM213",
    20: "COM222",
    21: "COM242",
    22: "XDES01",
    23: "SAHC04",
    24: "SAHC05",
    25: "XDES03",
    26: "SDES05",
    27: "STCO02",
    28: "SRSC03",
    29: "MAT017",
    30: "COM220",
    31: "SIN260",
    32: "COM240",
    33: "SIN132",
    34: "COM231",
    35: "SIN210",
    36: "COM213",
    37: "SIN412",
    38: "SIN413",
    39: "SIN414",
    40: "SIN313",
    41: "CCO016",
    42: "CCO016",
    43: "CCO016",
    44: "CCO016",
    45: "CCO016",
    46: "OPT1",
    47: "OPT2",
    48: "OPT3",
    49: "OPT4",
    50: "POS1",
    51: "POS2",
    52: "POS3",
    53: "POS5",
    54: "OPT1",
    55: "OPT2",
    56: "OPT3",
}

# Dicionário dos professores
professores = {
    0: "Prof 1",
    1: "Prof 2",
    2: "Prof 3",
    3: "Prof 4",
    4: "Prof 5",
    5: "Prof 6",
    6: "Prof 7",
    7: "Prof 8",
    8: "Prof 9",
    9: "Prof 10",
    10: "Prof 11",
    11: "Prof 12",
    12: "Prof 13",
    13: "Prof 14",
    14: "Prof 15",
    15: "Prof 16",
    16: "Prof 17",
    17: "Prof 18"
}

# Criação inicial da matriz com base nas dimensões de disciplinas e professores
matriz = np.zeros((len(disciplinas), len(professores)))

# Inserindo os valores conforme o dataset disponibilizado pelo professor


def completaMatriz(matriz):
    matriz[0][11] = 4
    matriz[1][12] = 4
    matriz[2][4] = 4
    matriz[3][15] = 2
    matriz[4][8] = 4
    matriz[5][0] = 4
    matriz[6][12] = 4
    matriz[7][17] = 4
    matriz[8][8] = 4
    matriz[9][15] = 4
    matriz[10][13] = 3
    matriz[11][4] = 4
    matriz[12][7] = 4
    matriz[12][10] = 4
    matriz[13][9] = 4
    matriz[14][11] = 4
    matriz[15][3] = 4
    matriz[16][1] = 3
    matriz[17][6] = 4
    matriz[18][0] = 4
    matriz[19][5] = 4
    matriz[20][14] = 5
    matriz[21][15] = 4
    matriz[22][14] = 4
    matriz[23][5] = 2
    matriz[24][9] = 4
    matriz[25][14] = 4
    matriz[26][7] = 4
    matriz[27][13] = 4
    matriz[28][10] = 4
    matriz[29][4] = 4
    matriz[30][8] = 4
    matriz[31][6] = 4
    matriz[32][3] = 4
    matriz[33][4] = 4
    matriz[34][17] = 4
    matriz[35][7] = 4
    matriz[36][5] = 4
    matriz[37][9] = 5
    matriz[38][7] = 4
    matriz[39][3] = 3
    matriz[40][1] = 3
    matriz[41][2] = 4
    matriz[42][2] = 4
    matriz[43][2] = 4
    matriz[44][10] = 4
    matriz[45][2] = 4
    matriz[46][1] = 4
    matriz[47][16] = 4
    matriz[48][0] = 4
    matriz[49][6] = 4
    matriz[50][13] = 4
    matriz[51][12] = 4
    matriz[52][11] = 4
    matriz[53][5] = 4
    matriz[54][16] = 4
    matriz[55][17] = 4
    matriz[56][10] = 4
    return matriz


# Atribuição dos valores à matriz anteriormente criada
matriz = completaMatriz(matriz)
matriz_int = matriz.astype(int)
matriz = matriz_int
