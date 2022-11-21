import os

def index_files(folder_path:str) -> list:
    files = []
    for object in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, object)):
            files.append(os.path.splitext(object)[0])
    return files

def folder_to_links(folder_path:str) -> list:
    files = index_files(folder_path)
    links = []
    for file in files:
        link = f'<a href="./Formatted/{file}.txt" target="_self">{file}</a>'
        links.append(link)
    return links

def create_index(folder_path:str) -> None:
    index_file = open('index.html', 'w')
    index_file.write('<html>\n<head>\n\t<title>Index</title>\n</head>\n')
    index_file.write('<body>\n')
    for line in folder_to_links(folder_path):
        index_file.write(f'\t{line}</br>\n')
    index_file.write('</body>\n</html>')
    index_file.close()

if __name__ == "__main__":
    create_index("./Formatted")
