import math
import time

formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]

argument_list = []


for i in range (1000000):
    argument_list.append(i/10)

for formula in formulas_list:

    results_list = []
    print("Formula {}".format(formula))
    start = time.time()
    for x in argument_list:
        results_list.append(eval(formula))
    print('min = {}  max = {}'.format(min(results_list), max(results_list)))
    stop = time.time()
    print("Calculation time: {}".format(stop - start))


for formula in formulas_list:

    results_list = []
    print("Formula {}".format(formula))

    start = time.time()
    compiled_formula = compile(formula, formula, 'eval')
    for x in argument_list:
        results_list.append(eval(compiled_formula))
    print('min = {}  max = {}'.format(min(results_list), max(results_list)))
    stop = time.time()

    print("Calculation time: {}".format(stop - start))

# Formula abs(x**3 - x**0.5)
# min = 0.0  max = 999997000002683.6
# Calculation time: 3.2249789237976074
# Formula abs(math.sin(x) * x**2)
# min = 0.0  max = 9997170253.720783
# Calculation time: 3.788158893585205
# Formula abs(x**3 - x**0.5)
# min = 0.0  max = 999997000002683.6
# Calculation time: 0.1717698574066162
# Formula abs(math.sin(x) * x**2)
# min = 0.0  max = 9997170253.720783
# Calculation time: 0.1841421127319336