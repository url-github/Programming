import datetime
import functools

def CreateFunctionWithWrapper_LogToFile(logFilePath):
	def CreateFunctionWithWrapper(func):
		def func_with_wrapper(*args, **kwargs):
			file = open(logFilePath,'a')
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
	return CreateFunctionWithWrapper

@CreateFunctionWithWrapper_LogToFile("/Users/p/Documents/Scripts/Programming/075-wrapper-with-parameter/salary_log.txt")
def ChangeSalary(emp_name, new_salary, is_bonus=False):
	print("Changing salary for {} to {} as bonus {}".format(emp_name, new_salary, is_bonus))
	return new_salary

@CreateFunctionWithWrapper_LogToFile("/Users/p/Documents/Scripts/Programming/075-wrapper-with-parameter/position_log.txt")
def ChangePosition(emp_name, new_position):
	print("Changing position for {} to {}".format(emp_name, new_position))
	return new_position

print(ChangeSalary("David", 40000, is_bonus=True))
print(ChangeSalary("David", 40000, False))

print(ChangePosition("Fox", 'Policeman'))
print(ChangePosition("Megan", 'Manager'))


# --------------------
# Function "ChangePosition" started at 2024-12-02T13:58:54.865862
# Following arguments were used:
# Fox Policeman
# Function returned Policeman
# --------------------
# Function "ChangePosition" started at 2024-12-02T13:58:54.865907
# Following arguments were used:
# Megan Manager
# Function returned Manager

# --------------------
# Function "ChangeSalary" started at 2024-12-02T13:58:54.865691
# Following arguments were used:
# David 40000
# is_bonus=True
# Function returned 40000
# --------------------
# Function "ChangeSalary" started at 2024-12-02T13:58:54.865789
# Following arguments were used:
# David 40000 False
# Function returned 40000

