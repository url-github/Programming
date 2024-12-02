import datetime

def ChangeSalary(emp_name, new_salary, is_bonus=False):
	print("Changing salary for {} to {} as bonus {}".format(emp_name, new_salary, is_bonus))
	return emp_name, new_salary

print(ChangeSalary("David", 40000, True))

# Changing salary for David to 40000 as bonus True
# 40000

def CreateFunctionWithWrapper(func):
	def func_with_wrapper(*args, **kwargs):
		print('Function "{}" started at {}'.format(func.__name__, datetime.datetime.now().isoformat()))
		print("Following arguments were used:")
		print(args, kwargs)
		result = func(*args, **kwargs)
		print("Function returned {}".format(result))
		return result
	return func_with_wrapper

ChangeSalary = CreateFunctionWithWrapper(ChangeSalary)

print(ChangeSalary("David", 40000, is_bonus=True))

# Function "ChangeSalary" started at 2024-12-02T10:01:47.770296
# Following arguments were used:
# ('David', 40000) {'is_bonus': True}
# Changing salary for David to 40000 as bonus True
# Function returned 40000
# 40000