def arithmetic_arranger(problems, statprint=False):
    first = ''
    second = ''
    sumx = ''
    lines = ''
    # maximal problems is 5
    # of course can be changed 
    if len(problems) >= 6:
        return 'Error: Too many problems.'
    # split problem into the components 
    for i in problems:
        components = i.split()
        firsts = components[0]
        seconds = components[2]
        operands = components[1]
        # check the length of the number, max 4 digits
        if (len(firsts) > 4 or len(seconds) > 4):
            return "Error: Numbers cannot be more than four digits."

        # check the input as valid digits
        if not firsts.isnumeric() or not seconds.isnumeric():
            return "Error: Numbers must only contain digits."
        
        # only addition and subtraction opperations are Valid
        if (operands == '+' or operands == '-'):
            if operands == "+":
                sums = str(int(firsts) + int(seconds))
            else:
                sums = str(int(firsts) - int(seconds))
            # set length of sum and top, bottom and dots values
            length = max(len(firsts), len(seconds)) + 2
            top = str(firsts).rjust(length)
            bottom = operands + str(seconds).rjust(length - 1)
            dots = ''
            res = str(sums).rjust(length)
            for s in range(length):
                dots += '-'
            # add to the overall string
            if i != problems[-1]:
                first += top + '    '
                second += bottom + '    '
                lines += dots + '    '
                sumx += res + '    '
            else:
                first += top
                second += bottom
                lines += dots
                sumx += res
        else:
            return "Error: Operator must be '+' or '-'."
    # strip out spaces to the right of the string
    first.rstrip()
    second.rstrip()
    lines.rstrip()
    # Check if wanted tto print the result
    if statprint:
        sumx.rstrip()
        arranged_problems = first + '\n' + second + '\n' + lines + '\n' + sumx
    else:
        arranged_problems = first + '\n' + second + '\n' + lines
    return arranged_problems