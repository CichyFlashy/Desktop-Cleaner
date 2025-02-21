import os

downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
list_of_download_files = os.listdir(downloads_path)
print(list_of_download_files)

description = '''
    Witaj w programie do usuwania zawartości twojego folderu Pobrane. 
    Wybierz jedną z poniższych opcji wpisując numer opcji:
    1.Usuń wszystko nie przneosząc do kosza.
    2.Usuń wszystko przenosząc do kosza
    3.Usuń wybrane rodzaje plików.
    4.Wyjdź   
    '''

print(description)
selected_option = input("Wybierz opcję: ")
print(selected_option)