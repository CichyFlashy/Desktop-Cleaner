import os
from send2trash import send2trash
import shutil

downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
list_of_download_files = os.listdir(downloads_path)
print(list_of_download_files)

description = '''
    Witaj w programie do usuwania zawartości twojego folderu Pobrane. 
    Wybierz jedną z poniższych opcji wpisując numer opcji:
    1.Usuń wszystko nie przenosząc do kosza.
    2.Usuń wszystko przenosząc do kosza
    3.Przenieś do kosza wybrane rodzaje plików.
    4.Wyjdź   
    '''

print(description)
selected_option = input("Wybierz opcję: ")
print(selected_option)

if selected_option == '1':
    for filename in list_of_download_files:
        file_path = os.path.join(downloads_path, filename)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

elif selected_option == '2':
    for filename in list_of_download_files:
        file_path = os.path.join(downloads_path, filename)
        send2trash(file_path)

elif selected_option == '3':
    type_of_file = input("Podaj rozszerzenie pliku: ")
    for filename in list_of_download_files:
        if filename.endswith(type_of_file):
            file_path = os.path.join(downloads_path, filename)
            send2trash(file_path)

elif selected_option == '4':
    exit()
