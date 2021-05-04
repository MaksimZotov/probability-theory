from copy import copy, deepcopy
import plotly.graph_objs as go
import random
import numpy

columns = 5
rows = 3

money = 100
money_list = []

symbols = {'S1': {3: 3, 4: 15, 5: 45},
           'S2': {3: 5, 4: 30, 5: 75},
           'S3': {3: 7, 4: 50, 5: 150},
           'S4': {3: 9, 4: 60, 5: 250},
           'S5': {3: 12, 4: 75, 5: 350},
           'S6': {3: 15, 4: 90, 5: 500},
           'S7': {3: 20, 4: 120, 5: 750},
           'S8': {3: 30, 4: 150, 5: 1000},
           'Scatter': {2: 100, 3: 600, 4: 1200, 5: 2400}}

matrix = [['Wild', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'Scatter'],
          ['Wild', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'Scatter'],
          ['Wild', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'Scatter'],
          ['Wild', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'Scatter'],
          ['Wild', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'Scatter']]


def create_matrix(matrix):
    for i in range(len(matrix)):
        column = matrix[i]
        prev_column = copy(column)
        rnd = random.randint(0, len(column) - 1)
        for j in range(len(column)):
            column[(j + rnd) % len(column)] = prev_column[j]


def get_prize(lines):
    prize = 0
    for line in lines:
        count = 1
        prev = line[0]
        for i in range(1, len(line)):
            next = line[i]
            if next == prev:
                count += 1
            else:
                break
            prev = next
        symbol = line[0]
        if count >= 3:
            prize += symbols[symbol][count]
        if count == 2 and symbol == 'Scatter':
            prize += symbols[symbol][count]
    return prize


while money > 0:
    money_list.append(money)
    money -= 5
    create_matrix(matrix)

    wild_indexes = []
    for i in range(columns):
        for j in range(rows):
            if matrix[i][j] == 'Wild':
                wild_indexes.append([i, j])

    matrix_variants = []
    symbols_keys = symbols.keys()
    n = len(symbols)
    m = len(wild_indexes)
    for s1 in symbols_keys:
        if m == 1:
            matrix_variant = deepcopy(matrix)
            matrix_variant[wild_indexes[0][0]][wild_indexes[0][1]] = s1
            matrix_variants.append(matrix_variant)
        for s2 in symbols_keys:
            if m < 2:
                break
            if m == 2:
                matrix_variant = deepcopy(matrix)
                matrix_variant[wild_indexes[0][0]][wild_indexes[0][1]] = s1
                matrix_variant[wild_indexes[1][0]][wild_indexes[1][1]] = s2
                matrix_variants.append(matrix_variant)
            for s3 in symbols_keys:
                if m < 3:
                    break
                if m == 3:
                    matrix_variant = deepcopy(matrix)
                    matrix_variant[wild_indexes[0][0]][wild_indexes[0][1]] = s1
                    matrix_variant[wild_indexes[1][0]][wild_indexes[1][1]] = s2
                    matrix_variant[wild_indexes[2][0]][wild_indexes[2][1]] = s3
                    matrix_variants.append(matrix_variant)
                for s4 in symbols_keys:
                    if m < 4:
                        break
                    if m == 4:
                        matrix_variant = deepcopy(matrix)
                        matrix_variant[wild_indexes[0][0]][wild_indexes[0][1]] = s1
                        matrix_variant[wild_indexes[1][0]][wild_indexes[1][1]] = s2
                        matrix_variant[wild_indexes[2][0]][wild_indexes[2][1]] = s3
                        matrix_variant[wild_indexes[3][0]][wild_indexes[3][1]] = s4
                        matrix_variants.append(matrix_variant)
                    for s5 in symbols_keys:
                        if m < 5:
                            break
                        if m == 5:
                            matrix_variant = deepcopy(matrix)
                            matrix_variant[wild_indexes[0][0]][wild_indexes[0][1]] = s1
                            matrix_variant[wild_indexes[1][0]][wild_indexes[1][1]] = s2
                            matrix_variant[wild_indexes[2][0]][wild_indexes[2][1]] = s3
                            matrix_variant[wild_indexes[3][0]][wild_indexes[3][1]] = s4
                            matrix_variant[wild_indexes[4][0]][wild_indexes[4][1]] = s5
                            matrix_variants.append(matrix_variant)

    if len(wild_indexes) == 0:
        matrix_variants.append(matrix)

    prize = 0
    matrix_prize = []
    for matrix_variant in matrix_variants:
        line_1 = [matrix_variant[0][0], matrix_variant[1][0], matrix_variant[2][0], matrix_variant[3][0], matrix_variant[4][0]]
        line_2 = [matrix_variant[0][1], matrix_variant[1][1], matrix_variant[2][1], matrix_variant[3][1], matrix_variant[4][1]]
        line_3 = [matrix_variant[0][2], matrix_variant[1][2], matrix_variant[2][2], matrix_variant[3][2], matrix_variant[4][2]]
        line_4 = [matrix_variant[0][0], matrix_variant[1][1], matrix_variant[2][2], matrix_variant[3][1], matrix_variant[4][0]]
        line_5 = [matrix_variant[0][2], matrix_variant[1][1], matrix_variant[2][0], matrix_variant[3][1], matrix_variant[4][2]]
        lines = [line_1, line_2, line_3, line_4, line_5]
        cur_prize = get_prize(lines)
        if cur_prize > prize:
            prize = cur_prize
            matrix_prize = matrix_variant

    if prize > 0:
        debug = 0

    money += prize

x_axis = numpy.arange(1, len(money_list), 1)
y_axis = money_list
figure = go.Figure()
figure.add_trace(go.Scatter(x=x_axis, y=y_axis))
figure.show()