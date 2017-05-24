
####

symbol_to_sort_map = {
    'begin': 1,
    'end': 2,
    'integer': 3,
    'if': 4,
    'then': 5,
    'else': 6,
    'function': 7,
    'read': 8,
    'write': 9,
    # '#b', 10,    # 标识符
    # '#c', 11,   # 常数
    '=': 12,
    '<>': 13,
    '<=': 14,
    '<': 15,
    '>=': 16,
    '>': 17,
    '-': 18,
    '*': 19,
    ':=': 20,
    '(': 21,
    ')': 22,
    ';': 23,
}

max_length_symbol = max([len(i) for i in symbol_to_sort_map.keys()])
