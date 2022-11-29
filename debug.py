#  Copyright (c) 2022.  @gamma-410

import sys

arg = sys.argv
fileName = arg[1]
createFileName = arg[2]
CUT_SPELL = []
INPUT = []
DOC = [
    'print'
]
BASE = [
    ['print(', 1, ')']
]
OUTPUT = []
out = ""

readFileTexts = open(fileName, "r")

for readFileText in readFileTexts:
    print("元テキスト", readFileText)
    readFileText = readFileText.split()
    print("テキストをカット", readFileText)
    CUT_SPELL.append(readFileText)

print("カットしたテキストのグループ", CUT_SPELL)

for INPUT in CUT_SPELL:
    print("カットしたテキストのグループ (for文)", INPUT)
    if INPUT[0] in DOC:
        print("DOCリストに該当する単語 (INPUT[0])", INPUT[0])
        searchDOCIndex = DOC.index(INPUT[0])
        print("該当のインデックス番号", searchDOCIndex)
        for sourceCode in BASE[searchDOCIndex]:
            print("変換用構文（該当のインデックス番号）", sourceCode)
            if type(sourceCode) is int:
                if sourceCode <= len(INPUT) - 1:
                    print(sourceCode, "<=", len(INPUT) - 1)
                    out = out + INPUT[sourceCode]
                    print("out", out)

            else:
                out = out + sourceCode
                print("out (else)", out)

        OUTPUT.append([out])
        out = ""


print("OUTPUT", OUTPUT)

for i in OUTPUT:
    for j in i:
        file = open(createFileName, mode='a')
        file.write(j + "\n")
