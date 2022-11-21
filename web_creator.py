import os
import shutil
import re

def index_files(folder_path:str) -> list:
    files = []
    for object in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, object)):
            files.append(os.path.splitext(object)[0])
    return files

def folder_to_links(folder_path:str) -> list:
    files = index_files(folder_path)
    files.sort()
    links = ['<ul>', '</ul>']
    for file in files:
        link = f'<li><a href="./Formatted/{file}.txt" target="_self">{file}</a></li>'
        links.insert(len(links)-1, link)
    return links

def create_index(folder_path:str) -> None:
    shutil.copy('web/index.html', './')

def update_index(folder_path:str) -> None:
    links = '\n'.join([l for l in folder_to_links(folder_path)])
    matching_string = r'(?<=<!--Begin Recipies-->\s)[\S\s]*(?=\s<!--End Recipies-->)'
    file_contents = ''

    if not os.path.isfile('index.html'):
        create_index(folder_path)

    with open('index.html') as f:
        file_contents = f.read()
    file_contents = re.sub(matching_string, links, file_contents)

    with open('index.html', 'w') as f:
        f.write(file_contents)

if __name__ == "__main__":
    update_index("./Formatted")
