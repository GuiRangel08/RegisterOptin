from file import *

def main(file):
    log_errors = get_log_file(file)

    print(type(log_errors))
    write_in_file(log_errors, file)

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

def write_in_file(log_errors, file):
    with open(f"log/errors_caught/{file}", "w") as f:
        for x in log_errors:
            print(type(x))
            f.write(x + '\n')

def catch_errors_from_log(log_file):
    errors = []
    for x in log_file:
        if 'Server error' in x:
            errors.append(x)
    return errors
    
if __name__ == '__main__':
    file = get_log_filename()
    main(file)

# 1717_20210620-000345