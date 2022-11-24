import os
import shutil
import subprocess

def get_out_of_date_files(input_folder: str, output_folder:str) -> list:
    files = []
    for item in os.listdir(input_folder):
        base_name = os.path.splitext(item)[0]
        input_file = os.path.join(input_folder, base_name + '.cook')
        output_file = os.path.join(output_folder, base_name + '.txt')

        if not os.path.isfile(output_file):
            files.append((input_file, output_file))
        else:
            input_mtime = os.path.getmtime(input_file)
            output_mtime = os.path.getmtime(output_file)
            if output_mtime < input_mtime:
                files.append((input_file, output_file))
    return files

def parse_files(file_list: str) -> None:
    for input_file, output_file in file_list:
        with open(output_file, 'w') as f:
            subprocess.run(['cook','recipe','read',input_file],
                           stdout=f)

if __name__ == '__main__':
    file_list = get_out_of_date_files('./Cook Files', './Formatted')
    if shutil.which('cook') is not None:
        parse_files(file_list)
        print(f'{len(file_list)} .cook files successfully processed.')
    else:
        print(f'\'cook\' not installed on this system: {len(file_list)} \
              files not processed.')
