import os
import re

def index_files(folder_path:str) -> list:
    files = []
    for item in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, item)):
            files.append(os.path.splitext(item)[0])
    return files

def folder_to_links(folder_path:str) -> list:
    files = index_files(folder_path)
    links = []
    for file in files:
        link = f'<li><a href="./Formatted/{file}.txt" target="_self">{file}</a></li>'
        links.append(link)
    return links

def create_index(folder_path:str) -> None:
    content = ['<html>','<head>','\t<title>Recipe Book</title>','</head>','<style>',
                '\ta:link, a:visited { color: blue }', '\tul { list-style-type: none}',
                '\tdiv { padding-top: 1vh; width: 400px; margin: auto }','\th3 { text-align: center }',
                '</style>','<body>','\t<div>','\t\t<h3>My Collected Recipies</h3>','\t\t<hr>',
                '\t\t<ul>','<!--Begin Recipes-->','','<!--End Recipes-->','\t\t</ul>','\t</div>',
                '</body>','</html>']
    content = '\n'.join(content)
    with open('index.html', 'w') as f:
        f.write(content)

def update_index(folder_path:str) -> None:
    links = '\n'.join([l for l in folder_to_links(folder_path)])
    matching_string = r'(?<=<!--Begin Recipes-->\s)[\S\s]*(?=\s<!--End Recipes-->)'
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
