import os

def file_exists(filename):
    if os.path.isfile(filename):
        return True
    else:
        return False

def folder_exists(foldername):
    if os.path.isdir(foldername):
        return True
    else:
        return False

def create_folder(foldename):
    os.makedirs(foldename)

    
def get_csv_filepath(file):
    filepath = os.path.abspath(f'csv/{file}')
    return filepath

def get_log_filepath(file):
    filepath = os.path.abspath(f'log/{file}')
    return filepath

def get_csv_filename():
    filename = input('Qual o nome do arquivo .CSV?\n')
    return filename + '.csv'

def get_log_filename():
    filename = input('Qual o nome do arquvio de log?\n')
    return filename + '.log'

def read_file(file):
    if file_exists(file):
        lines = []
        with open(f"{file}",'r', encoding = 'utf-8') as f:
            for line in f:
                lines.append((line.rstrip())) 
            return lines
    else:
        print('Arquivo não existe!')

def write_list_in_file(list, filename, path):
    with open(f"{path}/{filename}", "w") as f:
        for x in list:
            f.write(x + '\n')