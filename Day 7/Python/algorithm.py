from itertools import product ## used for cartesian product
import time ## used for simple runtime measurement

"""
Read input
"""
inputpath=""
eqs = []
with open(inputpath, 'r') as file:
    for line in file:
        line = line.strip()
        res, operands = line.split(":")
        res = int(res)
        operands = operands[1:]
        operands = list(map(int, operands.split(" ")))
        eqs.append((res, operands))

"""
Lambda functions for the operators
"""
add = lambda x,y: x + y # Task 1
mul = lambda x,y: x * y # Task 1
con = lambda x,y: int(str(x)+str(y)) # Task 2

"""
Helper functions for sequence generation and evaluation
"""
def evaluate(operands, operators): # Task 1 & 2
    res = operands[0]
    for i in range(0, len(operators)):
        res = operators[i](res, operands[i+1])
    return res

def generate_operator_sequences(operands, operators): # Task 1 & 2
    len_ops_seq = len(operands)-1
    ## Cartesian Product of [add, mul]^len_ops_seq
    return list(product(operators, repeat=len_ops_seq))

"""
Main loop
"""
def main_loop(eqs, operators=[add,mul]): # Task 1 & 2
    counter = 0
    for eq in eqs:
        operands = eq[1]
        goal = eq[0]
        sequences = generate_operator_sequences(operands, operators)
        for seq in sequences:
            if goal == evaluate(operands, seq):
                counter += goal
                break # Break if goal is met first time
    return counter
    
"""Task 1"""
st = time.time()
res = main_loop(eqs)
et = time.time()
print("Task a):", res,"(took "+ str(et-st) + " seconds)")

"""Task 2"""
st = time.time()
res = main_loop(eqs, [add, mul, con])
et = time.time()
print("Task b):", res,"(took "+ str(et-st) + " seconds)")
