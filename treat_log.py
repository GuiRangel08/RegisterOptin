from file import *
from getters import *

def main():
    filename = get_log_filename()
    company_id = get_company_id()
    log_errors = get_log_file(filename)
    path = f"log/errors_caught/{company_id}"

    if not folder_exists(path):
        create_folder(path)

    write_list_in_file(log_errors, filename, path)


    print('Finalizado.')
    
def get_log_file(file = False):
    log_errors = []
    if file:
        file = get_log_filepath(file)
        log_file = read_file(file)
        log_errors = catch_errors_from_log(log_file)
    else:
        pass
    return log_errors



def catch_errors_from_log(log_file):
    errors = []
    for x in log_file:
        if 'Server error' in x:
            errors.append(x)
    return errors
    
if __name__ == '__main__':
    main()

# 1717_20210620-000345