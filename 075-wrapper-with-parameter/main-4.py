import os

file_path = r'/Users/p/Documents/Scripts/Programming/075-wrapper-with-parameter/dummy_file.txt'

# Tworzenie folderów, jeśli nie istnieją
os.makedirs(os.path.dirname(file_path), exist_ok=True)

# Weryfikacja
if os.path.exists(os.path.dirname(file_path)):
    print("Folder został pomyślnie utworzony lub już istnieje.")
else:
    print("Nie udało się utworzyć folderu.")

print(os.path.dirname(file_path))