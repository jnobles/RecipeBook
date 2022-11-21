import os

def read_file(filepath: str) -> tuple[dict, list[str]]:
    metadata = {}
    recipe_steps = []
    with open(filepath) as f:
        metadata['title'] = os.path.splitext(os.path.basename(filepath))[0]
        for line in f:
            line = line.strip()
            if not line:
                continue
            elif line[0:2] == '>>':
                key, value = line[3:].split(':', 1)
                metadata[key.strip()] = value.strip()
            else:
                recipe_steps.append(line)
    return metadata, recipe_steps

def translate_to_latex(metadata:dict, recipe_steps:list) -> str:
    for item in ['title', 'yields', 'prep time']:
        if not item in metadata.keys():
            metadata[item] = 'Not provided'

    lines = []
    lines.append(f'''\\begin{{recipe}}{{{metadata['title']}}}{{{metadata['yields']}}}{{{metadata['prep time']}}}''')


    print(lines[0])

if __name__ == '__main__':
    translate_to_latex(read_file('./Cook Files/Sourdough Pumpkin Bread.cook')[0], [])
