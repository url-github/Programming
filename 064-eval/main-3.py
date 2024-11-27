var_x = 10
password = 'jhjchwcFRWfw434'
source = '__import__("os").getcwd()'  # Fragment kodu od użytkownika
# source = 'password'  # Fragment kodu od użytkownika

globals = {}

print("-" * 20)

# Wykonanie kodu z eval
result = eval(source, globals)
print(result)  # Oczekiwany wynik: 15