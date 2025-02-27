import os
from send2trash import send2trash
import shutil

try:
    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
except Exception as e:
    print(f"Błąd podczas odczytu folderu: {e}")
    exit()

list_of_download_files = os.listdir(downloads_path)

description = '''
    Witaj w programie do usuwania zawartości twojego folderu Pobrane. 
    Wybierz jedną z poniższych opcji wpisując numer opcji:
    1.Usuń wszystko nie przenosząc do kosza.
    2.Usuń wszystko przenosząc do kosza
    3.Przenieś do kosza wybrane rodzaje plików.
    4.Wyjdź   
    '''

print(description)
try:
    selected_option = int(input("\tWybierz opcję: "))
except ValueError:
    print("Wprowadzono niepoprawny numer!")
    exit()

if selected_option == 1:
    decision = input("Pliki zostaną usunięte bez możliwości ich odzyskania. Czy chcesz kontynuowac? T/N:")
    if decision.upper() == "T":
        for filename in list_of_download_files:
            file_path = os.path.join(downloads_path, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)


elif selected_option == 2:
    decision = input("Pliki zostaną przeniesione do kosza. Czy chcesz kontynuowac? T/N:")
    if decision.upper() =='T':
        for filename in list_of_download_files:
            file_path = os.path.join(downloads_path, filename)
            send2trash(file_path)

elif selected_option == 3:
    type_of_file = input("Podaj rozszerzenie pliku: ")
    decision = input("Pliki zostaną przeniesione do kosza. Czy chcesz kontynuowac? T/N:")
    if decision.upper() =='T':
        for filename in list_of_download_files:
            if filename.endswith(type_of_file):
                file_path = os.path.join(downloads_path, filename)
                send2trash(file_path)

elif selected_option == 4:
    exit()
