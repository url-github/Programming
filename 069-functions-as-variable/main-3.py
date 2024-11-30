# Definicja funkcji transformacyjnych
def double(x):
    return 2 * x

def square(x):
    return x**2

def negative(x):
    return -x

def div2(x):
    return x / 2

# Zmienna wejściowa
number = 8

# Lista transformacji
transformations1 = [double, square, div2, negative]
transformations2 = [square, square, div2, double]

# Funkcja przetwarzająca dane w oparciu o listę transformacji
def process_transformations(number, transformations):
    # Tymczasowa zmienna przechowująca wynik
    tmp_return_value = number

    # Iteracja przez funkcje w liście transformacji
    for transformation in transformations:
        # Wywołanie funkcji i zaktualizowanie wyniku
        tmp_return_value = transformation(tmp_return_value)
        # Wyświetlenie aktualnej wartości
        print(f"After {transformation.__name__}: {tmp_return_value}")

    # Zwrócenie końcowego wyniku
    return tmp_return_value

# Test dla pierwszej listy transformacji
print("Transformations 1:")
process_transformations(number, transformations1)

print("\nTransformations 2:")
# Test dla drugiej listy transformacji
process_transformations(number, transformations2)