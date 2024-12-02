import datetime
import functools

function_log = "/Users/p/Documents/Scripts/Programming/075-wrapper-with-parameter/function_log.txt"

def CreateFunctionWithWrapper(func):
	def func_with_wrapper(*args, **kwargs):
		file = open(function_log,'a')
		file.write("-"*20+"\n")
		file.write('Function "{}" started at {}\n'.format(func.__name__, datetime.datetime.now().isoformat()))
		file.write("Following arguments were used:\n")
		file.write(" ".join("{}".format(i) for i in args)) # Zapisywać mogę tylko str więc konwertuje
		file.write("\n")
		file.write(" ".join("{}={}\n".format(k, v) for k, v in kwargs.items()))
		result = func(*args, **kwargs)
		file.write("Function returned {}\n".format(result))
		file.close()
		return result
	return func_with_wrapper

@CreateFunctionWithWrapper
def ChangeSalary(emp_name, new_salary, is_bonus=False):
	print("Changing salary for {} to {} as bonus {}".format(emp_name, new_salary, is_bonus))
	return new_salary

print(ChangeSalary("David", 40000, is_bonus=True))
print(ChangeSalary("David", 40000, False))


# --------------------
# Function "ChangeSalary" started at 2024-12-02T12:35:50.758219
# Following arguments were used:
# David 40000
# is_bonus=True
# Function returned 40000
# --------------------
# Function "ChangeSalary" started at 2024-12-02T12:35:50.758340
# Following arguments were used:
# David 40000 False
# Function returned 40000
