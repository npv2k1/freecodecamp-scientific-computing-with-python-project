def arithmetic_arranger(problems, isSolve=False):
    if(len(problems) > 5):
        return("Error: Too many problems.")
    if(isSolve):
        res=[""]*4
    else:
        res = ['']*3
    a = []
    b = []
    c = []
    ans = []
    for i in problems:
        x, o, y = i.split()
        if(not str.isdigit(x) or not str.isdigit(y)):
            return ("Error: Numbers must only contain digits.")
        if(o != '+' and o != '-'):
            return ("Error: Operator must be '+' or '-'.")
        if o == '+':
            ans.append(int(x)+int(y))
        else:
            ans.append(int(x)-int(y))

        ml = max(len(x), len(y))+2
        if(ml > 6):
            return "Error: Numbers cannot be more than four digits."

        a.append('{: >{}}'.format(str(x), ml))
        b.append(o+'{: >{}}'.format(str(y), ml-1))
        ans.append('{: >{}}'.format(str(ans.pop()), ml))
        c.append("-"*ml)

    if(isSolve):
        arranged_problems = '    '.join(
            a) + '\n' + '    '.join(b) + '\n' + '    '.join(c)+'\n'+'    '.join(ans)
    else:
        arranged_problems = '    '.join(
            a) + '\n' + '    '.join(b) + '\n' + '    '.join(c)

    return arranged_problems
