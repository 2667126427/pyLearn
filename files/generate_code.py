arr = [i for i in range(0, 30)]
with open('code.cpp', 'w') as fp:
    for i in arr:
        fp.write('case ' + str(i) + ":\n" + "    break;\n")
