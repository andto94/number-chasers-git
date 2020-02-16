import random
import operator

def generate_operator(gene, answer, dna_integer):
    a = answer
    b = dna_integer
    operator_dict = {0: {'operator': operator.add(a, b),
                         'representation': '+'},
                     1: {'operator': operator.sub(a, b),
                         'representation': '-'},
                     2: {'operator': operator.mul(a, b),
                         'representation': '*'},
                     3: {'operator': operator.truediv(a, b),
                         'representation': '/'}}
    return operator_dict[gene]['operator']

random_line = [1, 2, 0, 0, 0]

answer = 0.0
dna_integer = 3
optimal = 5000
for i in random_line:
    answer = generate_operator(i, answer, dna_integer)
    if abs(answer) < optimal:
        answer = abs(answer) - optimal
    else:
        answer = optimal - abs(answer)

print(answer)
