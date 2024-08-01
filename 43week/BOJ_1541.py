# 55-50+40

# 00009-00009
def progress(elem):
    elem = elem.split('+')
    # if len(elem) == 1:
    #     return elem
    results = ""
    for e in elem:
        results += str(int(e))
        results += "+"

    return results[:-1]

line = input().split('-')
result = eval(progress(line[0]))
if len(line) > 1:
    for l in line[1:]:
        result -= eval(progress(l))

print(result)