import operator
import random
dna_integer = 5
operand = 5

def generate_operator(gene, operand, dna_integer):
    # ----
    # Converts genes into their corresponding operators
    # ----
    operator_dict = {0: {'operator': operator.add(operand, dna_integer),
                         'representation': '+'},
                     1: {'operator': operator.sub(operand, dna_integer),
                         'representation': '-'},
                     2: {'operator': operator.mul(operand, dna_integer),
                         'representation': '*'},
                     3: {'operator': operator.truediv(operand, dna_integer),
                         'representation': '/'}}
    return operator_dict[gene]['operator']

line = [1, 2, 0, 0, 0]

for i in line:
    print(generate_operator(i, operand, dna_integer))
