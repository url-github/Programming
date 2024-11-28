'''LAB - Funkcja exec()
Tym razem pracujesz w zwariowanym ośrodku badawczym...

Profesorowie przygotowują swoje skrypty i umieszczają je w określonym katalogu. Kolejno:
/Users/p/Documents/Scripts/Programming/065-exec/main-3.py
/Users/p/Documents/Scripts/Programming/065-exec/main-4.py

Twój skrypt ma za zadanie przeczytać te skrypty i je po kolei wykonywać.

Poniżej znajdują się dwa przykładowe skrypty. Każdy z nich skopiuj i zapisz w osobnym pliku (jeżeli wykonanie skryptu miało by być zbyt długie, możesz zmienić ilość iteracji w zmiennej for, ale nie powinno być tak źle):
'''

import os


files_to_process = [
	r"/Users/p/Documents/Scripts/Programming/065-exec/main-3.py",
	r"/Users/p/Documents/Scripts/Programming/065-exec/main-4.py"
]

for file_path in files_to_process:

    with open(file_path, 'r') as f:
        print("File {} ...".format(os.path.basename(file_path)))
        source = f.read()
        exec(source)
