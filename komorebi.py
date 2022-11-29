#  Copyright (c) 2022.  @gamma-410

import sys

arg = sys.argv
fileName = arg[1]
createFileName = arg[2]
CUT_SPELL = []
INPUT = []
DOC = [
    '--',
    '#',
    ':',
    ';',
    '(',
    ')',
    'put',
    'in',
    'let',
    'if',
    'else',
    'elif',
]
BASE = [
    [''],
    ['// ', 1],
    ['{'],
    ['}'],
    ['('],
    [')'],
    ['print(', 1, ')'],
    ['var ', 1, ': ', 2, ' = ', 3],
    ['let ', 1, ': ', 2, ' = ', 3],
    ['if ', 1, ' {'],
    ['else', ' {'],
    ['else if ', 1, ' {']
]
OUTPUT = []
out = ""

readFileTexts = open(fileName, "r")

for readFileText in readFileTexts:
    readFileText = readFileText.split()
    CUT_SPELL.append(readFileText)

for INPUT in CUT_SPELL:
    if INPUT[0] in DOC:
        searchDOCIndex = DOC.index(INPUT[0])
        for sourceCode in BASE[searchDOCIndex]:
            if type(sourceCode) is int:
                if sourceCode <= len(INPUT) - 1:
                    out = out + INPUT[sourceCode]
            else:
                out = out + sourceCode

        OUTPUT.append([out])
        out = ""

for i in OUTPUT:
    for j in i:
        file = open(createFileName, mode='a')
        file.write(j + "\n")